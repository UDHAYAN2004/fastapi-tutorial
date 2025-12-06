SECRET_KEY="jwtsecretkey1234567890"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# HS256 Explanation
# -----------------
# HS256 stands for "HMAC + SHA256".
#
# H  -> HMAC (Hash-based Message Authentication Code)
# S  -> SHA (Secure Hash Algorithm)
# 256 -> 256-bit hash output
#
# HS256 is a symmetric algorithm, meaning:
# - The SAME secret key is used to SIGN the JWT token
# - The SAME secret key is used to VERIFY the JWT token
#
# Why HS256 is used in JWT?
# - Fast and secure
# - Works well for authentication
# - Easy to implement with a single secret key
#
# Example:
# token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
# data  = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#
# HS256 ensures the token:
# - Is not tampered
# - Comes from your server
# - Is safe to verify and decode
