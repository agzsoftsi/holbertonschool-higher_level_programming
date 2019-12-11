#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Insert a node
 * @head: The linked list
 * @number: The number to insert
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nnode;
	listint_t *cnode = *head;

	if (!head)
		return (NULL);

	nnode = malloc(sizeof(listint_t));
	if (!nnode)
		return (NULL);

	nnode->n = number;
	nnode->next = NULL;

	if (*head == NULL)
		*head = nnode;
	else if (number < cnode->n)
	{
		nnode->next = cnode;
		*head = nnode;
	}
	else
	{
		while (cnode->next)
		{
			if (number > cnode->next->n)
				cnode = cnode->next;
			else
				break;
		}
		nnode->next = cnode->next;
		cnode->next = nnode;
	}

	return (nnode);
}
