class Sale:
    def __init__(self, user_details, item_id, quantity, total_price):
        self.user_details = user_details
        self.item_id = item_id
        self.quantity = quantity
        self.total_price = total_price

    def to_dict(self):
        return {'user_details': self.user_details,
                'item_id': self.item_id,
                'quantity': self.quantity,
                'total_price': self.total_price}