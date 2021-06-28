#imports
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

# Colour constants
Button_Text_Colour = "green"  # defining the colour of Array_Of_Button_Instances text
Button_Text_Outline_Colour = "yellow"  # outline of Array_Of_Button_Instances font text
Button_Background_Colour = "blue"  # defining the background colour of the buttons
Button_OnClick_Colour = "pink"  # defining the background colour which is to be made in signs buttons when clicked

# Constant arrays of Array_Of_Button_Instances parameters. DO NOT CHANGE THE ORDER.
# The code is paired with the ordering of the constant arrays

# Button name array
Array_Of_Operators = ['.', '/', '*', '+', '-',
                      'Indicator_key_for---Last_Answer_Is_Now_The_First_Operand']  # holds the names of all signes
Button_Name_Array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=', 'AC',
                     '.', '(', ')', 'D']  # holds the names of all buttons

# Button size
Button_Size_Unit = 0.2  # constant for one unit of Button size
# Array holding the sizes of each Button in accordance to Button_Name_Array
Button_Size_Unit_Array_X = [Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit,
                            Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit,
                            Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit,
                            Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit]

Button_Size_Unit_Array_Y = [Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit,
                            Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit,
                            Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit,
                            Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit]

# Button position- these arrays hold position of each in accordance to Button_Name_Array
Button_Position_Array_X = [0, 0, Button_Size_Unit, Button_Size_Unit * 2, 0, Button_Size_Unit, Button_Size_Unit * 2, 0,
                           Button_Size_Unit, Button_Size_Unit * 2, Button_Size_Unit * 3, Button_Size_Unit * 3,
                           Button_Size_Unit * 3, Button_Size_Unit * 3, Button_Size_Unit * 2, Button_Size_Unit * 4,
                           Button_Size_Unit, Button_Size_Unit * 4, Button_Size_Unit * 4, Button_Size_Unit * 4]

Button_Position_Array_Y = [0, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit, Button_Size_Unit * 2,
                           Button_Size_Unit * 2, Button_Size_Unit * 2, Button_Size_Unit * 3, Button_Size_Unit * 3,
                           Button_Size_Unit * 3, 0, Button_Size_Unit, Button_Size_Unit * 2, Button_Size_Unit * 3, 0, 0,
                           0, Button_Size_Unit, Button_Size_Unit * 2, Button_Size_Unit * 3]


def Build_Button_Array(i, label, Array_Of_Input_Values, Array_Of_Button_Instances):
    '''
    Function to make Array_Of_Button_Instances which have text according to Button_Name_Array, size according to the
    arrays Button_Size_Unit_Array_X and Button_Size_Unit_Array_Y and position according to Button_Position_Array_X and
    Button_Position_Array_Y. This also sets the lambda function On_Pressing_Button to activate whenever pressed.
    Input parameters:
                    i- the index of the button to be appended into the array
                    label -instance of label- by value-the label output which is to be given to the lambda function
                    Array_Of_Input_Values- Array which holds the operations- by value- to be passed to the lambda function
                    Array_Of_Button_Instances- The array in which the buttons are stored. This array is appended with
                     the text from Button_Name_Array (and thus changed) in this function.
    output parameters:
                     returns Array_Of_Button_Instances
                     the lambda function called here changes the value of the button text and Array_Of_Input_Values.
    '''
    Temporary_Button = Button(  #Temporary instance of Button to add to Array_Of_Button_Instances
        text=Button_Name_Array[i], #Text of the button is equal to elements of Button_Name_Array
        color=(Button_Text_Colour), #Set the text colour of the button
        size_hint=(Button_Size_Unit_Array_X[i], Button_Size_Unit_Array_Y[i]), #Set the size of the button
        background_color=(Button_Background_Colour), #Set the background colour of the button
        font_size=54, #Set the font size of the button
        outline_color=(Button_Text_Outline_Colour), #Set the outline colour of the button.
        outline_width=3, #Set the outline width
        pos_hint={"x": Button_Position_Array_X[i], "y": Button_Position_Array_Y[i]} #Set the position of the button
    )

    try:
        Temporary_Button.font_name = ("PocketMonk-15ze") #setting the font name if available
    except: #Pass if any error
        pass

    Array_Of_Button_Instances.append(Temporary_Button) #Add the instance of the button to Array_Of_Button_Instances.

    Array_Of_Button_Instances[i].fbind("on_press", #Activate the lambda function when the button is pressed.
                            lambda x: On_Pressing_Button(i, Array_Of_Button_Instances, label,  Array_Of_Input_Values))
