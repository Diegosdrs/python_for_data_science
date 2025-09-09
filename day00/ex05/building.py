# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 10:29:54 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 10:49:33 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def display(str):
    majs = 0
    mins = 0
    digit = 0
    sp = 0
    punc = 0
    
    for char in str:
        if char.isupper():
            majs += 1
        if char.islower():
            mins += 1        
        if char.isdigit():
            digit += 1
        if char.isspace():
            sp += 1
        if char in string.punctuation:
            punc += 1

    total = majs + mins + sp + digit + punc

    print(f"The text contains {total} char")
    print(f"{majs} maj, {mins} min, {sp} spaces, {digit} digit et {punc} punctuations !")
            

def main():
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    if (len(sys.argv) == 1):
        print("What is the text to count?")
        str = input("")
        display(str)
    else:
        display(sys.argv[1])


if __name__ == "__main__":
    main()