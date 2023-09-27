def decrypt(hex_values, key):
    plaintext = ""
    decrypted_decimals = []
    key_length = len(key)
    for i in range(len(hex_values)):
        hex_byte = hex_values[i]
        key_byte = ord(key[i % key_length])
        decrypted_byte = hex_byte ^ key_byte
        plaintext += chr(decrypted_byte)
        decrypted_decimals.append(decrypted_byte)
    return plaintext, decrypted_decimals

encrypted_hex = [0x0c, 0x3b, 0x13, 0x2d, 0x23, 0x2a, 0x2f, 0x16, 0x26, 0x39, 0x36]
key = "ABC"

plaintext, decrypted_decimals = decrypt(encrypted_hex, key)
print("Decrypted plaintext:", plaintext)
print("Decrypted decimals:", decrypted_decimals)
