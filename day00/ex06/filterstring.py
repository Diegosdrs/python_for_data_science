# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterstring.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 10:57:24 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 11:25:07 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def main():
    if (len(sys.argv) != 3):
        print("AssertionError: more or less than two argument is provided")
        sys.exit(1)

    try:
        number = int(sys.argv[2])
    except ValueError:
        print("AssertionError: second parameter is not an integer")
        sys.exit(1)

    text = sys.argv[1]

    for char in text:
        if char in string.punctuation:
            print("AssertionError: there is punctuation")
            sys.exit(1)

    words = text.split()
    
    filtered = [word for word in words if (lambda w: len(w) > number)(word)]
    print(filtered)
            

if __name__ == "__main__":
    main()
    