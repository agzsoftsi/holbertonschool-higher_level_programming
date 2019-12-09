#include "lists.h"
/**
 *check_cycle - check if exist a cycle
 *@list: list to check
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *nod1 = list;
	listint_t *nod2 = list;

	while (nod1 && nod2 && nod2->next)
	{
		nod1 = nod1->next;
		nod2 = nod2->next->next;
		if (nod1 == nod2)
			return (1);
	}
	return (0);
}
