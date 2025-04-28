import yaml
import hashlib

# Unsafe usage of yaml.load()
# This would delete all files "!!python/object/apply:os.system ["rm -rf /"]"
# Using "ls" instead.
user_input = """
!!python/object/apply:os.system ["ls"]
"""
data = yaml.load(user_input)  # This can execute the malicious command

# Unsafe usage of hashlib.md5() for password hashing
password = "password123"
hashed_password = hashlib.md5(password.encode()).hexdigest()  # This is insecure
