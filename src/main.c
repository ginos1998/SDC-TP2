#include "../inc/main.h"


int main(int argc, char* argv[])
{
    if(argc != 5)
    {
        printf("Error: Invalid number of arguments");
        return 1;
    }

    char  *crpyto_name = argv[1];
    float crypto_usd = atof(argv[2]);
    float ars_usd = atof(argv[3]);
    float euro_usd = atof(argv[4]);

    printf("%s: %f USD, %f EUR, %f ARS\n",crpyto_name,crypto_usd,converter_asm(crypto_usd,euro_usd), converter_asm(crypto_usd,ars_usd));
}