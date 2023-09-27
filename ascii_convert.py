#print(ord("A"))
#print(chr(65))
#print(hex(65))



#decimal_values = {65,66,67}

#byte_stream = bytes(decimal_values)

#print(byte_stream)


#import base64

plainText = "A"
password = "B"


ascii_decimal = ord(plainText)^ord(password)

#ascii_human = chr(ascii_decimal)

ascii_hex = hex(ascii_decimal)

print(ascii_hex)

ascii_decrypted = int(ascii_hex, 16) ^ ord(password)

print(ascii_decrypted)

print(chr(ascii_decrypted))

#base64_encoded = base64.b64encode(ascii_human.encode('utf-8')).decode('utf-8')

#print(base64_encoded)
