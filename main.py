import explore

def display(name):
    print(f'Hi, {name}')
    explore.calculate_pi()

#__name__ is dunder name or double underscore
if __name__ == '__main__':
    display('Bala')

#explore.displayList()
#explore.displayTuple()
#explore.displaySet()
explore.displayDict()
