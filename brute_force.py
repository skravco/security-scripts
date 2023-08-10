import hashlib
import itertools


def hash_with_sha256(string):
    """
    Hashes a given string using the SHA-256 algorithm.

    Args:
        string (str): The input string to be hashed.

    Returns:
        str: The hexadecimal representation of the hash.
    """
    return hashlib.sha256(string.encode()).hexdigest()


def brute_force(target_hash, charset, maxlength):
    """
    Brute forces a hash by trying all possible combinations of characters from a given charset up to a maximum length.

    Args:
        target_hash (str): The target hash to be matched.
        charset (str): The character set used for generating combinations.
        maxlength (int): The maximum length of the generated combinations.

    Returns:
        str or None: The matched combination that produces the target hash, or None if not found.
    """
    for length in range(1, maxlength + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt = ''.join(attempt)
            guess_hash = hash_with_sha256(attempt)
            if guess_hash == target_hash:
                return attempt
    return None


# Define the character set and the hashed password
charset = '0123456789abcdef'
hashed_password = hash_with_sha256('cafe23')

# Attempt to brute force the password and print the result
print(brute_force(hashed_password, charset, 6))
