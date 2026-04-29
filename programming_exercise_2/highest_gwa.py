def get_highest_gwa():
    source_file = open("students.txt", "r")

    highest_student_name = ""
    highest_gwa_value = 999

    for line_content in source_file:
        cleaned_line = line_content.strip()
        student_data = cleaned_line.split(",")

        student_name = student_data[0]
        gwa_value = float(student_data[1])

        if gwa_value < highest_gwa_value:
            highest_gwa_value = gwa_value
            highest_student_name = student_name

    source_file.close()

    print(highest_student_name + " has the highest GWA of " + str(highest_gwa_value))


get_highest_gwa()