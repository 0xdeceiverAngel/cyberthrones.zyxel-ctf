#include <stdio.h>
#include <stdlib.h>
#include <time.h>



int main(){

    srand( (int)time(NULL));
    int tmp=rand()%0x100000;
    printf("%d",tmp+1);
 
    return 0;
   
}
