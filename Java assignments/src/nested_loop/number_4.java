//자연수 n을 입력받아 n줄만큼 다음과 같이 출력하는 프로그램을 작성하시오.
package nested_loop;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_4 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("자연수를 입력하세요.");
		int n = scan.nextInt();
		for(int i=1; i<=n; i++) {
			for(int x=1; x<=i; x++) {
				System.out.print("*");
			}
			System.out.println();
			;
		}
		
	}
}
