# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    S1E9.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 09:17:34 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 09:33:59 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        pass
        #self.is_alive = False

class Stark(Character):
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        self.is_alive = False
    


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

if __name__ == "__main__":
    main()