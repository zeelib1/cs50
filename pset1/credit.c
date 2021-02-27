// // multiply every second from behind by 2 and make a sum of it
// //add the sum the the sum of the digits that were not multiplied by 2
// //if the total's last digit is 0, the card is valid

// 0. input and conditions applied
// 1. check every second and multiply by two
// 2. sum the digits of those multiples; if you have 10 or higher it is the digits you sum, thus, 12 is 1+2
// 3. take the sum and add it to the sum of digits we did not multiply by two
// 4. check if the last digit of result is 0, thus the card is valid, as the credit card satisfies the checksum


// Given the input check if it satisfies the checksum

// - get the individual digits of the number from a big number
// How do we get the digits of the number?

// 4003600000000014   >> how do we get the last digit of this credit card number - number 4?
// Take any big number and take the remainder, when you divide it by 10, you get the most right digit

// 4003600000000014 % 10 = 4

// Adapt this to get the second to last digit, or third, etc.

// 1.Prompt the user for credit card number
// 2.Calculate the checksum - valid or not based on whether the final result of checksum is or is not 0.
// 3.Check the credit card lenght and starting digits to figure out which brand it matches.
// 4.If it matches checksum, and lenght and digit req print accordingly.(amex, mc, visa, invalid).


#include <stdio.h>
#include <cs50.h>

int main (void)
{
    long number;
    do
    {
        number = get_long("Number: ");
    } while(cardNumber <= 0);

    // 4003600000000014
    // cardNumber % 10 >> the last one > 4


}