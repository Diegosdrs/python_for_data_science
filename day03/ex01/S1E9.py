# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    S1E9.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 09:17:34 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 09:58:04 by dsindres         ###   ########.fr        #
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
