#include <stdio.h>
#include <cs50.h>

int main(void)
{

    string s = get_string("s: ");
    string t = get_string("t: ");

    if (s==t)
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