
#include <stdio.h>
#include <stdlib.h>

long get_fact(int n){
	if (n < 0)
		return 0;
	else if (n == 0)
		return 1;
	else if (n == 1)
		return 1;
	else 
		return n * get_fact(n-1);
}

int main(int argc, char *argv[]){

	int num;
	if(argv[1] == NULL){
		printf("No number provided!\n");
		return 1;
	} else {
		num = atoi(argv[1]);
		printf("Factorial of %d is %ld\n", num, get_fact(num));
		return 0;
	}
}