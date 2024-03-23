from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from openai import OpenAI
from playsound import playsound
import threading
import os

# Your OpenAI API key
client = OpenAI(api_key='')


class ForestGame(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player_input = ""
        self.input_active = False

    def build(self):
        Window.fullscreen = 'auto'
        Window.clearcolor = (0, 0, 0, 1)
        Window.bind(on_key_down=self.on_key_down)

        self.layout = BoxLayout(orientation='vertical')
        self.loading_label = Label(text="Getting lost in forest....", font_size='20sp', color=(1, 1, 1, 1), halign="center", valign="middle")
        self.layout.add_widget(self.loading_label)

        Clock.schedule_once(self.init_game, 5)
        return self.layout

    def init_game(self, dt):
        self.layout.clear_widgets()
        self.scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.output_label = Label(text="Welcome to the Forest Adventure!\nWhat do you want to do?", size_hint_y=None, height=Window.height, markup=True, halign="center", valign="middle")
        self.scroll_view.add_widget(self.output_label)
        self.layout.add_widget(self.scroll_view)

        threading.Thread(target=self.play_theme_music, daemon=True).start()
        self.input_active = True

    def play_theme_music(self):
        playsound('theme_music.mp3')

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if self.input_active:
            if keycode == 40:  # Enter key
                self.process_input(self.player_input)
                self.player_input = ""
            else:
                self.player_input += text
                self.update_displayed_text()

    def process_input(self, text):
        ai_response = self.generate_response(text)
        self.output_label.text = "\n" + "User: " + text  + "\n"  + "AI: " + ai_response 
        self.scroll_view.scroll_y = 0  # Scroll to the top to simulate text fading/scrolling away

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
     if self.input_active:
        if keycode == 40:  # Enter key
            self.process_input(self.player_input)
            self.player_input = ""
        elif keycode == 42:  # Assuming 8 is the backspace key, adjust if necessary
            self.player_input = self.player_input[:-1]
            self.update_displayed_text()
        else:
            if text:  # Ensure text is not None
                self.player_input += text
                self.update_displayed_text()

    def update_displayed_text(self):
        self.output_label.text = "What do you want to do?\n" + self.player_input

    def generate_response(self, prompt):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are the Controller of a game environment..."},  # Truncated for brevity
                {"role": "user", "content": prompt}
            ],
            max_tokens=350
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    ForestGame().run()