import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String ussd;

        while (true) {
            System.out.println("Enter ussd code: ");
            ussd = input.next();

            if (ussd.equals("*131#")) {
                mainMenu(input);
//            } else if (ussd.equals("exit")) {
//                System.out.println("Exiting...");
//                break;
            } else {
                System.out.println("Invalid USSD code");
            }
        }

//        input.close();
    }

    public static void mainMenu(Scanner input) {
        System.out.println("          Send Instructions");
        System.out.println("0. Sh20 (30mins,3hrs)");
        System.out.println("1. Okoa Easy Sh50 (50mins, midnight)");
        System.out.println("2. Okoa 100");
        System.out.println("3. Okoa 50");
        System.out.println("4. Okoa 20 (or KSh50, Midnight)");
        System.out.println("5. Okoa 10");
        System.out.println("6. Okoa 5");
        System.out.println("7. Okoa Internet");
        System.out.println("98. More");

        System.out.println("Enter your option: ");
        int choice = input.nextInt();

        switch (choice) {
            case 0:
                int unpaidOkoa = 0;
                System.out.println("Existing Unpaid Okoa: " + unpaidOkoa);
                System.out.println("New Okoa request: 20");
                int debt = unpaidOkoa + 20;
                System.out.println("TOTAL DEBT will be: " + debt);
                System.out.println("1: Accept");
                System.out.println("2: Decline");
                System.out.println("0: BACK");
                System.out.println("00: HOME");

                System.out.println("Enter your option: ");
                String bundle = input.next();
                switch (bundle) {
                    case "1":
                        System.out.println("You have successfully okoa sh20");
                        break;
                    case "2":
                        System.out.println("You have declined okoa request");
                        break;
                    case "0":
                        mainMenu(input);
                        break;
                    case "00":
                        mainMenu(input);
                        break;
                    default:
                        System.out.println("Invalid option");
                        break;
                }
                break;
            case 98:
                // Handle 'More' option
                break;
            default:
                System.out.println("Invalid option");
                break;
        }
    }
}
