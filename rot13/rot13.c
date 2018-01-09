#include <stdio.h>

int rot13(int c){
    if(c >= 'A' && c <= 'Z'){
        return ((((c-'A')+13)%26)+'A');
    } else if(c >= 'a' && c <= 'z'){
        return ((((c-'a')+13)%26)+'a');
    }
    return c;
}

int main(void){
	int c;
    while((c = getchar()) != EOF){
        putchar(rot13(c));
    }	
	return 0;
}
