#!/usr/bin/env python3

from config import FOLDERS, DIR_TO_SORT, SORT_OTHERS, SORT_DIRS
import os
from datetime import datetime

def extension(file: str) -> str:
    extension = ""
    for char in file:
        if char == ".":
            extension = ""
        extension += char
    extension = extension[1:len(extension)]
    return extension



def sort_files():
    files = [name for name in os.listdir(DIR_TO_SORT) if not os.path.isdir(os.path.join(DIR_TO_SORT, name))]
    for file in files:
        file_extension = extension(file)
        for (folder, extensions) in FOLDERS.items():
            if file_extension in extensions:
                if not os.path.exists(os.path.join(DIR_TO_SORT, folder)):
                    os.mkdir(os.path.join(DIR_TO_SORT, folder))
                # Move the file inside the corresponding folder
                os.rename(
                    os.path.join(DIR_TO_SORT, file),
                    os.path.join(DIR_TO_SORT, folder, file)
                )
        if SORT_OTHERS:
            if os.path.exists(os.path.join(DIR_TO_SORT, file)):
                if not os.path.exists(os.path.join(DIR_TO_SORT, "Others")):
                    os.mkdir(os.path.join(DIR_TO_SORT, "Others"))
                os.rename(
                    os.path.join(DIR_TO_SORT, file),
                    os.path.join(DIR_TO_SORT, "Others", file)
                )
def sort_dirs(excluded):
    dirs = [
        name
        for name in os.listdir(DIR_TO_SORT)
        if os.path.isdir(os.path.join(DIR_TO_SORT, name))
        and name not in excluded
    ]
    if not os.path.exists(os.path.join(DIR_TO_SORT, "Directories")):
        os.mkdir(os.path.join(DIR_TO_SORT, "Directories"))
    for directory in dirs:
        os.rename(os.path.join(DIR_TO_SORT, directory), os.path.join(DIR_TO_SORT, "Directories", directory))



def main():
    from config import excluded

    sort_files()
    excluded += excluded + list(FOLDERS.keys())
    if SORT_OTHERS:
        excluded.append("Others")
    if SORT_DIRS:
        excluded.append("Directories")
        sort_dirs(excluded)

    print("SORTED AT", datetime.now())

main()
