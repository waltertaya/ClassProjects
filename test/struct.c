# include <stdio.h>

struct {
    char * name;
    char * surname;
    int age;
    int height;
} person;
int main() {
    person.name = "John";
    person.surname = "Doe";
    person.age = 30;
    person.height = 180;
    printf("Name: %s\n", person.name);
    printf("Surname: %s\n", person.surname);
    printf("Age: %d\n", person.age);
    printf("Height: %d\n", person.height);
    return 0;
}
