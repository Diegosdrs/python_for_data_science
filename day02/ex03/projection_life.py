# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    projection_life_2.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 14:14:58 by dsindres          #+#    #+#              #
#    Updated: 2025/09/10 15:18:45 by dsindres         ###   ########.fr        #
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
        with open(path, 'r') as f:
            lines = f.readlines()
        
        header = lines[0].strip().split(',')
        data_lines = [line.strip().split(',') for line in lines[1:]]
        
        data = np.array([[float(x) if x.replace('.', '', 1).isdigit() else x for x in row] 
                         for row in data_lines], dtype=object)                        
        return data
        
    except Exception as e:
        print(f"Error while loading file: {e}")
        return None

def display_graph(life: np.ndarray, pib: np.ndarray, year: str) -> None:
    if len(life) == 0 or len(pib) == 0 or life is None or pib is None:
        print("Error")
        return

    with open("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", 'r') as f:
        pib_header = f.readline().strip().split(",")

    with open("life_expectancy_years.csv", 'r') as f:
        life_header = f.readline().strip().split(",")

    try:
        life_year_index = life_header.index(year)
        pib_year_index = pib_header.index(year)
    except ValueError:
        print("Error: Year not found")
        return
        
    life_1900 = []
    pib_1900 = []
    
    life_countries = [row[0] for row in life]  # Première colonne = pays
    pib_countries = [row[0] for row in pib]    # Première colonne = pays
    
    for i, life_country in enumerate(life_countries):
        try:
            # Chercher le pays correspondant dans le fichier PIB
            pib_index = pib_countries.index(life_country)
            
            life_value = life[i][life_year_index]
            pib_value = pib[pib_index][pib_year_index]
            
            # CORRECTION 5: Vérifier que les valeurs sont numériques
            if (isinstance(life_value, (int, float)) and 
                isinstance(pib_value, (int, float)) and 
                not np.isnan(float(life_value)) and 
                not np.isnan(float(pib_value))):
                
                life_1900.append(float(life_value))
                pib_1900.append(float(pib_value))
                
        except (ValueError, IndexError):
            continue  # Skip ce pays s'il n'est pas trouvé ou a des données invalides
    
    # Convertir en arrays numpy
    life_1900 = np.array(life_1900)
    pib_1900 = np.array(pib_1900)
     
    print(f"Nombre de pays avec des données valides: {len(life_1900)}")

    plt.scatter(pib_1900, life_1900)
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life expectancy")
    plt.title(f"Life expectancy vs GDP in {year}")
    plt.show()


def main():
    life = load("life_expectancy_years.csv")
    pib = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    display_graph(life, pib, "1900")
    

if __name__ == "__main__":
    main()