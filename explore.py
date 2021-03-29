

# List ordered, mutable , allows duplictae
def displayList():
    testList1 = ["Test1", "Test11", "Test111"]
    testList2 = list(("Test2", "Test22", "Test222"))
    # This will replace the index values
    testList1[2] = "test5"
    testList1[1:3] = ["test3", "test4"]
    testList1.append("new")
    testList1.append(1, "old")
    # if you give one variable between1:3 , then it will replace everything value between 1st to 3rd index
    print("The List Values are ", testList1)
    print("The length of the list are ", len(testList1))
    print("The type of the list are", type(testList1))
    print("The List Values are ", testList2)
    print("The length of the list are ", len(testList2))
    print("The type of the list are", type(testList2))

    for _ in range(10):
        print(testList1)

# Access List

def accesslist():
    mylist = [56,76,89,23,58,32,63,93,62,31,72,51,45,89]
    print (mylist[1])
    print(mylist[-1])
    print(mylist[2:7])
    print(mylist[:4])
    print(mylist[5:])
    print(mylist[-4:-1])


#  Tuple ordered, immutable ( Unchangeable) , allows duplicate
def displayTuple():
    testTuple1 = ("T1", "T11", "T111")
    testTuple2 = tuple(("T2", "T22", "T222"))
    # testTuple2[1] = "6"
    print("The Tuple Values are ", testTuple1)
    print("The length of the Tuple are ", len(testTuple1))
    print("The type of the Tuple are", type(testTuple1))
    print("The Tuple Values are ", testTuple2)
    print("The length of the Tuple are ", len(testTuple2))
    print("The type of the Tuple are", type(testTuple2))
    # This will replace the index values
    testTuple1[2] = "test5"
    testTuple1[1:3] = ["test3", "test4"]
    testTuple1.append("new")
    testTuple1.append(1, "old")

    for _ in range(10):
        print(testTuple2)


# Set , unordered, unindexed,  immutable , doest not allow duplicates
def displaySet():
    testSet1 = {"T1", "T11", "T111"}
    testSet2 = set({"T2", "T22", "T222"})
    # testSet2[1] = "6"
    print("The Set Values are ", testSet1)
    print("The length of the Set are ", len(testSet1))
    print("The type of the Set are", type(testSet1))
    print("The Set Values are ", testSet2)
    print("The length of the Set are ", len(testSet2))
    print("The type of the Set are", type(testSet2))

    for _ in range(10):
        print(testSet2)


# Dictionary , map , unordered, mutable , does not allow duplicates
def displayDict():
    testDict1 = {"t1": "high", "t2": "low", }
    testDict2 =dict({"s1": "big", "s2": "small", })
    testDict2[0] = {"6": "one"}
    print("The Dict Values are ", testDict1)
    print("The length of the Dict are ", len(testDict1))
    print("The type of the Dict are", type(testDict1))
    print("The Dict Values are ", testDict2)
    print("The length of the Dict are ", len(testDict2))
    print("The type of the Dict are", type(testDict2))

    for _ in range(10):
        print(testDict2)