#Note that the lambda function has different values for different i.

    return Array_Of_Button_Instances[i] #Return the array with the instances of buttons to be added to the layout.


def On_Pressing_Button(i, Array_Of_Button_Instances, label, Array_Of_Input_Values):
    text = Array_Of_Button_Instances[i].text
    for j in range(0, len(Array_Of_Button_Instances)):#This is to change the values of the colour of the buttons when pressed
        Array_Of_Button_Instances[j].background_color = (Button_Background_Colour)
    if (text in Array_Of_Operators): #If the button is one of the sines, then the value stays.
        Array_Of_Button_Instances[i].background_color = (Button_OnClick_Colour)

    if len(Array_Of_Input_Values) != 0:  # initial case of empty array
        Add_Values_To__Array_Of_Input_Values(label, i, Array_Of_Input_Values, Array_Of_Button_Instances)
        if (Array_Of_Button_Instances[i].text == '='):
            finalanswer = Array_Of_Input_Values.copy()
            answer = (Calculate(Process_Array_Of_Input_Values(Array_Of_Input_Values)))
            if answer != Return_Error_Message():  # no error
                Array_Of_Input_Values.clear()
                Array_Of_Input_Values.append('(')
                Array_Of_Input_Values.append(str(round(answer, 3)))
                finalanswer.append(str(round(answer, 6)))
                Array_Of_Input_Values.append('Indicator_key_for---Last_Answer_Is_Now_The_First_Operand')
                str1 = ''
                label.text = str1.join(finalanswer)
            else:
                label.text = Return_Error_Message()
    else:
        Add_Values_To__Array_Of_Input_Values(label, i, Array_Of_Input_Values, Array_Of_Button_Instances)
    if (label.text == Return_Error_Message()):
        Array_Of_Input_Values.clear()
        label.outline_color = "white"
        label.color = "red"
        label.font_hinting = 'mono'


def Add_Values_To__Array_Of_Input_Values(label, i, Array_Of_Input_Values, Array_Of_Button_Instances):
    text = Array_Of_Button_Instances[i].text

    if len(Array_Of_Input_Values) == 3 and (Array_Of_Input_Values[len(
            Array_Of_Input_Values) - 1] == 'Indicator_key_for---Last_Answer_Is_Now_The_First_Operand') and text not in Array_Of_Operators:
        Array_Of_Input_Values.pop()
        Array_Of_Input_Values.pop()

    if (text == 'AC'):
        Array_Of_Input_Values.clear()
        label.text = ''
    else:
        if (len(Array_Of_Input_Values) != 0 and (
                text in Array_Of_Operators or  # no two consececutive signes
                (Array_Of_Input_Values[0] in Array_Of_Operators))):  # no sign before first element
            a = Array_Of_Input_Values.pop()
            if (str(a) not in Array_Of_Operators):
                Array_Of_Input_Values.append(a)

        if (text == 'D'):
            try:
                Array_Of_Input_Values.pop()
            except:
                Array_Of_Input_Values.clear()
                label.text = ''
        else:
            Array_Of_Input_Values.append(((text)))
        str1 = ''
        label.text = str1.join(Array_Of_Input_Values)
        label.outline_color = "blue"
        label.color = "white"
        label.font_hinting = 'normal'


