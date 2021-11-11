// 세 개의 정수를 입력 받아서 첫 번째 수가 가장 크면 1 아니면 0을 출력하고
// 세 개의 수가 모두 같으면 1 아니면 0을 출력하는 프로그램을 작성하시오.
//(JAVA는 1이면 true, 0이면 false를 출력한다.)

package java_assignmnet2;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_2 {
public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("첫 번쨰 정수를 입력하세요. ");
	int a = scan.nextInt();
	System.out.println(" 번쨰 정수를 입력하세요. ");
	int b = scan.nextInt();
	System.out.println("첫 번쨰 정수를 입력하세요. ");
	int c = scan.nextInt();
	
	
	System.out.print((a>b&a>c ? 1:0));
	System.out.print((a==b&b==c ? 1:0));
		
	}
	
};