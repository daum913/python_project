//영문 대문자를 입력받아 'A'이면  Excellent, 'B'이면 GOod, 'c'이면 Usually
//'d'이면 effort, 'f' 이면 Failure, 그 외 문자이면 error 라고 출력하시오.


package java_assignment3;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_2 {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("영문 대문자를 입력하세요. ");
		String a = scan.next();
		
		
	switch(a) {
	
	case "A" :
		System.out.println("Excellent") ;
		break ;
	case "B" : 
		System.out.println("Good") ;
		break ;
	case "C" : 
		System.out.println("Usually") ;
		break ;
	case "D" : 
		System.out.println("Effort") ;
		break ;
	case "F" : 
		System.out.println("Failure") ;
		break ;
		
	default :
		System.out.println("Error") ;
		
	}

	
		
	}

}
