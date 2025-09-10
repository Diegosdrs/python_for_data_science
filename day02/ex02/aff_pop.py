# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_pop.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/10 13:14:41 by dsindres          #+#    #+#              #
#    Updated: 2025/09/10 14:04:45 by dsindres         ###   ########.fr        #
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


def display_graph(data: np.ndarray, country_1: str, country_2: str) -> None:
    if len(data) == 0 or data is None:
        print("Error")
        return

    with open("population_total.csv", 'r') as f:
        header = f.readline().strip().split(',')[1:]
    years = [int(i) for i in header]

    row_1 = None
    row_2 = None
    for i in data:
        if i[0] == country_1:
            row_1 = i[1:]        
        if i[0] == country_2:
            row_2 = i[1:]

    if row_1 is None or row_2 is None:
        print("Error: country not found")
        return

    value_c1 = []
    value_c2 = []
    for i, j in zip(row_1, row_2):
        if i.endswith('M'):
            value_c1.append(float(i[:-1]) * 1_000_000)        
        elif i.endswith('k'):
            value_c1.append(float(i[:-1]) * 1_000) 
        else:
            value_c1.append(float(i))
        if j.endswith('M'):
            value_c2.append(float(j[:-1]) * 1_000_000)        
        elif j.endswith('k'):
            value_c2.append(float(j[:-1]) * 1_000)
        else:
            value_c2.append(float(j))

    plt.plot(years, value_c1, label=country_1)
    plt.plot(years, value_c2, label=country_2)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()

        

def main():
    data = load("population_total.csv")
    display_graph(data, "France", "Belgium")

if __name__ == "__main__":
    main()