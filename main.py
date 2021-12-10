### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions
### check readme for instructions

from random import randint
from time import sleep
import psutil

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

print("Looking for osu!.exe")
if checkIfProcessRunning("osu!"):
    print("Initializing...")
    sleep(10)
    num = randint(0, 100)
    if num != 1:
        print("Megumi failed to initialize, please refer to the guide on the github readme.")
        exit()
    print("Megumi successfully initialized.")
else:
    print("Please run osu!.exe first and then the cheat")
    exit()
