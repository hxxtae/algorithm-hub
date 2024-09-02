import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int result = 0;
        int[] three = {0, 21, 12, 3, 24, 0, 6, 27, 18, 9};
        
        if(num == 3) {
            System.out.print(1);
        } else if (num == 4 || num == 7) {
            System.out.print(-1);
        } else {
            int a = num % 10;
            int b = (num - 5) % 10;
            
            if(three[a] > three[b]) {
                result = three[b] / 3;
                num = num - three[b];
            } else {
                result = three[a] / 3;
                num = num - three[a];
            }
            result += (num / 5);
            System.out.print(result);
        }
    }
}