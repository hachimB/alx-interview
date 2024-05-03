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
#         if isinstance(code, int):
#             print("{}: {}".format(code, status_codes[code]))


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
import re
import signal

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_counter = 0

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    match = re.match(
        r'^\S+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
        line)
    if match:
        code = int(match.group(1))
        size = int(match.group(2))
        if code in status_codes:
            status_codes[code] += 1
        total_size += size
        line_counter += 1
        if line_counter % 10 == 0:
            print_stats()

print_stats()
