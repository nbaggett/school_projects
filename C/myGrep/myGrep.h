struct Node
{
	int lineNum;
	int wordNum;
	char theLine[100];
	struct Node *next;
};

void printList(struct Node *n, int listlen);