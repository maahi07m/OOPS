import fractions
class Fraction(object):
    # TODO: write your code here
    def __init__(self,num, den):
        self._numerator = num
        self._denominator = den
        self.f1 = 0
        self.f1 = fractions.Fraction(num,den)
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    def __mul__(self,other):
        f2 = fractions.Fraction(other._numerator,other._denominator)
        simplifi = str((self.f1*f2).numerator)+'/'+str((self.f1*f2).denominator)
        print("{} * {} = {}".format(self.f1,f2,simplifi))
        return self.f1*f2
    


if __name__ == "__main__":
    import json

    input_args = list(json.loads(input()))

    fraction_one = Fraction(*input_args[0])
    fraction_two = Fraction(*input_args[1])

    result_fraction = fraction_one * fraction_two

    try:
        fraction_one._numerator
    except AttributeError:
        print("Missed protecting numerator")

    try:
        fraction_one._denominator
    except AttributeError:
        print("Missed protecting denominator")

    try:
        fraction_one.numerator = 1
        print("Missed setting safe access to numerator")
    except AttributeError:
        pass

    try:
        fraction_one.denominator = 1
        print("Missed setting safe access to numerator")
    except AttributeError:
        pass

    print(isinstance(fraction_one, Fraction))
    print(isinstance(fraction_two, Fraction))
    print(result_fraction.numerator)
    print(result_fraction.denominator)
