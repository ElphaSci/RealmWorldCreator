import sys
from cx_Freeze import setup, Executable
import os.path

sys.argv.append("build")

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

filename = "World_Creator.py"
executables = [
    Executable(filename, base=base)
]

options = {
    'build_exe': {
        'include_files': [
        ],
        'excludes': [
            'Resources'
            'numpy',
            'matplotlib',
        ],
        'optimize': 2,
    },
}

setup(name='World Creator',
      version='1.0',
      description='World Editor for The Realm Online',
      options=options,
      executables=executables,
      )
