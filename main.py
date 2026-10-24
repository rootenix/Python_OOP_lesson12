# class StudentScore:
#     def __init__(self, name:str, score: float=0):
#         self.name=name
#         self.__score=score
#     def add_scode(self,great):
#         if great>0:
#             self.__score+=great
#             print(self.__score)
#         else:
#             print("musbat son kiriting")
#     def get_score(self):
#         print(self.__score)
# StudentScore("ali").add_scode(50)

# class Product:
#      def __init__(self,id:int, name:str, price:float, stock:int):
#         self.name = name 
#         self.price = price
#         self.id=id
#         self.stock=stock
# class Product_info(Product):
#     def info(self):
#         print(f"nomi:{self.name}\nnarxi:{self.price}\nBor:{self.stock}ta")
    
#     def total_price(self):
#         print(f"Jami:{self.stock*self.price}")
#     def product_add(self):
#         Products=[]
#         Products.append(self.name)
        
#     def shipping_cost(self,pul):



# class Product: 
#     def init(self, product_id, name, price, stock):
#         self.id = product_id 
#         self.name = name 
#         self.price = price 
#         self.stock = stock
# def get_info(self):
#     print(f"Product: {self.name}")
#     print(f"Price: ${self.price}")
#     print(f"Stock: {self.stock}")
# class Customer:
#      def init(self, name, balance):
#          self.name = name 
#          self.balance = balance 
#          self.cart = [] 
#          self.orders = []
# def add_to_cart(self, product, quantity):
#     if quantity <= 0:
#         print("Invalid quantity")
#         return

#     if product.stock < quantity:
#         print("Not enough stock")
#         return

#     for item in self.cart:
#         if item["product"].id == product.id:
#             item["quantity"] += quantity
#             print(f"{quantity} x {product.name} added to cart")
#             return

#     self.cart.append({
#         "product": product,
#         "quantity": quantity
#     })

#     print(f"{quantity} x {product.name} added to cart")

# def show_cart(self):
#     if not self.cart:
#         print("Cart is empty")
#         return

#     print("\n===== CART =====")

#     for item in self.cart:
#         product = item["product"]
#         quantity = item["quantity"]
#         subtotal = product.price * quantity

#         print(
#             f"{product.name} — "
#             f"${product.price} x {quantity} = ${subtotal}"
#         )

#     print(f"Total: ${self.get_total()}")

# def get_total(self):
#     total = 0

#     for item in self.cart:
#         product = item["product"]
#         quantity = item["quantity"]

#         total += product.price * quantity

#     return total

# def checkout(self):
#     if not self.cart:
#         print("Cart is empty")
#         return

#     total = self.get_total()

#     if total >= 1000:
#         discount = total * 0.10
#     elif total >= 500:
#         discount = total * 0.05
#     else:
#         discount = 0

#     final_price = total - discount

#     if self.balance < final_price:
#         print("Insufficient balance")
#         return

#     for item in self.cart:
#         product = item["product"]
#         quantity = item["quantity"]
#         product.stock -= quantity

#     self.balance -= final_price

#     order = {
#         "items": self.cart.copy(),
#         "total": total,
#         "discount": discount,
#         "final_price": final_price
#     }

#     self.orders.append(order)
#     self.cart.clear()

#     print("Order successfully completed!")

# def show_orders(self):
#     if not self.orders:
#         print("No orders yet")
#         return

#     for index, order in enumerate(self.orders, start=1):
#         print(f"\nOrder {index}:")

#         for item in order["items"]:
#             product = item["product"]
#             quantity = item["quantity"]

#             print(
#                 f"{product.name} — "
#                 f"${product.price} x {quantity}"
#             )

#         print(f"Total: ${order['total']}")
#         print(f"Discount: ${order['discount']}")
#         print(f"Final price: ${order['final_price']}")
# def search_product(products, keyword):
#     for product in products:
#         if keyword.lower() in product.name.lower():
#             print( f"{product.name} — " f"${product.price} — " f"Stock: {product.stock}" )
# products = [ Product(1, "Laptop", 800, 5), Product(2, "Mouse", 25, 20), Product(3, "Keyboard", 50, 10), Product(4, "Monitor", 300, 7), Product(5, "Headphones", 100, 15) ]
# customer = Customer("Ali", 1500)
# search_product(products, "mouse")
# customer.add_to_cart(products[0], 1)
# customer.add_to_cart(products[1], 2)
# customer.add_to_cart(products[2], 1)
# customer.show_cart()
# customer.checkout()
# customer.show_orders()
# print(customer.name)
# print(customer.balance)
# for product in products: print(product.name, product.stock)


# asli="rdtrcfkugvukhvkhv,jhn bhjb4654645132132      ".strip()

# asli_list=[]
# teskari=""
# for i in range(len(asli)):
#     asli_list.append(asli[i])
# for i in range(len(asli_list)):
#     teskari+=asli_list[-i-1]
# print(teskari)

son=int(input("djn"))

def tubson(son):
    count=0
    for i in range(1,son+1):
        if son%i==0:
            count+=1
    if count==2:
        print("bu tub son")
    else:
        print("murakkab son")
tubson(son)
