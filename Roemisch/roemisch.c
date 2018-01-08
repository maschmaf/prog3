#include <stdio.h>

void translate(int i, int rest, int teiler){
    if(rest < 5){
        while(rest != 0){
            printf("I");
            rest--;
        }
    }
    
    if(teiler > i){
        
    }
    
}

int main(void){
    int i = 0;
    printf("Zahl eingeben!\n");
    scanf("%d", &i);
    translate(i, i, 100);
    return 0;
}
