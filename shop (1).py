#Miguel Rodriguez
#March 4,2021
#CSS 225 Lab Activity 3
#shop.py


def check_money(total_cost, customer_money):
    if total_cost <= customer_money:
        return True 
    else:
        return False



#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)
