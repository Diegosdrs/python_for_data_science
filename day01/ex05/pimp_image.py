# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pimp_image.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 10:57:30 by dsindres          #+#    #+#              #
#    Updated: 2025/09/10 11:20:47 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import Optional
from PIL import Image, UnidentifiedImageError
import numpy as np
import matplotlib.pyplot as plt

def load_image(path: str) -> Optional[np.ndarray]:
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print("Error: file not found")
        return None
    except UnidentifiedImageError:
        print("Error: canno't identify image file")
        return None
    except OseError as e:
        print("Error: opening image")
        return None
    
    img = img.convert("RGB")
    arr = np.array(img)

    print(f"The shape of the image is: {arr.shape}")
    return arr


def display_image(img: np.ndarray, title: str) -> None:
    plt.imshow(img)
    plt.title(title)
    plt.axis("off")
    plt.show()


def ft_invert(arr: np.ndarray) -> np.ndarray:
    return 255 - arr

def ft_grey(arr: np.ndarray) -> np.ndarray:    
    if arr.ndim != 3 or arr.shape[2] != 3:
        print("Error: not an RGB image")
        return arr
        
    grey = (0.299 * arr[:, :, 0] + 
            0.587 * arr[:, :, 1] + 
            0.114 * arr[:, :, 2]).astype(np.uint8)
    return grey


def ft_red(arr: np.ndarray) -> np.ndarray:
    if arr.ndim != 3 or arr.shape[2] != 3:
        print("Error: not an RGB image")
        return arr
    red_img = arr.copy()
    red_img[:, :, 1] = 0
    red_img[:, :, 2] = 0

    return red_img
        


def main():
    if len(sys.argv) != 2:
        print("Error")
        sys.exit(1)

    path = sys.argv[1]
    arr = load_image(path)
    if arr is None:
        sys.exit(1)
    
    invert = ft_invert(arr)
    display_image(invert, "invert")

    plt.imshow(ft_grey(arr), cmap="gray")
    plt.title("Image en niveaux de gris")
    plt.show()
    #display_image(grey, "grey")

    rouge = ft_red(arr)
    display_image(rouge, "rouge")

    

if __name__ == "__main__":
    main()