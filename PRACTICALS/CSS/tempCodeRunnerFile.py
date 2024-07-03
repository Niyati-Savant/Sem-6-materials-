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

