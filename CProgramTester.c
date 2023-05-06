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