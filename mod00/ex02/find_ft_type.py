# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: egeraldo <egeraldo@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 14:08:44 by egeraldo          #+#    #+#              #
#    Updated: 2025/12/30 14:08:45 by egeraldo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    tp = type(object)

    if tp.__name__ == "int":
        print("Type not found")
    elif tp.__name__ == "str":
        print(f"{object} is in the kitchen : {tp}")
    else:
        print(f"{tp.__name__.capitalize()} : {tp}")

    return 42
