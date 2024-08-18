import base64
import re
from . import Enums
from .models import ccmobile
import ast

class CCDecode:
    def __init__(self):
        ...

    def decode(self,data:str,type:Enums.SaveType) -> ccmobile.CCSaveMobile:
        if type is Enums.SaveType.AUTODETECT:
            type = self.detectsavetype(data=data)

        if type is Enums.SaveType.PC:
            data = data.replace("%3D%21END%21","")
            decoded_save = base64.b64decode(data)
            decoded_save = decoded_save.decode("utf-8")
            sections = decoded_save.split('|')
            parsed_data = []

            for section in sections:
                if ';' in section:
                    parts = [subpart.split(',') if ',' in subpart else subpart for subpart in section.split(';')]
                else:
                    parts = section
                
                parsed_data.append(parts)
            return parsed_data
        if type is Enums.SaveType.MOBILE:
            decoded_save = base64.b64decode(data)
            decoded_save = decoded_save.decode("utf-8")
            decoded_save = ast.literal_eval(decoded_save)
            return ccmobile.CCSaveMobile(decoded_save)
        
        return "guh"

    def detectsavetype(self,data:str):
        if data.endswith("%3D%21END%21"):
            return Enums.SaveType.PC
        else:
            return Enums.SaveType.MOBILE
        