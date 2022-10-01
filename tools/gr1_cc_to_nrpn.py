#!/usr/bin/python
# Converts CC to NRPN (at least according to GR-1's manual)

import sys

cc = int(sys.argv[1])
msb = (cc & (0x7f << 7)) >> 7
lsb = cc & 0x7f

print(f'{msb}:{lsb}:14')
