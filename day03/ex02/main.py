# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 09:39:07 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 10:45:07 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from S1E7 import Baratheon, Lannister
from DiamondTrap import King


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)          # dictionnaire interne (attributs de l’objet)
    Joffrey.set_eyes("blue")         # change la couleur des yeux
    Joffrey.set_hairs("light")       # change la couleur des cheveux
    print(Joffrey.get_eyes())        # affiche les yeux
    print(Joffrey.get_hairs())       # affiche les cheveux
    print(Joffrey.__dict__)          # re-vérifie le contenu de l’objet


if __name__ == "__main__":
    main()