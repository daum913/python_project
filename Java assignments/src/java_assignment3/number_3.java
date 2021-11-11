// 1번은 개 2번은 고양이 3번은 병아리로 정하고 번호를 입력받아 번호에 해당하는
//동물을 영어로 출력하는 프로그램을 작성하세요.
//해당 번호가 없으면 "I don't know"라고 출력하세요.


package java_assignment3;
import java.util.*;
import java.lang.ClassNotFoundException;

public class number_3 {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("숫자 입력하세요. ");
		int a = scan.nextInt();
		
		
	switch(a) {
	
	case 1 :
		System.out.println("dog") ;
		break ;
	case 2 : 
		System.out.println("cat") ;
		break ;
	case 3 : 
		System.out.println("chick") ;	
		break;

	default :
		System.out.println("I don't know.");
	}

	
		
	}

}
