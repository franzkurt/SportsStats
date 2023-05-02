import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}


setup(
    name="SofaScore Data",
    version="0.1",
    description="Captura dados das partidas no sofascore",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)