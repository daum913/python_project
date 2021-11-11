//100이하 양의 정수만 입력한다.
//while 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력하는 프로그램을 작성.

package java_loop;
import java.util.Scanner;
import java.lang.ClassNotFoundException;
import java.util.*;
public class number_4 {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("100이하의 양의 정수만 입력하세요.");
	int num = scan.nextInt();
	int sum = 0 ; 
	int num_2 = 0 ;
	
	while (num_2<= num) {
		sum += num_2 ;
		num_2++ ;
	System.out.println("1부터 "+num+"까지의 합은 "+sum+"입니다.");
	}
	
	}

}
