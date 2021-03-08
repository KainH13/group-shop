

# create object to model a shopping order
class ShoppingTrip:
    def __init__(self, item_total, tip, delivery_fee, service_fee):
        self.item_total = item_total
        self.tip = tip
        self.delivery_fee = delivery_fee
        self.service_fee = service_fee

    def get_share(self, item_price):
        fraction = item_price / self.item_total
        share = ((fraction * self.item_total) 
                + (fraction * self.tip) 
                + (fraction * self.delivery_fee)
                + (fraction * self.service_fee))
        return share


if __name__ == "__main__":
    item_total = float(input("Item Total: "))
    tip = float(input("Tip: "))
    delivery_fee = float(input("Delivery Fee: "))
    service_fee = float(input("Service Fee: "))

    trip = ShoppingTrip(item_total=item_total, 
                        tip=tip, 
                        delivery_fee=delivery_fee, 
                        service_fee=service_fee)
    
    group_item_price = float(input("Group Item Price: "))
    group_share = trip.get_share(item_price=group_item_price)
    print(f"This groups share of the total price is: {group_share}")
