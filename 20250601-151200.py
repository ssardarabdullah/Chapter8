Question 6________
Printing Models: Put the functions 
    for the example printing_models.py 
in a separate file called printing_
functions.py. Write an import 
statement at the top of printing
_models.py, and modify the file to 
use the imported functions. 

solution ____________
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left."""
    while unprinted_designs:
        current_design = unprinted
        _designs.pop()
        print(f"Printing model: 
        {current_design}")
        completed_models.append(
            current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)
        

import printing_functions

unprinted = ['phone case', 'robot pendant', 'dodecahedron']
completed = []

printing_functions.print_models(unprinted, completed)
printing_functions.show_completed_models(completed)
