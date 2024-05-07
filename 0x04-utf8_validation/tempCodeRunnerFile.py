def validUTF8(data):
    """ValidUTF8"""
    for i in data:
        binary = bin(i)
        if binary[0:2] == 0:
            print()