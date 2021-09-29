import math


def calculate_equal_proportions(num_seats, populations):
    """
    Calculate the initial fair shares, final fair shares, initial quotas, final quotas, initial divisor, and modified
    divisor using the method of equal proportions.
    """

    # The number of states to apportion seats to.
    num_states = len(populations)

    # fair shares
    fair_shares = []

    # each state gets one seat by default
    for _ in range(num_states):
        fair_shares.append(1)

    # reciprocals of the geometric means
    priority_numbers = []

    # calculate the priority numbers
    for i in range(num_states):
        priority_numbers.append(populations[i] / math.sqrt(fair_shares[i] * (fair_shares[i] + 1)))

    # apportion
    while sum(fair_shares) != num_seats:
        # calculate the priority numbers
        for i in range(num_states):
            priority_numbers[i] = (populations[i] / math.sqrt(fair_shares[i] * (fair_shares[i] + 1)))

        # find the biggest priority number, and give that state another seat
        highest_priority = max(priority_numbers)
        index = priority_numbers.index(highest_priority)

        fair_shares[index] += 1

    print(fair_shares)


seats = 435
pops = [
    4903185,
    731545,
    7278717,
    3017804,
    39512223,
    5758736,
    3565287,
    973764,
    21477737,
    10617423,
    1415872,
    1787065,
    12671821,
    6732219,
    3155070,
    2913314,
    4467673,
    4648794,
    1344212,
    6045680,
    6892503,
    9986857,
    5639632,
    2976149,
    6137428,
    1068778,
    1934408,
    3080156,
    1359711,
    8882190,
    2096829,
    19453561,
    10488084,
    762062,
    11689100,
    3956971,
    4217737,
    12801989,
    1059361,
    5148714,
    884659,
    6829174,
    28995881,
    3205958,
    623989,
    8535519,
    7614893,
    1792147,
    5822434,
    578759,

]
calculate_equal_proportions(seats, pops)
