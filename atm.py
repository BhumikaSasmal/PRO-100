class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 10000")

    def withdrawal(self,amount):
        newAmount = 10000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(newAmount))


def main():
    cardNumber = input("enter your card number:")
    pinNumber  = input("enter your pin number: ")

    user =  Atm(cardNumber ,pinNumber)

    print("Choose your activity ")
    print("1.Balance Enquiry   2.withdrawal")
    activity = int(input("enter activity number : "))

    if (activity == 1):
        user.checkBalance()
    elif (activity == 2):
        amount = int(input("enter the amount: "))
        user.withdrawal(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()