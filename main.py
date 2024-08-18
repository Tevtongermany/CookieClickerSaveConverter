from CCParse import CCDecode, SaveType
import os
import datetime
decoder = CCDecode()


with open("CookieClickerSaveMobileExample.txt",mode="r") as file:
    decoded_save = decoder.decode(file.read(),type=SaveType.AUTODETECT)
    print(f"""

    Game First Time Started: {decoded_save.get_game_started}
    Last Login: {decoded_save.get_time}
    Run Started: {decoded_save.get_run_started}
    Seed: {decoded_save.get_seed}

    """)
    print(f"""
    Current Cookies: {decoded_save.get_cookies}
    Clicked Cookies: {decoded_save.get_clicked_cookies}
    Earned Cookies: {decoded_save.get_earned_cookies}
    Total Cookies: {decoded_save.get_total_cookies}

    """)



    # print(f"""
    # Cursor:
    #     Bought: {decoded_save.get_buildings.cursor.bought}
    #     Amount: {decoded_save.get_buildings.cursor.amount}
    #     Amount Max: {decoded_save.get_buildings.cursor.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.cursor.cookiesmade}

    # Grandma:
    #     Bought: {decoded_save.get_buildings.grandma.bought}
    #     Amount: {decoded_save.get_buildings.grandma.amount}
    #     Amount Max: {decoded_save.get_buildings.grandma.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.grandma.cookiesmade}

    # Farm:
    #     Bought: {decoded_save.get_buildings.farm.bought}
    #     Amount: {decoded_save.get_buildings.farm.amount}
    #     Amount Max: {decoded_save.get_buildings.farm.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.farm.cookiesmade}

    # Mine:
    #     Bought: {decoded_save.get_buildings.mine.bought}
    #     Amount: {decoded_save.get_buildings.mine.amount}
    #     Amount Max: {decoded_save.get_buildings.mine.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.mine.cookiesmade}

    # Factory:
    #     Bought: {decoded_save.get_buildings.factory.bought}
    #     Amount: {decoded_save.get_buildings.factory.amount}
    #     Amount Max: {decoded_save.get_buildings.factory.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.factory.cookiesmade}

    # Bank:
    #     Bought: {decoded_save.get_buildings.bank.bought}
    #     Amount: {decoded_save.get_buildings.bank.amount}
    #     Amount Max: {decoded_save.get_buildings.bank.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.bank.cookiesmade}

    # Temple:
    #     Bought: {decoded_save.get_buildings.temple.bought}
    #     Amount: {decoded_save.get_buildings.temple.amount}
    #     Amount Max: {decoded_save.get_buildings.temple.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.temple.cookiesmade}

    # Wizard Tower:
    #     Bought: {decoded_save.get_buildings.wizard_tower.bought}
    #     Amount: {decoded_save.get_buildings.wizard_tower.amount}
    #     Amount Max: {decoded_save.get_buildings.wizard_tower.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.wizard_tower.cookiesmade}

    # Shipment:
    #     Bought: {decoded_save.get_buildings.shipment.bought}
    #     Amount: {decoded_save.get_buildings.shipment.amount}
    #     Amount Max: {decoded_save.get_buildings.shipment.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.shipment.cookiesmade}

    # Alchemy Lab:
    #     Bought: {decoded_save.get_buildings.alchemy_lab.bought}
    #     Amount: {decoded_save.get_buildings.alchemy_lab.amount}
    #     Amount Max: {decoded_save.get_buildings.alchemy_lab.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.alchemy_lab.cookiesmade}

    # Portal:
    #     Bought: {decoded_save.get_buildings.portal.bought}
    #     Amount: {decoded_save.get_buildings.portal.amount}
    #     Amount Max: {decoded_save.get_buildings.portal.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.portal.cookiesmade}

    # Time Machine:
    #     Bought: {decoded_save.get_buildings.time_machine.bought}
    #     Amount: {decoded_save.get_buildings.time_machine.amount}
    #     Amount Max: {decoded_save.get_buildings.time_machine.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.time_machine.cookiesmade}

    # Antimatter Condenser:
    #     Bought: {decoded_save.get_buildings.antimatter_condenser.bought}
    #     Amount: {decoded_save.get_buildings.antimatter_condenser.amount}
    #     Amount Max: {decoded_save.get_buildings.antimatter_condenser.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.antimatter_condenser.cookiesmade}

    # Prism:
    #     Bought: {decoded_save.get_buildings.prism.bought}
    #     Amount: {decoded_save.get_buildings.prism.amount}
    #     Amount Max: {decoded_save.get_buildings.prism.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.prism.cookiesmade}

    # Chancemaker:
    #     Bought: {decoded_save.get_buildings.chancemaker.bought}
    #     Amount: {decoded_save.get_buildings.chancemaker.amount}
    #     Amount Max: {decoded_save.get_buildings.chancemaker.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.chancemaker.cookiesmade}

    # Fractal Engine:
    #     Bought: {decoded_save.get_buildings.fractal_engine.bought}
    #     Amount: {decoded_save.get_buildings.fractal_engine.amount}
    #     Amount Max: {decoded_save.get_buildings.fractal_engine.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.fractal_engine.cookiesmade}

    # JavaScript Console:
    #     Bought: {decoded_save.get_buildings.javascript_console.bought}
    #     Amount: {decoded_save.get_buildings.javascript_console.amount}
    #     Amount Max: {decoded_save.get_buildings.javascript_console.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.javascript_console.cookiesmade}

    # Idleverse:
    #     Bought: {decoded_save.get_buildings.idleverse.bought}
    #     Amount: {decoded_save.get_buildings.idleverse.amount}
    #     Amount Max: {decoded_save.get_buildings.idleverse.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.idleverse.cookiesmade}

    # Cortex Baker:
    #     Bought: {decoded_save.get_buildings.cortex_baker.bought}
    #     Amount: {decoded_save.get_buildings.cortex_baker.amount}
    #     Amount Max: {decoded_save.get_buildings.cortex_baker.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.cortex_baker.cookiesmade}

    # You:
    #     Bought: {decoded_save.get_buildings.you.bought}
    #     Amount: {decoded_save.get_buildings.you.amount}
    #     Amount Max: {decoded_save.get_buildings.you.amountMax}
    #     Cookies Made: {decoded_save.get_buildings.you.cookiesmade}
    # """)