#######################################################################################
#                                                                                     #      
#  _ __ ___  __| | __ _ _ __   __| | __ _ _ __ ___  ___ _ __    ___ ___  _   _| | __  #
# | '__/ _ \/ _` |/ _` | '_ \ / _` |/ _` | '__/ _ \/ _ \ '_ \  / __/ _ \| | | | |/ /  #
# | | |  __/ (_| | (_| | | | | (_| | (_| | | |  __/  __/ | | || (_| (_) | |_| |   <   #
# |_|  \___|\__,_|\__,_|_| |_|\__,_|\__, |_|  \___|\___|_| |_(_)___\___(_)__,_|_|\_\  #
#                                   |___/                                             #
#######################################################################################


import os
import subprocess

def main():

    # path to your windows 'videos' folder
    # Pi Software Solutions
    videos_dir = "C:/Users/piss/Videos/"

    try:
        # change to videos directory   
        os.chdir(videos_dir)
    except OSError:
        print("Can't change the Current Working Directory")

    # name the project
    project = input("What is project name?\n")
    project = project.title()
    
    # create the directories
    if not os.path.exists(project):
        print(f"Ok, the project folder will be called: {project}")
        os.mkdir(project)
        os.chdir(project)
        fls=["audio","video","images", "images/ppt","images/photoshopped","output","text","code"]
        [os.mkdir(i) for i in fls]

        # make a readme.md for GitHub
        try:
            with open (videos_dir + f"{project}" + "/text/readme.md","wb") as f:
                f.write("Put readme shizz here")
        except:
            pass

        # finish up - show dirs and open explorer
        os.listdir(os.getcwd())
        print(os.listdir(os.getcwd()))
        path = os.listdir(os.getcwd())
        subprocess.Popen(f'explorer {os.path.realpath(videos_dir + project)}')
        p.wait()
    else:
        print("Directory already exists, nothing to do")

if __name__ == "__main__":
    main()
    
