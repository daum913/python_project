//민수와 가영이의 키와 몸무게를 입력받아 민수가 키도 크고 몸무게도 크면 1 
//그렇지 않으면 0을 출력하는 프로그램을 작성하시오.

package java_assignmnet2;
import java.util.*;
import java.lang.ClassNotFoundException;

public class number_4 {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("민수의 키를 입력하세요. ");	
	int m_height = scan.nextInt();
	System.out.println("민수의 몸무게를 입력하세요. ");	
	int m_weight = scan.nextInt();
	
	System.out.println("가영의 키를 입력하세요.");
	int k_height = scan.nextInt();
	System.out.println("가영의 몸무게를 입력하세요.");	
	int k_weight = scan.nextInt();
	

	System.out.print(m_height>k_height&m_weight>k_weight ? 1:0);
}


}
