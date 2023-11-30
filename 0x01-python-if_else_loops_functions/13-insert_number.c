#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 *@number: new data
 *@head: current list
 *
 * Return: new node oor NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if(*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	current = *head;

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new->next = current->next;
	current->next = new;

	return (new);
}
