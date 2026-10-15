import java.util.Scanner;

public class Main {

    public static int luckyNumber(String s) {
        if (s.length() == 0) {
            return 0;
        }

        if (s.charAt(0) == '4' || s.charAt(0) == '7') {
            return 1 + luckyNumber(s.substring(1));
        }

        return luckyNumber(s.substring(1));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String s = scanner.next();
        int count = luckyNumber(s);

        if (count == 4 || count == 7) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

    }
}