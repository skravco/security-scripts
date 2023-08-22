from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA 
from Crypto.Random import get_random_bytes

class EncryptionTool:

    def generate_rsa_key(self):
        # Generate an RSA key pair of 2048 bits
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    def rsa_encrypt(self, data, public_key):
        # Import the recipient's RSA public key
        recipient_key = RSA.import_key(public_key)
        # Create an RSA cipher using PKCS1_OAEP padding
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        # Encrypt the data using the RSA cipher
        encrypted_data = cipher_rsa.encrypt(data.encode())
        return encrypted_data

    def rsa_decrypt(self, encrypted_data, private_key):
        # Import the recipient's RSA private key
        key = RSA.import_key(private_key)
        # Create an RSA cipher using PKCS1_OAEP padding
        cipher_rsa = PKCS1_OAEP.new(key)
        # Decrypt the encrypted data using the RSA cipher
        decrypted_data = cipher_rsa.decrypt(encrypted_data).decode()
        return decrypted_data

    def aes_encrypt(self, data, key):
        # Generate a random nonce and create an AES cipher
        nonce = get_random_bytes(16)
        cipher_aes = AES.new(key, AES.MODE_EAX, nonce=nonce)
        # Encrypt the data using the AES cipher
        encrypted_data, tag = cipher_aes.encrypt_and_digest(data.encode())
        return encrypted_data, nonce, tag

    def aes_decrypt(self, encrypted_data, key, nonce, tag):
        # Create an AES cipher with the provided nonce
        cipher_aes = AES.new(key, AES.MODE_EAX, nonce=nonce)
        # Decrypt the encrypted data and verify the authenticity using the tag
        decrypted_data = cipher_aes.decrypt_and_verify(encrypted_data, tag).decode()
        return decrypted_data
        
# Create an instance of EncryptionTool
encryption_tool = EncryptionTool()

# Generate an RSA key pair
private_key, public_key = encryption_tool.generate_rsa_key()

# Encrypt and decrypt data using RSA encryption
encrypted_data = encryption_tool.rsa_encrypt('success!', public_key)
decrypted_data = encryption_tool.rsa_decrypt(encrypted_data, private_key)

# Generate a random AES key
aes_key = get_random_bytes(16)

# Encrypt and decrypt data using AES encryption
encrypted_data, nonce, tag = encryption_tool.aes_encrypt('have no idea what is here', aes_key)
decrypted_data = encryption_tool.aes_decrypt(encrypted_data, aes_key, nonce, tag)

# Print the decrypted data
print('Decrypted data:', decrypted_data)
