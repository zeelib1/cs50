#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Prompt user for an input
    string name = get_string("What is your name?\n");

    //Print a message to the user
    printf("Hello, %s!\n", name);
}