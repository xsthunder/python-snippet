# [pathlib — Object-oriented filesystem paths — Python 3.8.6 documentation](https://docs.python.org/3/library/pathlib.html)
import os
import re
import sys 
from pathlib import Path

channel_name = sys.argv[2]
workdir = Path('bulid-by-channel-name/')
base_path = workdir/channel_name/('static/js')
files = os.listdir(base_path)
