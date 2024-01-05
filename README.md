# Folder sorter
A simple configurable script for sorting a directory into more directories.

## Usage
If you want to run it once simply run 
```bash
./dirSorter/__init__.py 
```
If what you want is to run it periodically use 
```bash
watch -n [interval] dirSorter/__init__.py
```

## Configuration
All configurations are done inside `config.py` file.\
You can change directories' names and what extensions go where changing `DIRECTORIES`.\
You can change whether you want to move all directories into a single one called `Directories` changing `SORT_DIRS`.\
You can exclude some directories to be moved into this directory by adding their names to `excluded`.\
You can change whether you want to move files with extensions not listed in `DIRECTORIES`  changing `SORT_OTHERS`.
