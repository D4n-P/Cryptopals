import base64

#convert hex string to base64
def convert(x):
    x = bytes.fromhex(x)
    return base64.b64encode(x)

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(convert(hex_string))
