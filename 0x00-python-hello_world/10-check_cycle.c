#include "stdio.h"
#include "lists.h"

/**
 * check_cycle - check linked list cycle
 * @list: linked list
 *
 * Return: 0 if no cycle or 1
 */
int check_cycle(listint_t *list)
{
	const listint_t *current;

	while (list != NULL)
	{
		current = list->next;
		while (current != NULL)
		{
			if (list == current)
				return (1);
			current = current->next;
		}
		list = list->next;
	}
	return (0);
}
