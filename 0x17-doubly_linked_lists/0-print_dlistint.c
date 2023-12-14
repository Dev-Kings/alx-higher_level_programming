#include "lists.h"

/**
 * print_dlistint - prints elements of a doubly linked list
 * @h: const pointer to head node
 *
 * Return: Number of nodes in the linked list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t node_counter;
	const dlistint_t *current;

	current = h;
	node_counter = 0;
	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		node_counter++;
	}
	return (node_counter);
}
