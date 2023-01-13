import rece
class Restaurant:
    def __init__(self):
        self.food_item_codes = [0] * 12
        self.food_item_names = [""] * 12
        self.food_item_prices = [0] * 12
        self.total_tax = 0

    def getd(self, n):
        for i in range(n):
            #print("Enter Food Code :")
            self.food_item_codes[i] = input()
            #print("Enter Food Name :")
            self.food_item_names[i] = input()
            #print("Enter Food Price :")
            self.food_item_prices[i] = int(input())

    def disd(self, n):
        print("\t\t\t", "MENU", "\t\t\t")
        print("\t\t", "______________________", "\t\t\t")
        print("item code\t\t", "item name\t\t\t\t\t\t", "item price\t\t")
        for i in range(n):
            print(self.food_item_codes[i], "\t\t\t", end="")
            print(self.food_item_names[i], "\t\t\t\t\t", end="")
            print(self.food_item_prices[i], "\t\t\t")


if __name__ == "__main__":
    n = int(input())
    a = Restaurant()
    a.getd(n)
    total = 0
    a.disd(n)
    print()
    tn = input("Enter Table No :")
    noi = int(input("Enter No Of Items : "))
    itemcode = [0] * 12
    quantity = [0] * 12
    price = [0] * 12
    price_indiv = [0] * 12
    itemname = [""] * 12
    for i in range(noi):
        while True:
            print("Enter item", i + 1, "code :")
            itemcode1 = input()
            for j in range(12):
                if itemcode1 == a.food_item_codes[j]:
                    v = 1
                    itemcode[i] = itemcode1
                    break
                else:
                    v = 0
            if v == 0:
                print("Incorrect food code.Enter Again!!")
            else:
                break
        print("Enter item", i + 1, "Quantity :")
        quantity1 = int(input())
        quantity[i] = quantity1
    for i in range(noi):
        for j in range(12):
            if itemcode[i] == a.food_item_codes[j]:
                price0 = a.food_item_prices[j]
                price_indiv[i] = price0
                price1 = a.food_item_prices[j] * quantity[i]
                price[i] = price1
#show bill to customer
    print("\t\t\t", "BILL", "\t\t\t")

    print("\t\t", "______________________", "\t\t\t")
    print("item code\t\t", "item name\t\t\t\t\t\t","price(single)\t\t\t","quantity\t\t", "item price\t\t")
    for i in range(noi):
        for j in range(12):
            if itemcode[i] == a.food_item_codes[j]:
                itemname[i] = a.food_item_names[j]
                #quantity1 = quantity[i]
                print(itemcode[i], "\t\t\t", end="")
                print(itemname[i], "\t\t\t\t\t", end="")
                print(price_indiv[i], "\t\t\t\t", end="")
                print(quantity[i], "\t\t\t\t\t", end="")
                print(price[i], "\t\t\t")
                total = total + price[i]



    print("Total : ", total)
    print("Tax : ", total * 0.05)
    print("Total Bill : ", total + total * 0.05)
    print("Thank You For Visiting Us!!")
    # Create data for the bill receipt
    data = []
    data.append(["Item Code", "Item Name", "Price(single)", "Quantity", "Total(item)"])
    for i in range(noi):
        data.append([itemcode[i], itemname[i], price_indiv[i], quantity[i], price[i]])

    # define the text and style for the paragraph

    # define the text and style for the paragraph
    text = """
    Table No : {tn}
    Total : {total}
    Tax : {total* 0.05}
    Total Bill : {total + total * 0.05}
    Thank You For Visiting Us!!
    """

    rece.create_bill_receipt(data, "bill.pdf")






