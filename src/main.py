import os
import shutil
from textnode import *

def main():
    static_to_public()

def static_to_public():
    #clean public
    if os.path.exists('public'):
        shutil.rmtree('public')
    shutil.copytree('static', 'public')

if __name__ == "__main__":
    main()