"""
Package for determining different values and attributes of crypto
"""


class Crypto:
    def __init__(self, name, value=0.00, shares=0):
        self.name = name
        self.value = value
        self.shares = shares

    def update_value(self, new_value=0.00):
        self.value = new_value

    def purchase(self, dollar_spent=1.00):
        self.shares = dollar_spent / self.value

    def update_shares(self, shares=0.0):
        self.shares = shares

    def total_value(self):
        print("$", round(self.value * self.shares, 2))


crypto = Crypto("SHIB")
crypto.update_value(0.47)
crypto.total_value()
# crypto.purchase(408.11)
crypto.update_shares(608.117301)
crypto.total_value()
crypto.update_value(5)
crypto.total_value()
