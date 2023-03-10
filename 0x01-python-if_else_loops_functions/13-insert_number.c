#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that insters a number into a sorted linked list
 *
 * @head: the head of the linked list
 * @number: the linked list data
 *
 * Return: the address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *newNode = malloc(sizeof(newNode));

	if (newNode == NULL)
	{
		free(newNode);
		return (NULL);
	}

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL)
		*head = newNode;
	else
	{
		current = *head;

		while (current->next != NULL)
			current = current->next;

		current->next = newNode;
	}

	return (newNode);
}
