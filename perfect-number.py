# Get Number
name = input("Check if is perfect number:")
# Keep number and convert to int
real_number = n = int(name)
# Check the divisors
numbers_divisible = [i for i in [1,2,3,5,7] if n%i==0]
# Make a list of divisors
total = []
while n > 1:
    for i in numbers_divisible:
        if n%i == 0:
            n = n/i
            total.append(int(i))
# Sum the list
total_values = sum(total)
# Check if is perfect number
if total_values == real_number:
    total_text = ' + '.join(str(i) for i in total)
    print("{} is a perfect number".format(real_number))
    print("{} = {} ".format(total_text, total_values))
else:
    print("{} is not a perfect number".format(real_number))