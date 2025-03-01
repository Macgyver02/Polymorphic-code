import random
import string

def generate_key(length=8):
    """Generate a random XOR key."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def xor_encrypt(data, key):
    """Encrypt/Decrypt data using XOR."""
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def polymorphic_code():
    """Generate polymorphic variant of the script dynamically."""
    new_key = generate_key()
    obfuscated_code = f"""
import random
import string

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

data = "Hello, Polymorphic World!"
key = "{new_key}"
cipher = xor_encrypt(data, key)
print("Encrypted:", cipher)
print("Decrypted:", xor_encrypt(cipher, key))
"""
    return obfuscated_code

if __name__ == "__main__":
    poly_code = polymorphic_code()
    print("Generated Polymorphic Code:\n")
    print(poly_code)
    exec(poly_code)
