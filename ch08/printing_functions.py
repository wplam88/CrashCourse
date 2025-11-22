"This program makes a module with functions we can import"
#unprinted_designs: list[str] = ['chain', 'labubu', 'shoes'],
#completed_models: list[str] = []

#8.15 print models
def print_models(unprinted_designs: list[str], completed_models: list[str]):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing {current_design.title()}!')
        completed_models.append(current_design)

#8.15 show completed models
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f'-{model.title()}')

