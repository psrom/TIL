#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x;
    int *y;

    x = malloc(sizeof(int));

    *x = 42;

    // y가 가리키는 곳과 x가 가리키는 곳이 동일
    y = x;
    // 결과적으로 x, y는 둘 다 13을 가리키게 됨
    *y = 13;
}
