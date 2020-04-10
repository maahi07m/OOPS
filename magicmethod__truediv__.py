class ComplexNumber:
    # TODO: write your code here
    def __init__(self,real=0, imag=0):
        self.real_part = real
        self.imaginary_part = imag
    def __str__(self):
        return f"{self.real_part}{self.imaginary_part:+}i"

if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number = ComplexNumber(*input_args)
    complex_number_str_value = str(complex_number)

    print(complex_number_str_value)
'''
Input:
[[1,2],[3,4]]

Output:
0.44
0.08
'''

