#!/usr/bin/python3 -u
from Crypto.Cipher import DES
import binascii
import itertools
import random
import string


def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def generate_key():
    return pad("".join(random.choice(string.digits) for _ in range(6)))
    
    
    


def get_input():
    try:
        res = binascii.unhexlify(input("What data would you like to encrypt? ").rstrip()).decode()
    except:
        res = None
    return res

def double_encrypt(m):
    msg = pad(m)
    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(msg)
    cipher2 = DES.new(KEY2, DES.MODE_ECB)
    return binascii.hexlify(cipher2.encrypt(enc_msg)).decode()

flag=binascii.unhexlify("748bef2b8b4703269c86df8acead9873f11097548834233f77aca41b266899efcfd10fc0500d8f48")
ciphertext=binascii.unhexlify("e03e88363f709b28")
inputs = (binascii.unhexlify("41").decode())
inputs = pad(inputs)
mydict = {}

for KEY1tuple in itertools.product(string.digits, repeat=6):
    KEY1t = pad(''.join(KEY1tuple))
    cipher1 = DES.new(KEY1t, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(inputs)
    mydict[enc_msg] = KEY1t
    
for KEY2tuple in itertools.product(string.digits, repeat=6):
    KEY2t = pad(''.join(KEY2tuple))
    cipher2 = DES.new(KEY2t, DES.MODE_ECB)
    dec_msg = cipher2.decrypt(ciphertext)
    if dec_msg in mydict:
        KEY1t = mydict[dec_msg]
        print(KEY1t)
        print(KEY2t)
        dec_msg = cipher2.decrypt(flag)
        cipher1 = DES.new(KEY1t,DES.MODE_ECB)
        dec_msg = cipher1.decrypt(dec_msg)
        print(dec_msg)
        break


