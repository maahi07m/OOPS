class ComplexNumber:
    # TODO: write your code here
    def __init__(self,real=0,imag=0):
        self.real_part = real
        self.imaginary_part = imag

if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))
    complex_number = ComplexNumber(*input_args)
    
    print(complex_number.real_part)
    print(complex_number.imaginary_part)
