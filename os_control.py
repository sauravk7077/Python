import os
from dotenv import load_dotenv

load_dotenv()

sub_id = os.getenv("SUBID")

print(sub_id)