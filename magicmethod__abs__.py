class ComplexNumber:
    # TODO: write your code here
    def __init__(self,x_comp=0,y_comp=0):
        self.x_comp=x_comp
        self.y_comp=y_comp
    def __abs__(self):
        return round((self.x_comp**2+ self.y_comp**2) ** 0.5,3)


if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number = ComplexNumber(*input_args)
    absolute_value = abs(complex_number)

    print(absolute_value)
    '''
    [1,2]
    2.236
    '''
