#Prices and cuts
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Find the average price of a haircut using a loop
total_price = 0
for price in prices:
    total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price:")
print(average_price)

#That's an expensive average price! Cut all the prices by $5 using list comprehension
new_prices = [price - 5 for price in prices]
print(new_prices)

#Revenue
#Calculate the total revenue that was brought in last week
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] + last_week[i]
    
print("Total Revenue:")
print(total_revenue)

#Find the average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#Use list comprehension to advertise all of the haircuts that are under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)