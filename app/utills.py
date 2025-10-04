from passlib.context import CryptContext
import bcrypt

# Create a more robust password context
pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto",
    bcrypt__default_rounds=12,
    bcrypt__min_rounds=10,
    bcrypt__max_rounds=15
)

def hash(password: str):
    # Ensure password is properly truncated to 72 bytes for bcrypt
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        # Truncate to exactly 72 bytes
        password_bytes = password_bytes[:72]
        password = password_bytes.decode('utf-8', errors='ignore')
    
    # Use bcrypt directly to avoid passlib initialization issues
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str):
    # Verify password with same truncation logic
    password_bytes = plain_password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
        plain_password = password_bytes.decode('utf-8', errors='ignore')
    
    # Use bcrypt directly for verification
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
 