#include <stdio.h>

int main(){
    int age;
    printf("Entrez votre âge : ");
    scanf("%i",&age);

    if (age >= 18){
        printf("Tu es majeur.\n");
    }

    else{
        printf("Tu es mineur.\n");
    }

    return 0;
}