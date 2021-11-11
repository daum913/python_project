//100이하의 정수를 입력받아서 입력받은 정수부터 100까지의 합을 출력하는 프로그램을 작성.

package java_loop;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_2 {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("100이하의 양의 정수만 입력하세요.");
	int num = scan.nextInt();
	int num_2 = 100, sum = 0 ;
	while(num <= num_2) {
		sum += num ;
		num++;
		}
	System.out.println(num-2+"부터 100 까지의 합은 "+sum+"입니다.");
	
		
	
		
	};

}
