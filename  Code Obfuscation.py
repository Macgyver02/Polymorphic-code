import random
import string
import base64
import hashlib
import time

def generate_key(length=16):
    """Generate a random XOR key."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def xor_encrypt(data, key):
    """Encrypt/Decrypt data using XOR."""
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def generate_algorithm():
    """Generate a dynamic mathematical operation for obfuscation."""
    operations = [
        "result = sum([i**2 for i in range(10)])",
        "result = sum([i*3 for i in range(5, 15)])",
        "result = sum([i%4 for i in range(1, 20)])"
    ]
    return random.choice(operations)

def polymorphic_code():
    """Generate polymorphic variant of the script dynamically."""
    new_key = generate_key()
    encoded_key = base64.b64encode(new_key.encode()).decode()
    var_name = ''.join(random.choices(string.ascii_lowercase, k=6))
    algorithm = generate_algorithm()
    obfuscated_code = f"""
import random
import string
import base64
import time

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def execute_algorithm():
    {algorithm}
    return result

{var_name} = base64.b64decode("{encoded_key}").decode()
print("Executing Polymorphic Competitive Programming Code...")
time.sleep(2)
print("Algorithm Output:", execute_algorithm())
"""
    return obfuscated_code

if __name__ == "__main__":
    poly_code = polymorphic_code()
    print("Generated Polymorphic Code:\n")
    print(poly_code)
    exec(poly_code)
