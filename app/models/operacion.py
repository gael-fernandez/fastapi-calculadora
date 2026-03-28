from pydantic import BaseModel
class numeros(BaseModel):
    a:float
    b:float

class FakeDB():
 def __init__(self):
    self.a=23
    self.b=34