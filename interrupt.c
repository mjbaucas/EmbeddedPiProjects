#include <stdio.h>
#include <unistd.h>

extern void counter_function(void);

void interrupt_function(int value){
	printf("Value received from assembly: %d\n", value);
	usleep(1000000);
}

int main(){
	counter_function();
	return 0;
}

