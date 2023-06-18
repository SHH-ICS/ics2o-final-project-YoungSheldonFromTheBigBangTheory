

class Inventory():
    inventory:list = []
    slots:int = 8

class Item():
    def __init__(self, Name:str, Description:str, Amount:int=1) -> None:
        self.Name:str = Name
        self.Description:str = Description
        self.Amount:int = Amount
    def Check(self, _Item) -> bool:
        return self.Name == _Item.Name and self.Description == _Item.Description
    
    def itmStr(self, _Item) -> any:
        return self.Name == _Item.Name

class Items():
    Null:Item = Item("Null", "Null")
    Spoon:Item = Item("Spoon", "Can hurt people")
    Beans:Item = Item("Beans", "Beans")
    HouseKey:Item = Item("House Key", "Unlocks house")

#Inventory.inventory[0].check(Items.Spoon)