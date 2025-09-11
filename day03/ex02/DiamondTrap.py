# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    DiamondTrap.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 10:22:17 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 10:48:21 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from S1E7 import Baratheon, Lannister

class King (Baratheon, Lannister):
    def __init__(self, first_name: str):
        super().__init__(first_name)

    def set_eyes(self, color: str):
        self.eyes = color
        
    def set_hairs(self, color: str):
        self.hairs = color
        
    def get_eyes(self):
        return self.eyes
        
    def get_hairs(self):
        return self.hairs
