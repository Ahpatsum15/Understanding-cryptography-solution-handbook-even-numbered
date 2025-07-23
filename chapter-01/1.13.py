#Affine cipher 1.13

#it's in the form y = a.x + b mod 26
#in our case a = 7, 7*15 =1 mod 26

alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipher= 'falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj'

def affine_decypher(text,a,b):
    m = ''
    for e in text:
        if e in alphabet:
            i = (alphabet.index(e)-b)%26
            m+= alphabet[(pow(a,-1,26)*i)%26]
        else:
            m+= e
    return m

print(affine_decypher(cipher,7,22))

#answer: first the sentence and then the evidence said the queen
#it's from alice in wonderlands by lewis carrol (he was also mathematics professor)

