from CPrograms import generate_sum_of_digits_code, generate_decimal_to_binary_code, generate_operation_code, generate_palindrome

# input_sentence = input("Enter a sentence: ")
# input_sentence = "Write a program that reads in any positive integer and display the sum of its digits"
# input_sentence = "Write a program that converts positive integer to a binary"
# input_sentence = "Write a program that adds two digits"
# input_sentence = "Write a program that subtracts two digits"
# input_sentence = "Write a program that multiplies two digits"
# input_sentence = "Write a program that divides two digits"
input_sentence = "Write a program that converts a word into a palindrome"


if "positive integer" in input_sentence and "sum of its digits" in input_sentence:
    c_code = generate_sum_of_digits_code()
    print(c_code)
elif "converts" in input_sentence and "positive integer" in input_sentence and "binary" in input_sentence:
    c_code = generate_decimal_to_binary_code()
    print(c_code)
elif "two digits" in input_sentence:
    if "adds" in input_sentence:
        c_code = generate_operation_code("+")
        print(c_code)
    elif "subtracts" in input_sentence:
        c_code = generate_operation_code("-")
        print(c_code)
    elif "multiplies" in input_sentence:
        c_code = generate_operation_code("*")
        print(c_code)
    elif "divides" in input_sentence:
        c_code = generate_operation_code("/")
        print(c_code)
elif "word" in input_sentence and "palindrome" in input_sentence:
        c_code = generate_palindrome()
        print(c_code)
else:
    print("The system did not detect the instruction")