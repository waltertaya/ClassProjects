# include <stdio.h>

struct person {
    char * name;
    char * surname;
    int age;
    int height;
};
char * waltermitty(){
    struct person walter;
    walter.age = 45;
    walter.height = 270;
    walter.name = "Reginah";
    walter.surname = "Reg";

    return (walter.surname, walter.name);
}
int main() {
    struct person person1;
    person1.name = "John";
    person1.surname = "Doe";
    person1.age = 30;
    person1.height = 180;
    printf("Name: %s\n", person1.name);
    printf("Surname: %s\n", person1.surname);
    printf("Age: %d\n", person1.age);
    printf("Height: %d\n", person1.height);

    printf("Walter surname %s Name: %s\n", waltermitty(),waltermitty());

    return 0;
}
