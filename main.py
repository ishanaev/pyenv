import yaml
import os
from pathlib import Path
from src import download


def main():
    root_path = str(Path(os.environ.get('HOME'), '.pyenv').resolve())
    if not os.path.isdir(root_path):
        os.environ['ROOT_PATH'] = root_path  # ROOT_PATH in HOME directory
        os.mkdir(root_path)
        print(f"The directory {root_path} has been created.")
        pyenv = download.InitDist(name=str(list(config['dist'].keys())[1]),
                                  url=config['dist']['pyenv']['url'],
                                  path=str(Path(root_path, 'pyenv_dist')),
                                  file=None)
        pyenv.download_dist()
        return True
    else:
        print(f"The directory {root_path} already exists. Please remove {root_path} and try again")
        return False


if __name__ == '__main__':
    with open('config.yml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    main()
