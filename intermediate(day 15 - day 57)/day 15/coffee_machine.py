from data_cafe import MENU, resources


def total(a, b, c, d):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    pay = a * quarters + b * dimes + c * nickles + d * pennies
    return pay


def residual_material(choose):
    residual_material = {"water": [], "milk": [], "coffee": []}
    if choose == "espresso":
        residual_material = (
            resources["water"] - MENU["espresso"]["ingredients"]["water"]
        )
        residual_material["milk"] = (
            resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
        )
        residual_material["coffee"] = (
            resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        )
    if choose == "latte":
        residual_material["water"] = (
            resources["water"] - MENU["latte"]["ingredients"]["water"]
        )
        residual_material["milk"] = (
            resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        )
        residual_material["coffee"] = (
            resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        )
    elif choose == "cappuccino":
        residual_material["water"] = (
            resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        )
        residual_material["milk"] = (
            resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        )
        residual_material["coffee"] = (
            resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        )
    elif choose == "report":
        residual_material = resources
    return residual_material


if __name__ == "__main__":
    end = False
    while not end:
        money = 0
        choose = input("What would you like? (espresso/latte/cappuccino)?")
        residual_material(choose)
        water = residual_material(choose)["water"]
        milk = residual_material(choose)["milk"]
        coffee = residual_material(choose)["coffee"]
        if choose == "off":
            end = True
        elif choose == "report":
            print(
                f"Water: {water}ml \nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney:${money}"
            )
        else:
            if water > 0 and milk > 0 and coffee > 0:
                print("Please insert coin.")
                a = float(input("How many quarters?"))
                b = float(input("How many dimes"))
                c = float(input("How many nickles?"))
                d = float(input("How many pennies?"))
                extra = total(a, b, c, d) - MENU[choose]["cost"]
                if extra == 0:
                    print(f"Here your {choose}. Enjoy!!")
                    money += MENU[choose]["cost"]
                    resources = residual_material(choose)
                elif extra > 0:
                    print(f"Here is ${round(extra,2)} in change")
                    print(f"Here your {choose}. Enjoy!!")
                    money += MENU[choose]["cost"]
                    resources = residual_material(choose)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            elif water < 0:
                print("Sorry there is not enough water.")
            elif milk < 0:
                print("Sorry there is not enough milk.")
            elif coffee < 0:
                print("Sorry there is not enough coffee.")
