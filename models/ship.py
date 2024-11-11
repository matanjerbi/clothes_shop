class Shipping:
    def __init__(self, user_details, type_ship, adress):
        self.user_details = user_details
        self.type_ship = type_ship
        self.adress = adress

    def to_dict(self):
        return {'user_details': self.user_details,
                'type_ship': self.type_ship,
                'adress': self.adress}

