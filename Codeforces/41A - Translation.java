import java.util.Scanner;

public class Main {
    public static String reverse(String s) {

        if (s.length() <= 1){
            return s;
        }

        return reverse(s.substring(1)) + s.charAt(0);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String r = sc.next();

        if (reverse(s).equals(r)) {
            System.out.print("YES");
        } else {
            System.out.print("NO");
        }

    }
}