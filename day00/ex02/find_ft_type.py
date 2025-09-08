# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/08 16:19:32 by dsindres          #+#    #+#              #
#    Updated: 2025/09/08 16:32:03 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):
        if object == "Brian":
            print(f"Brian is in the kitchen : {type(object)}")
        elif object == "Toto":
            print(f"Toto is in the kitchen : {type(object)}")
        else:
            print("Type not found")
    else:
        print("Type not found")
    return 42


if __name__ == "__main__":
    # Ici rien ne doit s’exécuter (donc pas d’appel à la fonction)
    pass
