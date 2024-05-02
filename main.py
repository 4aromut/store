class Store:
    def __init__(self, name, address, assortment):
        self.name = name
        self.address = address
        self.assortment = assortment

    def display_info(self):
        print(f"Store Name: {self.name}")
        print(f"Address: {self.address}")
        print("Assortment:")
        for item in self.assortment:
            print(f"- {item}")

# Пример использования
store1 = Store("SuperMart", "123 Main Street", ["Groceries", "Household Items", "Electronics"])
store2 = Store("Fashionista", "456 Elm Street", ["Clothing", "Accessories", "Shoes"])

store1.display_info()
print("\n")
store2.display_info()