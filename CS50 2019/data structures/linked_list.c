#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    node *list = NULL;

    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    n->number = 1; //(*n).number와 동일한 의미
    n->next = NULL;

    list = n; // list pointer -> n pointer로 바꿈

    //==================================================
    // to allocate new node
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    n->number = 2;
    n->next = NULL;

    list->next = n;

    //==================================================
    // to allocate new node
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    n->number = 3;
    n->next = NULL;

    list->next->next = n;

    //==================================================
    // 중간에 있는 2 삭제하기
    node *temp = list->next->next;
    free(list->next);
    list->next=temp;

    //==================================================
    // 중간에 2 추가하기
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    
    n->number = 2;
    n->next = list->next;
    list->next = n;

    //==================================================
    // list에 연결된 node를 처음부터 방문하면서 number 값 출력
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }

    //==================================================
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
}
