#return the minimum amount of bills needed to withdraw in an atm for amount less than 10000

def minumum_return_bills(n):
    number_of_bills = 0
    while n > 0:
        if n >= 500 and n < 1000:
            n -=500
            number_of_bills += 1
        elif n >= 200 and n < 500:
            n -=200
            number_of_bills +=1
        elif n >=100 and n <200:
            n -=100
            number_of_bills += 1
        elif n >= 50 and n < 100:
            n -=50
            number_of_bills += 1
        elif n >= 20 and n < 50:
            n -=20
            number_of_bills += 1
        elif n >= 10 and n < 20:
            n -=10
            number_of_bills += 1
        else:
            return "Amount not possible to be withdrawn"
    return number_of_bills