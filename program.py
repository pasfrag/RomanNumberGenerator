def break_number(number: int):
    return [number // 1000, number // 100 % 10, number // 10 % 100 % 10, number % 10]


def get_latin(number_list):
    thousands = {0: "", 1: "M", 2: "MM", 3: "MMM"}
    hundreds = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
    dozens = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
    units = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
    return thousands[number_list[0]] + hundreds[number_list[1]] + dozens[number_list[2]] + units[number_list[3]]


def main():
    input_value = input("Give as a number or press x to exit: ")
    while True:
        if input_value.lower() == "x":
            break

        try:
            number = int(input_value)
            number_list = break_number(number)
            print("Your latin number is: {}".format(get_latin(number_list)))

        except ValueError:
            print("That's not an integer or an x!")

        input_value = input("Give as another number or press x to exit: ")


if __name__ == '__main__':
    main()
