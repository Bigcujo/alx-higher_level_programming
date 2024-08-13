#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a node into a sorted lonked list
 * @head: double pointer to the head of the linked list
 * @number: the number to be indert into the list
 * 
 * Return: the address of the new node, or NULL if it fails 
 * 
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *previous;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        return (NULL);
    }

    new_node->n = number;
    new_node->next = NULL;

 if (*head == NULL || (*head)->n >= number)
 {
    new_node->next = *head;
    *head = new_node;
    return (new_node);
 }   

 previous = *head;
 current = (*head)->next;

 while (current != NULL && current->n < number)
 {
    previous = current;
    current = current->next;
 }

 previous->next = new_node;
 new_node->next = current;

 return (new_node);
}