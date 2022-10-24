# JWT token brute forcer

## This is a python script for cracking the JWT token.

Usage:
` python3 jwt_secret.py <jwt_token> [<min_length>] [<max_length>] [<chars>] `

where:
jwt_token: full HS256 JWT token
min_length: the minimum length of the secret (default 1) 
max_length: the maximum length of the secret (default 20)
chars: optional characters to included in bruteforcing (default "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")


Example usage:
python3 jwt_secret.py "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZXhwIjoxNjcxODIwODg1fQ.jP6P7ljkT9bNvg6aik2p4DFwhQPTCRrPrY6L-hOHrhw" 6 7 secrt
Secret found: secret

Requirements:
python3
jwt
itertools
sys