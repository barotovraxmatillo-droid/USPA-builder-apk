from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class APKConverterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="Python to APK Builder", font_size=24))
        
        self.code_input = TextInput(hint_text="Python kodingizni shu yerga joylang...", multiline=True)
        layout.add_widget(self.code_input)
        
        convert_btn = Button(text="APK Qurish", size_hint=(1, 0.2), background_color=(0, 1, 0, 1))
        layout.add_widget(convert_btn)
        return layout

if __name__ == '__main__':
    APKConverterApp().run()
