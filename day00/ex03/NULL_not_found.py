# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/08 16:19:32 by dsindres          #+#    #+#              #
#    Updated: 2025/09/08 16:39:07 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1

