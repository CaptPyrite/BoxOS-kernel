# BoxOS-kernel

Part of the BoxOS project (Kernel/Linker) [Python 3.10]


# How it works:

Using BoxOS's new emulated disk, kernel and linker files are coded directly into the disk and the shell communicates with the emulated disk, such as `making new files`, `new directories`, `changing directories`, `deleting files`, `deleting direcotries`


# Security feature:

All files in the BoxOS envoriment are encrypted in with `SHA256` as their filenames. The file's data is encoded in `Base64`. Also the files always end in a `.file` for even more entropy...


<br></br>
**Shell commands:**
```
touch {filename} - Make a new file
mkdir {filename} - Make a new directory
rm {filename} - Delete a file
rmdir {filename} - Delete a directory
cd {directory} - Chage directory
```

**RUN: `shell.py`**


