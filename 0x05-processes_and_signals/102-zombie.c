#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while   - Prevents program from exiting
 *
 * Return:            (Success): 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main              - Creates 5 zombie processes
 *
 * Return:             (Success): 0
 */

int main(void)
{
	pid_t pid;
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid <= 0)
		{
			exit(1);
		}

		printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();

	return (0);
}

/* Ref: https://stackoverflow.com/questions/25172425/create-zombie-process */
