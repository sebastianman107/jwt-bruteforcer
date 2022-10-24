import jwt
import sys
import itertools

if __name__ == "__main__":
    sample_jwt = str(sys.argv[1])
    try:
        min_length = int(sys.argv[2])
    except:
        min_length = 1
    try:
        max_length = int(sys.argv[3])
    except:
        max_length = 20
    try:
        secret_chars = sys.argv[4]
    except:
        secret_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for length in range(min_length, max_length+1):
        perms = itertools.product(secret_chars, repeat = length)
        payload = jwt.decode(sample_jwt, options={"verify_signature": False})
        for secret in perms:
            encoded_jwt = jwt.encode(payload, "".join(secret), algorithm="HS256")
            if encoded_jwt == sample_jwt:
                print(f"Secret found: {''.join(secret)}")
                sys.exit(1)