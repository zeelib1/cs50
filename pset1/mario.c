#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Prompt the user for height

    int height;
    do
    {
        height = get_int("Enter a number between 1 and 8: ");
    }
    while (height < 1 || height > 8);

    // Iterate from 1 to 8

    for (int i = 0; i < height; i++)
    {
        // On iteration j align the pyramid to the right
        for (int j = 0; j < height - i - 1; j++)
        {
            printf(" ");
        }
        // On iteration k print the hash
        for (int k = 0; k <= i ; k++)
        {
            printf("#");

        }
        printf("  ");

        for (int z = 0; z <= i; z++)
        {
            printf("#");
        }

        printf("\n");
    }


}

