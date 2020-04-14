import math
class Fraction:
    def __init__(self, num, den):
        self._numerator = num
        self._denominator = den
        if self._denominator < 0:
            self._numerator = -1*(self._numerator)
            self._denominator = -1*(self._denominator)
        self.simplifi()
    
    def simplifi(self):
        gcd_nums = math.gcd(self.numerator,self.denominator)
        self._numerator //= gcd_nums
        self._denominator //= gcd_nums
        
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    def __sub__(self,other):
        result_numerator = (self.numerator*other.numerator)
        result_denominator = (self.denominator*other.denominator)
        print(self,end=' * ')
        print(other,end=' = ')
        result = Fraction(result_numerator,result_denominator)
        print(result)
        return result
    
    def __repr__(self):
        return repr(self.numerator)+'/'+repr(self.denominator)


if __name__ == "__main__":
    import json

    input_args = list(json.loads(input()))

    fraction_one = Fraction(*input_args[0])
    fraction_two = Fraction(*input_args[1])

    result_fraction = fraction_one - fraction_two

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
