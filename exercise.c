#include <stdio.h>
#include <string.h>

int main() {

    // Defining the Book structure
    struct Book {
        char title[50];
        char author[50];
        float price;
    };

    struct Book book;
    FILE *file;

    printf("Enter book title: ");    // Input book title 
    fgets(book.title, sizeof(book.title), stdin)

    printf("Enter author name: ");     //input book author name 
    fgets(book.author, sizeof(book.author), stdin);

    // Saving to file
    file = fopen("book_details.txt", "w");

    //checking whether the file was created or exists 
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(file, "%s\n%s\n%.2f\n", book.title, book.author, book.price);
    fclose(file);
    printf("\nBook details saved to book_details.txt\n");

    // Read saved details
    file = fopen("book_details.txt", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    printf("\nBook Details:\n");  //display book title
    printf("Title: ");
    fgets(book.title, sizeof(book.title), file);
    printf("%s\n", book.title);

    printf("Author: ");  //display book author
    fgets(book.author, sizeof(book.author), file);
    printf("%s\n", book.author);

    float price;
    fscanf(file, "%f", &price);
    printf("Price: %.2f\n", price);

    fclose(file);

    return 0;
}
