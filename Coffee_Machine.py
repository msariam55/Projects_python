"""The MENU of drinks in machine"""
MENU={
    'espresso':{
        'ingrediants':{
            'water':100,
            'coffee':15,
        },
       'cost': 2.5
    },
    'latte':{
        'ingrediants':{
            'water':100,
            'coffee':20,
            'milk':50
        },
        'cost':3.00
    
     },
    'cappuccino':{
        'ingrediants':{
            'water':100,
            'milk':30,
            'coffee':20
        },
        'cost':2.25
    }
}




profit=0
resources={#resources input machine 
        'milk':200,
        'water':300,
        'coffee':100
    }



# to ensure the drink ingredients is enough
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:# input drink ingrdients is not enough in machine ,it can't make your drink
        if order_ingredients[item]>resources[item]:
            print('Sorry, ingredients is not enough in machine')
            return False
        else:# ==>>ingredients is enough
            return True 
        
    
def process_coins():
   """return the total calculated  from coins inserted """
   print('Please insert coins ')
   total=int(input('how many quarters:'))#0.25
   total+=int(input('how many dimess:'))#0.5
   total+=int(input('how many nickles:'))#0.01
   total+=int(input('how many piness:'))#0.05
   return total



def is_transaction_successful(money_recived,drink_cost):
    """ Return true when money is payment and return false when money is insuficient"""
    if money_recived>=drink_cost:
        change=round(money_recived - drink_cost, 2)
        print(f'Here is ${change} in change')
        global profit
        profit+=drink_cost
        return True
    
    else:
        print('sorry not enough money, Money unfunded')
        return False
    
        
def make_coffee(drink_name,order_ingredients): 
    """Deduct the order ingredients from resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]   
    print(f'Here is your drink{drink_name}, Enjoy')
    
    
    
is_on=True
while is_on:
    choice=input('what is your drink(espresso,latte,cappuccino):')
    if choice=='off':
        is_on= False
    elif choice=='report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk:{resources['milk']}ml")
            print(f"Coffee:{resources['coffee']} ml")
            print(f'Money:${profit}')
            
    else:
        drink=MENU[choice]
        if is_resources_sufficient(drink['ingrediants']):
            payment=process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingrediants'])
                
    
    