from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

end = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while not end:
    choose = input("What would you like? (espresso/latte/cappuccino)?")
    if choose == "off":
        end = True
    elif choose == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choose)
        is_enough_ingredient = coffee_maker.is_resource_sufficient(drink)
        make_payment = money_machine.make_payment(drink.cost)
        if is_enough_ingredient and make_payment:
            coffee_maker.make_coffee(drink)
