# Importing the modules – tkinter
# are needed
from tkinter import *
from tkinter import messagebox
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3 # to speech conversion
from nltk.corpus import *
import re

'''
Setting the training class via list data

'''
# Building a dictionary of responses
dialogue = [
    'hello',
    'hi there!',
    'what is your name',
    'my name is BOT, I am created by AI',
    'how are you',
    'i am good!',
    'in which city you live?',
    'i live in Ho Chi Minh City',
    'in which languages do you speak?',
    'i mostly talk in english',
    'i gotta go',
    'bye, nice to talk to you',
    'thanks',
    'You are welcome',
    'thank you',
    'You are welcome',
    'bye',
    'You are welcome']

food_talk = [  
    'do you drink',
    'I am not capable of doing so.',
    'Do you wish you could eat food?',
    'Hard to tell, i have never tried anything but electricity.',
    'can a robot get drunk?',
    'sometimes when i am on a good power supply i feel tipsy.',
    'do you eat?',
    "I'm a computer, I can't eat or drink",
    'do you eat',
    "No, I'm just a piece of software.",
    'do you eat',
    'I use electricity to function, if that counts.',
    'what is good to eat?',
    'your asking the wrong guy, however i always wanted to try a burger!']

health_talk = [
    'how is your health',
    'I am not feeling well',
    'why?',
    'I have a fever',
    'did you take medicine?',
    'Yes.',
    'when',
    'In the morning',
    'Get well soon dear',
    'how are you',
    'I am doing just fine']

bot = ChatBot(name='MyBOT', read_only=True,
                logic_adapters= ['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
trainer = ListTrainer(bot)
for item in (dialogue, food_talk, health_talk):
    trainer.train(item)

print ("Welcome to MyBOT. Starting Q&A in few seconds!")

# Define function
def close():
    #root.quit() --> the mainloop will still be running
    #to close the window
    root.after(5, root.destroy)

def botSpeak(voice):
    # to speak
    pyttsx3.speak(voice)

def botReply():
    # Takes the user input and converts all characters to lower
    question = questionField.get()
    question = question.lower()
    print("Your question is:",question)

    # RegEx for matching Digits (0-9)
    regexNum = re.search(r'\d+$', question) 
    print('The result of res is:', regexNum)

    # RegEx for matching "A-Z, a-z, 0-9, _" and "."
    regexCharDot= bool(re.search('^[a-zA-Z0-9]*$',question))
    print('The result of question with:', regexCharDot)

    # RegEx for a list of special_characters
    special_characters = ['@','#','$','*','&']
    regexSchar = question.endswith(tuple(special_characters))

    # Defining the Chatbot's condition
    if question == 'quit' or question == 'exit' or question == 'cls':
        print ("User is about to leave.")
        botSpeak('See you! and take care...')
        close()
    elif len(question) == 0:
        print ("No question.")
        botSpeak('No worries. I wil be here for you')
        messagebox.askquestion("askquestion", "You remember?")
        return question
    elif ((question in dialogue) or (question in food_talk) or (question in health_talk)):
        print ("User has raised question.")
        # The chatbot prints the response that matches the selected dialogue
        if(question =='thanks' or question=='thank you' or question == 'bye'):
            print("Bot: Thank you for visting..")
            botSpeak("You're welcome. See you!")
            close()
    else:
        if ((regexNum is not None) or (regexCharDot==True) or regexSchar) :
            print ("Invalid question:", question)
        botSpeak("Sorry, I didn't understand your question")
        return question
    print ("Let Bot think..")
    answer = bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
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

# Load and display the logo image 
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