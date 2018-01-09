#include <stdio.h>
#include <string.h>

const char from[] = {"abcdefghijklmnopqrstuvwxyz"};
const char to[] =   {"irjmnzltacogdeksvbphxqyuwf"};

int getIndexFrom(int c, const char bla[]){
	int len = strlen(bla);
	int i;
	for(i = 0; i <= len; i++){
		if(c == bla[i]){
			return i;
		}
	}
	
	return 0;
}

void encrypt(){
	int input = 0;
	while((input = getchar()) != EOF){
		if(input>= 'a' && input <= 'z'){
			putchar(to[getIndexFrom(input, from)]);
		}else{
			putchar(input);
		}
	}
}

void decrypt(){
	int input = 0;
	while((input = getchar()) != EOF){
		if(input >= 'a' && input <= 'z'){

			putchar(from[getIndexFrom(input, to)]);
		}else{
			putchar(input);
		}
	}
}

int main(int argc, char* argv[]){
	
	if(strcmp(argv[1], "encrypt") == 0){
		printf("\nVerschluessen!\n");
		encrypt();

	}else if(strcmp(argv[1], "decrypt") == 0){
		printf("\nEntschluesseln!\n");
		decrypt();
	}
	
	return 0;
}
