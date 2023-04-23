# use oop to do coffee machine
# menu
class menu_items:
    """Resources in coffee machine"""
    def __init__(self,cost,water,milk,coffee):# initialization the class
       self.cost= cost
       self.water=water
       self.milk=milk
       self.coffe=coffee
class MENU:
    def __init__(self):
        """Ingredients of drinks"""
        self.menu={
            'latte':{
                'ingredients':
            
                  {'water':100,
                   'milk':50,
                   'coffee':25},
            
                     'cost':2.5} ,
                'cappicinno':{
                    
                    'ingredients':
                           
                 {'water':75,
                  'milk':60,
                  'coffee':20},
                  'cost':3},
                 
              'espresso':{
                    'ingredients':{
                     'water':80,
                     'coffee':25 },  
                      'cost':4}
              }
       
    def get_item(self):
        """Return all name avaliabe in  menu"""
        option=''
        for item in self.menu:
            option+=f"{item}/"
            
        return option  # to return names   
            
    def find_order(self,order_drink):
        """Search for drink in menu particular drink by name return the drink is found and return NONE is not"""
        if order_drink in self.menu:
            return self.menu[order_drink]
        else:
             print('Sorry is not found in Coffee machine') # drink is not availabe in Coffee machine
           
class MoneyMachine:
    CURANCY='$'
    Coins_value={# kind of coins 
        'quarters':0.25,
        'dimes':0.1,
        'pennies':0.01,
         'nickes':0.05   
    }
    
    # put variables
    def __init__(self):
        self.profit=0 # 
        self.money_receieved=0
        
    def report(self):
        """return current profit """
        print(f'Money:{self.CURANCY}{self.profit }')
        
    def process_coins(self):
        """ return the total calculated from coins inerted"""
        print('insert your money:')
        for coin in self.Coins_value:
            self.money_receieved+=int(input(f'How money {coin}: '))*self.Coins_value[coin]
        return self.money_receieved    
    def   make_payment(self,cost):

        self.process_coins()
        """ Return true when payment is accepted , or false insufficient """
        if self.money_receieved >cost:
            change=round(self.money_receieved-cost , 2)
            print(f'Here is : {self.CURANCY}{change} in change')
            return True
        else:
            print('Your momney is not enough so, MONEY refunded')   
            self.money_receieved=0
            return False 
class coffee_maker:
    """" models the machine made coffee"""
    
    def __init__(self): 
        # resoue=rces in coffe machine 
        self.resources={
            'water':300,
            "milk": 200,
            "coffee":100,
            
        }        
    def report(self):   
        """" Report of resources in coffee machine"""
    

        print(f"Water:{self.resources['water'] } ml")
        print(f"Milk:{self.resources['milk']} ml")
        print(f"Coffee:{self.resources['coffee']} g")
        
        
            
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        
        can_make = True
        for item in drink['ingredients']:
            if drink['ingredients'][item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def new_method(self, drink):
        return drink      
    def make_coffe(self,drink,drinks):
        """Deducted the required ingredients from resources """ 
        
        
        for item in drinks['ingredients']:
            self.resources[item]-=drinks['ingredients'][item]
            
        print(f'Here is your {drink} \u2615 ,Enjoy')    
            
        
is_on=True
while is_on:
    option=MENU().get_item()
    choice=input(f'What would you like {option}?')
    if choice=='off':
        is_on=False
    elif choice=='report':
        MoneyMachine().report()
        coffee_maker().report()
    else:
        drink=MENU().find_order(choice) 
        if coffee_maker().is_resource_sufficient(drink) and  MoneyMachine().make_payment(drink['cost']):
            coffee_maker().make_coffe(choice,drink)
                
        
        