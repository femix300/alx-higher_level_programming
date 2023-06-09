#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head pointer of the linked list
 * @number: the number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	else
	{

		while (node && node->next && node->next->n < number)
			node = node->next;

		new->next = node->next;
		node->next = new;

		return (new);
	}
}

