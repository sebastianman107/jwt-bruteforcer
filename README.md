# JWT token brute forcer

## This is a python script for cracking the JWT token.

Usage:
` python3 jwt_secret.py <jwt_token> [<chars>] [<length>] `

where:
jwt_token: full HS256 JWT token \n
chars: optional characters to included in bruteforcing (default "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") \n
length: the length of the secret \n

Example usage:
` python3 jwt_secret.py 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.TeFEGHKT2ZnIRduOnDVbzPeW8CxkH80S7H_5ZuOdV4I' 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 4 ` \n
Output: \n
Secret found: test \n
python3 jwt_secret.py  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  32.39s user 0.97s system 97% cpu 34.346 total \n

Requirements:
python3