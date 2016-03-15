def countBits(n):
    return sum([int(bit) for bit in bin(n) if bit == "1"])