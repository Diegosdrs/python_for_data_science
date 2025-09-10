# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rotate.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 09:51:55 by dsindres          #+#    #+#              #
#    Updated: 2025/09/10 10:50:33 by dsindres         ###   ########.fr        #
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
        
def cropped_image(img: np.ndarray, crop_h: int, crop_w: int) -> np.ndarray:
    start_y = max((img.shape[0] - crop_h) // 2, 0)
    start_x = max((img.shape[1] - crop_w) // 2, 0)

    end_y = min(start_y + crop_h, img.shape[0])
    end_x = min(start_x + crop_w, img.shape[1])
    
    return img[start_y:end_y, start_x:end_x]


def display_image(img: np.ndarray, title: str) -> None:
    if img.ndim == 3 and img.shape[2] == 3:
        cmap = None
        imshow_arg = img
    else:
        cmap = "gray"
        imshow_arg = img

    #creation de a figure
    fig, ax = plt.subplots(figsize=(6, 6))

    #afficher image + set le titre
    ax.imshow(imshow_arg, cmap=cmap)
    ax.set_title(title)

    h, w = img.shape[:2]

    step_y = max(h // 8, 1)
    step_x = max(w // 8, 1)

    ax.set_yticks(np.arange(0, h, step_y))
    ax.set_xticks(np.arange(0, w, step_x))

    ax.set_xlabel("X (pixels)")
    ax.set_ylabel("Y (pixels)")

    ax.grid(color="red", linestyle="--", linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.show()
    

def main():
    if len(sys.argv) != 2:
        print("Assertion error")
        sys.exit(1)
        
    path = sys.argv[1]
    arr = load_image(path)
    if arr is None:
        sys.exit(1)
    print(arr)

    cropped = cropped_image(arr, 400, 400)
    print("New shape after slicing:", cropped.shape)

    
    if arr.ndim == 3 and arr.shape[2] == 3:
        gray = (0.299 * cropped[:, :, 0] +
                0.587 * cropped[:, :, 1] +
                0.114 * cropped[:, :, 2]).astype(np.uint8)
        #print(f"The shape of the image is: {arr.shape}")
        print(gray)
    else:
        #print(f"The shape of the image is: {arr.shape}")
        print(cropped)

    transposed = np.array([[gray[j][i] for j in range(len(gray))] for i in range(len(gray[0]))], dtype=np.uint8)
    print("New shape after Transpose:", (len(transposed), len(transposed[0])))
    print(transposed)

    try:
        display_image(transposed, "Image renversee")
    except Exception as e:
        print("Error: while displaying the image")
        

    

if __name__ == "__main__":
    main()