def Process_Array_Of_Input_Values(Array_Of_Input_Values):
    a = 0
    Array_Of_Processed_Values = []
    for i in range(0, len(Array_Of_Input_Values)):
        try:
            a = 10 * a + float(Array_Of_Input_Values[i])
        except:
            if (Array_Of_Input_Values[i] != '(' and Array_Of_Input_Values[
                i - 1] != ')'):  # because these are signes when two signes can come together
                Array_Of_Processed_Values.append(a)
            Array_Of_Processed_Values.append(Array_Of_Input_Values[i])
            a = 0
    return Array_Of_Processed_Values


def Operations(a, sign, b):
    if (sign == '+'):
        answer = a + b
    if (sign == '-'):
        answer = a - b
    if (sign == '*'):
        answer = a * b
    if (sign == '/'):
        try:
            answer = a / b
        except:
            return Return_Error_Message()
    if (sign == '.'):
        while (b >= 1):
            b = b / 10
        answer = a + b
    return answer


def Return_Error_Message():
    return 'error!'


def Calculate(Array_Of_Processed_Values):
    Array_Of_Processed_Values_copy = Array_Of_Processed_Values.copy()
    Array_Of_Processed_Values_copy.pop  # remove the = sign
    Operator = 0.0
    Operand = 0.0

    # checking if the brackets are aligned or not
    Count_brackets = 0
    for k in range(0, len(Array_Of_Processed_Values_copy)):
        if (Array_Of_Processed_Values_copy[k] == '('):
            Count_brackets = Count_brackets + 1
        if (Array_Of_Processed_Values_copy[k] == ')'):
            Count_brackets = Count_brackets - 1
        if (Count_brackets < 0):
            return Return_Error_Message()
    if (Count_brackets != 0):
        return Return_Error_Message()
    New_Array = []
    New_Array.clear()

    for k in range(0, len(Array_Of_Processed_Values_copy)):
        if (len(Array_Of_Processed_Values_copy) > k and Array_Of_Processed_Values_copy[k] == '('):
            Count_brackets = Count_brackets + 1
            Array_Of_Processed_Values_copy.pop(k)
            while (Count_brackets != 0):
                if (Array_Of_Processed_Values_copy[k] == '('):
                    Count_brackets = Count_brackets + 1

                if (Array_Of_Processed_Values_copy[k] == ')'):
                    Count_brackets = Count_brackets - 1
                New_Array.append(Array_Of_Processed_Values_copy.pop(k))

            New_Array.pop()
            New_Array.append("=")
            Array_Of_Processed_Values_copy.insert(k, Calculate(New_Array.copy()))
            New_Array.clear()

    for j in range(0, len(Array_Of_Operators) - 1):  # bodmas
        temp = Array_Of_Operators[j]
        while (temp in Array_Of_Processed_Values_copy):
            for i in range(0, len(Array_Of_Processed_Values_copy)):
                try:
                    if (Array_Of_Processed_Values_copy[i] == temp):
                        Operator = Array_Of_Processed_Values_copy[i - 1]
                        sign = Array_Of_Processed_Values_copy[i]
                        Operand = Array_Of_Processed_Values_copy[i + 1]
                        Array_Of_Processed_Values_copy[i - 1] = Operations(Operator, sign, Operand)
                        Array_Of_Processed_Values_copy.pop(i)
                        Array_Of_Processed_Values_copy.pop(i)
                except:
                    pass
    return Array_Of_Processed_Values_copy[0]


class DemoApp(App):
    def build(self):
        Array_Of_Input_Values = []
        float = FloatLayout()
        label = Label(text='Calculate...',
                      size_hint=(Button_Size_Unit * 5, Button_Size_Unit),
                      font_hinting='light',
                      font_size=75,
                      outline_color=[1,1,1],
                      outline_width=4,
                      color=[0.5,0.5,0.5,0.35],
                      pos_hint={"x": 0, "y": 4 * Button_Size_Unit})
        float.add_widget(label)
        Array_Of_Button_Instances = []
        for i in range(0, len((Button_Name_Array))):
            float.add_widget(Build_Button_Array(i, label, Array_Of_Input_Values, Array_Of_Button_Instances))
        return float


# main
App = DemoApp()
App.run()
