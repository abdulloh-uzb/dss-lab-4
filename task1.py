class Cart:
    items = []
 
    def __init__(self, user_id, coupons=[]):
        self.user_id = user_id
        self.coupons = coupons
 
    def add(self, sku, qty=1):
        self.items.append((sku, qty))
 
    def apply_coupon(self, code):
        self.coupons.append(code)