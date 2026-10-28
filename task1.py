from dataclasses import dataclass, field

# class Cart:
#     # items = []
 
#     def __init__(self, user_id, coupons=None):
#         self.user_id = user_id
#         self.coupons = coupons or []
#         self.items = []

#     def add(self, sku, qty=1):
#         self.items.append((sku, qty))
 
#     def apply_coupon(self, code):
#         self.coupons.append(code)

@dataclass
class Cart:
    user_id: int
    coupons: list = field(default_factory=list)
    items: list = field(default_factory=list)

    def add(self, sku, qty=1):
        self.items.append((sku, qty))

    def apply_coupon(self, code):
        self.coupons.append(code)

# javoblar => bug 1. Cart classda items attributi static yani class attribute bo'lib qolgan. Shu sababli barcha objectlarning itemslari bitta bo'lib qolgan.
# agar shuni items __init__ ichida self.items qilib yozsak, to'g'ri ishlashni boshlaydi
# bug2. yangi object create qilinyaotgan couponsga qiymat bermasak u ham default sifatida barcha objectlarda bir xil bo'lib qoladi. unda allaqachon qiymat berilsa 
# self.couponsga yozilyatgandi lekin defaul value logikani buzayotgandi. shuni None qabul qiladigan qilib, agar None bo'lsa, 
# empty qilib qo'ysak to'g'ri ishlayd

# 1.3 => ValueError bo'ladi. ValueError: mutable default <class 'list'> for field coupons is not allowed: use default_factory
# o'rniga field(default_factory=list) ishlataamiz

# 1.4 chunki assign (=) belgisi class ga emas har doim objectga tasir qiladi