from cx_Freeze import setup, Executable

build_exe_options = {"include_files": ["all_items","audio","images","mon_icons"]}

setup(name = "Indev RPG" ,
      version = "0.1" ,
      description = "" ,
      options = {"build_exe": build_exe_options},
      executables = [Executable("rpg.py")])