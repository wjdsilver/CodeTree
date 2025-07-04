product_name, product_code = input().split()
product_code = int(product_code)

class Item:
    def __init__(self,name="codetree",code=50):
        self.name=name
        self.code=code

item1=Item()
item2=Item(product_name,product_code)
print(f"""product {item1.code} is {item1.name}
product {item2.code} is {item2.name}""")