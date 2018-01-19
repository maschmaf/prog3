#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct ListEle{
    int zahl;
    struct ListEle *next;
}listEle;

listEle *ersteListe = NULL;
listEle *zweiteListe = NULL;
listEle *zippedList = NULL;
listEle *headZipped = NULL;

void addEle(int nListe, int z){
    listEle *neu = malloc(sizeof(listEle));
    listEle *head;
    neu->zahl = z;
    neu->next = NULL;
    if(nListe == 1){
        if(ersteListe == NULL){
            ersteListe = neu;
        }else{
            head = ersteListe;
            
            while(ersteListe->next != NULL){
                ersteListe = ersteListe->next;
            }
            ersteListe->next = neu;
            ersteListe = head;
        }
    }else{
        if(zweiteListe == NULL){
            zweiteListe = neu;
        }else{
            head = zweiteListe;
            
            while(zweiteListe->next != NULL){
                zweiteListe = zweiteListe->next;
            }
            zweiteListe->next = neu;
            zweiteListe = head;
        }
    }
}

void printList(){
    while(zippedList != NULL){
        printf("%i\n", zippedList->zahl);
        zippedList = zippedList->next;
    }
    
    zippedList = headZipped;
}

void printFirstList(){
    listEle *head = ersteListe;
    while(ersteListe != NULL){
        printf("%i\n", ersteListe->zahl);
        ersteListe = ersteListe->next;
    }
    ersteListe = head;
}

void zipLists(){
    listEle *headFirst = ersteListe;
    listEle *headSecond = zweiteListe;
    listEle *neu;
    listEle *neuneu;
    
    int sizeFirstList = 0;
    int sizeSecondList = 0;
    
    while(ersteListe != NULL){
        sizeFirstList +=1;
        ersteListe = ersteListe->next;
    }
    ersteListe = headFirst;
    while(zweiteListe != NULL){
        sizeSecondList += 1;
        zweiteListe = zweiteListe->next;
    }
    zweiteListe = headSecond;
    
    if(sizeFirstList == sizeSecondList){
        while(ersteListe != NULL){
            if(zippedList == NULL){
                zippedList = malloc(sizeof(listEle));
                headZipped = zippedList;
                zippedList->zahl = ersteListe->zahl;
                zippedList->next = NULL;
                neu = malloc(sizeof(listEle));
                neu->zahl = zweiteListe->zahl;
                neu->next = NULL;
                zippedList->next = neu;
                ersteListe = ersteListe->next;
                zweiteListe = zweiteListe->next;
                zippedList = zippedList->next;
            }else{
                neu = malloc(sizeof(listEle));
                neu->zahl = ersteListe->zahl;
                neuneu = malloc(sizeof(listEle));
                neuneu->zahl = zweiteListe->zahl;
                neuneu->next = NULL;
                neu->next = neuneu;
                zippedList->next = neu;
                
                ersteListe = ersteListe->next;
                zweiteListe = zweiteListe->next;
                zippedList = zippedList->next->next;
            }
        }
        
    }
    
    zippedList = headZipped;
    ersteListe = headFirst;
    zweiteListe = headSecond;
}

void freeLists(){
    while(ersteListe->next != NULL){
        listEle *tmp = ersteListe;
        ersteListe = ersteListe->next;
        free(tmp);
    }
    free(ersteListe);
    
    while(zweiteListe->next != NULL){
        listEle *tmp = zweiteListe;
        zweiteListe = zweiteListe->next;
        free(tmp);
    }
    free(zweiteListe);
}

void freeList(){
    printf("WARUM");
    while(zippedList != NULL){
        listEle *tmp = zippedList;
        zippedList = zippedList->next;
        free(tmp);
    }
}

void anfangAnEnde(){
    listEle *head = ersteListe;
    listEle *vorletzte;
    
    while(ersteListe->next->next != NULL){
        ersteListe = ersteListe->next;
    }
    
    vorletzte = ersteListe;
    ersteListe = vorletzte->next;
    vorletzte->next->next = head->next;
    vorletzte->next = head;
    head->next = NULL;
    
    
}

int main(void){
    addEle(1,1);
    addEle(2,2);
    addEle(1,3);
    addEle(2,4);
    addEle(1,5);
    addEle(2,6);
    addEle(1,7);
    addEle(2,8);
    /*
    printFirstList();
    anfangAnEnde();
    printFirstList();
    */
    
    
    zipLists();
    printList();
    freeLists();
    freeList();
    
    return 0;
}
