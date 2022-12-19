import java.util.Scanner;  //Import the Scanner class
import java.util.InputMismatchException;

public class Calculator{
  public static void main(String[] args){
    System.out.println("List of operations: add,subtract,multiply,divide,alphabetize");
    Scanner input = new Scanner(System.in);
    System.out.print("Enter an operation: \n");
    String operation=input.nextLine().trim().toLowerCase();
    //System.out.println(operation);
    switch (operation) {
        case "add":
        case "subtract":
        System.out.print("Enter Two Integers: \n");
          try{
              int Num1 = input.nextInt();
              int Num2 = input.nextInt();
              int Result1;
              if (operation.equals("add")){
                Result1 = Num1+Num2;
              }
              else{
                Result1 = Num1-Num2;
              }
              System.out.println("Answer: " +Result1);

            }
          catch (InputMismatchException e){
              System.out.println("Invalid input entered. Terminating...");
          }
              //System.out.println("Num1"+Num1);
              //System.out.println("Num2"+Num2);
              break;

        case "multiply":
        case "divide":
             System.out.print("Enter Two Doubles: \n");
             try{
               double Num3 = input.nextDouble();
               double Num4 = input.nextDouble();
               double Result2=0;
               if (operation.equals("multiply")){
                 Result2 = Num3 * Num4;
               }
               else{
                 if (Num4 == 0.0){
                   System.out.println("Invalid input entered. Terminating...");
                   break;
                 }
                 else{
                   Result2 = Num3/Num4;
                 }

               }
               System.out.printf("Answer: " + "%.2f%n",Result2);}
               catch (InputMismatchException e){
                 System.out.println("Invalid input entered. Terminating...");
               }

               break;
          case "alphabetize":
                System.out.print("Enter Two Words: \n");

                try{
                  String Word1=input.next();
                  String Word2=input.next();
                  int result=(Word1.toLowerCase()).compareTo(Word2.toLowerCase());
                  if (result <0){
                    System.out.println("Answer: "+ Word1 + " comes before "+Word2+" alphabetically.");
                  }
                  else if (result==0){
                    System.out.println("Answer: "+ "Chicken or Egg.");
                  }
                  else{
                    System.out.println("Answer: " + Word2 +" comes before "+Word1+" alphabetically.");
                  }



                }
                catch (InputMismatchException e){
                  System.out.println("Invalid input entered. Terminating...");
                }

              break;


      default:
            System.out.println("Invalid input entered. Terminating...");

      }
   }
}
