import jwt
import sys

#DECODED PAYLOAD FROM THE JWT SAMPLE
payload = {
    "user": None
}

#FULL JWT SAMPLE TOKEN (DECODED)
sample_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.Tr0VvdP6rVBGBGuI_luxGCOaz6BbhC6IxRTlKOW8UjM"

if __name__ == "__main__":
    secrets_file = sys.argv[1]
    with open(secrets_file) as f:
            secret_list = f.read().split()
    for secret in secret_list:
        encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")
        if encoded_jwt == sample_jwt:
            print(f"Secret found: {secret}")