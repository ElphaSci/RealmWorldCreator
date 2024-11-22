import sys
from cx_Freeze import setup, Executable
import os.path

sys.argv.append("build")  # replaces commandline arg 'build'

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
# os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
# os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

filename = "World_Creator.py"
executables = [
    Executable(filename, base=base)
]

options = {
    'build_exe': {
        'include_files':[
            # os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            # os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
        'excludes':[
            'Resources'
            'numpy',
            'matplotlib',
        ],
        'optimize':2,
    },
}

setup(name = 'World Creator',
      version = '1.0',
      description = 'World Editor for The Realm Online',
      options = options,
      executables = executables,
      )