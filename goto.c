#include <stdio.h>
int main(){
  int a= 0;
  start_loop:
    printf("%d\n", a);
    a++;
    if(a<=10){
      goto start_loop;
    }
return 0;
}
