/*
    Program that computes the approximate grade
    level needed to comprehend some text
    in accordance with the Coleman-Liau Index
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

//Function prototypes

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
float coleman_liau_index(float letters, float words, float sentences);

int main(void)
{
    // Prompting user for a text input

    string text = get_string("Text: ");

    // Return values as variables passed to the Coleman-Liau formula

    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentences(text);

    // Passing values to Coleman-Liau formula
    coleman_liau_index(letters, words, sentences);
}

// Counting the number of letters

int count_letters(string text)
{
    int letter = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letter++;
        }
    }

    return letter;
}

// Counting the number of words

int count_words(string text)
{
    int words = 0;
    for (int i = 0; i < strlen(text); i++)
        if (text[i] == ' ')
        {
            words++;
        }

    return words + 1;
}

// Counting the number of sentences

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '?' || text[i] == '!' || text[i] == '.')
        {
            sentences++;
        }

    }
    return sentences;
}

// Coleman - Liau Index formula

float coleman_liau_index(float letters, float words, float sentences)

{
    float L = (letters / words) * 100;
    float S = (sentences / words) * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;

    int grade = round(index);

    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
    return 0;
}