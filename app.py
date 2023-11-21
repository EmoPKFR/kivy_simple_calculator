from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#Set the app size
Window.size = (400, 560)

Builder.load_file("calc.kv")


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"
        
    #Create a button pressing function
    def button_press(self, button):
        #create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text
        
        #Test for error first
        if "Error" in prior:
            prior = ""
        
        #determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"
            
    def pos_neg(self):
        prior = self.ids.calc_input.text
        
        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-', '')}"
        else:
            self.ids.calc_input.text = f"-{prior}"          
            
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior
            
    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        operators = ['+', '-', '*', '/']

        # Check if the current number already contains a dot
        for operator in operators:
            if operator in prior:
                num_list = prior.split(operator)
                if "." not in num_list[-1]:
                    prior = f"{prior}."
                    self.ids.calc_input.text = prior
                    return  # Exit the loop if a dot is added

        # If no operator is found, check for a dot in the entire expression
        if "." not in prior:
            prior = f"{prior}."
            self.ids.calc_input.text = prior
            
            
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}{sign}"
      
    def equals(self):
        prior = self.ids.calc_input.text
        #Error handling
        try:
            #Evaluate the math from the text box
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)[:12]
        except:
            self.ids.calc_input.text = "Error"
            
        
class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == "__main__":
    CalculatorApp().run()