def process_numbers():
    source_file = open("numbers.txt", "r")
    content = source_file.read()
    source_file.close()

    number_list = content.split()

    even_result = []
    odd_result = []

    for number_value in number_list:
        integer_value = int(number_value)

        if integer_value % 2 == 0:
            squared_value = integer_value * integer_value
            even_result.append(str(squared_value))
        else:
            cubed_value = integer_value * integer_value * integer_value
            odd_result.append(str(cubed_value))

    even_file = open("double.txt", "w")
    for even_value in even_result:
        even_file.write(even_value + "\n")
    even_file.close()

    odd_file = open("triple.txt", "w")
    for odd_value in odd_result:
        odd_file.write(odd_value + "\n")
    odd_file.close()


process_numbers()