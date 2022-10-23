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
1. Install chatterbot (command: pip install chatterbot==1.0.2)
2. Install pyttsx3 (command: pip uninstall pyttsx3 and pip install pyttsx3 and pip install --upgrade comtypes)
3. Install ssl <error installing nltk supporting packages>
4. Install nltk <error installing nltk supporting packages>
'''
# Importing the modules – tkinter
# are needed
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 # to speech conversion
from nltk.corpus import *
import re

# Building a dictionary of responses
dialogue = [
    'hello',
    'hi there',
    'what is your name?',
    'My name is BOT, I am created my a hooman ',
    'how are you',
    'i am good! Things are going pretty well for me',
    'in which city you live?',
    'i live in Ho Chi Minh City',
    'in which languages do you speak?',
    'i mostly talk in english',
    'i gotta go',
    'bye, nice to talk to you',
    'thanks',
    'You are welcome'
]

'''
Setting the training class via list data

'''
bot = ChatBot("My Bot")
trainer = ListTrainer(bot)
trainer.train(dialogue)

# Define a function to close the window
def close():
    #root.quit() --> the mainloop will still be running
    root.after(60, root.destroy)
   
def botReply():
    print ("Welcome to MyBOT. Starting our Q&A in few seconds!")
    # While loop to run the chatbot indefinetely
    while (True):  
        # Takes the user input and converts all characters to lower
        question = questionField.get()
        question = question.lower()
        regSign = re.search(r'\d+$', question)
        # Defining the Chatbot's exit condition
        if question == 'quit':
            print ("User is about to leave.")
            # for Bot to speak
            pyttsx3.speak("Bye! Take care...")
            # close the window
            close()
            break
        elif len(question) == 0:
            print ("User has no question.")
            # for Bot to speak
            pyttsx3.speak("MyBOT's always be there to answer you.")
            # close the window
            close()
            break
        elif regSign is not None:
            # if the string ends in digits m will be a Match object, or None otherwise.
            print (regSign.group())
            pyttsx3.speak("Sorry! I didn't understand that")
            return question
        else:
            print ("User has raised question.")
            # The chatbot prints the response that matches the selected dialogue
            if(question =='thanks' or question=='thank you' or question == 'bye'):
                print("Bot: You are welcome..")
            else:
                print ("Got an Amazing question..")
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
logoPic = PhotoImage(file='pic.png')
logoPicLabel = Label(root,image=logoPic,bg='deep pink')
logoPicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame,font=('Helvetica 13',20,'bold'),height=10,yscrollcommand=scrollbar.set,wrap='word')
textarea.tag_configure(centerFrame, foreground='deep pink')
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