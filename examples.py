import apportionpy.apportionment as ap

seats = 10
populations = [100, 120, 113, 199, 144]

# Adam's method of apportionment.
method_adam = ap.Apportion(seats=seats, populations=populations, method="adam")
print("\n->", method_adam.method,
      "\ninitial fair shares", method_adam.initial_fair_shares,
      "\nfinal fair shares", method_adam.final_fair_shares,
      "\ninitial quotas", method_adam.initial_quotas,
      "\nfinal quotas", method_adam.final_quotas,
      "\ninitial divisor", method_adam.initial_divisor,
      "\nmodified divisor", method_adam.modified_divisor)


# Hamilton's method of apportionment.
method_hamilton = ap.Apportion(seats=seats, populations=populations, method="hamilton")
print("\n->", method_hamilton.method,
      "\ninitial fair shares", method_hamilton.initial_fair_shares,
      "\nfinal fair shares", method_hamilton.final_fair_shares,
      "\ninitial quotas", method_hamilton.initial_quotas,
      "\nfinal quotas", method_hamilton.final_quotas,
      "\ninitial divisor", method_hamilton.initial_divisor,
      "\nmodified divisor", method_hamilton.modified_divisor)


# Jefferson's method of apportionment.
method_jefferson = ap.Apportion(seats=seats, populations=populations, method="jefferson")
print("\n->", method_jefferson.method,
      "\ninitial fair shares", method_jefferson.initial_fair_shares,
      "\nfinal fair shares", method_jefferson.final_fair_shares,
      "\ninitial quotas", method_jefferson.initial_quotas,
      "\nfinal quotas", method_jefferson.final_quotas,
      "\ninitial divisor", method_jefferson.initial_divisor,
      "\nmodified divisor", method_jefferson.modified_divisor)


# Webster's method of apportionment.
method_webster = ap.Apportion(seats=seats, populations=populations, method="webster")
print("\n->", method_webster.method,
      "\ninitial fair shares", method_webster.initial_fair_shares,
      "\nfinal fair shares", method_webster.final_fair_shares,
      "\ninitial quotas", method_webster.initial_quotas,
      "\nfinal quotas", method_webster.final_quotas,
      "\ninitial divisor", method_webster.initial_divisor,
      "\nmodified divisor", method_webster.modified_divisor)
