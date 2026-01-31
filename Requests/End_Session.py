# Will reset token after 1 hour to ensure the old token is not kept in the .env file and for too long.
import os
import time

from dotenv import load_dotenv, set_key


# Load Environment Variables
load_dotenv()


time.sleep(int(os.getenv('REQRES_TOKEN_TIMEOUT')))

set_key('.env', 'REQRES_TOKEN', os.getenv('REQRES_DUMMY_VALUE'))

print('Your Token Has Reset')
