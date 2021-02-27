
//Program that spell-checks a file using a hash table

// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <ctype.h>
#include "dictionary.h"
#include <string.h>



// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 100;

// Hash table
node *table[N];
// Word counter
int word_count = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = hash(word);

    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;

    }
    return false;
}

// Hash function - hashes word to a number

// https://research.cs.vt.edu/AVresearch/hashing/strings.php
//  sum of character values translated to C

unsigned int hash(const char *word)
{

    int sum  = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return (sum % N);
}


// Loads dictionary into memory, returning true if successful

bool load(const char *dictionary)
{
// Open the file with appropriate conditions

    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        printf("File does not exist.");
        return 1;
    }
    char specific_word[LENGTH + 1];

    while (fscanf(dict, "%s", specific_word) != EOF)
    {

        node *n = malloc(sizeof(node));


        if (n == NULL)
        {

            return false;
        }
        // set values for these pointers

        strcpy(n->word, specific_word);

        int index = hash(n->word);

        n->next = table[index];
        table[index] = n;
        // Counting the size of the words
        word_count += 1;
    }

    fclose(dict);
    return true;
}


// Returns number of words in dictionary

unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory

bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }

    }
    return true;
}
