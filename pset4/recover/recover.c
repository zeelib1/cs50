#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


// Defining necessary dtypes and memory allocation
typedef uint8_t BYTE;
BYTE buffer[512];
int counter = 0;
FILE *image;
char filename[8];

int main(int argc, char *argv[])
{


// check the command line argument

    if (argc != 2)
    {
        printf("CL arguments must be equal 2");
        return 1;
    }
// Open the file with appropriate conditions

    FILE *stream;
    stream = fopen(argv[1], "r");
    if (stream == NULL)
    {
        printf("File does not exist.");
        return 1;
    }



    // Read 512 bytes into a buffer

    while (fread(buffer, sizeof(BYTE), 512, stream) == 512)
    {
        //Checking if JPG

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //Close opened image if JPG exists

            if (counter > 0)
            {
                fclose(image);
            }
            //creating JPG file

            sprintf(filename, "%03i.jpg", counter);
            counter++;
            image = fopen(filename, "w");
            fwrite(buffer, 512, 1, image);

        }
        //JPEG exist, continue writing to it

        else if (counter > 0)
        {

            fwrite(buffer, sizeof(buffer), 1, image);
        }

    }
    fclose(image);
    fclose(stream);


}
