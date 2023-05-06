import string


def generate_sum_of_digits_code():
    c_code = '''#include <stdio.h>

int main() {
    int num, sum = 0, remainder;
    printf("Enter a positive integer: ");
    scanf("%d", &num);
    while (num != 0) {
        remainder = num % 10;
        sum += remainder;
        num /= 10;
    }
    printf("The sum of the digits is %d\\n", sum);
    return 0;
}
'''
    return c_code


def generate_decimal_to_binary_code():
    c_code = '''#include <stdio.h>

void decimalToBinary(int num) {
    int binary[32], i = 0;
    while (num > 0) {
        binary[i] = num % 2;
        num /= 2;
        i++;
    }
    printf("Binary number: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binary[j]);
    }
    printf("\\n");
}

int main() {
    int num;
    printf("Enter a positive integer: ");
    scanf("%d", &num);
    decimalToBinary(num);
    return 0;
}
'''
    return c_code


def generate_operation_code(operation):
    operations = {
        '+': {'symbol': '+', 'name': 'addition', 'expression': 'num1 + num2'},
        '-': {'symbol': '-', 'name': 'subtraction', 'expression': 'num1 - num2'},
        '*': {'symbol': '*', 'name': 'multiplication', 'expression': 'num1 * num2'},
        '/': {'symbol': '/', 'name': 'division', 'expression': 'num1 / num2'}
    }

    if operation not in operations:
        raise ValueError("Invalid operation")

    op = operations[operation]

    c_code = string.Template('''
    #include <stdio.h>

    int main() {
        float num1, num2, result;
        printf("Enter two integers: ");
        scanf("%f%f", &num1, &num2);
        result = num1 $op_symbol num2;
        printf("The result of $op_name is: %f\\n", result);
        return 0;
    }
    ''').substitute(op_symbol=op["symbol"], op_name=op["name"])

    return c_code

def generate_palindrome():
    c_code = '''
#include <stdio.h>
#include <string.h>

int main() {
    char str[100], rev_str[100];
    int i, j, len;

    printf("Enter a string: ");
    scanf("%s", str);

    len = strlen(str);
    j = len - 1;

    // Reverse the original string
    for(i = 0; i < len; i++) {
        rev_str[i] = str[j];
        j--;
    }
    rev_str[len] = NULL;

    // Remove the first letter of the reversed string
    for(i = 0; i < len - 1; i++) {
        rev_str[i] = rev_str[i + 1];
    }
    rev_str[len - 1] = NULL;

    // Append the reversed string to the original string
    strcat(str, rev_str);

    printf("The palindrome of %s is: %s", str, str);
    
    return 0;
}

'''

    return c_code




