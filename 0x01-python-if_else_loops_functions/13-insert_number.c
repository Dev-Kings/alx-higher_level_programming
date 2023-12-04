#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly
 * linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of new node if succesful, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;

	current = *head;
	previous = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	if (previous == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		new->next = current;
		previous->next = new;
	}

	return (new);
}
