def xor_byte(xored_string):
    for i in range(255):
        decoded = []
        xored_string_aux = bytes.fromhex(xored_string)
        for k in range(len(xored_string_aux)):
            decoded.append(chr(xored_string_aux[k] ^ i))
        print ("String: " + ''.join(decoded) + " Byte: " + hex(i))

xored_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
xor_byte(xored_string)