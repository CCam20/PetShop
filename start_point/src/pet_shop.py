


def get_pet_shop_name(list):
    return list["name"]

def get_total_cash(list):
    return list["admin"]['total_cash']

def add_or_remove_cash(list, num):
    list["admin"]['total_cash'] += num
    return list

def get_pets_sold(list):
    return list["admin"]['pets_sold']

def increase_pets_sold(list, num):
    list["admin"]['pets_sold'] += num
    return list

def get_stock_count(list):
    return len(list['pets'])

def get_pets_by_breed(list, breed):
    found_pets = []
    for pet in list['pets']:
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
            list['pets'].remove(pet)



def add_pet_to_stock(list, name):
    return list['pets'].append(name)

def get_customer_cash(list):
    return list['cash']

def remove_customer_cash(cust, num):
    cust['cash'] -= num 
    return cust

def get_customer_pet_count(list):
    return len(list["pets"])

def add_pet_to_customer(cust, new_pet):
        cust["pets"].append(new_pet)
#You should commit when you get to here
##########################################################
# optional below        