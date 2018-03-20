#include <stdio.h>

void power2(int i)
{
   int products[10];
   int x = 1;
   int c = 0;
   while(i>0)
   {
      if(i%2)
      {
         products[c++]=x;
      }
      x=x*2; // Multiply by 2
      i=i>>1; // Do a shift. Is this a bug?
   }
   for(x=0; x< c; x++)
   {
      printf("%i\n",products[x]);
   }

}


void main(int argc, char* argv[])
{
    int value = atoi(argv[1]);
    power2(value);
}
