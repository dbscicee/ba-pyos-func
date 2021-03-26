def calculate_pi():
    print('Test')


# List ordered, mutable
def displayList():
    testList1 = ["Test1", "Test11", "Test111"]
    testList2 = list(("Test2", "Test22", "Test222"))
    testList1[2] = "test5"
    print("The List Values are ", testList1)
    print("The length of the list are ", len(testList1))
    print("The type of the list are", type(testList1))
    print("The List Values are ", testList2)
    print("The length of the list are ", len(testList2))
    print("The type of the list are", type(testList2))

    for _ in range(10):
        print(testList1)


#  Tuple ordered, immutable
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

    for _ in range(10):
        print(testTuple2)


# Set , unordered immutable
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


# Dictionary , map
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
