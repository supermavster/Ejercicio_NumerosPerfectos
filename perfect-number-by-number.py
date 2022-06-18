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
            if self.is_prime(complement):
                calc = math.pow(2, (number - 1))
                result = calc * complement
                print("{} is {}".format(number, result))
    
    def main_method(self):
        # Manual
        # n = self.get_number()
        # try:
        #     self.calculate_perfect(n)
        # except Exception as e:
        #     print(float('inf'))

        # Automatic
        for n in range(0,100):
            try:
                self.calculate_perfect(n)
            except Exception as e:
                print(float('inf'))

    
# Init program
if __name__ == "__main__":
    perfect_number = PerfectNumberByNumber()
    perfect_number.main_method()
