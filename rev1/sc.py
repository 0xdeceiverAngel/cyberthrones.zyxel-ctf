from pwn import *
r=process("./a.out")
rec=r.recv()
print(rec)
r=process("./guess")
r.sendline(rec)
r.interactive()
