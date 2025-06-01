Question 4_________
Make a list containing 
a series
of short text messages. Pass the
list to a function called show_
messages(), which prints each text
message.

solution _________

def show_messages(messages):
    for message in messages:
        print(message)
text_messages = [
    "Hey, how are you?",
    "Don't forget the meeting at 10am.",
    "Lunch later?",
    "Happy birthday!",
    "Call me when you're free."
]
show_messages(text_messages)
