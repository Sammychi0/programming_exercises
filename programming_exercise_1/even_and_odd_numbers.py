def separate_even_and_odd_numbers():
    with open("numbers.txt", "r") as source_file:
        file_contents = source_file.read().split()

    even_number_list = []
    odd_number_list = []

    for number_string in file_contents:
        converted_number = int(number_string)

        if converted_number % 2 == 0:
            even_number_list.append(str(converted_number))
        else:
            odd_number_list.append(str(converted_number))

    with open("even.txt", "w") as even_file:
        even_file.write("\n".join(even_number_list))

    with open("odd.txt", "w") as odd_file:
        odd_file.write("\n".join(odd_number_list))


separate_even_and_odd_numbers()