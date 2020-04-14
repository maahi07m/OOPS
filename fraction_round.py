Input:
[23, 43]

Output:
23/43 = 0.535
True
0.535


---------------------------------------------------
import fractions
class Fraction(object):
    # TODO: write your code here
    def __init__(self, num, den):
        self._numerator = num
        self._denominator = den
        if num > 0  and den < 0:
            self._numerator = -(self._numerator)
            self._denominator = abs(self._denominator)
        elif num<0 and den<0:
            self._numerator = abs(self._numerator)
            self._denominator = abs(self._denominator)
         
    
    @property 
    def numerator(self):
        self._numerator = fractions.Fraction(self._numerator,self._denominator).numerator
        return self._numerator
    
    @property
    def denominator(self):
        self._denominator = fractions.Fraction(self._numerator,self._denominator).denominator
        return self._denominator
    
        
    
    def to_value(self):
        # TODO: write your code here
        result = round(self._numerator/self._denominator,3)
        print('{}/{} = {}'.format(self._numerator,self._denominator,result))
        return result
        

if __name__ == "__main__":
    import json

    input_args = list(json.loads(input()))

    fraction_one = Fraction(*input_args)

    result_decimal_value = fraction_one.to_value()

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
    print(result_decimal_value)
