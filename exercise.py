class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return 2.5 * self.wall_area


class Paint:

    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        price_of_paint = 0
        if self.color.lower() == "white":
            price_of_paint = self.buckets * 1.99
        else:
            price_of_paint = self.buckets * 2.19
        return price_of_paint


class DiscountedPaint(Paint):

    def discounted_price(self, discount_percentage: float):
        total_price = self.total_price()
        if not 0 <= discount_percentage <= 100.0:
            return total_price
        total_price *= (1.0 - discount_percentage/100)
        return total_price


p1 = Paint(10, "white")
p2 = Paint(15, "blue")
p3 = DiscountedPaint(15, "blue")
print(f"Total price for {p1.buckets} buckets (color: {p1.color}) is ${p1.total_price()}.")
print(f"Total price for {p2.buckets} buckets (color: {p2.color}) is ${p2.total_price()}.")
discount_percent = 20
print(f"Total price for {p3.buckets} buckets (color: {p2.color}) is ${p3.discounted_price(discount_percent)} \
with a discount of {discount_percent}%.")
