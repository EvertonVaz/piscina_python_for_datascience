# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: egeraldo <egeraldo@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 14:08:54 by egeraldo          #+#    #+#              #
#    Updated: 2025/12/30 14:08:55 by egeraldo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def what_is():
    if len(sys.argv) < 2:
        return
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        arg = int(sys.argv[1])

        if arg % 2 == 0:
            return print("I'am Even")
        return print("I'am Odd")

    except Exception:
        print("AssertionError: argument is not an integer")


what_is()
