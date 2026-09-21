from naggetscipher import *
import time


a = 'apple'
encrypted_text = NaggetsCipher.encrypt(a)
print(encrypted_text)

b = 'яблоко'
encrypted_text = NaggetsCipher.encrypt(b)
print(encrypted_text)