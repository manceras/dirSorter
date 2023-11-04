# Folder sorter
A simple configurable script for sorting a folder into more folders.

## Usage
If you want to run it once simply run 
```bash
py folderSorter/__init__.py 
```
If what you want is to run it periodically use 
```bash
chmod +x folderSorter/__init__.py
watch -n [interval] folderSorter/__init__.py
```

## Configuration
All configurations are done inside `config.py` file.
You can change folders' names and what extensions go where changing `FOLDERS`.
You can change whether you want to move all folders into a single one called `Directories` changing `SORT_DIRS`.
You can exclude some folders to be moved into this folder by adding their names to `excluded`.
You can change whether you want to move files with extensions not listed in `FOLDERS`  changing `SORT_OTHERS`.
