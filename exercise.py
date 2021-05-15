
"""
Problem Statement

                      Navin and Kavin are brothers , Navin is the elder brother,
They went to a shop to buy a gift to their younger sister Brinda for her birthday. She likes reading books ,
so they selected a story book and asked the shopkeeper Mani for book price. The price of the book was Rs.100.55 paise,
Navin had Rs.50 and Kavin had Rs.40, they both added the amount and gave Rs.90 to mani and asked him to provide the book
at a discounted price, Mani agreed and sold the book for Rs.90. Navin and Kavin gave it to their sister brinda
and she was very happy. The actual price (MRP) of the book is Rs.70

Write a program to answer the following

1) Who are family Members in this story ?
2) Which brother had less money than the other ?
2) How much percentage did Navin and kavin spent individually for buying the book?
3) How much Money was discounted for the book ?
4) How much money did shopkeeper profit and profit percentage by selling the book?
5) Had brinda sister happy on receiving the gift?

"""

# Global Variables
elderBrotherName = "Navin" # String
youngerBrotherName = "Kavin"
youngerSisterName = "Brinda"
elderBrotherMoney = 50   # Integer
youngerBrotherMoney = 40
totalBrothersMoney = 90
shopKeeperName = "Mani"
familyMembers = ["Navin", "Kavin", "Brinda"] # Array
bookPrice = 100.55  # float
soldPrice = 90
actualbookprice = 70
isSisterHappy = True


def calculateShopKeeperProfit():
    # Local Variables
    costprice = 70
    soldprice = 90
    profit = soldprice - costprice
    print(" The profit gained by shop keeper Mani is Rs.", profit)
    profitpercentage = profit * 100 / costprice
    print(" The profit percentage by shop keeper Mani is ", format(profitpercentage, ".2f"), "%")


def findLessMoneyBrother():
    if elderBrotherMoney < youngerBrotherMoney:
        return elderBrotherName
    elif elderBrotherMoney == youngerBrotherMoney:
        print(" ElderBrotherMoney and YoungerBrotherMoney are equal")
        return 0
    else:
        return youngerBrotherName


def calculateBrothersPercentage(brotherName):
    while (brotherName == youngerBrotherName):
        youngerbrotherpercentage = (youngerBrotherMoney / totalBrothersMoney) * 100;
        return youngerbrotherpercentage
        break
    else:
        elderbrotherpercentage = (elderBrotherMoney / totalBrothersMoney) * 100;
        return elderbrotherpercentage


def goShopping():
    print("The Elder Brother Name is " + elderBrotherName)
    print("The Younger Brother Name is " + youngerBrotherName)
    print("The Younger Sister Name is " + youngerSisterName)
    print("The Shopkeeper Name is " + shopKeeperName)
    print("Navin had Rs.", elderBrotherMoney)
    print("Kavin had Rs.", youngerBrotherMoney)
    print("Both Navin and Kavin collectively had Rs.", totalBrothersMoney)
    print("Book price told to brothers was  Rs.", bookPrice)
    print("Book was sold for Rs.", soldPrice)
    print("Actual Book price of shop keeper is  Rs.", actualbookprice)

    print(" The Family Members are ", familyMembers)
    print(" The Brother who had less money is ", findLessMoneyBrother())
    print(" The percentage spent by Navin for buying the book is ",
          format(calculateBrothersPercentage(elderBrotherName), ".2f"), "%")
    print(" The percentage spent by Kavin for buying the book is ",
          format(calculateBrothersPercentage(youngerBrotherName), ".2f"), "%")
    print(" Money that was discounted for brothers is Rs.", bookPrice - soldPrice)
    calculateShopKeeperProfit()
    happySister = "Happy" if isSisterHappy == True else "Unhappy"
    print(" The Younger sister Brinda is", happySister)




