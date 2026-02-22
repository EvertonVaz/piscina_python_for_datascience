# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterstring.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: egeraldo <egeraldo@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 14:09:04 by egeraldo          #+#    #+#              #
#    Updated: 2025/12/30 14:09:05 by egeraldo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from ft_filter import ft_filter


def main(ac: int, av: list[str]) -> None:
    if ac != 3:
        raise AssertionError("the arguments are bad")

    input = av[1].split(" ")
    length = int(av[2])
    result_builtin = list(ft_filter(lambda s: len(s) > length, input))
    return print(result_builtin)


if __name__ == "__main__":
    try:
        main(len(sys.argv), sys.argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")