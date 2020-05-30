import decimal


class Geodetic:

    def __init__(self):
        self.precision = '1.000'
        self.rounding = decimal.ROUND_UP

        self.decimal = decimal
        self.decimal.getcontext().prec = 6

    def getdecimal(self, degrees: int, minutes: int, seconds: int, direction: int):
        dec = self.decimal.Decimal(degrees + (minutes * 60 + seconds) / 3600)
        dec = dec.quantize(self.decimal.Decimal(self.precision), rounding=self.rounding)

        return direction*float(dec)

    def geodetic(self, measure: float, direction: int = 1):
        """

        :param measure: The geodetic value whose decimal form is being calculated
        :param direction: The longitude sign -> +1 eastward, -1 westward
        :return:
        """
        arc = str(int(measure)).zfill(6)

        degrees = int(arc[:2])
        minutes = int(arc[2:4])
        seconds = int(arc[4:])

        return self.getdecimal(degrees=degrees, minutes=minutes, seconds=seconds, direction=direction)
