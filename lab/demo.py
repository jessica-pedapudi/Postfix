#include<stdio.h>
int main()
{
int roll_number;
char name [50];
int marks [5], total=0;
int i;
printf("Enter Roll Number: ");
scanf("%d", &roll_number);
printf("Enter Name: ");
scanf("%s", &name);
for(i=0;i < 5; i++) {
printf("Enter Marks for subject %d: ", i + 1);
scanf("%d", &marks[i]);
total += marks[i];
}
printf("\n...student details (using Array)...\n");
printf("Roll number: %d\n", roll_number);
printf("Name: %s\n", name);
printf("Marks: ");
for(i=0;i<5;i++) {
printf("%d", marks[i]);
}
printf("\n Total: %d\n", total);
getch();
return 0;
}
