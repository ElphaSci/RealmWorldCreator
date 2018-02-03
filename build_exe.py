import os

os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python36-32\\tcl\\tk8.6"

import sys
from cx_Freeze import setup, Executable

sys.argv.append("build")  # replaces commandline arg 'build'
# change the filename to your program file
filename = "World_Creator.py"
base = None
buildOptions = dict(packages=[], excludes=['C:\\Users\\caleb\\PycharmProjects\\World_Editor\\PyFotoSCIop\\PySCIs',
                                           'C:\\Users\\caleb\\PycharmProjects\\World_Editor\\PyFotoSCIop\\TraduSCI',
                                           'C:\\Users\\caleb\\PycharmProjects\\World_Editor\\PyFotoSCIop\\v56_files',
                                           'C:\\Users\\caleb\\PycharmProjects\\World_Editor\\PyFotoSCIop\\World_Creator_old'],
                    include_files=['C:\\Python36\\DLLs\\tcl86t.dll', 'c:/python36/DLLs/tk86t.dll'],
                    includes=['numpy.core._methods', 'numpy.lib.format'])
if sys.platform == "win32":
    base = "Win32GUI"
setup(name="Avalon's Sandbox", version="1.0", description="World Editor for The Realm Online",
      options={'build_exe': buildOptions}, executables=[Executable(filename, base=base)])
