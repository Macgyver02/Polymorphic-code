import random
import string
import base64
import hashlib

def generate_key(length=16):
    """Generate a random XOR key."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def xor_encrypt(data, key):
    """Encrypt/Decrypt data using XOR."""
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def generate_license():
    """Generate a license key based on system parameters."""
    sys_identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    license_key = hashlib.sha256(sys_identifier.encode()).hexdigest()[:16]
    return sys_identifier, license_key

def polymorphic_code():
    """Generate polymorphic variant of the script dynamically."""
    new_key = generate_key()
    encoded_key = base64.b64encode(new_key.encode()).decode()
    var_name = ''.join(random.choices(string.ascii_lowercase, k=6))
    sys_id, license_key = generate_license()
    obfuscated_code = f"""
import random
import string
import base64
import hashlib

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def validate_license(license_key):
    sys_identifier = "{sys_id}"
    expected_key = hashlib.sha256(sys_identifier.encode()).hexdigest()[:16]
    return expected_key == license_key

data = "Licensed Software Execution"
{var_name} = base64.b64decode("{encoded_key}").decode()
cipher = xor_encrypt(data, {var_name})

license_key = "{license_key}"
if validate_license(license_key):
    print("License Valid! Executing Code...")
    print("Encrypted:", cipher)
    print("Decrypted:", xor_encrypt(cipher, {var_name}))
else:
    print("Invalid License! Exiting...")
"""
    return obfuscated_code

if __name__ == "__main__":
    poly_code = polymorphic_code()
    print("Generated Polymorphic Code:\n")
    print(poly_code)
    exec(poly_code)
