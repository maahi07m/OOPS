class ComplexNumber:
    # TODO: write your code here
    def __init__(self, real=0, imag=0):
        self.real_part = real
        self.imaginary_part = imag
    def __add__(self, other):
        #print(help(ComplexNumber))
        return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
    
if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number1 = ComplexNumber(*input_args[0])
    complex_number2 = ComplexNumber(*input_args[1])

    complex_numbers_addition = complex_number1 + complex_number2

    print(complex_numbers_addition.real_part)
    print(complex_numbers_addition.imaginary_part)
