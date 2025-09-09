# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    array2D.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 14:23:33 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 14:50:58 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        print("AssertionError")
        sys.exit(1)


    if not all(isinstance(li, list) for li in family):
            print("AssertionError")
            sys.exit(1)
        
    len_li = len(family[0])

    if not all(len(li) == len_li for li in family):
        print("AssertionError")
        sys.exit(1)

    row = len(family)
    coll = len(family[0])
    print(f"My shape is : ({row}, {coll})")

    # count_row = 0
    # new_f = []
    # for li in family:
    #     if count_row >= abs(start) and count_row < abs(end) and count_row < row:
    #         new_f.append(li)
    #         count_row += 1

    new_f = family[start:end]


    row_new = len(new_f)
    coll_new = len(new_f[0]) if new_f else 0
    print(f"My new shape is : ({row_new}, {coll_new})")
    
    return new_f
        
        