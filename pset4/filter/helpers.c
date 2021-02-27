#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avg;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avg = round(((float)image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3);

            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

int sepiaRed, sepiaGreen, sepiaBlue;
// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sepiaRed = round((float)image[i][j].rgbtRed * 0.393 + (float)image[i][j].rgbtGreen * 0.769 + (float)image[i][j].rgbtBlue * 0.189);
            sepiaGreen = round((float)image[i][j].rgbtRed * 0.349 + (float)image[i][j].rgbtGreen * 0.686 + (float)image[i][j].rgbtBlue * 0.168);
            sepiaBlue = round((float)image[i][j].rgbtRed * 0.272 + (float)image[i][j].rgbtGreen * 0.534 + (float)image[i][j].rgbtBlue * 0.131);

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;

// Check if pixels are not going over limit
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE tmp = image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {

            tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;

        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Temporary copy of the original image

    RGBTRIPLE tmp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;
            int horizontal[] = {i - 1, i, i + 1};
            int vertical[] = {j - 1, j, j + 1};
            float totalR = 0;
            float totalG = 0;
            float totalB = 0;

            for (int k = 0; k < 3; k++)
            {
                for (int l = 0; l < 3; l++)
                {
                    int current_r = horizontal[k];
                    int current_c = vertical[l];

// Check for the adjacent positions inside; bound issue

                    if (current_r >= 0 && current_r < height && current_c >= 0 && current_c < width)
                    {
// Add to total for those inside inside bounds
                        totalR += image[current_r][current_c].rgbtRed;
                        totalG += image[current_r][current_c].rgbtGreen;
                        totalB += image[current_r][current_c].rgbtBlue;

                        count++;
                    }
                }
            }
// Asign the values to a temporary copy

            tmp[i][j].rgbtRed = round(totalR / count);
            tmp[i][j].rgbtGreen = round(totalG / count);
            tmp[i][j].rgbtBlue = round(totalB / count);
        }
    }
// Assign copy to the original image

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = tmp[i][j];
        }
    }


    return;
}