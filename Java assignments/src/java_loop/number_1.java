//100이하의 양의 정수만 입력한다.
//while문을 이용하여 1부터 입력받은 정수까지의 합을 구하는 프로그럄을 작성하라.

package java_loop;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_1 {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("100이하의 양의 정수만 입력하세요.");
	int num = scan.nextInt();
	int num_2 = 1, sum = 0 ;
	while(num_2 < num) {
		sum += num_2 ;
		num_2++;
		}

	
		
	System.out.println("1부터 "+num_2+"까지의 합은 "+(sum+num)+"입니다.");
		
	};

}
