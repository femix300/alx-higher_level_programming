#include "lists.h"
/**
 * reverse_listint - a function that everses a linked list
 * @head: a pointer to the first node in the list
 *
 * Return: Pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks whether a linked list is a palindrome.
 * @head: Double pointer to the linked list.
 *
 * Return: 1 if it is a palindrome, and return 0 if it isn't.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *temp = *head;
	listint_t *reversed = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			reversed = slow->next;
			break;
		}
		if (!fast->next)
		{
			reversed = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_listint(&reversed);

	while (reversed && temp)
	{
		if (temp->n == reversed->n)
		{
			reversed = reversed->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!reversed)
		return (1);
	return (0);
}
