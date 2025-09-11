# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_calculator.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 10:57:38 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 11:27:54 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class calculator:
    def __init__(self, vector: list):
        if len(vector) == 0:
            print("Error")
            return
        self.vector = np.array(vector)
    
    def __add__(self, number):
        # result = [float(x + float(number)) for x in self.vector]
        result = self.vector + number
        print (result)

    def __mul__(self, number):
        result = self.vector * number
        print(result)    

    def __sub__(self, number):
        result = self.vector - number
        print(result)  
        
    def __truediv__(self, number):
        if number == 0:
            print("Error: division par zero impossible")
            return
        result = self.vector / number
        print(result)
        
        

def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")

    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")

    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()