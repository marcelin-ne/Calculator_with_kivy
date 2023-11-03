import kivy
from kivy.app import App
from kivy.uix.widget import Widget #To use the Widget class
from kivy.properties import ObjectProperty #To use the ObjectProperty class
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image
#Set the size of the window
Window.size = (500, 700)

#The first way to load the file
Builder.load_file('calculator.kv')
#Construct the Layout
class MyLayout(Widget):
    def press(self):
        #Create variables for our widget
        name=self.ids.name_input.text #Text Input
        #Update the label
        self.ids.name_label.text = f'Hello {name}!'
        #Clear input box
        self.ids.name_input.text = ''

#Call the class
class CalculatorApp(App):
    def build(self):
       #Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()


