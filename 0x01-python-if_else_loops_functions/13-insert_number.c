#include "lists.h"

/**
 * insert_node - will insert node to a linked list
 * @head: head of a linked list
 * @number: the new value
 *
 * Return: address of new node list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		if (temp_node)
			return (NULL);
		*head = new_node;
		return (new_node);
	}
	while (temp_node != NULL)
	{
		if ((temp_node)->n > number)
		{
			new_node->next = temp_node;
			temp_node = new_node;
			return (new_node);
		} else if ((temp_node)->next == NULL)
		{
			(temp_node)->next = new_node;
			return (new_node);
		} else if ((temp_node)->next->n > number)
		{
			new_node->next = (temp_node)->next;
			(temp_node)->next = new_node;
			return (new_node);
		}
		temp_node = (temp_node)->next;
	}
	return (NULL);
}
