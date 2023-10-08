from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = [50, 50]

        self.username_input = TextInput(hint_text="Username", multiline=False)
        self.password_input = TextInput(hint_text="Password", multiline=False, password=True)
        
        self.login_button = Button(text="Login")
        self.login_button.bind(on_press=self.check_credentials)
        
        self.add_widget(Label(text="Login", font_size=24))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)
        self.message_label = Label(text="", color=[1, 0, 0, 1])
        self.add_widget(self.message_label)
    
    def check_credentials(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        # Check username and password (you can replace this with your own logic)
        if username == "link" and password == "123qwe":
            self.message_label.text = "Login successful!"
        else:
            self.message_label.text = "Login failed. Try again."

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
