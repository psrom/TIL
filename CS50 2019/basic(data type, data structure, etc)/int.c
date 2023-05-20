#include <cs50.h>
#include <stdio.h>

int main(void){
    // terminal: make int -> compiles int.c
    int age = get_int("What's your age?\n");
    printf("You are at least %i days old.\n", age*365);
}