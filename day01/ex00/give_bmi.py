# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    give_bmi.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 13:27:55 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 14:18:26 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        print("AssertionError")
        sys.exit(1)

    for w, h in zip(weight, height):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            print("AssertionError")
            sys.exit(1)
        
    bmi = []
    for wi, hi in zip(weight, height):
        bmi.append(wi / (hi ** 2))
    
    return bmi
    
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        value = int(limit)
    except ValueError:
        print("AssertionError")
        sys.exit(1)

    app = []
    for val in bmi:
        if val > limit:
            app.append(True)
        else:
            app.append(False)

    # return [val > limit for val in bmi] ou ca aussi
            
    return app
