from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# Optional: Set window size for testing on desktop
Window.size = (300, 500)

class DialerApp(App):
    def build(self):
        self.number_input = TextInput(
            font_size=32, readonly=True, halign='center', multiline=False, size_hint_y=None, height=80
        )
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        main_layout.add_widget(self.number_input)
        
        # Buttons layout
        buttons = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9'],
            ['','0','']
        ]
        
        for row in buttons:
            h_layout = GridLayout(cols=3, spacing=10, size_hint_y=None, height=80)
            for label in row:
                if label == '':
                    h_layout.add_widget(Label())
                    continue
                btn = Button(text=label, font_size=28)
                btn.bind(on_press=self.button_pressed)
                h_layout.add_widget(btn)
            main_layout.add_widget(h_layout)
        
        # Call and Backspace buttons
        bottom_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80)
        call_btn = Button(text="Call", background_color=(0,1,0,1), font_size=24)
        call_btn.bind(on_press=self.call_number)
        back_btn = Button(text="⌫", background_color=(1,0,0,1), font_size=24)
        back_btn.bind(on_press=self.backspace)
        bottom_layout.add_widget(call_btn)
        bottom_layout.add_widget(back_btn)
        
        main_layout.add_widget(bottom_layout)
        return main_layout
    
    def button_pressed(self, instance):
        self.number_input.text += instance.text
    
    def backspace(self, instance):
        self.number_input.text = self.number_input.text[:-1]
    
    def call_number(self, instance):
        number = self.number_input.text
        if number:
            popup = Popup(title="Calling",
                          content=Label(text=f"Dialing {number}..."),
                          size_hint=(0.7,0.3))
            popup.open()
            # Here you can integrate real call logic for APK
        else:
            popup = Popup(title="Error",
                          content=Label(text="Enter a number first!"),
                          size_hint=(0.7,0.3))
            popup.open()

if __name__ == "__main__":
    DialerApp().run()
