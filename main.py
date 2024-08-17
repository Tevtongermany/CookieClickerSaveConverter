from CCParse import CCDecode, SaveType
import os
import datetime
decoder = CCDecode()


with open("CookieClickerSaveMobileExample.txt",mode="r") as file:
    decoded_save = decoder.decode(file.read(),type=SaveType.AUTODETECT)
    print(decoded_save.get_game_started)
    print(decoded_save.currentcookies)