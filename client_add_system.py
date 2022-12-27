from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput



def add_client(*client):
    file = open("names.txt", "a")
    file.write(str(client) + ", ")
    file.close()
    return file
    
class MainUI(GridLayout):
    def __init__(self, **kwargs):
        super(MainUI, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Provide a name"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.addButton = Button(text="Add")
        # self.name.bind(on_complete=clients)
        self.add_widget(self.addButton)
        self.addButton.bind(on_press=lambda x: add_client(self.name.text))
        self.exitbutt = Button(text="Exit")
        self.exitbutt.bind(on_press=App.get_running_app().stop)
        self.add_widget(self.exitbutt)
        self.display = Button(text="Display Added Users") 
        self.add_widget(self.display)
       # self.display.bind(on_press=lambda x: self.add_widget(Label(text="Hello")))

        def display_users(self):
            with(open("names.txt", "r")) as file:
                users = file.read()
                splitted = users.split(", ")
                splitted = splitted[:-1]
                for user in splitted:
                    self.add_widget(Label(text=user))
        self.display.bind(on_press=display_users)
              
class runTheApp(App):
    def build(self):
        return MainUI()

def main():
    runTheApp().run()


if __name__ == '__main__':
    main()
