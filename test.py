import apportionpy.apportionment as ap

x = ap.Apportion(seats=10, populations=[23, 35, 10, 32, 19], method="jefferson")

print("method\n", x.method)
print("\npopulations\n", x.populations)
print("\ninitial quotas\n", x.initial_quotas)
print("\nfinal quotas\n", x.final_quotas)
print("\ninitial fair shares\n", x.initial_fair_shares)
print("\nfinal fair shares\n", x.final_fair_shares)
print("\ninitial divisor\n", x.initial_divisor)
print("\nmodified divisor\n", x.modified_divisor)