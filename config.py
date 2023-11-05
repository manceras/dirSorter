# Customize your subdirectories here
DIRECTORIES = {
    "Documents": ["pdf", "doc", "docx", "top"],
    "Photos": ["webp", "png", "jpeg", "jpg", "arw", "raw"],
    "Plain text": ["py", "xml", "txt", "md", "rs", ""],
    "Archives": ["zip", "xz", "tz"],
}

# What directory do you want to sort?
DIR_TO_SORT = "~/Downloads"

# Do you want to sort not listed extensions in an "Others" directory?
SORT_OTHERS: bool = True
# Do you want to sort direcotories in an "Direcotories" directory?
SORT_DIRS: bool = True

# Is there any directory that you do not want to move into "Directories" directory? Put them here
excluded = ["Telegram Desktop"]

