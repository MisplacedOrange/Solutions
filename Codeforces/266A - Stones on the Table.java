import java.util.Scanner;

public class temp {

    public static int consecStones(String s) {

        if (s.length() <= 1) {
            return 0;
        }

        if (s.charAt(0) == s.charAt(1)) {
            return 1 + consecStones(s.substring(1));
        }

        return consecStones(s.substring(1));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String s = sc.next();

        System.out.println(consecStones(s));

    }
}