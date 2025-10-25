import os 

def load_gif(gif_file: str=None):
  if gif_file is None:
    raise "gif_file is missing!"
  
  DIRNAME = os.path.dirname(os.path.abspath(__file__))
  return os.path.join(DIRNAME, "animations", gif_file)