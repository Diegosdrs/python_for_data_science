# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statistics.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 11:44:38 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 13:29:07 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_statistics(*args: any, **kwargs: any) -> None:
    num = list(args)
    options = dict(kwargs)
    
    if len(num) == 0:
        print("Error")
        return
        
    num.sort()  # classer dans l'ordre croissant
    n = len(num)  # taille
      
    # moyenne
    mean = sum(num) / len(num)
    
    # mediane
    if n % 2 == 0:
        med = (num[n // 2] + num[n // 2 + 1]) / 2
    else:
        med =  num[n // 2]

    # quartiles
    if n % 2 == 0:
        q1 = (num[n // 4] + num[n // 4 + 1]) / 2
        q3 = (num[n // 4 * 3] + num[n // 4 * 3 + 1]) / 2
    else:
        q1 =  num[n // 4]
        q3 =  num[n // 4 * 3]

    # variance
    var = sum((x - mean)**2 for x in num) / n

    # ecart_type
    std = var ** 0.5
       
    for key, stat in options.items():
        if stat == "mean":
            print("mean : ", mean)
        elif stat == "median":
            print ("mediane : ", med)
        elif stat == "quartile":
            print("quartile : ", list[float(q1), float(q3)])
        elif stat == "std":
            print("std: ", std)
        elif stat == "var":
            print("variance: ", var)
            
        

def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")

if __name__ == "__main__":
    main()