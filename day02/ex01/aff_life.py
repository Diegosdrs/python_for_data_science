# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_life.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 12:53:08 by dsindres          #+#    #+#              #
#    Updated: 2025/09/10 13:00:12 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


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
    
        #print("Loading dataset of dimensions", data.shape)
        
        #Affichage lisible
        # print(' '.join(header))  # afficher le hedef main():ader
        # for row in data:
        #     print(' '.join(map(str, row)))  # chaque ligne sans crochets ni array
        
        return data
        
    except Exception as e:
        print(f"Error while loading file: {e}")
        return None


def display_graph(data: np.ndarray) -> None:
    """
    Affiche un graphique de l'espérance de vie d'un pays (campus) en fonction des années.
    data : np.ndarray chargé par load()
    """
    if data is None or len(data) == 0:
        print("No data to display")
        return

    # Récupère les années depuis la première ligne du fichier CSV (header)
    with open("life_expectancy_years.csv", "r") as f:
        header = f.readline().strip().split(',')[1:]  # on enlève la première colonne 'country'
    
    years = [int(y) for y in header]

    # Chercher la ligne correspondant à ton campus (ex: France)
    campus_country = "France"  # change si nécessaire
    row = None
    for r in data:
        if r[0] == campus_country:
            row = r[1:]  # on enlève la colonne 'country'
            break
    
    if row is None:
        print(f"Country {campus_country} not found in dataset")
        return

    # Convertir en float pour le graphe
    values = [float(v) for v in row]

    # Création du graphique
    plt.figure(figsize=(12, 6))
    plt.plot(years, values, marker='o', linestyle='-', color='blue', label=campus_country)
    plt.title(f"Life Expectancy over years for {campus_country}")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
        


def main():
    dataset = load("life_expectancy_years.csv")
    display_graph(dataset)
    

if __name__ == "__main__":
    main()
