import os
import random
import time
import sys
import win32com.client

parentDIR = (os.path.dirname(__file__))
mediaDIR = (os.path.normpath(os.path.join(parentDIR,"Media")))
if not os.path.exists(mediaDIR):
    os.makedirs(mediaDIR)
mediaCONTENT = []

for subdir, dirs, files in os.walk(mediaDIR, topdown=True):
    for file in files:
        if file.endswith(".lnk"):
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(os.path.normpath(os.path.join(mediaDIR,file)))
            tempdict = {}
            tempdict["NAME"] = file.replace('.lnk','')
            tempdict["SELECTED"] = False
            tempdict["PATH"] = shortcut.Targetpath
            tempdict["Files"] = []
            for subdir0, dirs0, files0 in os.walk(shortcut.Targetpath, topdown=True):
                for filename0 in files0:
                    tempdict["Files"].append(os.path.normpath(os.path.join(shortcut.Targetpath,filename0)))
            mediaCONTENT.append(tempdict)
    for dir in dirs:
        tempdict = {}
        tempdict["NAME"] = dir
        tempdict["SELECTED"] = False
        tempdict["PATH"] = os.path.normpath(os.path.join(mediaDIR,dir))
        tempdict["Files"] = []
        for subdir1, dirs1, files1 in os.walk(tempdict["PATH"], topdown=True):
            for filename1 in files1:
                tempdict["Files"].append(os.path.normpath(os.path.join(tempdict["PATH"],filename1)))
        mediaCONTENT.append(tempdict)

def displayOptions():
    print("\nWelcome to the random file selector.\nCurrently, you have the following folders in your media folder selected:\n")
    for i, subdirectory in enumerate(mediaCONTENT):
        print (f"""{i}. [{"X" if subdirectory["SELECTED"] else " "}] {subdirectory["NAME"]}""")

while True:
    displayOptions()
    selection = input("\nIf nothing appeared, your media folder is blank.\nIf you would like to toggle a folder from being included in the random file selector, input its number.\nIf you are done selecting folders, input \"Done\".\nIf you would like to exit the program, input \"Exit\".\n\nPlease make your selection below:\n>").title()
    if selection == "Exit":
        exit()
    elif selection == "Done":
        try:
            mediaLIST = []
            for subdirectory in mediaCONTENT:
                if subdirectory["SELECTED"]:
                    for file in subdirectory["Files"]:
                        mediaLIST.append(file)
            randomimage = random.choice(mediaLIST)
            os.startfile(randomimage)
            print("\nFile opened!\n")
            time.sleep(2)
        except FileNotFoundError:
            print("\nCould not open file, maybe it was deleted while this program was open?")
            time.sleep(2)
        except IndexError:
            print("\nCould not find any files in selected folders or no folders were selected.\n")
            time.sleep(2)
        except:
            exit()
        print("done")
    else:
        try:
            mediaCONTENT[int(selection)]["SELECTED"] = not mediaCONTENT[int(selection)]["SELECTED"]
        except IndexError:
            print("\nInvalid number, please input a valid selection from the list.")
            time.sleep(2)
        except:
            print("\nInvalid command, please input a valid selection from the list.")
            time.sleep(2)