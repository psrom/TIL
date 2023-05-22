#include <stdio.h>

int main(void)
{
    char *s = "EMMA";
    printf("%s\n", s); // result: EMMA
    printf("%p\n", s); // address of s
    printf("%p\n", &s[0]); // the first address of s("E")
}
