# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    S1E7.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 09:17:34 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 10:51:47 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from S1E9 import Character

# class Stark(Character):
#     def __init__(self, first_name: str, is_alive: bool = True):
#         super().__init__(first_name, is_alive)

#     def die(self) -> None:
#         self.is_alive = False
    

class Baratheon(Character):
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "Brown"
        self.hairs = "Dark"

    def die(self) -> None:
        self.is_alive = False

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
      
    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name: str, is_alive: bool = True):
        return cls(name, is_alive)

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
      
    def __repr__(self):
        return self.__str__()