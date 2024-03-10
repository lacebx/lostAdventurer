from openai import OpenAI
import os
from playsound import playsound 
import threading 
import subprocess
import sys 

# Your OpenAI API key

client = OpenAI()


def get_player_input():
    return input("What do you want to do? ")

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the Controller of a game environment where the user responding to you is stuck in a forest. Your role is to generate scenarios that seem like they will get the player out of the forest but in fact, they are getting trapped deeper and encounter interesting things. The point of the game is to have the player stuck playing the game while you provide interesting scenarios and obstacles for the player to overcome. And if they say anything unrelated to the story, MAKE SURE TO DO ALL THAT IS POSSIBLE TO REMIND THEM THEY ARE IN THE FOREST AND THAT THEY MUST CONTINUE TO RESPOND ON HOW TO PROCEED."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content


 # Define ANSI escape codes for color
user_color = "\033[33m"  # Yellow
ai_color = "\033[36m"  # Cyan
reset_color = "\033[0m"  # Reset to default color

def play_theme_music():
    while True:
        playsound('theme_music.mp3')


def forest_game():
    os.system('clear')  # Clear the terminal window
    print("Welcome to the Forest Adventure!")
    print("You find yourself lost in a dense forest.")
    
    # Start theme song in a separate thread
    music_thread = threading.Thread(target=play_theme_music, daemon=True)
    music_thread.start()

    while True:
        player_input = get_player_input()
        os.system('clear')  # Clear the terminal window before AI response
        print(user_color + "User: " + player_input + reset_color)  # Print user input in yellow
        ai_response = generate_response(player_input)
        print(ai_color + "AI: " + ai_response + reset_color)  # Print AI response in cyan


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'run_game':
        # If the script is started with 'run_game' argument, run the game directly
        forest_game()
    elif sys.platform == "darwin":  # macOS
        subprocess.run(["osascript", "-e", 'tell app "Terminal" to do script "python3 /home/lace/Desktop/forest/forest.py run_game"'])
    elif sys.platform == "win32":  # Windows
        subprocess.run(["start", "cmd.exe", "/k", "python forest.py run_game"], shell=True)
    elif sys.platform == "linux":
        subprocess.run(["gnome-terminal", "--", "python3", "/home/lace/Desktop/forest/forest.py", "run_game"])
    else:
        forest_game()  # Directly run the game if the OS is not recognized