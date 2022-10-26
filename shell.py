"""
Created on Tue Oct 18 11:05:35 2022 
@author: Fahim Ferdous
"""
import base64
import os

def load_from_disk(path):
    file = open(path,"r")
    loaded_ = base64.b64decode(file.read()).decode("utf-8")
    file.close()
    return loaded_

def __run__(code):
    try:
        exec(code, globals())
        return True
    except:
        return False

kernel_path = 'Disk/14387605140ae19713bdeec5b768557fc67885d6a9c5cd9319bffc560fc57029.file' #Using the BoxOS kernel
linker_path = 'Disk/302cc562721e82253f87d2054b0a9f80956a693a90c0767d013304b100dbc390.file' #Using the BoxOS linker

#loading the kernel and linker
kernel = load_from_disk(kernel_path)
linker = load_from_disk(linker_path)

#running kernel and linker
kernel = __run__(kernel)
linker = __run__(linker)

#simple operating system
current_dir = "Disk"

def format_Cdir():
    global current_dir
    cu = current_dir
    if current_dir.endswith("\\"):
        pass 
    else:
        cu += "\\"
    return cu

while True:
    DISK = Disk(USER_OS.path.abspath(USER_OS.getcwd())+"\Disk\FSystem-manager.json")
    
    DIR = "~"+"\\".join(format_Cdir().split("\\")[1:])
    command = input(f"BoxOS@Admin:{DIR}$ ")
    
    match command.split(" ")[0]:
        case "ls":
            LS_last = ""
            for i in current_dir.split("\\"):
                if LS_last == "":
                    LS_last = DISK._view_disk()["Disk"]
                else:
                    LS_last = LS_last[i]
            print(", ".join([x for x in LS_last]))
            
        case "cd":
            CD = command.split(" ",1)[1]
            if DISK.File_exists(current_dir+"\\"+CD):
                current_dir += "\\"+CD
            
            elif CD == "..":
                if current_dir == "Disk":
                    pass
                else:
                    current_dir = "\\".join(current_dir.split("\\")[:-1])
                
            else:
                print(f"Directory `{command.split(' ')[1]}` doesn't exist")

        case "touch":
            file_name = command.split(" ",1)[1]
            DISK.New_file(format_Cdir()+file_name,"\n")
        
        case "mkdir":
            dir_name = command.split(" ",1)[1]
            DISK.New_dir(format_Cdir()+dir_name)
            
        case "rm":
            name_ = command.split(" ",1)[1]
            DISK.Delete_file(format_Cdir()+name_)
            
        case "rmdir":
            name_ = command.split(" ",1)[1]
            DISK.Delete_dir(format_Cdir()+name_)
        
        case "clear":
            os.system("cls")
