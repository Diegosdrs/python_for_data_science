# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 11:27:21 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 13:23:43 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main():
    if (len(sys.argv) != 2):
        print("AssertionError")
        sys.exit(1)

    text = sys.argv[1]

    for char in text:
        if not char.isalnum() and not char.isspace():
            print("AssertionError")
            sys.exit(1)

    morse = {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        " ": "/"
    }

    new_text = text.upper()
    
    morse_text = [morse[char] for char in new_text]
    print(" ".join(morse_text))

        
    


if __name__ == "__main__":
    main()