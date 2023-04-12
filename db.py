import csv

#Read the money.txt file
def get_money():
    try:
        with open('money.txt', 'r') as m:
            reader = csv.reader(m)
            money = int(next(reader)[0])
            if money < 5:
                print("Sorry. You don't have enough money to play right now.")
                while True:
                    answer = input("Would you like to buy some chips? (y/n)")
                    if answer.lower() == 'y':
                        money = 100
                        write_money(money)
                        break
                    elif answer.lower() == 'n':
                        return
                    else:
                        print("Invalid input. Please enter either y or n.")
        return money
    except (FileNotFoundError, ValueError):
        #Handle exceptions that may occur when reading the money.txt file.
        #If the file is not found, start with a default value of 100.
        print("Can't read money.txt file. Using default money value of 100.")
        return 100


#Write inside the money.txt whenever the amount of money is updated.
def write_money(money):
    with open('money.txt', 'w', newline='') as m:
        writer = csv.writer(m)
        writer.writerow([money])