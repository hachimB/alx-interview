#!/usr/bin/python3
"""Module documentation"""


# def validUTF8(data):
#     # Variable to track the number of expected bytes following the current byte
#     num_bytes_to_follow = 0

#     # Iterate over each integer in the data set
#     for byte in data:
#         # Check if the current byte represents the start of a new UTF-8
#         # character
#         if num_bytes_to_follow == 0:
#             # Count the number of leading 1s in the byte
#             mask = 1 << 7
#             while mask & byte:
#                 num_bytes_to_follow += 1
#                 mask >>= 1

#             # Invalid start byte if num_bytes_to_follow is 0 or greater than 4
#             if num_bytes_to_follow == 1 or num_bytes_to_follow > 4:
#                 return False

#             # If num_bytes_to_follow is 0, the byte is a single ASCII character
#             if num_bytes_to_follow == 0:
#                 continue

#         # If num_bytes_to_follow is not 0, the current byte should start with
#         # "10"
#         elif byte >> 6 != 0b10:
#             return False

#         # Decrease the count of expected bytes following the current byte
#         num_bytes_to_follow -= 1

#     # If num_bytes_to_follow is 0 at the end of the loop, all characters are
#     # valid
#     return num_bytes_to_follow == 0

def validUTF8(data):
    num_bytes_to_follow = 0
    
    for byte in data:
        if num_bytes_to_follow == 0:
            if (byte >> 3) == 0b11110:
                num_bytes_to_follow = 3
            elif (byte >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (byte >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (byte >> 7) & 1:  # Check if MSB is set
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1
    
    return num_bytes_to_follow == 0
