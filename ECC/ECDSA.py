from inspect import signature

from Crypto.Hash import SHA256
#ECC
from  Crypto.PublicKey import ECC
# DSS digital signature standard
from Crypto.Signature import DSS


key = ECC.generate(curve='P-256')


#print(key.pointQ.x)
#print(key.pointQ.y)
#print(key)
#print(key.public_key())

#file= open("myprivatekey.pem" , "wt")
#file.write(key.export_key(format='PEM'))
#file.close()


###########################################################3


message = "transaction #322121 is sent from a to b in bitcoin "

#convert any message to 256 bit hash
message_hash= SHA256.new(message.encode())

signer = DSS.new(key,"fips-186-3")

signature = signer.sign(message_hash)

print(signature)

### verify signature

verifier = DSS.new(key,"fips-186-3")




try:
    verifier.verify(message_hash, signature)
    print("signature is valid")
except ValueError:
    print("signature is invalid")





#print(key.export_key(format='PEM'))




#print(key.public_key().export_key(format='PEM'))


