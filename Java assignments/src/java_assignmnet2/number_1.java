//두 개의 정수를 입력받아서 다음과 같이 4가지 관계연산자의 결과를 출력하시오.
//이 때, 입력받은 두 정수를 이용하여 출력하시오.
//Java는 1이면 true, 0이면 false를 출력한다.


package java_assignmnet2;
import java.util.*;
import java.lang.ClassNotFoundException;


public class number_1 {
public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("첫 번쨰 정수를 입력하세요. ");
	int a = scan.nextInt();
	System.out.println("두 번째 정수를 입력하세요. ");
	int b = scan.nextInt();

	System.out.println(a+" > "+b+" --- "+(a>b ? 1:0));
	System.out.println(a+" < "+b+" --- "+(a<b ? 1:0));
	System.out.println(a+" >= "+b+" --- "+(a>=b ? 1:0));
	System.out.println(a+" <= "+b+" --- "+(a<=b ? 1:0));
	
	
	
}
}