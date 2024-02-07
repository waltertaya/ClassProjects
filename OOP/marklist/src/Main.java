import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String line = new String(new char[75]).replace('\0', '*');
        // Multidimensional array
        int marks[][] = new int[4][3];
        String names[] = new String[4];
        int totals[] = new int[4];
        int avg[] = new int[4];
        int total;
        String grade[] = new String[4];
        // Allow the user to enter name and marks
        for (int i = 0; i < 4; i++){
            System.out.print("Enter your name: ");
            names[i] = input.next();
            total = 0;
            for (int j = 0; j < 3;j++){
                System.out.print("Enter mark " + (j + 1) + ":");
                marks[i][j] = input.nextInt();
                total += marks[i][j];
            }
            totals[i] = total;
            avg[i] = total/3;
        }
        // Calculate grades based on average
        for (int n = 0; n < 4; n++) {
            if (avg[n] > 79.9) {
                grade[n] = "A";
            } else if (avg[n] > 74.9) {
                grade[n] = "B+";
            } else if (avg[n] > 64.9) {
                grade[n] = "B";
            } else if (avg[n] > 54.9) {
                grade[n] = "C+";
            } else if (avg[n] > 49.9) {
                grade[n] = "C";
            } else if (avg[n] > 39.9) {
                grade[n] = "D";
            } else{
                grade[n] = "F";
            }
        }

        // Print the header
        System.out.println(line);
        System.out.println("\t\t\t\t\t\tSTUDENT MARKLIST");
        System.out.println(line);
        System.out.println("ROLL\tNAME\tMARK1\tMARK2\tMARK3\tTOTAL\tRESULT\tAverage\tGRADE");

        // Create the tables for the students
        for (int i = 0; i < 4; i++){
            System.out.print((i + 100) + "\t\t" + names[i] + "\t");
            for (int j = 0; j < 3;j++){
                System.out.print(marks[i][j] + "\t\t");
            }
            System.out.print(totals[i] + "\t\tP\t\t" + (float)avg[i] + "\t" + grade[i] + "\n");
        }
    }
}
