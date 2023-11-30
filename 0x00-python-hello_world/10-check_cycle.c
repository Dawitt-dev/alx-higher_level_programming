#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
/**
 * check_cycle - checks if a list has a cycle in it
 *@list: tha list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t* slow;
	listint_t* fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
