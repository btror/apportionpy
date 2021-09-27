import math


class Hamilton:
    def __init__(self, num_seats, populations):
        """
        Initialize variables.

        :param num_seats: The amount of seats to apportion.
        :type num_seats: int

        :param populations: A list of populations corresponding to each state.
        :type populations: [float]
        """

        # The number of seats to apportion.
        self.num_seats = num_seats

        # The number of states to apportion seats to.
        self.num_states = len(populations)

        # The populations for each state respectively.
        self.populations = populations

        # The original divisor.
        self.original_divisor = sum(populations) / num_seats

        # The original state quotas respectively.
        self.original_quotas = []
        for i, population in enumerate(self.populations):
            self.original_quotas.append(population / self.original_divisor)

        # The initial state fair shares respectively.
        self.initial_fair_shares = []
        for i, quota in enumerate(self.original_quotas):
            self.initial_fair_shares.append(math.floor(quota))

    def calculate(self):
        """
        Calculate final fair shares and final quotas.

        :return: A list for the final fair shares and final quotas.
        """

        # Initialize the final quota and original quota list values.
        final_quotas = []

        decimal_list = []

        # Initialize the modified divisor variable.
        # At this point, the modified divisor is the same as the original divisor value.
        modified_divisor = sum(self.populations) / self.num_seats

        # Calculate the original quota values.
        # At this point, the final quotas list is the same as the original quotas list.
        for i, population in enumerate(self.populations):
            final_quotas.append(population / modified_divisor)
            decimal_list.append(math.modf(population / self.original_divisor)[0])

        # Initialize the final fair shares list to list of zeros.
        final_fair_shares = [0] * self.num_states

        # Calculate the original quota values.
        # At this point, the final quotas list is the same as the original quotas list.
        for i, quota in enumerate(self.original_quotas):
            final_fair_shares[i] = math.floor(quota)

        # Initialize a time keeper to break from the loop if apportionment is impossible.
        time_keeper = 0

        # Start the apportionment process.
        while sum(final_fair_shares) != self.num_seats:
            if time_keeper == 5000:
                break
            if sum(final_fair_shares) != self.num_seats:
                highest_decimal = max(decimal_list)
                index = decimal_list.index(highest_decimal)
                final_fair_shares[index] += 1
                decimal_list[index] = 0
            time_keeper += 1

        # If the loop didn't naturally end, return null values.
        if time_keeper == 5000:
            return None, None

        # Return a list for final fair shares and final quotas.
        else:
            return final_fair_shares, final_quotas, modified_divisor
