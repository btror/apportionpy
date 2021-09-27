from apportionpy.methods.adam import Adam
from apportionpy.methods.jefferson import Jefferson
from apportionpy.methods.webster import Webster
from apportionpy.methods.hamilton import Hamilton


class Apportion:
    def __init__(self, seats, populations, method):
        self.seats = seats
        self.populations = populations
        self.method = method.lower()

        ap = None
        if method.upper() == "ADAM":
            ap = Adam(self.seats, self.populations)
        elif method.upper() == "HAMILTON":
            ap = Hamilton(self.seats, self.populations)
        elif method.upper() == "JEFFERSON":
            ap = Jefferson(self.seats, self.populations)
        elif method.upper() == "WEBSTER":
            ap = Webster(self.seats, self.populations)

        self.final_fair_shares, self.final_quotas, self.modified_divisor = ap.calculate()

        self.initial_fair_shares = ap.initial_fair_shares
        self.initial_quotas = ap.original_quotas
        self.initial_divisor = ap.original_divisor
