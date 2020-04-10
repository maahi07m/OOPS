class ComplexNumber:
    # TODO: write your code here
    def __init__(self,real=0, imag=0):
        self.real_part = real
        self.imaginary_part = imag
    def __mul__(self,other):
        real_part = (self.real_part*other.real_part)-(self.imaginary_part*other.imaginary_part)
        imag_part = (self.real_part*other.imaginary_part)+(self.imaginary_part*other.real_part)
        
        return self.__class__(real_part, imag_part)
    
if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number1 = ComplexNumber(*input_args[0])
    complex_number2 = ComplexNumber(*input_args[1])

    complex_numbers_multiplication = complex_number1 * complex_number2

    print(complex_numbers_multiplication.real_part)
    print(complex_numbers_multiplication.imaginary_part)
