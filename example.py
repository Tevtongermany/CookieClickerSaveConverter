from CCParse import CCDecode, SaveType, ccpc,ccmobile
from CCParse.models.ccmobile import CCSaveMobile
from CCParse.models.ccpc import CCSavePC
import os
import datetime
decoder = CCDecode()


def Parse_Mobile_Save():
    with open("CookieClickerSaveMobileExample.txt",mode="r") as file:
        decoded_save:CCSaveMobile = decoder.decode(file.read(),type=SaveType.MOBILE)

        print(f"""
        Game First Time Started: {decoded_save.get_game_started}
        Last Login: {decoded_save.get_time}
        Run Started: {decoded_save.get_run_started}
        Seed: {decoded_save.get_seed}

        """)

        print(f"""
        Current Cookies: {decoded_save.get_cookies}
        Clicked Cookies: {decoded_save.get_Clicked_Cookies}
        Earned Cookies: {decoded_save.get_Earned_Cookies}
        Total Cookies: {decoded_save.get_Total_Cookies}

        """)



        print("")

            
        print(f"""
        Cursor:
            Bought: {decoded_save.get_Buildings.cursor.bought}
            Amount: {decoded_save.get_Buildings.cursor.amount}
            Amount Max: {decoded_save.get_Buildings.cursor.amountMax}
            Cookies Made: {decoded_save.get_Buildings.cursor.cookiesmade}

        Grandma:
            Bought: {decoded_save.get_Buildings.grandma.bought}
            Amount: {decoded_save.get_Buildings.grandma.amount}
            Amount Max: {decoded_save.get_Buildings.grandma.amountMax}
            Cookies Made: {decoded_save.get_Buildings.grandma.cookiesmade}

        Farm:
            Bought: {decoded_save.get_Buildings.farm.bought}
            Amount: {decoded_save.get_Buildings.farm.amount}
            Amount Max: {decoded_save.get_Buildings.farm.amountMax}
            Cookies Made: {decoded_save.get_Buildings.farm.cookiesmade}

        Mine:
            Bought: {decoded_save.get_Buildings.mine.bought}
            Amount: {decoded_save.get_Buildings.mine.amount}
            Amount Max: {decoded_save.get_Buildings.mine.amountMax}
            Cookies Made: {decoded_save.get_Buildings.mine.cookiesmade}

        Factory:
            Bought: {decoded_save.get_Buildings.factory.bought}
            Amount: {decoded_save.get_Buildings.factory.amount}
            Amount Max: {decoded_save.get_Buildings.factory.amountMax}
            Cookies Made: {decoded_save.get_Buildings.factory.cookiesmade}

        Bank:
            Bought: {decoded_save.get_Buildings.bank.bought}
            Amount: {decoded_save.get_Buildings.bank.amount}
            Amount Max: {decoded_save.get_Buildings.bank.amountMax}
            Cookies Made: {decoded_save.get_Buildings.bank.cookiesmade}

        Temple:
            Bought: {decoded_save.get_Buildings.temple.bought}
            Amount: {decoded_save.get_Buildings.temple.amount}
            Amount Max: {decoded_save.get_Buildings.temple.amountMax}
            Cookies Made: {decoded_save.get_Buildings.temple.cookiesmade}

        Wizard Tower:
            Bought: {decoded_save.get_Buildings.wizard_tower.bought}
            Amount: {decoded_save.get_Buildings.wizard_tower.amount}
            Amount Max: {decoded_save.get_Buildings.wizard_tower.amountMax}
            Cookies Made: {decoded_save.get_Buildings.wizard_tower.cookiesmade}

        Shipment:
            Bought: {decoded_save.get_Buildings.shipment.bought}
            Amount: {decoded_save.get_Buildings.shipment.amount}
            Amount Max: {decoded_save.get_Buildings.shipment.amountMax}
            Cookies Made: {decoded_save.get_Buildings.shipment.cookiesmade}

        Alchemy Lab:
            Bought: {decoded_save.get_Buildings.alchemy_lab.bought}
            Amount: {decoded_save.get_Buildings.alchemy_lab.amount}
            Amount Max: {decoded_save.get_Buildings.alchemy_lab.amountMax}
            Cookies Made: {decoded_save.get_Buildings.alchemy_lab.cookiesmade}

        Portal:
            Bought: {decoded_save.get_Buildings.portal.bought}
            Amount: {decoded_save.get_Buildings.portal.amount}
            Amount Max: {decoded_save.get_Buildings.portal.amountMax}
            Cookies Made: {decoded_save.get_Buildings.portal.cookiesmade}

        Time Machine:
            Bought: {decoded_save.get_Buildings.time_machine.bought}
            Amount: {decoded_save.get_Buildings.time_machine.amount}
            Amount Max: {decoded_save.get_Buildings.time_machine.amountMax}
            Cookies Made: {decoded_save.get_Buildings.time_machine.cookiesmade}

        Antimatter Condenser:
            Bought: {decoded_save.get_Buildings.antimatter_condenser.bought}
            Amount: {decoded_save.get_Buildings.antimatter_condenser.amount}
            Amount Max: {decoded_save.get_Buildings.antimatter_condenser.amountMax}
            Cookies Made: {decoded_save.get_Buildings.antimatter_condenser.cookiesmade}

        Prism:
            Bought: {decoded_save.get_Buildings.prism.bought}
            Amount: {decoded_save.get_Buildings.prism.amount}
            Amount Max: {decoded_save.get_Buildings.prism.amountMax}
            Cookies Made: {decoded_save.get_Buildings.prism.cookiesmade}

        Chancemaker:
            Bought: {decoded_save.get_Buildings.chancemaker.bought}
            Amount: {decoded_save.get_Buildings.chancemaker.amount}
            Amount Max: {decoded_save.get_Buildings.chancemaker.amountMax}
            Cookies Made: {decoded_save.get_Buildings.chancemaker.cookiesmade}

        Fractal Engine:
            Bought: {decoded_save.get_Buildings.fractal_engine.bought}
            Amount: {decoded_save.get_Buildings.fractal_engine.amount}
            Amount Max: {decoded_save.get_Buildings.fractal_engine.amountMax}
            Cookies Made: {decoded_save.get_Buildings.fractal_engine.cookiesmade}

        JavaScript Console:
            Bought: {decoded_save.get_Buildings.javascript_console.bought}
            Amount: {decoded_save.get_Buildings.javascript_console.amount}
            Amount Max: {decoded_save.get_Buildings.javascript_console.amountMax}
            Cookies Made: {decoded_save.get_Buildings.javascript_console.cookiesmade}

        Idleverse:
            Bought: {decoded_save.get_Buildings.idleverse.bought}
            Amount: {decoded_save.get_Buildings.idleverse.amount}
            Amount Max: {decoded_save.get_Buildings.idleverse.amountMax}
            Cookies Made: {decoded_save.get_Buildings.idleverse.cookiesmade}

        Cortex Baker:
            Bought: {decoded_save.get_Buildings.cortex_baker.bought}
            Amount: {decoded_save.get_Buildings.cortex_baker.amount}
            Amount Max: {decoded_save.get_Buildings.cortex_baker.amountMax}
            Cookies Made: {decoded_save.get_Buildings.cortex_baker.cookiesmade}

        You:
            Bought: {decoded_save.get_Buildings.you.bought}
            Amount: {decoded_save.get_Buildings.you.amount}
            Amount Max: {decoded_save.get_Buildings.you.amountMax}
            Cookies Made: {decoded_save.get_Buildings.you.cookiesmade}
        """)


def Parse_PC_Save():
    with open("GexBakery.txt",mode="r") as file:
        decoded_save:CCSavePC = decoder.decode(file.read(),type=SaveType.PC)
        print(decoded_save.cookies)
        print(decoded_save.cookiesEarned)
        print(decoded_save.cookiesSuckedByWrinklers)
        print(decoded_save.bakeryName)
        

Parse_PC_Save()