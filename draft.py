# Importing the modules – tkinter
# are needed
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import response_selection
import pyttsx3 # to speech conversion

'''
Setting the training class via list data

'''

# Conversations are stored as a dictionary 
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

'''#Way 2: ChatterBotCorpusTrainer allows you to train from YAML or JSON data.
Create a new instance of a ChatBot
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
trainer.train('conversations.yml')'''
# Chat function
def botReply():
    print ("Welcome to MyBOT. How may I help you?")
    question = questionField.get()
    question = question.capitalize()
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

# Load the image and display the image
logoPic = PhotoImage(file='logo.png')
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

# bind the event "click"
textarea.tag_configure('answer',foreground='green')
root.bind('<Return>',click)

# Execute Tkinter
root.mainloop()