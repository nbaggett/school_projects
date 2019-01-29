/*Nicholas Baggett CSC 225*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "myGrep.h"

int main(int argc, char **argv)
{
	FILE* file;

	char tempLine[100];
	char line[100];
	int numlines = 0;
	int numchars = 0;
	char longestLine[100];
	int theLineNum = 0;
	int wordTotal = 0;

	char delim[] = " .?!,\n";

	struct Node* head = NULL;
	struct Node* tail = NULL;

	char search[100];
	strcpy(search, argv[2]);

	head  = (struct Node*)malloc(sizeof(struct Node));
	tail = (struct Node*)malloc(sizeof(struct Node));
	tail = head;

	if (argc != 3)
	{
		printf("myGrep: improper number of arguments \n");
		printf("Usage: ./a.out <filename> <word> \n");
		return 1;
	}

	if ((file = fopen(argv[1], "r")) == NULL)
	{
		printf("Unable to open file: %s\n", argv[1]);
		return 1;
	}

	else
	{
		printf("%s %s %s", argv[0], argv[1], argv[2]);
	}

	while (fgets(line, sizeof(line), file))
	{
		char *ptr;
		int i = 0;
		int charCount = 0;
		int wordIndex = 0;
		int len = strlen(line);

		numlines++;
		strcpy(tempLine, line);

		for (i = 0; i < len; i++)
		{
			charCount++;
		}

		if (charCount > numchars)
		{
			numchars = charCount;
			strcpy(longestLine, tempLine);
		}

		ptr= strtok(line, delim);

		while(ptr != NULL)
		{
			if (strcmp(ptr, search) == 0)
			{
				struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
				newNode->lineNum = theLineNum;
				newNode->wordNum = wordIndex;
				strncpy(newNode->theLine, tempLine, strlen(tempLine));
				newNode->next = NULL;

				wordTotal++;

				if (head->next == NULL)
				{
					head->next = newNode;
					tail = newNode;
				}

				else
				{
					tail->next = newNode;
					tail = newNode;
				}
			}
			ptr = strtok(NULL, delim);
			wordIndex++;
		}
		theLineNum++;
	}

	printf("\n");
	printf("longest line: %s", longestLine);
	printf("num chars: %d\n", numchars);
	printf("num lines: %d\n", numlines);
	printf("total occurrences of word: %d\n", wordTotal);

	printList(head, wordTotal);

	fclose(file);

	return 0;
}

void printList(struct Node *n, int listLen)
{
	for (; listLen >= 0; listLen--)
	{
		if (strcmp(n->theLine, "") != 0)
		{
			printf("line %d; word %d; %s", n->lineNum, n->wordNum, n->theLine);
			free(n);
		}
		n = n->next;
	}
}