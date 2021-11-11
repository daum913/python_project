//세 개의 정수를 입력받아 합과 평균을 출력하는 프로그램을 작성하시오.
//(단, 평균은 소수 이하를 버림하여 정수 부분만 출력한다.)
//입력 예 20 50 100
//출력 예 sum = 170 avg = 50
package java_assignment1;

import java.util.* ;
import java.lang.ClassNotFoundException;
public class number_4 {
public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.print("정수를 입력하세요.");
	int a = scan.nextInt();
	
	System.out.print("두 번째 정수를 입력하세요.");
	int b = scan.nextInt();
	
	System.out.print("세 번째 정수를 입력하세요.");
	int c = scan.nextInt();
	
	System.out.println("sum = "+(a+b+c));
	System.out.println("avg = "+(a+b+c)/3);
	scan.close();
	}
}
