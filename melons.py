"""Classes for melon orders."""

import random
# import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        
    def get_base_price(self):
        """Choooses a random integer between 5-9 as base price."""
        base_price = random.randrange(5, 10)

        base_price = float(base_price)

        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        elif self.qty < 10 and self.order_type == "international":

            total = (1 + self.tax) * self.qty * base_price
            total += 3
            
        total = (1 + self.tax) * self.qty * base_price
       
        return total
        
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)
        """Initialize melon order attributes."""

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty,  "international", 0.17)
        self.country_code = country_code
        """Initialize melon order attributes."""

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """No tax on government orders"""
    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
        print (self.passed_inspection)

