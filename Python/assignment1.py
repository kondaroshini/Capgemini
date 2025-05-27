inventory = [
    ["Strawberry", "Fruit", 3.50, 40, 10],
    ["Broccoli", "Vegetable", 2.20, 25, 8],
    ["Cheddar", "Dairy", 5.00, 18, 4],
    ["Baguette", "Bakery", 2.80, 35, 2],
    ["Blueberry", "Fruit", 4.00, 22, 6],
    ["Spinach", "Vegetable", 1.80, 30, 12],
    ["Yogurt", "Dairy", 1.20, 50, 15],
    ["Croissant", "Bakery", 3.00, 28, 3]
]


# 1)Calculate the TotalRevenue

# total_revenue=0
# for row in inventory:
#     total_revenue+=row[2]*row[3]
# print(f'Total_Revenue :{total_revenue}')


# 2)List Low stock item if stock is less than 5

# for row in inventory:
#     if row[-1] <5:
#         print(row[0])


# 3)Calculte the categorywise Revenue 

# category_rev={}
# for row in inventory:
#     revenue =row[2]*row[3]
#     if row[1] in category_rev:
#         category_rev[row[1]]+=revenue
#     else:
#         category_rev[row[1]]=revenue
# for category in category_rev:
#     print(f'Category:%s - Revenue:%1.0f'%(category,category_rev[category]))
    