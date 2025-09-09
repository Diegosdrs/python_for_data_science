# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/09 13:49:26 by dsindres          #+#    #+#              #
#    Updated: 2025/09/09 14:17:09 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from give_bmi import give_bmi, apply_limit

if __name__ == "__main__":
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 66))
