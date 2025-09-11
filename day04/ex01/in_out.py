# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    in_out.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 13:32:37 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 13:47:55 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def square(x: int | float) -> int | float:
    return x ** 2

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        nonlocal x
        x = function(x)
        return x
    return inner

def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")

    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())

if __name__ == "__main__":
    main()