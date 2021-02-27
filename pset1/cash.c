#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float dollars;
    int coins = 0;

    do
    {
        // Prompt user for input
        dollars = get_float("Change owed: ");
    }

    // Input critera; converting dollar value to cents and rounding
    while (dollars <= 0);

    int cents = round(dollars * 100);
    printf("%i\n", cents);



    // Find the least number of coins/ step for change

    while (cents >= 25)
    {
        cents -= 25;
        coins++;
    }
    while (cents >= 10)
    {
        cents -= 10;
        coins++;
    }
    while (cents >= 5)
    {
        cents -= 5;
        coins++;
    }
    while (cents >= 1)
    {
        cents -= 1;
        coins++;
    }

    // Print the least amount of coins needed for providing a change
    printf("%i\n", coins);

}