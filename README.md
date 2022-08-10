# JWT token brute forcer

### This is a python script for bruteforcing the JWT token using a predefined secrets list.

Usage:
1. Replace the "payload" value in the jwt_secret.py by adding decoded payload from the known JWT token.
2. Replace the "sample_jwt" value in the jwt_secret.py by adding the known encoded JWT token.
3. Run the script "python3 jwt_secret.py <sample_secrets.txt>" with the secret list file name as an argument.