/* This program reads from
   stdin and it removes duplicate
   lines. */
#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	char *prevline = NULL; /* next line */
	char *currline = NULL; /* current line */
	size_t len = 0; /* len of each line for getline */
	ssize_t read; /* success of getline determined by this */

	prevline = (char *)malloc(sizeof(currline));
	if (NULL == prevline)
	{
		perror("bad malloc");
		exit(EXIT_FAILURE);
	}

	while ((read = getline(&currline, &len, stdin)) != -1)
	{
		currline[strcspn(currline, "\r\n")] = 0; /* remove newline char */
		if (NULL == prevline)
		{
			printf("%s\n", currline);
		}

		else
		{
			if (strcmp(prevline, currline) != 0)
			{
				printf("%s\n", currline);
			}
		}

		prevline = (char *)realloc(prevline, strlen(currline) + 1); 
		/* realloc with null char */
		if (NULL == prevline)
		{
			perror("bad realloc");
			exit(EXIT_FAILURE);
		}
		strcpy(prevline, currline); /* copy the current line to the previous line */
	}

	free(currline);
	free(prevline);

	return 0;
}