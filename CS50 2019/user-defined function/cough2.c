#include <stdio.h>
// main function should be on the top->good code
void cough(int n);

int main(void)
{
    cough(3);
}








void cough(int n)
{
    for (int i = 0; i < n ; i++)
    {
        printf("cough\n");
    }
}