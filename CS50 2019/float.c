#include <cs50.h>
#include <stdio.h>

int main(void){
    // terminal: make float -> compiles float.c
    float price = get_float("What's the price?\n");
    printf("Your total is %2f.\n", price * 1.0625);
}