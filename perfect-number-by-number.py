import math

class PerfectNumberByNumber:
    
    def get_number(self):
        # Get Number
        number = input("Get perfect number by number:")
        # Convert to int
        return int(number)
  
    def is_prime(self, number):
        # Check if is prime number
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        for i in range(5, int(number**0.5) + 1, 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False
        return True
  
    def calculate_perfect(self,number):
        if self.is_prime(number):
            complement = (math.pow(2, number) - 1)
            print("{} is a perfect number".format(complement))
            if self.is_prime(complement):
                calc = math.pow(2, (number - 1))
                result = calc * complement
                print("{} is {}".format(number, result))
    
# Init program
if __name__ == "__main__":
    perfect_number = PerfectNumberByNumber()
    # Manual
    # n = perfect_number.get_number()
    # try:
    #     perfect_number.calculate_perfect(n)
    # except Exception as e:
    #     print(float('inf'))
    
    # Automatic
    for n in range(0,100):
        try:
            perfect_number.calculate_perfect(n)
        except Exception as e:
            print(float('inf'))

