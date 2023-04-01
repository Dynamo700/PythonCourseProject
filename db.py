import csv

#Read the money.txt file
def get_money():
    with open('money.txt', 'r') as m:
        reader = csv.reader(m)
        money = int(next(reader)[0])
    return money

#Write inside of the money.txt whenever the amount of money is updated.
def write_money(money):
    with open('money.txt', 'w', newline='') as m:
        writer = csv.writer(m)
        writer.writerow([money])