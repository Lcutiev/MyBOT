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
'''Error 4: AttributeError: 'str' object has no attribute 'get' (Python)
Wrong YAML format
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
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import response_selection
import pyttsx3 # to speech conversion
import ssl
import nltk

# Conversations are stored as a dictionary 
'''dialogue = [
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
    'igotta go',
    'bye',
    'thanks',
    'thank you'

]'''


'''
Setting the training class via list data

'''
'''
Way 1: ListTrainer class allows you to train from a List Data Structure while
'''
#bot = ChatBot("My Bot")
#trainer = ListTrainer(bot) 
#trainer.train(dialogue)

'''
Way 2: ChatterBotCorpusTrainer allows you to train from YAML or JSON data.
'''
# Create a new instance of a ChatBot
bot = ChatBot(name='MyBOT',read_only = True,
                 response_selection_method=response_selection.get_random_response,
                 logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'empty',
            'output_text': ''
        },
        {   
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'sorry, I have no answer',
            'maximum_similarity_threshold': 0.9
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }

    ]
    )
trainer = ChatterBotCorpusTrainer(bot)

trainer.train('conversations')

# Define a function to close the window
def close():
   #root.destroy()
   root.quit()

# Chat function
def botReply():
    print ("Welcome to MyBOT. How may I help you?")

    question = questionField.get()
    question = question.capitalize()
    '''if question =='exit' or question =='Null':
        print ("Thank you for visiting.")
        # Create a Button to call close()
        Button(root, text= "Close the Window", font=("Calibri",14,"bold"), command=close).pack(pady=20)
        break'''
    answer = bot.get_response(question)
    #print(answer)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    #for Bot to speak
    pyttsx3.speak(answer)
    questionField.delete(0,END)

# GUI
'''
Widgets are added here
'''
root = Tk()
root.title('ChatBot')

# Set the size and the background of the window
root.geometry('500x570+100+30')
root.config(bg='deep pink')
root.resizable(width=FALSE, height=FALSE)

# Load the image
logoPic = PhotoImage(file='pic.png')
# Add a label widget to display the image
logoPicLabel = Label(root,image=logoPic,bg='deep pink')
logoPicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame,font=('Helvetica 13',20,'bold'),height=10,yscrollcommand=scrollbar.set,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(root,font=('Helvetica 13',20,'bold'))
questionField.pack(pady=15,fill=X)

askPic = PhotoImage(file='ask.png')

# Create Button and add function
askButton = Button(root,image=askPic,command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()

# bind the event "click" of the
# root to the socket
textarea.tag_configure('answer',foreground='green')
root.bind('<Return>',click)

# Execute Tkinter
root.mainloop()