# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 10:11:55 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 10:24:33 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("AssertionError: more than one argument is provided")
        sys.exit(1) 

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
               
    if (number % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm odd.")

    