# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/08 16:22:43 by dsindres          #+#    #+#              #
#    Updated: 2025/09/08 16:39:39 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from NULL_not_found import NULL_not_found


if __name__ == "__main__":
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = "’’"
    Fake = False
    
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    
    print(NULL_not_found("Brian"))