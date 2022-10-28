class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        item = {
            "name": name,
            "price": price
        }
        self.items.append(item)

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

myStore = Store("Best Store Ever")
myStore.add_item("Rubik's Cube", 12.99)
myStore.add_item("Table tennis table", 350.99)
myStore.add_item("Badminton rackquet", 45)

print(myStore.stock_price())