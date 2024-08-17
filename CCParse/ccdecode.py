import base64
from . import Enums


class CCDecode:
    def __init__(self):
        ...

    def decode(self,data:str,type:Enums.SaveType):
        if isinstance(type,Enums.SaveType.AUTODETECT):
            type = self.detectsavetype(data=data)



    def detectsavetype(self,data:str):
        if data.endswith("%3D%21END%21"):
            return Enums.SaveType.PC
        else:
            return Enums.SaveType.MOBILE
        