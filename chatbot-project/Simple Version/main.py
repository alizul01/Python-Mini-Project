# Simple Chat Bot Program using Python 

class ChatBot:
    def __init__(self):
        pass
    def answer(self, input):
        print("Chatbot: ", end="")
        if input == 'hi':
            print('Hello!')
        elif input == 'how are you':
            print('I am fine!')
        elif input == 'who are you':
            print('I am a chatbot!')
        elif input == 'what is your name':
            print('I am ChatBot!')
        elif input == 'what is your favorite color':
            print('I like blue!')
        elif input == 'what is your favorite food':
            print('I like pizza!')
        elif input == 'what is your favorite sport':
            print('I like football!')
        elif input == 'what is your favorite movie':
            print('I like Star Wars!')
        elif input == 'what is your favorite song':
            print('I like "The Sign" by Ace of Base!')
        elif input == 'what is your favorite animal':
            print('I like dogs!')
        elif input == 'what is your favorite book':
            print('I like "The Hunger Games" by Suzanne Collins!')
        elif input == 'what is your favorite game':
            print('I like "The Hunger Games" by Suzanne Collins!')
        elif input == "that is good!":
            print('Thank you!')
        else:
            print('I do not understand!')
def main():
    # Confirm that the user wants to continue
    confirm = True
    
    # Initialize the chatbot
    chatbot = ChatBot()
    # Initialize the chatbot's response
    while confirm:
        # Get the user's input
        inputUser = input('You: ')
        # Get the chatbot's response
        if inputUser.lower() == 'bye':
            print('ChatBot: Bye!')
            confirm = False
            break
        chatbot.answer(inputUser.lower())
        

main()