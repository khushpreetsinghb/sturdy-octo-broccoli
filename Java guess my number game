import java.util.Scanner;
import static java.lang.Math.random;

public class Program{
    public static void main(String args[]){
         
        Scanner sc = new Scanner(System.in);
        int number = (int)(Math.random()*100);
        int guess = 0;
        do {
            System.out.println("Guess my chosen number between 1 to 100: ");
            guess = sc.nextInt();
            
            if (number == guess) {
                System.out.println("Congratulations, you guessed the number.");
                break;
            } 
            else if(number > guess) {
                System.out.println("The number is greater than " + guess);
            }
            else {
                System.out.println("The number is smaller than " + guess);
            } 
        } while(guess >= 0);
        
        System.out.println("My number was " + number);
        System.out.println();
    }
}
