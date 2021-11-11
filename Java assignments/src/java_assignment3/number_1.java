// 정수를 입력받아 0이면 "zero" 양수아면 "plus" 음수이면 "minus" 


package java_assignment3;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_1 {
public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("정수를 입력하세요. ");
	int a = scan.nextInt() ;
	
	
	if (a==0) {
	System.out.println("zero");}
	
	else if(a>0) {
		
	System.out.println("plus");}
	
	else  
	{
	System.out.println("minus");
	}
	
	
	
	}
	
}
