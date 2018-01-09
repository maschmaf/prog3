#include <stdio.h>

int main(void){
	double x = 0.0;
	double w = 0.0;
	double wOld = 0.0;
	double teiler = 2.0;
	double abbruch = 1e-7;
	double differenz = 0.0;
	while(x<= 0){
		printf("Geben Sie eine Zahl ein: ");
		scanf("%lf", &x);
	}
	w = (1.0+x)/teiler;
	
	differenz = x-w;
	printf("Zahl: %f ", w);
	printf("Differenz: %f\n", differenz);
	
	while(differenz > abbruch){
		wOld = w;
		w = (w+(x/w))/teiler;
		
		differenz = wOld - w;
		
		if(differenz < 0){
			differenz *= -1;
		}
		
		printf("Zahl = %6.4f\n", w);
		

	}
	
	
	
	return 0;
}
