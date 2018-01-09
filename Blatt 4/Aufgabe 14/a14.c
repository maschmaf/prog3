#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _liste{
	void* data;
	struct _liste *next;
	struct _liste *prev;
}nodep;


void printList(nodep* list){
	nodep* element = list;
	
	while(element->next != NULL && element->next != list){
		printf("Adresse: %p\n", element->data);
		element = element->next;
	}
	printf("Adresse: %p\n", element->data);
}

nodep* insertAt(nodep* lst, int pos, void *data){
	nodep* head, *new;
	
	if(pos == 0){
		head = malloc(sizeof(nodep));
		head->data = data;
		head->next = lst;
		head->prev = NULL;
		lst->prev = head;
	}else if(pos == -1){
		head = lst;
		new = malloc(sizeof(nodep));
		for(;lst;lst = lst->next){}
		new->data = data;
		new->prev = lst;
		new->next = NULL;
		lst->next = new;
	}
	return head;
}

int main(int argc, char *argv[]){
	nodep* head = malloc(sizeof(nodep));
	head->data = "Hallo";
	head->prev = NULL;
	head->next = NULL;

	head = insertAt(head, -1, "Gude");
	head = insertAt(head, -1, "Tach");
	
	printList(head);
	
	return 0;
}
