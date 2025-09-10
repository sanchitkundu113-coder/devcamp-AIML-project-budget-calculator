monthly_income = float(input('monthly income:'))

food = float(input('food:'))

rent = float(input('rent:'))

electricity = float(input('electricity:'))

others = float(input('others:'))

net_expenses =  food + rent + electricity +others

savings = monthly_income - net_expenses

print(f"your savings:{savings}")

percentage_savings = (savings*100)/monthly_income #the fraction of income which goes to savings #

print(f"you saves about {percentage_savings} percent of your income")

if percentage_savings <= 5 :#if savings are less than or equal to 5 percent of income #

    print(" advice :you are overspending too much.") 

elif percentage_savings <= 30 : #if savings are less than or equal to 30 percent of income #

    print(" advice : you need to spend a little wisely")

elif 30 < percentage_savings < 50:

         #if savings are more than 30 percent but less than 50 percent of the income #

    print(" advice: you are financialy stable")

elif percentage_savings >= 50: #if savings are more than or equal to 50 percent of income #

   print(" advice : great savings ")

   summary = (f"income:{ monthly_income }"

   f"expenses:{net_expenses}"

   f"savings:{savings}")

with open('buget.txt','w') as f:

 f.write (summary)   

 print('saved to buget.txt')
