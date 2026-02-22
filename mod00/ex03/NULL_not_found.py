# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: egeraldo <egeraldo@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 14:08:51 by egeraldo          #+#    #+#              #
#    Updated: 2025/12/30 14:08:52 by egeraldo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
    try:
        tp = type(object)
        if object is None:
            print(f"Nothing: {object} {tp}")
        elif tp is float:
            print(f"Cheese: {object} {tp}")
        elif tp is int:
            print(f"Zero: {object} {tp}")
        elif tp is str and object == "":
            print(f"Empty: {object} {tp}")
        elif tp is bool and not object:
            print(f"Fake: {object} {tp}")
        else:
            raise TypeError("Type not Found")
        return 0
    except TypeError as e:
        print(e)
        return 1
