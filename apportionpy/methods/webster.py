import math


class Webster:
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
            self.initial_fair_shares.append(round(quota))

    def calculate(self):
        """
        Calculate final fair shares, final quotas, and the modified divisor.

        :return: A list for the final fair shares, final quotas, and a value for the modified divisor.
        """

        # Initialize the final quota and original quota list values.
        final_quotas = []

        # Initialize the modified divisor variable.
        # At this point, the modified divisor is the same as the original divisor value.
        modified_divisor = sum(self.populations) / self.num_seats

        # Calculate the original quota values.
        # At this point, the final quotas list is the same as the original quotas list.
        for i, population in enumerate(self.populations):
            final_quotas.append(population / modified_divisor)

        # Initialize the final fair shares list to list of zeros.
        final_fair_shares = [0] * self.num_states

        # Initialize an estimator to use in changing the quotas if they need to be reapportioned.
        estimator = sum(self.populations) / self.num_seats

        # Initialize a time keeper to break from the loop if apportionment is impossible.
        time_keeper = 0

        # Start the apportionment process.
        while sum(final_fair_shares) != self.num_seats:
            if time_keeper == 5000:
                break
            for i, quota in enumerate(self.original_quotas):
                final_fair_shares[i] = round(final_quotas[i])

            # Recalculate the divisor if the seats are not fully apportioned.
            if sum(final_fair_shares) != self.num_seats:

                # Increase the modified divisor if it is too little.
                if sum(final_fair_shares) > self.num_seats:
                    modified_divisor += estimator

                # Decrease the modified divisor if it is too high
                else:
                    modified_divisor -= estimator

                # Decrease the estimator so the next loop will not result in the previous modified divisor
                estimator = estimator / 2

                # The modified divisor cannot ever be 0 (prevents divide by 0 error)
                if modified_divisor == 0:
                    modified_divisor = 1

                # Recalculate the quotas with the updated modified divisor.
                for i, population in enumerate(self.populations):
                    final_quotas[i] = population / modified_divisor

                # Reapportion the seats to states given a set of new quotas.
                for i, quota in enumerate(self.original_quotas):
                    final_fair_shares[i] = round(final_quotas[i])
            time_keeper += 1

        # If the loop didn't naturally end, return null values.
        if time_keeper == 5000:
            return None, None, None

        # Return a list for final fair shares, final quotas and a value for the modified divisor.
        else:
            return final_fair_shares, final_quotas, modified_divisor
