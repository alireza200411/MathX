class Basic:
    error_code = {

    }

    def __init__(self, number: float):
        self.number = number
        print(type(number)) 
        while type(number) != int and type(number) != float:
            self.number = input('Enter the number to create the object: ')

            try:
                self.number = float(self.number)
                if self.number - int(self.number) == 0:
                    self.number = int(self.number)
            except ValueError:
                print('Please enter a valid number.')
            else:
                print('Error __Invalid input__: You can only enter a number for input.')

    def power(self, num: int):
        while True:
            if self.number == 0 and num < 0:
                command = input(
                    'Error __Division by zero__: The base is zero and the power is negative!!!\nDo you want '
                    'to go out?[y/N] ')
                if command == 'y':
                    return 'Good bye!'
                else:
                    choice = input('')

            return self.number ** num

    def root(self, num: int):
        """ Radical Function:
 This function calculates the radical of a number. The inputs are:
 1. Radicand: The number from which the radical is calculated. This number can be positive, zero, or negative.
 2. Root Index: The degree of the radical (e.g., for square root, the index is 2).

 Important notes:
 - If the root index is even (e.g., 2, 4, 6 ...) and the radicand is negative, the result will be a complex number.
 - If the root index is odd (e.g., 3, 5 ...), even if the radicand is negative, the result will be a real number.
 - If the root index is zero, a division by zero error will occur.
 - If the radicand is zero, the result will always be zero.

 Note: The function should handle invalid inputs (like division by zero or taking the root of a negative number with an even index) appropriately.
    """
        while True:
            if self.number < 0 and num % 2 == 0:
                print('Error __Negative ending__: The object created is negative.')
                self.number = input('Enter a positive number: ')
                try:
                    self.number = float(self.number)
                    if self.number - int(self.number) == 0:
                        self.number = int(self.number)
                except ValueError:
                    print('Please enter a valid number.')
                else:
                    print('Error __Invalid input__: You can only enter a number for input.')
            elif num == 0:
                print('Error __Division by zero__')
                while True:
                    num = input('Enter a non-zero number for the radical term: ')
                    try:
                        num = int(num)
                        break
                    except ValueError:
                        print('Please enter a valid number.')
            else:
                break
        return self.number ** (1 // num)















































