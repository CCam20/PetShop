


def get_pet_shop_name(list):
    return list["name"]

def get_total_cash(list):
    return list["admin"]['total_cash']

def add_or_remove_cash(list, num):
    list["admin"]['total_cash'] += num
    return list  # not actualy required as the test file does not need a var returned

def get_pets_sold(list):
    return list["admin"]['pets_sold']

def increase_pets_sold(list, num):
    list["admin"]['pets_sold'] += num
    return list  # not actualy required as the test file does not need a var returned

def get_stock_count(list):
    return len(list['pets'])

def get_pets_by_breed(list, breed):
    found_pets = []
    for pet in list['pets']:        # LIST INSIDE A DICT
        if pet['breed'] == breed:
            found_pets.append(pet)
    return found_pets


def find_pet_by_name(list, name):
    for pet in list['pets']:
        if pet['name'] == name:
            return pet

def remove_pet_by_name(list, name):
    for pet in list['pets']:
        if pet['name'] == name:
            list['pets'].remove(pet) # Trust in code, not Vsc, white does not mean not working



def add_pet_to_stock(list, name):
    return list['pets'].append(name) # Same here

def get_customer_cash(list):
    return list['cash']

def remove_customer_cash(cust, num):
    cust['cash'] -= num 
    return cust

def get_customer_pet_count(list):
    return len(list["pets"])

def add_pet_to_customer(cust, new_pet):
        cust["pets"].append(new_pet)

#You should commit when you get to here if you havent already!
##########################################################
# optional below        

def customer_can_afford_pet(cust, new_pet):
    if cust['cash'] >= new_pet['price']:
        return True
    else:
        return False
#This seemed too easy for all 3 tests to run
#Check with instructors?

#remove pet form petshop, 3
#add pet to cust list['pets'] 1
#remove price of pet from customers['cash'] 4
#add money to cc_pet_shop['total_cash] 2


def sell_pet_to_customer(list, sell_pet, cust):
    for pet in list['pets']:
        if pet == sell_pet and customer_can_afford_pet(cust, pet):
            list['pets'].remove(pet)
            list['admin']['total_cash'] += sell_pet['price']
            list["admin"]['pets_sold'] += 1
            cust['cash'] -= sell_pet['price']
            cust['pets'].append(pet)
