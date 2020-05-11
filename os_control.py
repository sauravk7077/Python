import os
from dotenv import dotenv_values

os_ver = os.getenv('OS')
print(os_ver)