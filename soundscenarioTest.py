import os
from openai import OpenAI
import pygame

# Initialize Pygame Mixer
pygame.mixer.init()

# Your OpenAI API key
client = OpenAI(api_key='your-api-key')

# Sound effects mapping
sounds = {
    "rain": "sounds/rain.mp3",
    "footsteps": "sounds/footsteps.mp3",
    "animal": "sounds/animal.mp3",
    # Add more scenarios and corresponding sound files here
}

def play_sound(keyword):
    pygame.mixer.music.load(sounds[keyword])
    pygame.mixer.music.play()

def get_player_input():
    return input("What do you want to do? ")

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the Controller of a game environment..."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    text_response = response.choices[0].message.content
    # Check for keywords in the response and play corresponding sounds
    for keyword in sounds:
        if keyword in text_response:
            play_sound(keyword)
    return text_response

 # Define ANSI escape codes for color
user_color = "\033[33m"  # Yellow
ai_color = "\033[36m"  # Cyan
reset_color = "\033[0m"  # Reset to default color

def forest_game():
    os.system('clear')  # Clear the terminal window
    print("Welcome to the Forest Adventure!")
    print("You find yourself lost in a dense forest.")
    
    #Themese song 
    # playsound('theme_music.mp3')

    while True:
        player_input = get_player_input()
        os.system('clear')  # Clear the terminal window before AI response
        print(user_color + "User: " + player_input + reset_color)  # Print user input in yellow
        ai_response = generate_response(player_input)
        print(ai_color + "AI: " + ai_response + reset_color)  # Print AI response in cyan

if __name__ == "__main__":
    forest_game()
