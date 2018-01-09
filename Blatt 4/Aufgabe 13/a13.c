#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _person{
	char* name;
	struct _person *next;
}person;


person* deletePerson(person* liste, int count){
	person* delete;
	person* lastElement;
	
	int i = 0;
	delete = liste;
	
	if(delete->next == delete){
		delete->next = NULL;
		return delete;
	}
	
	while(i<count){
		if(i>0){
			lastElement = liste;
		}
		delete = delete->next;
		i+=1;
	}
	lastElement = lastElement->next;
	lastElement->next = delete->next;
	free(delete);
	
	return lastElement;
}

int main(int argc, char *argv[]){
	char nameIn[25];
	int i = 0;
	person *startElement, *lastElement, *newElement;
	
	startElement = malloc(sizeof(person));
	
	
	while(scanf("%s", nameIn) != EOF){		
		if(i == 0){
			startElement->name = malloc(sizeof(nameIn));
			strcpy(startElement->name, nameIn);
			startElement->next = startElement;
			lastElement = startElement;
			i++;
		}else{;
			newElement = malloc(sizeof(person));
			newElement->name = malloc(sizeof(nameIn));
			strcpy(newElement->name, nameIn);
			newElement->next = startElement;
			lastElement->next = newElement;
			lastElement = newElement;
		}
	}
	
	while(startElement->next != NULL){
		startElement = deletePerson(startElement, argc-1);
	}
	
	printf("Person %s muss abwaschen!\n", startElement->name);
	
	
	return 0;
}
