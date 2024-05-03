#!/usr/bin/python3
"""Module documentation"""
# import sys
# import re
# import signal

# status_codes = {}
# total_size = 0
# line_counter = 0


# def print_stats():
#     """print_stats"""
#     print("File size: {}".format(total_size))
#     for code in sorted(status_codes.keys()):
#         print("{}: {}".format(code, status_codes[code]))


# def signal_handler(sig, frame):
#     """signal_handler"""
#     print_stats()
#     sys.exit(0)


# signal.signal(signal.SIGINT, signal_handler)

# for line in sys.stdin:
#     match = re.match(
#         r'^\S+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
#         line)
#     if match:
#         code = int(match.group(1))
#         size = int(match.group(2))
#         status_codes[code] = status_codes.get(code, 0) + 1
#         total_size += size
#         line_counter += 1
#         if line_counter % 10 == 0:
#             print_stats()

# print_stats()
import sys
import signal

status_codes = {}
total_size = 0
line_counter = 0

def print_stats():
    """print_stats"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """signal_handler"""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split('"')
        status_code_and_size = parts[2].split()
        code = int(status_code_and_size[0])
        size = int(status_code_and_size[1])
        status_codes[code] = status_codes.get(code, 0) + 1
        total_size += size
        line_counter += 1
        if line_counter % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
except IndexError:
    pass

print_stats()