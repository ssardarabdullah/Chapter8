def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello!", "How are you?", "See you soon.", "Have a great day!"]
sent_messages = []

send_messages(messages, sent_messages)

print("\nOriginal messages list:", messages)
print("Sent messages list:", sent_messages)