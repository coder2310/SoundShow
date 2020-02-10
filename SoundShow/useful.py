# This will be used for usefull functions like
# hashing and password strength
import hashlib
import os
def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()
