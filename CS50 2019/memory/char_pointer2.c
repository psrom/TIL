#include <stdio.h>

int main(void)
{
  char *s = "EMMA";
  printf("%p\n", s); // EMMA address
  printf("%c\n", *s); // E
  printf("%c\n", *(s+1)); // M
  printf("%c\n", *(s+2)); // M
  printf("%c\n", *(s+2)); // A
}