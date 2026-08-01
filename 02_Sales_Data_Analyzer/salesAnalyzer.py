file = open("sales_data.csv","r")
lines = file.readlines()
print(lines)

newData = []

for line in lines[1: ]:
   field = line.strip().split(",")
   field[5] = int(field[5])
   field[6] = int(field[6])
   newData.append(field)
   
print(newData)

total_revenue = 0
for row in newData:
  quantity = row[5]
  price = row[6]
  total_revenue = total_revenue + quantity*price
print("total_revenue",total_revenue)


total_orders = len(newData)
print("Total orders :",total_orders )


total_quantity = 0

for row in newData:
   total_quantity += row[5]

print(total_quantity)


category_revenue = {}

for row in newData:
   category = row[4]
   revenue = row[5]*row[6]

   if category in category_revenue:
      category_revenue[category] += revenue

   else :
      category_revenue[category] = revenue

for cat,rev in category_revenue.items():
    
   print(f"{cat} : {rev}")


product_revenue = {}

for row in newData:
   product = row[3]
   revenue = row[5]*row[6]

   if product in product_revenue:
      product_revenue[product] += revenue

   else: 
      product_revenue[product] = revenue

for pro , rev in product_revenue.items():
   print(f"{pro} : {rev}")
      

product_quantity = {}

for row in newData:
   product = row[3]
   quantity = row[5]

   if product in product_quantity:
      product_quantity[product] += quantity

   else: 
      product_quantity[product] = quantity

highest_sold = None
max_qty = 0

for pro , qty in product_quantity.items():
     
     if max_qty < qty :
       max_qty = qty
       highest_sold = pro

print("highest sold :", highest_sold)    
        
      
customer_revenue = {}

for row in newData:
   customer = row[2]
   revenue = row[5]*row[6]

   if customer in customer_revenue:
      customer_revenue[customer] += revenue
   else:
      customer_revenue[customer] = revenue

highest_revenue_customer = None
max_revenue = 0 

for cust , rev in customer_revenue.items():
   
   if max_revenue<rev:
    max_revenue = rev 
    highest_revenue_customer = cust

print(f"highest_revenue_customer : {highest_revenue_customer}\n max_revenue : {max_revenue}")

daily_revenue =  {}

for row in newData:
   date = row[1]
   revenue = row[5]*row[6]

   if date in daily_revenue:
      daily_revenue[date] += revenue

   else: 
      daily_revenue[date] = revenue

print("Total Revenue : \n")

for date,rev in daily_revenue.items():
 print(f"{date} : {rev}")

from datetime import datetime

start = input("enter the start date(YYYY-MM-DD)")
end = input("enter the end date(YYYY-MM-DD)")

start_date = datetime.strptime(start , "%Y-%m-%d")
end_date = datetime.strptime(end , "%Y-%m-%d")


totald_revenue = 0

for row in newData:
   order_date = datetime.strptime(row[1],"%d-%m-%Y")
   
   if start_date <=order_date<=end_date:
      totald_revenue += row[5]*row[6]


print("total revenue =",totald_revenue)


elecfile = open("electrical.csv","w")

elecfile.write("OrderID,Date,Customer,Product,Category,Quantity,Price\n")

for row in newData:
   if row[4] == "Electronics":
     str_row = ",".join([str(item) for item in row])
     elecfile.write(str_row + "\n")
elecfile.close()

print("All Electrical Items saved to elctrical.csv")