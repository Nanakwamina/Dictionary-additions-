# Name: Kobena Badu Enyam
# Email: kobena.badu@azubiafrica.org
import os

#welcome the stock zero level strategy
print('welcome to the zero-stock level strategy')

#enter the number of months 
number_of_months = int(input('enter the number of months:'))

if number_of_months <= 12:
    print('you are good to go')



#create an empty list to store values
list_of_planned_sales = []

#initial stock level
initial_stock_level = int(input('please enter the initial stock level: '))

list_of_planned_sales.append(initial_stock_level)

list_length = number_of_months 

#while another_month == 'yes':
for i in range(list_length):
        planned_sales_month = int(input('Enter planned sales quantity for the month: '))
        list_of_planned_sales.append(planned_sales_month)
        #another_month = input('please enter yes or no if you have more sales quantities for proceeding months: ')

        #if another_month == 'yes':
        os.system('cls')
print(list_of_planned_sales)


(new_list_of_planned_sales) = []
new_list_of_planned_sales.append(0)

#computation for actual production quantity for the second month
k = list_of_planned_sales[2] - (list_of_planned_sales[0] - list_of_planned_sales[1])
print(k)
new_list_of_planned_sales.append(k)

#print a list from the list_of_planned_sales from the 4th element to the last element
r = list_of_planned_sales[3:]
print(r)

#joining two lists
new_list_of_planned_sales.extend(r)

#printing joined lists
print(new_list_of_planned_sales)

#defining a new list with the format 'production quantity month plus the month number'
new_list = []
basestring = 'production quantity month'
result = ['{}_{}'.format(basestring,j) for j in range(1,number_of_months+1)]

#populating new list        
new_list.extend(result)
        

#printing new list
print(new_list)

#joining two list into dictionaries
res = {}
for key in new_list:
    for value in new_list_of_planned_sales:
        res[key] = value
        new_list_of_planned_sales.remove(value)
        break
 
# Printing resultant dictionary
print("production quantity per the number of months requested is : " + str(res))
