import bcrypt

def hash_password(password: bytes):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=password, salt=salt)
    return hashed_password

def verify_password(password: bytes, hashed_password: bytes):
    return bcrypt.checkpw(password=password, hashed_password=hashed_password)
