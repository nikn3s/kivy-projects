from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class ButtonClicker(BoxLayout):
    def __init__(self, **kwargs):
        super(ButtonClicker, self).__init__(**kwargs) 

        self.start = Label(text='Clicks: 0')
        self.clicks = 0
        self.clicked = Button(text='Click!')
        self.clicked.bind(on_press=self.click)
        self.add_widget(self.start)
        self.add_widget(self.clicked)

    def click(self, aa):
        self.clicks += 1
        self.start.text = f'Clicks: {self.clicks}'
             
class ClickerApp(App):
    def build(self):
        return ButtonClicker()
    

def main():
    ClickerApp().run()


if __name__ == '__main__':
    main()
