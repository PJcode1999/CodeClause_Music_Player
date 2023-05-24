import pygame
import os

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    while True:
        print("1. Play music")
        print("2. Stop music")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter the path to the music file: ")
            if os.path.exists(file_path):
                play_music(file_path)
            else:
                print("File not found!")

        elif choice == "2":
            stop_music()

        elif choice == "3":
            stop_music()
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
