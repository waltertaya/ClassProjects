import java.util.Scanner;
public class BookInputTest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Book BookTest = new Book();
        System.out.println("Please enter the title of the book");
        BookTest.title = input.nextLine();
        System.out.println("Please enter the author name");
        BookTest.author = input.nextLine();
        System.out.println("Please enter the number of pages");
        BookTest.numberOfPages = input.nextInt();
        System.out.println("The book title is: " + BookTest.title);
        System.out.println("The book author is: " + BookTest.author);
        System.out.println("The book has: " + BookTest.numberOfPages + " pages");
    }
}
