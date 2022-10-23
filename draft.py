'''Error 1: Caused by SSLError
System Env needs to set below paths:
    ..\Anaconda3
    ..\Anaconda3\scripts
    ..\Anaconda3\Library\bin
'''
'''Errors 2: ImportError: cannot import name 'chatterbot'
Checking the version of chatterbot compatibility with Python that you have installed
'''
'''Errors 3: ImportError: cannot import name 'ChatBot'
Change chatterbot.trainers to chatterbot
'''
'''AttributeError: '_tkinter.tkapp' object has no attribute 'Message' althought import * of tkinter
'''
'''Steps:
Step 1 Prepare the Dependencies
+Install chatterbot (command: pip install chatterbot==1.0.2)
+Install pyttsx3 (command: pip uninstall pyttsx3 and pip install pyttsx3 and pip install --upgrade comtypes)
+Install ssl <error installing nltk supporting packages>
+Install nltk <error installing nltk supporting packages>

Step 2 Import Classes

Step 3 Create and Train the Chatbot

Step 4 Create Function (Get input - process input - return reponse)

Step 5 GUI
'''
# Importing the modules – tkinter
# are needed
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 # to speech conversion
from nltk.corpus import *
import re
import os

# Building a dictionary of responses
dialogue = [
    'hello',
        'hi there!',
    'what is your name',
        'My name is BOT, I am created by AI',
    'how are you',
        'i am good!',
    'in which city you live?',
        'i live in Ho Chi Minh City',
    'in which languages do you speak?',
        'i mostly talk in english',
    'i gotta go',
        'bye, nice to talk to you',
    'thanks',
        'You are welcome']

sport_talk = [  
    'WHAT IS BASKETBALL',
        'A game with tall players.',
    'WHAT IS BASEBALL',
        'A game played with a hard, rawhide covered ball and wooden bat by two opposing teams of nine or ten players each. It is played on a field with four bases forming a diamond-shaped circuit.',
    'WHAT IS SOCCER?',
        'A game played with a round ball by two teams of eleven players on a field with a goal at either end; the ball is moved chiefly by kicking or by using any part of the body except the hands and arms.']

health_talk = [
    'how is your health',
        'I am not feeling well',
    'why?',
        'I have a fever',
    'did you take medicine?',
       'Yes.',
    'when',
        'In the morning',
        'Get well soon dear']

'''
Setting the training class via list data

'''
bot = ChatBot(name='MyBOT', read_only=True,
                logic_adapters= ['chatterbot.logic.MathematicalEvaluation',
                                    'chatterbot.logic.BestMatch'])
trainer = ListTrainer(bot)
for item in (dialogue, sport_talk, health_talk):
    trainer.train(item)

print ("Welcome to MyBOT. Starting Q&A in few seconds!")

# Define function
def close():
    #root.quit() --> the mainloop will still be running
    #to close the window
    root.after(60, root.destroy)

def botSpeak(voice):
    # to speak
    pyttsx3.speak(voice)

def botReply():
    global question
    # Takes the user input and converts all characters to capitalize
    question = questionField.get()
    # Initializing res - end number
    regSign = re.search(r'\d+$', question) 
    # A list of special_characters to be removed
    special_characters = ['@','#','$','*','&', '!']

    # Defining the Chatbot's condition
    if question == 'quit':
        print ("User is about to leave.")
        botSpeak('Bye! Take care...')
        close()
    elif len(question) == 0:
        print ("No question.")
        botSpeak('No worries. Let me know when you have.')
        close()
    elif (regSign is not None) or question.endswith(tuple(special_characters)) or (bool(re.search('^[a-zA-Z0-9]*$',question))==True) :
        # if the string ends in digits regSign will be a Match object, or None otherwise.
        #print (regSign.group())
        print ("Invalid question is", question)
        botSpeak("Sorry, I didn't understand your question")
        return question
    elif question not in dialogue or question not in sport_talk or question not in health_talk:
        print ("Question not found in list data")
        botSpeak("It's not easy. Ask another question, please!")
        return question
    else:
        print ("User has raised question.")
        # The chatbot prints the response that matches the selected dialogue
        if(question =='thanks' or question=='thank you' or question == 'bye'):
            print("Bot: Thank you for visting..")
            botSpeak("You're welcome. See you!")
            close()
        # To be continued
        # elif(question.endswith(tuple(special_characters))):
        #     for i in special_characters:
                
        #         # Replace the special character with ?
        #         question=question.replace(i,"?")
        #         print(question,"after replaching with question mark")
        # elif((bool(re.search('^[a-zA-Z0-9]*$',question))==True)):
        #     # Remove Special Chars
        #     new_question = question
        #     new_question = re.sub('[^a-zA-Z0-9 \n\.]', '', new_question)
        #     print(question, "after removal of special characters")

        print ("Let Bot think..")
    question = question.capitalize()
    answer = bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    # for Bot to speak
    pyttsx3.speak(answer)
    questionField.delete(0,END)

# GUI
'''
Widgets are added here
'''
root = Tk()
root.title('MyBOT')

# Set the size and the background of the window
root.geometry('500x570+100+30')
root.config(bg='deep pink')

# Load the image and display the image
logoPic = PhotoImage(file='logo.png')
logoPicLabel = Label(root,image=logoPic,bg='deep pink')
logoPicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame,fg='deep pink',font=('Helvetica 13',20,'bold'),height=10,yscrollcommand=scrollbar.set,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(root,font=('Helvetica 13',20,'bold'))
questionField.pack(pady=15,fill=X)

# Display a welcome message

# Create Button and add botReply function
askPic = PhotoImage(file='ask.png')
askButton = Button(root,image=askPic,command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()

# bind the event "click" of the root
root.bind('<Return>',click)

# Execute Tkinter
root.mainloop()