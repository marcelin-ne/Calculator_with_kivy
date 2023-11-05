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
    def math_sign(self,sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    #create decimal function
    def dot(self):
        prior= self.ids.calc_input.text
        #split out text box by +
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]: 
            #Add a decimal to the end of the text
            prior=f'{prior}.'
        #Output back to the text box
            self.ids.calc_input.text = f'{prior}'
        elif "." in prior:
            pass
        else:
        #Add a decimal to the end of the text
            prior=f'{prior}.'
        #Output back to the text box
            self.ids.calc_input.text = f'{prior}'
    #create function to make text box positive or negative
    def pos_neg(self):
        prior= self.ids.calc_input.text
        #test to see if there's a - sign already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
    #Create equals function
    def equals(self):
        prior = self.ids.calc_input.text
        #Addition
        if "+" in prior:
            num_list= prior.split("+")
            answer = 0.0
            #Loop through our list
            for number in num_list:
                answer = answer + float(number)
            #print the answer in the text box
            self.ids.calc_input.text = str(answer)


#Call the class
class CalculatorApp(App):
    def build(self):
    #Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()


