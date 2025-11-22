"Here, I am practicing importing modules"

from printing_functions import print_models, show_completed_models

unprinted_designs: list[str] = ['chain', 'labubu', 'shoes']
completed_models: list[str] = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

