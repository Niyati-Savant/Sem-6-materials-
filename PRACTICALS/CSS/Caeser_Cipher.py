lst_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']


def Caeser_Cipher_encrypt(plaintxt, key):
    print("Encryption Process")
    key = key % 26
    cipher_txt = ""
    for letter in plaintxt:
        if letter in lst_alphabet:
            p = lst_alphabet.index(letter)

            val = (p + key) % 26
            E_p = (lst_alphabet[val]).upper()
            print(f"{letter} = ({p}+{key})%26 = {val} = {E_p}")
            cipher_txt += E_p
        else:
            print(" ")
            cipher_txt += " "
    print(f"The Encrypted text is: {cipher_txt}")


def Caeser_Cipher_decrypt(ciphertxt, key):
    print("Decryption Process")
    key = key % 26
    plain_txt = ""
    ciphertxt = ciphertxt.lower()
    for letter in ciphertxt:
        if letter in lst_alphabet:
            c = lst_alphabet.index(letter)
            val = (c - key) % 26
            D_c = (lst_alphabet[val])
            print(f"{letter.upper()} = ({c}-{key})%26 = {val} = {D_c}")
            plain_txt += D_c
        else:
            print(" ")
            plain_txt += " "
    print(f"The Decrypted text is: {plain_txt}")

print("Niyati's code for Caeser Cipher - ")
print("Enter 1 for encryption,2 for decryption")
user_choice = input("Enter choice: ")

txt = input("Enter text: ")
k = int(input("Enter key Value: "))

if user_choice== '1':
    txt = txt.lower()
    Caeser_Cipher_encrypt(txt,k)

elif user_choice=='2':
    txt = txt.upper()
    Caeser_Cipher_decrypt(txt,k)


# Diffie-Hellman Code


# def prime_checker(p):
# 	# Checks If the number entered is a Prime Number or not
# 	if p < 1:
# 		return -1
# 	elif p > 1:
# 		if p == 2:
# 			return 1
# 		for i in range(2, p):
# 			if p % i == 0:
# 				return -1
# 			return 1


# def primitive_check(g, p, L):
# 	# Checks If The Entered Number Is A Primitive Root Or Not
# 	for i in range(1, p):
# 		L.append(pow(g, i) % p)
# 	for i in range(1, p):
# 		if L.count(i) > 1:
# 			L.clear()
# 			return -1
# 		return 1


# l = []
# while 1:
# 	P = int(input("Enter P : "))
# 	if prime_checker(P) == -1:
# 		print("Number Is Not Prime, Please Enter Again!")
# 		continue
# 	break

# while 1:
# 	G = int(input(f"Enter The Primitive Root Of {P} : "))
# 	if primitive_check(G, P, l) == -1:
# 		print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
# 		continue
# 	break

# # Private Keys
# x1, x2 = int(input("Enter The Private Key Of User 1 : ")), int(
# 	input("Enter The Private Key Of User 2 : "))
# while 1:
# 	if x1 >= P or x2 >= P:
# 		print(f"Private Key Of Both The Users Should Be Less Than {P}!")
# 		continue
# 	break

# # Calculate Public Keys
# y1, y2 = pow(G, x1) % P, pow(G, x2) %  P

# # Generate Secret Keys
# k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

# print(f"\nSecret Key For User 1 Is {k1}\nSecret Key For User 2 Is {k2}\n")

# if k1 == k2:
# 	print("Keys Have Been Exchanged Successfully")
# else:
# 	print("Keys Have Not Been Exchanged Successfully")
