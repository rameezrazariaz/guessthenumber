import csv

productid=input("Enter the product ID: ")
quantity=int(input("Enter the quantity: "))
csv_file=csv.reader(open("shoppinglist.csv", "r"),delimiter=",")

for row in csv_file:
    if productid==row[0]:
        product_id=row[0]
        product_name=row[1]
        product_price=row[2]
        print("\nProduct ID: {}".format(row[0]))
        print("Product Name: {}".format(row[1]))
        print("Product Price: {}".format(row[2]))

total=quantity*(int(product_price))
print("\nThe Total Amount Payable is: {}".format(total))