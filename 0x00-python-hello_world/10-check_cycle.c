#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list;
	listint_t *y = list;

	if (!list)
		return (0);

	while (x && y && y->next)
	{
		x = x->next;
		y = y->next->next;
		if (x == y)
			return (1);
	}

	return (0);
}
