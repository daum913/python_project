//두 개의 정수를 입력받아서 첫 번째는 후치 증가 연산자를 사용하고 
//두 번쨰는 전치 감소 연산자를 사용하여 두 수의 곱을 구한 후 각각의 값을 출력하라
//입력 예 : 10 20 , 출력 예 : 11 19 190

package java_assignmnet2;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_3 {
public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("첫 번째 정수를 입력하세요.");
	int a = scan.nextInt();
	System.out.println("두 번째 정수를 입력하세요.");
	int b = scan.nextInt();
	
	System.out.print(++a+" "+b--+" "+ ++a*b--);
	
	}
}
