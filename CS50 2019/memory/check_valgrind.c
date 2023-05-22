#include <stdlib.h>

void f(void)
{
    int *x = malloc(10 * sizeof(int));
    x[9] = 0; // x[10] = 0; 일 시 오류 남(buffer overflow)
    free(x);
}

int main(void)
{
    f();
    return 0;
}