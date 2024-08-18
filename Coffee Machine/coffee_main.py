from menu_coffee import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

My_money_machine = MoneyMachine()
My_coffee_maker = CoffeeMaker()
My_menu = Menu()

Logo="""

  _____ _________________ _____ _____    ___  ___  ___  _____  _   _ _____ _   _  _____     
/  __ \  _  |  ___|  ___|  ___|  ___|   |  \/  | / _ \/  __ \| | | |_   _| \ | ||  ___|  _ 
| /  \/ | | | |_  | |_  | |__ | |__     | .  . |/ /_\ \ /  \/| |_| | | | |  \| || |__   (_)
| |   | | | |  _| |  _| |  __||  __|    | |\/| ||  _  | |    |  _  | | | | . ` ||  __|     
| \__/\ \_/ / |   | |   | |___| |___    | |  | || | | | \__/\| | | |_| |_| |\  || |___   _ 
 \____/\___/\_|   \_|   \____/\____/    \_|  |_/\_| |_/\____/\_| |_/\___/\_| \_/\____/  (_)
                                                                                           
                                                                                           
                                                                                           
                                                                                           
                                                                                           
                                                                                           
                                                                                             """

is_on = True

def My_report():

 My_coffee_maker.report()
 My_money_machine.report()

def My_refill():
 My_coffee_maker.refill()


print(Logo)

while is_on:
    
    print()
    print("Latte: $2.5 , Espresso: $1.5 , Cappuccino: $3 ....\n")
    print("To get details of the machine enter 'report'..\n")
    print("To off the machine enter 'off'..\n")
    print("To refill the ingredients enter 'refill'\n")

    order = My_menu.get_items()
    Choice = input(f"Which coffee do you want? ({order})? ")
    if Choice == "report":
      My_report()
    elif Choice =="refill":
      My_refill()

    elif Choice =="off":
      is_on = False
    else:
        drink = My_menu.find_drink(Choice)
        if My_coffee_maker.is_resource_sufficient(drink):
          if My_money_machine.make_payment(drink.cost):
              My_coffee_maker.make_coffee(drink)



