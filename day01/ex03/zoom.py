# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    zoom.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 16:17:47 by dsindres          #+#    #+#              #
#    Updated: 2025/09/10 09:19:24 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
"""
zoom.py
Charge une image (par défaut 'animal.jpeg' ou chemin fourni en argument),
affiche sa shape et son contenu pixel, effectue un "zoom" par slicing (centre 400x400),
affiche la nouvelle shape, affiche la zone zoomée (avec échelle X et Y).
Gère proprement les erreurs et nève pas le programme brutalement.
"""

import sys
from typing import Optional
from PIL import Image, UnidentifiedImageError
import numpy as np
import matplotlib.pyplot as plt


def load_image(path: str) -> Optional[np.ndarray]:
    """
    Charge l'image depuis `path`, convertit en RGB et retourne un numpy.ndarray.
    En cas d'erreur retourne None après avoir affiché un message clair.
    """
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return None
    except UnidentifiedImageError:
        print(f"Error: cannot identify image file '{path}'.")
        return None
    except OSError as e:
        print(f"Error opening image '{path}': {e}")
        return None

    # Affiche le format détecté (JPEG, PNG, ...)
    print("Format of image is:", img.format)

    # S'assure d'avoir 3 canaux R,G,B
    img = img.convert("RGB")
    arr = np.array(img)  # shape -> (height, width, 3)

    # Affiche la shape conformément au sujet
    print("The shape of image is:", arr.shape)
    return arr


def crop_center(img: np.ndarray, crop_h: int, crop_w: int) -> np.ndarray:
    """
    Retourne un crop centré de taille (crop_h, crop_w).
    Si l'image est plus petite que la taille demandée, on retourne la partie disponible.
    """
    h, w = img.shape[:2]

    # calcul des indices de début (clamp à 0)
    start_y = max((h - crop_h) // 2, 0)
    start_x = max((w - crop_w) // 2, 0)

    # indices de fin (clamp à h,w)
    end_y = min(start_y + crop_h, h)
    end_x = min(start_x + crop_w, w)

    return img[start_y:end_y, start_x:end_x]


def display_with_axes(img: np.ndarray, title: str = "Zoomed area") -> None:
    """
    Affiche l'image (RGB ou grayscale) avec les axes X/Y montrant l'échelle.
    Affiche des ticks réguliers et une grille légère pour bien voir l'échelle.
    """
    if img.ndim == 3 and img.shape[2] == 3:
        cmap = None
        imshow_arg = img
    else:
        cmap = "gray"
        imshow_arg = img

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(imshow_arg, cmap=cmap)
    ax.set_title(title)

    h, w = img.shape[:2]

    # Choisir un pas de ticks raisonnable (8 divisions maximum)
    step_x = max(w // 8, 1)
    step_y = max(h // 8, 1)

    ax.set_xticks(np.arange(0, w, step_x))
    ax.set_yticks(np.arange(0, h, step_y))

    ax.set_xlabel("X (pixels)")
    ax.set_ylabel("Y (pixels)")

    # grille pour visualiser l'échelle
    ax.grid(color="white", linestyle="--", linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.show()


def main() -> None:
    """
    Main : gère les arguments, charge l'image, imprime pixels, fait le slicing et affiche.
    Accepts 0 or 1 argument: if none given, uses 'animal.jpeg'.
    If more than 1 argument prints an assertion-like error and exits.
    """
    # gestion des arguments : aucun ou un chemin autorisé
    if len(sys.argv) > 2:
        print("AssertionError: too many arguments")
        sys.exit(1)

    path = sys.argv[1] if len(sys.argv) == 2 else "animal.jpeg"

    # load
    pixels = load_image(path)
    if pixels is None:
        sys.exit(1)

    # Affiche le contenu entier des pixels (conforme au sujet : gros dump)
    # Attention : énorme sortie possible selon la taille de l'image.
    print(pixels)

    # Crop (le "zoom" demandé) : zone centrée 400x400
    cropped = crop_center(pixels, 400, 400)
    print("New shape after slicing:", cropped.shape)

    # Pour l'affichage textuel (exemples du sujet montrent parfois 1 canal)
    # on montre aussi une version en niveau de gris (moyenne) si image RGB.
    if cropped.ndim == 3 and cropped.shape[2] == 3:
        # conversion en grayscale pour affichage compact (valeurs entières)
        gray = (0.299 * cropped[:, :, 0] +
                0.587 * cropped[:, :, 1] +
                0.114 * cropped[:, :, 2]).astype(np.uint8)
        # Affiche la version à un canal (shape (h,w))
        print(gray)
    else:
        print(cropped)

    # Affiche visuellement la zone zoomée avec axes et grille
    try:
        display_with_axes(cropped, title="Zoomed (sliced) image")
    except Exception as e:
        print(f"Error while displaying image: {e}")
        # ne plante pas brutalement

if __name__ == "__main__":
    main()
