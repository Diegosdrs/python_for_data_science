# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    load_csv.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 11:29:23 by dsindres          #+#    #+#              #
#    Updated: 2025/09/10 12:51:46 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd
from pathlib import Path


def load(path: str) -> np.ndarray:
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        print("Error: file not found")
        return None
    
    try:
        # On utilise numpy pour lire le CSV en gardant les headers
        with open(path, 'r') as f:
            lines = f.readlines()
        
        # Extraire le header et les données
        header = lines[0].strip().split(',')
        data_lines = [line.strip().split(',') for line in lines[1:]]
        
        
        # Convertir en array numpy, en essayant de convertir en float quand c'est possible
        data = np.array([[float(x) if x.replace('.', '', 1).isdigit() else x for x in row] 
                         for row in data_lines], dtype=object)
    
        print("Loading dataset of dimensions", data.shape)
        
        #Affichage lisible
        print(' '.join(header))  # afficher le header
        for row in data:
            print(' '.join(map(str, row)))  # chaque ligne sans crochets ni array
        
        return data
        
    except Exception as e:
        print(f"Error while loading file: {e}")
        return None


def main():
    dataset = load("life_expectancy_years.csv")
    #print (dataset)


if __name__=="__main__":
    main()