## Ex 1.2
from collections import Counter

cipher = '''xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Filter the cipher to only include letters in the alphabet
filtered_cipher = ''.join([c for c in cipher if c in alphabet])

# Frequency analysis on filtered text
freq_order_cipher = [c for c, _ in Counter(filtered_cipher).most_common()]

def shift_cipher(text, n):
    code = ''
    for e in text:
        if e in alphabet:
            code += alphabet[(alphabet.index(e) + n) % 26]
        else:
            code += e
    return code

def shift_decrypt(text, n):
    code = ''
    for e in text:
        if e in alphabet:
            code += alphabet[(alphabet.index(e) - n) % 26]
        else:
            code += e
    return code

# Guess shift by aligning most frequent cipher letter to 'e'
most_common_letter = freq_order_cipher[0]
shift = (alphabet.index(most_common_letter) - alphabet.index('e')) % 26

# Decrypt using the guessed shift
print("Most common letter:", most_common_letter)
print("Guessed shift:", shift)
print("Decrypted text:")
print(shift_decrypt(cipher, shift))

#The answer then is "if we all unite we will cause the rivers to stain the great waters with their blood" _Tecumseh speech to the osages
