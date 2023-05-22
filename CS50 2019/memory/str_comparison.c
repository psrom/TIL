#include <stdio.h>
#include <cs50.h>

int main(void)
{

    string s = get_string("s: ");
    string t = get_string("t: ");

    if (s==t) // Different
    {
        printf("Same\n");
    }
    else
    {
    printf("Different\n");
    }
}
// 같은 문자열을 입력해도 주소가 다르기 때문에 다른 문자열이라고 결과가 나온다.
// 이를 어떻게 해결해야 할까?

// if (*s == *t) : 주소가 아닌, 주소 안에 있는 값을 비교
// 이 때는 Same이라고 올바른 결과가 나옴