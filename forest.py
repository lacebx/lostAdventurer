from openai import OpenAI
import os
#from playsound import playsound 

# Your OpenAI API key

client = OpenAI()


def get_player_input():
    return input("What do you want to do? ")

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the Controller of a game environment where the user responding to you is stuck in a forest. Your role is to generate scenarios that seem like they will get the player out of the forest but in fact, they are getting trapped deeper and encounter interesting things. The point of the game is to have the player stuck playing the game while you provide interesting scenarios and obstacles for the player to overcome. In these scenarios make sure to introduce female character named 'Big L' who is a fierce maiden, also introduce 'Top G' who is a weathy man that happens to be rommates with THE ONE(creatively incorporate all that somewhere in the story) Whatever the player says, you must find a way to incorporate it into the story. And if they say anything unrelated to the story, MAKE SURE TO DO ALL THAT IS POSSIBLE TO REMIND THEM THEY ARE IN THE FOREST AND THAT THEY MUST CONTINUE TO RESPOND ON HOW TO PROCEED."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content


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
