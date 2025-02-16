# Demonstrating boolean arithmetic
x = True + True + False  # True = 1, False = 0, so 1 + 1 + 0 = 2
y = True + False + False  # 1 + 0 + 0 = 1
print(x, y)  # Output: 2 1

# Simple variable reassignment
x = 10
print(x)  # Output: 10

class Business:
    level = 1
    revenue = 1000
    upgrade_cost = 500

    def show_status(self):
        print(f"Business Level: {self.level}")
        print(f"Current Revenue: ${self.revenue}")
        print(f"Upgrade Cost: ${self.upgrade_cost}")

    @classmethod
    def upgrade(cls):
        if cls.revenue >= cls.upgrade_cost:
            cls.revenue -= cls.upgrade_cost
            cls.level += 1
            cls.revenue *= 1.5  # 50% increase in revenue per upgrade
            cls.upgrade_cost *= 2  # Double the cost for next upgrade
            print("Business upgraded successfully!")
        else:
            print("Not enough revenue for upgrade!")

# Example usage
business = Business()
business.show_status()
business.upgrade()
business.show_status()






