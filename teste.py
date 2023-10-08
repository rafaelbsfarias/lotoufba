from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginSystem(BoxLayout):
    def __init__(self, users, **kwargs):
        super(LoginSystem, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = [50, 50]

        self.users = users
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
        
        # Check username and password against the user array
        for user in self.users:
            if username == user.username and password == user.password:
                self.message_label.text = "Login successful!"
                return

        self.message_label.text = "Login failed. Try again."

class LoginApp(App):
    def __init__(self, users, **kwargs):
        super(LoginApp, self).__init__(**kwargs)
        self.users = users

    def build(self):
        return LoginSystem(self.users)

if __name__ == '__main__':
    users = [User("user1", "password1"), User("user2", "password2")]
    LoginApp(users).run()
