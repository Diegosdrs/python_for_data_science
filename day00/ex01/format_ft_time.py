# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsindres <dsindres@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/08 16:09:02 by dsindres          #+#    #+#              #
#    Updated: 2025/09/08 16:18:00 by dsindres         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

if __name__ == "__main__":
    now = time.time()
    print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")
    print(time.strftime("%b %d %Y", time.localtime(now)))
