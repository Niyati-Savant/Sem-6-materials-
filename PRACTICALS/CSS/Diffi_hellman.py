import random

print("Niyati's code for Diffie Hellman ")
p = int(input("Enter P:"))
g = int(input("Enter G:"))
a = random.randint(1, 100)
# a = 2
print(f"Private key of Sender {a} ")

b = random.randint(1, 100)
# b= 3
print(f"Private key of Receiver {b}")
R1 = ((pow(g, a)) % p)
R2 = ((pow(g, b)) % p)
print(f"Sender receives key {R2}  and receiver gets key {R1} ")
print("The symmetric Keys")
Ka = ((pow(R2, a)) % p)
Kb = ((pow(R1, b)) % p)
print(f"Secret key at A = {Ka}")
print(f"Secret key at B = {Kb}")

