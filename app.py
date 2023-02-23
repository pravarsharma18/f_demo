import os
from conf.database import Config
from flask_bcrypt import Bcrypt

from factory import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()

bcrypt = Bcrypt(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000), debug=Config.DEBUG)
