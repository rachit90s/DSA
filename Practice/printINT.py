#Complete the function printNumber which takes an integer input from the user and prints it on the screen.


class Solution:
    def printNumber(self):
        a=int(input("Enter the integer: "))
        return a

my_solution = Solution()

returned_number = my_solution.printNumber()
print(returned_number)