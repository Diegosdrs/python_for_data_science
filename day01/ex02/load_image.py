# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    load_image.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 14:54:03 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 15:44:57 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray: 
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print("fichier introuvable")
        return None 
    except OseError:
        print("format du fichier non supporte")
        return None

    print("Format de l'image: ", img.format)
    img = img.convert("RGB")
    pixels = np.array(img)
    print("The shape of image is:", pixels.shape)
    return pixels
    
        
    

def main():
    print(ft_load("landscape.jpg"))

if __name__ =="__main__":
    main()