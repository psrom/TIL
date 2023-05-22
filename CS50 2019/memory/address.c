#include <stdio.h>

int main(vod)
{
    int n = 50;
    // n의 주소값 가져오기
    printf("%p\n", &n);

    //n의 주소 => 주소에 해당하는 값 가져오기
    printf("%i\n", *&n);
}