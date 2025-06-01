Question 7__________
Using a program you wrote that has
one function in it, store that
function in a separate file.
Import the function into your main
program file, and call the function 
using each of these approaches:

solution _____________
def greet_user(name):
    print(f"Hello, {name}!")
    import greetings
greetings.greet_user("Alice")
import greetings
greetings.greet_user("Alice")
import greetings as gr
gr.greet_user("Diana")
