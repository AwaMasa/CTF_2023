import gmpy2
from Crypto.Util.number import *
from sympy import isprime

ct = 1471008558899965874655048493052767780401586538366045232356405469999470920009
d = 23253315394144849295935820351052537635670172871279133337364403317334766527377
e = 65537
# print(pow(ct,d))

# phi = d*e -1 
# flag = long_to_bytes(pow(ct, d, phi))
# print(f'{phi = }')
# print(f"{flag = }")

# for i in range(100):
#     phi = d*e // (i+1)
#     print(phi)
#     flag = long_to_bytes(pow(ct, d, phi))
#     print(flag)
#     print(f"{flag = }")
# el1 = [109244465871822933443784547013,19079454912872049277533432209]
# el2 = [2,2,2,2,3,5,5,719,1543,1831,700963 , 109831]

def gori():
    b =[2,2,18661,28056361,1568162354407270827499647648637,199]
    x =1
    for i in range(len(b)):
        x *= b[i]
    print(x)
    print(isprime(x+1))

def solve():
    a = [ 2,2,2,2 , 3 , 19 , 31 , 193,199,18661,3142639,28056361,543942193739817147941279,1568162354407270827499647648637]
    print(len(a))
    for counter in range(2**len(a)):
        alpha = 1
        beta = 1
        selector = "{:014b}".format(counter)
        for index, ch in enumerate(selector):
            if (ch == "1"):
                alpha *= a[index]
            else:
                beta *= a[index]
        alpha += 1
        beta += 1
        print("alpha = {}: {}, beta = {}: {}".format(alpha, isprime(alpha), beta, isprime(beta)))
        assert (isprime(alpha) and isprime(beta)), [alpha, beta]
        alpha = 1
        beta = 1

def calc_phi():
    phi_n_sub = e * d - 1
    print(phi_n_sub)
    # while (mult_e_d)

calc_phi()
gori()
# solve()


# print(19079454912872049277533432209* 70963 * 1543 * 719 * 2 +1)