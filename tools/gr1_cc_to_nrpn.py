#!/usr/bin/python
# Converts CC to NRPN (according to GR-1's manual)
import sys


def main():
    if len(sys.argv) < 2:
        print(f'Syntax: {sys.argv[0]} <cc number>')
        sys.exit(1)

    cc = int(sys.argv[1])
    msb = (cc >> 7) & 0x7f
    lsb = cc & 0x7f

    print(f'MSB {msb} LSB {lsb}')


if __name__ == '__main__':
    main()
