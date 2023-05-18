#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // terminal: make hello -> compiles spring.c
    string ans = get_string("What's your name?\n");
    printf("hello, %s\n", ans);
}