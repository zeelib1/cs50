// Program for decypering an input text

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Prompt user for command line arguments
int main(int argc, string argv[])
{
    // Arguments need to be equal to 1; needs to be decimal integer
    if (argc == 2)
    {
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }

        }
        // Converts string into an integer

        int k = atoi(argv[1]);

        // Prompt user for a text input:

        string p = get_string("plaintext: ");

        int n = strlen(p);
        printf("ciphertext:");

        for (int i = 0; i < n; i++)
        {
            // Input requirements: alphabetic, lower or uppercase
            if (isalpha(p[i]))
            {
                if (isupper(p[i]))
                {

                    int alpha_index = p[i] - 65;
                    int c = (alpha_index + k) % 26;
                    c += 65;
                    printf("%c", c);
                }
                else if (islower(p[i]))
                {
                    int alpha_index = p[i] - 97;
                    int c = (alpha_index + k) % 26;
                    c += 97;
                    printf("%c", c);
                }

            }
            else
            {
                printf("%c", p[i]);
            }

        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    return 0;
}