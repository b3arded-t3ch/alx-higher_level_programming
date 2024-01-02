#include <stdio.h>
#include "lists.h"
#include <string.h>

/**
 * check_cycle - checks if a linked list is a cycle
 * @list: linked list to check
 * Return: 1 if it's a cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *earlier = list;

	if (!list)
	{
		return (0);
	}

	while (current && earlier && earlier->next)
	{
		current = current->next;
		earlier = earlier->next->next;
		if (current == earlier)
		{
			return (1);
		}
	}
	return (0);
}
