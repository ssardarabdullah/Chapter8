Question 8_______
 Make a list containing a series of short
text messages. Pass the 
list to a function called
show_messages(), which prints each
text message.


solution __________
def show_messages(messages):
    for message in messages:
        print(message)
messages = ["Hello!", "How are you?", "See you soon.", "Have a great day!"]
show_messages(messages)
