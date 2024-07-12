from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Datos para cifrar
data = b"Este es el texto que vamos a cifrar. Es confidencial."

# AES
def aes_encryption(data):
    key = b'\x01'*32  # Clave AES de 256 bits
    iv = b'\x00'*16   # Vector de inicialización
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(data) + encryptor.finalize()
    return ct

def aes_decryption(ct):
    key = b'\x01'*32
    iv = b'\x00'*16
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ct) + decryptor.finalize()
    return decrypted

# DES
def des_encryption(data):
    key = b'\x02'*8
    iv = b'\x00'*8
    cipher = Cipher(algorithms.TripleDES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(data) + encryptor.finalize()
    return ct

def des_decryption(ct):
    key = b'\x02'*8
    iv = b'\x00'*8
    cipher = Cipher(algorithms.TripleDES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ct) + decryptor.finalize()
    return decrypted



# Ejemplo de uso
ct_aes = aes_encryption(data)
decrypted_aes = aes_decryption(ct_aes)
print(f"Encrypted AES: {ct_aes}")
print(f"Decrypted AES: {decrypted_aes}")

ct_des = des_encryption(data)
decrypted_des = des_decryption(ct_des)
print(f"Encrypted DES: {ct_des}")
print(f"Decrypted DES: {decrypted_des}")

ct_rsa, rsa_private = rsa_encryption(data)
decrypted_rsa = rsa_decryption(ct_rsa, rsa_private)
print(f"Encrypted DES: {ct_rsa}")
print(f"Decrypted RSA: {decrypted_rsa}")
