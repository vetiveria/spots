import decimal


class Geodetic:

    def __init__(self):
        self.precision = '1.000'
        self.rounding = decimal.ROUND_UP

        self.decimal = decimal
        self.decimal.getcontext().prec = 6

    def proximate(self, degrees: int, minutes: int, seconds: int):
        dec = self.decimal.Decimal(degrees + (minutes * 60 + seconds) / 3600)
        dec = dec.quantize(self.decimal.Decimal(self.precision), rounding=self.rounding)

        return float(dec)

    def geodetic(self, measure: float):
        arc = str(int(measure)).zfill(6)

        degrees = int(arc[:2])
        minutes = int(arc[2:4])
        seconds = int(arc[4:])

        return self.proximate(degrees=degrees, minutes=minutes, seconds=seconds)
