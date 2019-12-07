import Constants


class Converter:
    def run(self, number):
        unit_digit = str(number)[-1]
        unit_text = self.get_unit_text(unit_digit)
        return f"forty{unit_text} dollars"

    def get_unit_text(self, value):

        return UNITY_NUMBER_CONVERTER[value]
        # number_text = str(number)
        # pos = number_text[len(number_text)-1]
        # replacement = " " + dic[pos]
