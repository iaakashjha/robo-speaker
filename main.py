import os

if __name__ == '__main__' :
    print("Welcome to RoboSpeaker 1.1 Created by Aakash Jha")
    while True:
        x = input("Enter what you want me to speak : ")
        if x == "q":
            break

        command = f'wsay "{x}"'
        os.system(command)
