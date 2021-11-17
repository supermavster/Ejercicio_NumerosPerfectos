class PerfectNumber:
    
    def get_number(self):
        # Get Number
        number = input("Check if is perfect number:")
        # Convert to int
        return int(number)
    
    def prime_number(self, number):
        list = []
        for i in range(1, number):
            if number % i == 0:
                list.append(i)
        # Return list
        return list
    
    def is_perfect(self, number):
        # Check if is perfect number
        if sum(self.prime_number(number)) == number:
            return True
        else:
            return False
    
    def run(self, number):
        # Validate number
        if number <= 1:
            print("The number must be greater than 1")
            return
        # Get list divisors
        list_numbers = self.prime_number(number)
        # Sum the list
        total = sum(list_numbers)
        # Check if is perfect number (is_perfect)
        check = total == number
        # Print the result
        if check:
            total_text = ' + '.join(str(i) for i in list_numbers)
            print("{} = {} ".format(total_text, total))
            # Check if is perfect number
            print("{} is {}a perfect number".format(number, "not " if not check else ""))

        
# Init program
if __name__ == "__main__":
    perfect_number = PerfectNumber()
    # Manual
    # n = perfect_number.get_number()
    # perfect_number.run(n)

    # Automatic
    # Perfect numbers: 6, 28, 496 y 8128.
    for n in range(0,9999):
        perfect_number.run(n)
