import jwt
import sys
import itertools

if __name__ == "__main__":
    sample_jwt = str(sys.argv[1])
    try:
        secret_chars = sys.argv[2]
    except:
        secret_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    try:
        secret_length = int(sys.argv[3])
    except:
        secret_length = 12
    perms = itertools.product(secret_chars, repeat = secret_length)
    payload = jwt.decode(sample_jwt, options={"verify_signature": False})

    for secret in perms:
        encoded_jwt = jwt.encode(payload, "".join(secret), algorithm="HS256")
        if encoded_jwt == sample_jwt:
            print(f"Secret found: {''.join(secret)}")
            break