import time
from colorama import Fore


# ------------------------------------------------------------------------------------------
# Creating class for calculating fibonacci sequence
class FibonacciIterator:
    def __init__(self, n: int) -> None:
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.count > self.n:
            raise StopIteration

        if self.count == 0:
            self.count += 1
            return self.a

        elif self.count == 1:
            self.count += 1
            return self.b

        else:
            next_fib = self.a + self.b
            self.a, self.b = self.b, next_fib
            self.count += 1
            return next_fib


# -------------------------------------------------------------------------------------------------
class Display:
    @classmethod
    def menu(cls):
        """ Display menu """
        print(Fore.LIGHTWHITE_EX +
              "\nWhat would you like to do?"
              "\n1 => Get information about fibonacci"
              "\n2 => Display fibonacci numbers \n0 => Exit" + Fore.RESET)
        return input(Fore.LIGHTYELLOW_EX + "....." + Fore.RESET)

    @classmethod
    def display_fibonacci(cls) -> None:

        number: int = int(input(Fore.LIGHTWHITE_EX + "Enter a number: " + Fore.RESET))
        fibonacci_iter: FibonacciIterator = FibonacciIterator(number)
        count: int = 0
        for fib_num in fibonacci_iter:
            last_number: int = fib_num
            count += 1
            if count > number:
                print(Fore.LIGHTGREEN_EX + "Fibonacci number is " + str(last_number)
                      + Fore.RESET)
        choice = input(Fore.LIGHTMAGENTA_EX + "For see all fibonacci sequence press => "
                                              "1\nFor exit => 0\n ... " + Fore.RESET)
        if choice == "1":
            fibonacci_iter: FibonacciIterator = FibonacciIterator(number)
            for fib_num in fibonacci_iter:
                print(Fore.LIGHTCYAN_EX + str(fib_num), end=', ' + Fore.RESET)
        elif choice == "0":
            return
        else:
            print("Invalid input")


    @classmethod
    def run(cls):

        while True:
            choice: str = Display.menu()
            if choice == "1":
                Display.info_fibonacci()
            elif choice == "2":
                Display.display_fibonacci()
            elif choice == "0":
                print(Fore.LIGHTGREEN_EX + "Thank you " + Fore.RESET)
                break
            else:
                print(Fore.LIGHTRED_EX + "Invalid input" + Fore.RESET)


if __name__ == "__main__":
    Display.run()