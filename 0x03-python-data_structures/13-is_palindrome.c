#include <stdlib.h>
#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: linked list
 *
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int j, p, t, x, *list;
	listint_t *temp;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	j = getSize(&temp);
	list = getArray(&temp, j);
	if (j % 2 == 0)
	{
		p = (j + 2) / 2;
		t = (j - 2) / 2;
	}
	else
	{
		p = (j + 3) / 2;
		t = (j - 3) / 2;
	}
	for (x = 1; x < p; x++)
		temp = temp->next;
	while (temp->next != NULL)
	{
		if (temp->n != list[t])
		{
			free(list);
			return (0);
		}
		temp = temp->next;
		t--;
	}
	free(list);
	return (1);
}
/**
 * getSize - gets size of a linked list
 * @temp: linked list
 *
 * Return: size
 */
int getSize(listint_t **temp)
{
	listint_t *lst;
	int j = 1;

	lst = *temp;
	while (lst->next != NULL)
	{
		lst = lst->next;
		j++;
	}
	return (j);
}
/**
 * getArray - gets an array of half of the integer data of the list's nodes
 * @temp: list
 * @j: size of list
 *
 * Return: array of integers
 */
int *getArray(listint_t **temp, int j)
{
	listint_t *tem = *temp;
	int a, b, *list;

	if (j % 2 == 0)
		a = j / 2;
	else
	       a = (j - 1) / 2;
	list = (int *)malloc(sizeof(int) * a);
	for (b = 0; b < a; b++)
	{
		list[b] = tem->n;
		tem = tem->next;
	}
	return (list);
}
