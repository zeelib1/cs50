
# Program that computes the approximate grade
# level needed to comprehend some text
# in accordance with the Coleman-Liau Index

# translated from C version

from cs50 import get_string
import string


def main():

    # Prompting user for a text input
    text = input("Text: ")

    # Return values as variables passed the the CL formula

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Passing values to the CL formula
    coleman_liau_index(letters, words, sentences)


def count_letters(text):
    letter = 0
    text.lower()
    for i in text:
        if i.isalpha():
            letter += 1
    return letter

# Counting the number of words


def count_words(text):
    words = 0
    for i in text:
        if i.isspace():
            words += 1
    return words + 1

# Counting the number of sentences


def count_sentences(text):
    sentences = 0
    for i in text:
        if i == "?" or i == "!" or i == ".":
            sentences += 1
    return sentences

# Coleman - Liau Index formula


def coleman_liau_index(letters, words, sentences):
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    grade = round(index)

    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


main()
