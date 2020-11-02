import os
import subprocess

def main():

    # path to your windows 'videos' folder
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
        fls=["audio","video","images", "images/ppt","images/photoshopped","output","text"]
        [os.mkdir(i) for i in fls]
        
        # make a readme.md for GitHub
        try:
            with open(videos_dir + "readme.txt") as s:
                rm = s.read()
            with open ("text/readme.md","w") as f:
                f.write(rm)
        except:
            pass

        # finish up - show dirs and open explorer
        os.listdir(os.getcwd())
        print(os.listdir(os.getcwd()))
        path = os.listdir(os.getcwd())
        subprocess.Popen('explorer videos_dir')
    else:
        print("Directory already exists, nothing to do")

if __name__ == "__main__":
    main()
    
