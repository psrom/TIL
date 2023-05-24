// binary-search tree structure
typedef struct node
{
    int number;

    struct node *left;
    struct node *right;
}
node;

// binary-search function
bool search(node *tree)
{
    if (tree = NULL)
    {
        return false;
    }

    else if (50 < tree->number)
    {
        return search(tree->left);
    }

    else if (50 > tree->number)
    {
        return search(tree->right);
    }
    
    else
    {
        return true;
    }
}
