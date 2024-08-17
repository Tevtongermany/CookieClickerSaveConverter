import CCParse
import os
import datetime
decoder = CCParse.ccdecode.CCDecode()


with open("CookieClickerSaveMobileExample.txt",mode="r") as file:
    decoded_save = decoder.decode(file.read(),type=CCParse.Enums.SaveType.AUTODETECT)
    print(decoded_save.get_game_started)