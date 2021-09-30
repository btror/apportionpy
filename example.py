import apportionpy.apportionment as ap
from apportionpy.experimental.boundary import estimate_lowest_divisor, estimate_highest_divisor

seats = 70
populations = [300500, 200000, 50000, 38000, 21500]

# Adam's method of apportionment.
method_adam = ap.Apportion(seats=seats, populations=populations, method="adam")
print("\n->", method_adam.method,
      "\ninitial fair shares", method_adam.initial_fair_shares,
      "\nfinal fair shares", method_adam.fair_shares,
      "\ninitial quotas", method_adam.initial_quotas,
      "\nfinal quotas", method_adam.final_quotas,
      "\ninitial geometric means", method_adam.initial_geometric_means,
      "\nfinal geometric means", method_adam.final_geometric_means,
      "\ninitial divisor", method_adam.initial_divisor,
      "\nmodified divisor", method_adam.modified_divisor)

# Hamilton's method of apportionment.
method_hamilton = ap.Apportion(seats=seats, populations=populations, method="hamilton")
print("\n->", method_hamilton.method,
      "\ninitial fair shares", method_hamilton.initial_fair_shares,
      "\nfinal fair shares", method_hamilton.fair_shares,
      "\ninitial quotas", method_hamilton.initial_quotas,
      "\nfinal quotas", method_hamilton.final_quotas,
      "\ninitial geometric means", method_hamilton.initial_geometric_means,
      "\nfinal geometric means", method_hamilton.final_geometric_means,
      "\ninitial divisor", method_hamilton.initial_divisor,
      "\nmodified divisor", method_hamilton.modified_divisor)

# Jefferson's method of apportionment.
method_jefferson = ap.Apportion(seats=seats, populations=populations, method="jefferson")
print("\n->", method_jefferson.method,
      "\ninitial fair shares", method_jefferson.initial_fair_shares,
      "\nfinal fair shares", method_jefferson.fair_shares,
      "\ninitial quotas", method_jefferson.initial_quotas,
      "\nfinal quotas", method_jefferson.final_quotas,
      "\ninitial geometric means", method_jefferson.initial_geometric_means,
      "\nfinal geometric means", method_jefferson.final_geometric_means,
      "\ninitial divisor", method_jefferson.initial_divisor,
      "\nmodified divisor", method_jefferson.modified_divisor)

t1 = estimate_lowest_divisor("jefferson", method_jefferson.modified_divisor, populations, seats)
print("boundary test: ", t1)

t2 = estimate_highest_divisor("jefferson", method_jefferson.modified_divisor, populations, seats)
print("boundary test: ", t2)

# Webster's method of apportionment.
method_webster = ap.Apportion(seats=seats, populations=populations, method="webster")
print("\n->", method_webster.method,
      "\ninitial fair shares", method_webster.initial_fair_shares,
      "\nfinal fair shares", method_webster.fair_shares,
      "\ninitial quotas", method_webster.initial_quotas,
      "\nfinal quotas", method_webster.final_quotas,
      "\ninitial geometric means", method_webster.initial_geometric_means,
      "\nfinal geometric means", method_webster.final_geometric_means,
      "\ninitial divisor", method_webster.initial_divisor,
      "\nmodified divisor", method_webster.modified_divisor)

# Huntington Hill method of apportionment.
method_huntington_hill = ap.Apportion(seats=seats, populations=populations, method="huntington hill")
print("\n->", method_huntington_hill.method,
      "\ninitial fair shares", method_huntington_hill.initial_fair_shares,
      "\nfinal fair shares", method_huntington_hill.fair_shares,
      "\ninitial quotas", method_huntington_hill.initial_quotas,
      "\nfinal quotas", method_huntington_hill.final_quotas,
      "\ninitial geometric means", method_huntington_hill.initial_geometric_means,
      "\nfinal geometric means", method_huntington_hill.final_geometric_means,
      "\ninitial divisor", method_huntington_hill.initial_divisor,
      "\nmodified divisor", method_huntington_hill.modified_divisor)

# Method of equal proportions.
method_equal_proportions = ap.Apportion(seats=seats, populations=populations, method="equal proportions")
print("\n->", method_equal_proportions.method,
      "\ninitial fair shares", method_equal_proportions.initial_fair_shares,
      "\nfinal fair shares", method_equal_proportions.fair_shares,
      "\ninitial quotas", method_equal_proportions.initial_quotas,
      "\nfinal quotas", method_equal_proportions.final_quotas,
      "\ninitial geometric means", method_equal_proportions.initial_geometric_means,
      "\nfinal geometric means", method_equal_proportions.final_geometric_means,
      "\ninitial divisor", method_equal_proportions.initial_divisor,
      "\nmodified divisor", method_equal_proportions.modified_divisor)
