class Address:
    def __init__(self, street: str, city: str):
        self.street = street
        self.city = city

    def to_dict(self):
        return {
            'street': self.street,
            'city': self.city
        }


class Shipping:
    def __init__(self, user_id: int, address: dict):
        self.user_id = user_id
        self.address = Address(
            street=address['street'],
            city=address['city']
        )

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'address': self.address.to_dict()
        }




