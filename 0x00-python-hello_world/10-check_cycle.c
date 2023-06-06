#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: a pointer to the head node of the linked list
 * Return: 1 if a cycle is found and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
		{
			return (1);
		}
	}

	return (0);
}
