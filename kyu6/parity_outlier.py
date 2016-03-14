def find_outlier(integers):
    PARITY = 0
    if integers[0] % 2 == 0:
        if integers[1] % 2 == 0:
            PARTIY = 0
        else:
            if integers[2] % 2 == 0:
                PARITY = 0
            else:
                PARITY = 1
    else:
        if integers[1] % 2 != 0:
            PARITY = 1
        else:
            if integers[2] % 2 != 0:
                PARITY = 1
            else:
                PARITY = 0
    for number in integers:
        if PARITY == 0:
            if (number % 2) != 0:
                return number
        else:
            if (number % 2) == 0:
                return number