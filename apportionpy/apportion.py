from apportionpy.methods.adam import Adam
from apportionpy.methods import hamilton
from apportionpy.methods import jefferson
from apportionpy.methods import webster

method = Adam(10, [10, 23, 40])
print("initial fair shares:",method.initial_fair_shares)
print("original quotas:", method.original_quotas)
print("original divisor:", method.original_divisor)
method.calculate()
print("initial fair shares:",method.initial_fair_shares)
print("original quotas:", method.original_quotas)
print("original divisor:", method.original_divisor)