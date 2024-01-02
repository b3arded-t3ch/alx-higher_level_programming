#include <stdio.h>
#include "lists.h"
#include <string.h>

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current != NULL && current->next != NULL)
	{
		if (current == current->next)
		{
			return (1);
		}
		current = current->next;
	}
	return (0);
}
