# -*- coding: utf-8 -*-

import codecs
import base64
import numpy as np
import unicodedata as ucd

with open('161.xor', 'rb') as f:
    cipher_text = f.read()

#print(cipher_text.decode("ISO-8859-2"))

with open("test.txt","wb") as f:
    f.write(cipher_text)

print (len(cipher_text))

# Tajny kod zadania:
code_task = cipher_text[10583:10602]
code_task_text = 'Tajny kod zadania: '

short_key = [a ^ ord(b) for (a, b) in zip(code_task, code_task_text)]

#print (short_key)
#for a in short_key:
    #print (chr(a))

short_cipher = [cipher_text[i:i+256] for i in range(0, len(cipher_text), 256)]
for i in short_cipher:
    short_cipher_values = i[87:106]
    decrypted = [a ^ b for (a, b) in zip(short_key, short_cipher_values)]
    #for a in decrypted:
         #print(chr(a), end='')
    #print()

plaintext = 'Tamten drgn\xb9\xb3. Ruchy mia\xb3 p\xb3ynne i niezwykle szybkie. Pojawi\xb3 si\xea naraz ca\xb3y, wyprostowany na owym d\xeaba stoj\xb9cym g\xb3azie, jakby wci\xb9\xbf jeszcze wypatrywa\xb3 tajemniczej przyczyny dw\xf3ch eksplozji. Potem odwr\xf3ci\xb3 si\xea i zeskoczywszy w d\xf3\xb3, zacz\xb9\xb3, lekko pochylony '
print(len(plaintext))

whole_key = [a ^ ord(b) for (a, b) in zip(cipher_text[0:256], plaintext)]
#print(whole_key)

cipher = [cipher_text[i:i+256] for i in range(0, len(cipher_text), 256)]
plain_text = ''
for j in cipher:
    long_cipher_values = j[0:256]
    decrypted_all = [a ^ b for (a, b) in zip(whole_key, long_cipher_values)]
    for b in decrypted_all:
         #print(chr(b), end='')
        plain_text += chr(b)

print(plain_text)

x=plain_text.encode('utf-8')
with open("tekst.txt","w") as f:
    f.write(plain_text)

with open("tekst2.txt","wb") as f:
    f.write(x)
