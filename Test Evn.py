# # Test Evn
import hashlib
import base64
import AES
import os



key = b'1234567890123456'
# key = os.urandom(16) 
# iv = os.urandom(16) 
iv = b'1234567890123456'
# encrypted = AES.AES(key).encrypt_ctr(b'Thehash', iv)

encrypted = AES.AES(key).encrypt_ctr(input('your hash: '), iv)
TheChiper = encrypted
decrypt = AES.AES(key).decrypt_ctr(encrypted, iv)

encoded = base64.b64encode(TheChiper.encode('ascii'))
Hashstring = hashlib.sha256(TheChiper.encode('UTF-8')).hexdigest()



print('base64:' , encoded,"\n" + 'sha256: ' ,Hashstring,'\n','AES: ',encrypted)
print('Decoded Hash')
print(encoded.decode('ascii'),"\n" ,decrypt)



# aes = AES.new(key, AES.MODE_CBC, iv)
# def encrypt_payload(cipher,data):
#     return cipher.encrypt(data)

# def decrypt_payload(cipher, payload):
#     return cipher.decrypt(payload)
 
# AESdecode = AES.new(key, AES.MODE_GCM, iv)
# decd = AESChiper.decrypt(bytes(encd))

# print(encrypt_payload(AESChiper,data))
# print(decrypt_payload(AESChiper,encrypt_payload(AESChiper,data)))

#print("Encrypted data:" + encrypted)
# print(AESChiper.encrypt(data))









    









