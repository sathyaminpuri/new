#include <stdio.h>

int main() {
    char name[100];  // Assuming the name will not exceed 100 characters

    // Prompt the user to enter their name
    printf("Enter your name: ");
    scanf("%s", name);  // Read the input as a string

    // Greet the user
    printf("Hello, %s! Welcome to C programming.\n", name);

    return 0;
}
