class Order:
    def __init__(self,name,items,price,discount):
        self.name = name
        self.items = items
        self.__price = price
        self.__discount = discount

    def __finalcharges(self):
        return self.__price - self.__discount

    def _adminview(self):
        return {
            "Customer name:" : self.name,
            "Ordered Items" : self.items,
            "Price:" : self.__price,
            "Discount:" : self.__discount,
            "Final Charges:" : self.__finalcharges()
        }
    def customerview(self):
          return {
              "Customer name:" : self.name,
              "Ordered Items" : self.items,
              "Final Bill:" : self.__finalcharges()
          }

class Admin:
    def show_adminview(self,order):
        return order._adminview()
class Customer:
    def show_customerview(self,order):
        return order.customerview()

order=Order(name="Subramanian",items=["Paratto","Salna","Omlete"],price=500,discount=50)

admin=Admin()
customer=Customer()

print("Admin View:")
print(admin.show_adminview(order))

print("Customer View:")
print(customer.show_customerview(order))
