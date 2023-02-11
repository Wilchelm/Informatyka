#!/usr/bin/python3

#sudo apt-get install -y python3-gmpy2

import binascii
import time
import gmpy2
 
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def decrypt(c):
  m1 = pow(c, dp, p)
  m2 = pow(c, dq, q)
  h = (qinv * (m1 - m2)) % p 
  m = m2 + h * q
  return m
 
p = 1090660992520643446103273789680343
q = 1162435056374824133712043309728653
e = 65537
m = 83678269879577658472958479799572658268
ct = pow(m,e,(p*q))
#ct = 299604539773691895576847697095098784338054746292313044353582078965
 
dp = gmpy2.invert(e, (p-1))
dq = gmpy2.invert(e, (q-1))
qinv = gmpy2.invert(q, p)

# compute n
n = p * q
 
# Calulate phi phi(n)
phi = (p - 1) * (q - 1)
 
# Computation of modular inverse of e
gcd, a, b = egcd(e, phi)
d = a

print("Ciphertext:", ct)
# Decryption of ciphertext
start1 = time.time()
pt = pow(ct, d, n)
end1 = time.time()
print( "Decryped text",pt, "\nin time:", '{:f}'.format(end1-start1))
start2 = time.time()
pt2 = decrypt(ct)
end2 = time.time()
print( "\n\nDecrypted text",pt2,"\nin time:",'{:f}'.format(end2-start2))
