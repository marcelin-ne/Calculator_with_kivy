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
    def clear(self):
        self.ids.calc_input.text = '0'
    #Create a button pressing function
    def button_press(self, button):
        #Create a variable that contains whatever is in the input field
        prior = self.ids.calc_input.text 
        #Determine if 0 is in the input field
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
        #Test for error first
        if "Error" in prior:
            prior = ''

        #Determine if 0 is in the input field
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    
    #Create addition function
    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'
    #Create subtraction function
    def subtract(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'
    #Create multiplication function
    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}*'
    #Create division function
    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'
    #Create equals function
    def equals(self):
        prior = self.ids.calc_input.text
        #Addition 
        if "+" in prior:
            num_list= prior.split("+")
            answer = 0
            #Loop through our list
            for number in num_list:
                answer = answer + int(number)
            #print the answer in the text box
            self.ids.calc_input.text = str(answer)


#Call the class
class CalculatorApp(App):
    def build(self):
    #Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()


