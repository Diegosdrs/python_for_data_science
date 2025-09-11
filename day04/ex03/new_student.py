# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    new_student.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 14:17:14 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 14:30:52 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()

def main():
    student = Student(name="Edward", surname="agle")
    print(student)

if __name__ == "__main__":
    main()