import yaml

# Unsafe usage of yaml.load()
# This would delete all files "!!python/object/apply:os.system ["rm -rf /"]"
# Using "ls" instead

user_input = """
!!python/object/apply:os.system ["ls"]
"""
data = yaml.load(user_input)  # This can execute the malicious command
