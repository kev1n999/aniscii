# import os 
# from dotenv import load_dotenv
from api.app import create_app

if __name__ == "__main__":
  # If you wanna to run in localhost
  # load_dotenv()
  # port = os.getenv("SERVER_PORT")

  app = create_app()
  app.run(host="0.0.0.0", threaded=True)