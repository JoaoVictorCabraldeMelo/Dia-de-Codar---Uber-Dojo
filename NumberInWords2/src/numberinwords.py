class Converter:
    def run(self, number):

        return "forty two dollars"

    def unidade(self, number):
        number = number % 10
        dictionary = {1: "one",
                      2: "two",
                      3: "three",
                      4: "four",
                      5: "five",
                      6: "six",
                      7: "seven",
                      8: "eight",
                      9: "nine",
                      0: "zero"
                      }

        number = dictionary[number]

        return f"{number} dollars"

      def dezena(self, number):
        number = number % 100
        number = number % 10
