#include <stdio.h>
int main(){
   int initial_amount= 50000;
   int withdraw= 20000;
   int balance= initial_amount-withdraw;
   if(withdraw<=initial_amount){
      printf("Your balance after withdrawing %d shillings is %d shillings\nq",
      withdraw, balance);
   }
   else{
      printf("You have insufficient balance on your account\n");
      printf("Please enter an amount of money less than %d shillings on the next transaction\n", initial_amount);
   }
   return 0;
}
