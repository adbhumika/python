RECORD_FILE = "record.txt"


def show_history():
    try:
        file = open(RECORD_FILE, "r")
    except FileNotFoundError:
        print("No any history.")
        return

    lines = file.readlines()
    if len(lines) == 0:
        print("No any history.")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()


def del_history():
    file = open(RECORD_FILE, "w")
    file.close()
    print("History cleared")


def save_history(equation, result):
    file = open(RECORD_FILE, "a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()


def calculating(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use this format (eg: 8 + 8)")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "**":
        result = num1 ** num2
    elif op == "%":
        result = num1 % num2
    elif op == "/":
        if num2 == 0:
            print("cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    if result.is_integer():
        result = int(result)

    print("Result:", result)
    save_history(user_input, result)


def main():
    print("__CALCULATOR__(excess history, clear or exit?)")
    while True:
        user_input = input("Do any calcultion(*,+,_,/) or command(history, clear or exit): ").strip()
        if user_input.lower() == "exit":
            print("Goodybye")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            del_history()
        else:
            calculating(user_input)


main()
