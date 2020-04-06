import binascii

#Equal len xor

def equal_xor(hex_string, key):
    xored_string = []
    hex_string = bytes.fromhex(hex_string)
    key = bytes.fromhex(key)
    
    for i in range(len(hex_string)):
        xored_string.append(hex(hex_string[i] ^ key[i]))
    return ''.join(xored_string).replace("0x", "")

hex_string = '1c0111001f010100061a024b53535009181c'
key = '686974207468652062756c6c277320657965'
print(equal_xor(hex_string, key))

