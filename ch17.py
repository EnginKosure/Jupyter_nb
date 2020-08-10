class BasicPlan:
    can_stream = True
    can_download = True
    num_of_devices = 1
    has_SD = True
    has_HD = False
    has_UHD = False
    price = '$8.99'


class StandardPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '$12.99'


class PremiumPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '$15.99'


print(BasicPlan.has_SD)  # ➞ True

print(PremiumPlan.has_SD)  # ➞ True

print(BasicPlan.has_UHD)  # ➞ False

print(BasicPlan.price)  # ➞ "$8.99"

print(PremiumPlan.num_of_devices)  # ➞ 4
