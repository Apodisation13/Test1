class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def reset(self):
        self.count = 0
        print(self.count)

    def can_add(self, v):
        if self.count + v <= self.capacity:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.count += v
            print(self.count)
        else:
            print(f"can't add {v}, capacity exceeded, still {self.count}")

    def can_dec(self):
        if self.count == 0:
            return False
        return True

    def dec(self, v):
        if self.can_dec():
            self.count -= v
            if self.count < 0:
                self.count = 0
            print(self.count)
        else:
            print("Sorry, you have 0 coins already, couldn't have less")

    def check(self):
        print(self.count)

    # def any_func(self, reset, add, dec):
    #     print(self.count)


total_capacity = int(input("Введите ёмкость копилки: "))

A = MoneyBox(total_capacity)

print("Instruction: you can input "
      "add int (ex: add 60), "
      "dec int (ex: dec 30), "
      "reset"
      "To quit - input quit")

while True:
    user_input = input().split()
    command = user_input[0]

    if command == 'quit':
        print('Bye!')
        break

    if command == "add":
        A.add(int(user_input[1]))
    elif command == "dec":
        A.dec(int(user_input[1]))
    elif command == "reset":
        A.reset()
    elif command == "check":
        A.check()
    else:
        print("Wrong command, try again")
