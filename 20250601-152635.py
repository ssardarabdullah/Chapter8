Question 10___________
Call the 
function send_messages() 
with a copy of the list 
of messages. After calling the 
function, print both of your
lists to show that the original 
list has retained its 
message

solution ___________
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
original_messages = ["Hello!", 
                    "How are you?", "See you soon.", "Have a great day!"]
sent_messages = []
Use a copy of the original list to
preserve the original
send_messages(original_messages[:], sent_messages)

print("\nOriginal messages list 
(after copy was used):", original_
messages)
print("Sent messages list:", 
      sent_messages)
