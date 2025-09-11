# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    callLimit.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/11 13:53:45 by dsindres          #+#    #+#              #
#    Updated: 2025/09/11 14:10:39 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def callLimit(limit: int):
    def callLimiter(function):
        count = 0
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
            else:
                count += 1
                return function(*args, **kwds)
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()

if __name__ == "__main__":
   main()