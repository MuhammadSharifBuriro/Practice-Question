class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def show_details(self):
        print("Name of product is: ", self.name)
        print("Price of product is: ", self.price)
        print("Quantity of product is: ", self.quantity)
        print("Total Price: ", self.total_price())
        print("---------------------------")


class Bill:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.product_list = []        # ✔ Correct name

    def add_product(self, product):
        self.product_list.append(product)   # ✔ No double function

    def calculate_total_bill(self):
        total = 0
        for p in self.product_list:         # ✔ SAME variable name
            total += p.total_price()
        return total

    def display_bill(self):
        print("\n===== CUSTOMER BILL =====")
        print(f"Customer Name: {self.customer_name}")
        print("-------------------------------")

        for p in self.product_list:
            p.show_details()               # ✔ Correct spelling

        print(f"FINAL TOTAL BILL = {self.calculate_total_bill()}")
        print("===============================")


# MAIN PROGRAM
p1 = Product("Sugar", 120, 2)
p2 = Product("Oil", 500, 1)
p3 = Product("Rice", 180, 3)

bill = Bill("Muhammad Sharif")

bill.add_product(p1)
bill.add_product(p2)
bill.add_product(p3)

bill.display_bill()
