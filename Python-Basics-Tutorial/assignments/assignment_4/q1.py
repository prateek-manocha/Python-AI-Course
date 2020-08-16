class SpecialString:
    def __init__(self, special_string):
        self.spec_str = special_string

    def print_string(self):
        print('***************************')
        print('*  '+self.spec_str+'  *')
        print('***************************')

if __name__ == '__main__':
    x = input('Enter the string: ')
    obj1 = SpecialString(x)
    obj1.print_string()
