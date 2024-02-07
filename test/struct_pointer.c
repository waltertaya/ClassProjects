# include <stdio.h>

typedef struct struct_pointer
{
    int age;
    char * name;
}person;

int main(){
    person person1 = {23, "Walter"};

    person *ptr = &person1;

    printf("Age: %d\nName: %s\n", ptr->age, ptr->name);

    return 0;
}