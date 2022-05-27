while True:
    exponent = int(input("Enter the exponent"))
    after_decimal = int(input("Enter how many numbers after decimal point"))
    all_output_list = []
    while True:
        input_number = input("Copy-paste the number (nothing/enter = exit)")
        if input_number == "":
            break
        output_number_list = [char for char in input_number if char.isnumeric()]
        # print(output_number_list)
        output_number_str = "".join(output_number_list)
        # print(output_number_str)
        output_number_int = int(output_number_str)*(10**(exponent-after_decimal))
        # print(output_number_int)
        all_output_list.append(output_number_int)
        print(f"{output_number_int} entered.")

    print("-" * 50)
    print("Copy-paste this result: ")
    for x in all_output_list:
        print(x)
    print("-" * 50)
    input("Press enter to restart, or close the program to end.")

