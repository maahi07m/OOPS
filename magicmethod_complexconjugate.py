class ComplexNumber:
    # TODO: write your code here
    def __init__(self, real=0, imag=0):
        self.real_part = real
        self.imaginary_part = imag
    
    def conjugate(self):
        return ComplexNumber(self.real_part, -self.imaginary_part)
        
    

if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number = ComplexNumber(*input_args)
    complex_number_conjugate = complex_number.conjugate()

    print(complex_number_conjugate.real_part)
    print(complex_number_conjugate.imaginary_part)
