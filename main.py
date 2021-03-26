import explore

def display(name):
    print(f'Hi, {name}')
    explore.calculate_pi()

if __name__ == '__main__':
    display('Bala')


# This represents the list features
def displayList():
 testList1 = ["Test1", "Test11", "Test111"]
 testList2 = list(("Test2", "Test22", "Test222"))

 print("The List Values are ",testList1)
 print("The length of the list are ",len(testList1))
 print("The type of the list are",type(testList1))
 print("The List Values are ",testList2)
 print("The length of the list are ",len(testList2))
 print("The type of the list are",type(testList2))

displayList()