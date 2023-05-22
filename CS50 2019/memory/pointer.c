#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n; // 주소값을 받을 때는 * 붙여줘야 함
    printf("%p\n", p); // result: n의 주소값
    printf("%i\n", *p); // result: 50
}