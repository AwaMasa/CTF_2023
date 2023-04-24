from Crypto.Util.number import *
from pwn import *
import re
from fractions import Fraction


# actf = bytes_to_long(f.encode())


# get (n,e,c)
p = remote('challs.actf.co',32400)
ret = p.recv()
output = ret.decode()
n = int(re.search(r"n = (\d+)", output).group(1))
e = int(re.search(r"e = (\d+)", output).group(1))
c = int(re.search(r"c = (\d+)", output).group(1))

bounds = [0,Fraction(n)]
c2 = (c*pow(2,e,n)
p.sendline(b"1")
ret2 = p.recv()

print("e:",e)
print(ret2)

# print(pow(actf,e,n))