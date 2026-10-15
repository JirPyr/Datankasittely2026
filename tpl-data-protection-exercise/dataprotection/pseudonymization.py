from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""
key = Fernet.generate_key()
f = Fernet(key)


def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """
    encrypted_names = []
    for name in names:
        token = f.encrypt(name.encode())
        encrypted_names.append(token.decode())
    return encrypted_names

    pass


def restore_names(encrypted):
    """
    TODO: Decrypt previously pseudonymized names.
    - return list of decrypted names
    """
    decrypted_names = []
    for token in encrypted:
        name = f.decrypt(token.encode()).decode()
        decrypted_names.append(name)
    return decrypted_names

    pass