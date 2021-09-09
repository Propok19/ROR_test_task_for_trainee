encrypt_array = [] # creating future array with encrypted words for easier way to decrypt this words in the future

def encrypt(text, n):
    if not text or text is None or n <= 0:
        encrypted_text = text
        print(encrypted_text)
    else:
        i = 1
        encrypt_array.append(text)
        while i <= n:
           encrypted_text = text[1::2] + text[0::2] # concatenating even (text[1::2]) and odd (text[0::2]) characters
           print(encrypted_text.lower()) # setting lowercase for encrypted word
           text = encrypted_text
           encrypt_array.append(encrypted_text)
           i+=1


def decrypt(encrypt_array, n):
    if not encrypt_array or encrypt_array is None or n <= 0:
        decrypted_text = encrypt_array
        print(decrypted_text)
    else:
        while n >= 0:
           decrypted_text = encrypt_array[n]
           print(decrypted_text.lower())
           n-=1
           

print('Encrypted text:')
encrypt("Abcdefghij", 2)
print('\nDecrypted text:')
decrypt(encrypt_array, 2)
