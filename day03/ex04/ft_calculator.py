# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_calculator.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 11:26:37 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 11:41:54 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class calculator:
    def __init__(self):
        pass
       
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = sum(i * j for i, j in zip(V1, V2))
        print(res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = [i + j for i, j in zip(V1, V2)]
        print (res)    

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = [i - j for i, j in zip(V1, V2)]
        print(res)

    

def main():
    a = [5, 10, 2]
    b = [2, 4, 3]

    calculator.dotproduct(a,b)
    calculator.add_vec(a,b)
    calculator.sous_vec(a,b)

if __name__ == "__main__":
    main()