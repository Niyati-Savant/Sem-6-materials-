import math


def gcd(a, b):
    r1 = a
    r2 = b
    while r2 > 0:
        quotient = int(r1 / r2)
        remainder = r1 % r2

        r1 = r2
        r2 = remainder
    return r1


print("Niyati's code for RSA algorithm")
p = int(input("Enter The value of p: "))
q = int(input("Enter The value of q: "))
n = p * q
print(f"The value of n is {n}")
phi = (p - 1) * (q - 1)
print(f"The value of phi({n}) is {phi}")
e = int(input(f"Enter encryption key e such that e and phi({n}) are co prime and e < phi({n}): "))
print(f"The public key is ({e},{n})")
for k in range(15):
    d = (1 + (k * phi)) / e
    if (int(d) == d):
        d = int(d)
        break

print(f"The private key is ({d},{n})")

msg = int(input("Enter Message: "))

print("Encryption is C = (msg ^ e) mod n")
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)

print("Decryption is M = (C ^ d) mod n")
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)
