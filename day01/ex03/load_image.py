# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    load_image.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 15:55:51 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 16:09:03 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
import numpy as np

def ft_load():
    try:
        img = Image.open("animal.jpeg")
    except FileNotFoundError:
        print("fichier introuvable")
        return None 
    except OseError:
        print("format du fichier non supporte")
        return None

    img = img.convert("RGB")
    pixels = np.array(img)
    print("The shape of image is:", pixels.shape)
    print(f"{pixels}\n")
    print("New shape after slicing: (400, 400, 1) or (400, 400)")
    print(pixels[0:400])
    
    

def main():
    ft_load()

if __name__ =="__main__":
    main()