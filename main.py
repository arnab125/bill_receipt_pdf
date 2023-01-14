from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Spacer
from reportlab.lib import colors
import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_CENTER, TA_LEFT


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


    title = "Some Restaurant"
    heading = "BILL"
    underline = "________________"
    text1 = f"Table no : {tn}"
    text2 = f"Total : {total} TK"
    text3 = f"Tax : {total * 0.05} TK"
    text4 = f"Total Bill : {total + total * 0.05} TK"
    text5 = "Thank You For Visiting Us!!"

    timestamp = f"generated on {datetime.datetime.now()} using a Python script"


    def create_bill_receipt(data, filename):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        t = Table(data)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 12)
        ]))



        style = getSampleStyleSheet()["Normal"]
        style.alignment = TA_CENTER
        style.fontSize = 11
        style.fontName = "Helvetica-Bold"

        #heading style
        style1 = getSampleStyleSheet()["Heading1"]
        style1.alignment = TA_CENTER
        style1.fontSize = 14
        style1.fontName = "Helvetica-Bold"


        style2 = getSampleStyleSheet()["Normal"]
        style2.alignment = TA_LEFT
        style2.fontSize = 8
        style2.fontName = "Helvetica-Bold"
        style2.spaceBefore = 100

        style3 = getSampleStyleSheet()["Normal"]
        style3.alignment = TA_LEFT
        style3.fontSize = 11
        style3.fontName = "Helvetica-Bold"



        spacer = Spacer(1, 20)


        # create the paragraph object
        title_p = Paragraph(title, style1)
        heading_p = Paragraph(heading, style)
        underline_p = Paragraph(underline, style)
        p1 = Paragraph(text1, style3)
        p2 = Paragraph(text2, style)
        p3 = Paragraph(text3, style)
        p4 = Paragraph(text4, style)
        p5 = Paragraph(text5, style)
        timestamp_p = Paragraph(timestamp, style2)

        elements.append(title_p)
        elements.append(spacer)
        elements.append(heading_p)
        elements.append(underline_p)
        elements.append(spacer)
        elements.append(p1)
        elements.append(spacer)
        elements.append(t)

        elements.append(spacer)


        elements.append(p2)
        elements.append(p3)
        elements.append(p4)
        elements.append(spacer)
        elements.append(p5)
        elements.append(timestamp_p)

        doc.build(elements)

    create_bill_receipt(data, "bill.pdf")






