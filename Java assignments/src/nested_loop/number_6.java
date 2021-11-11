//1부터 100까지의 정수 중 한 개를 입력받아 100보다 작은 배수들을 차례로 출력하다가
//10의 배수가 출력되면 프로그램을 종료하도록 프로그램을 작성하시오.

package nested_loop;
import java.util.*;

public class number_6 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("자연수 입력하세요 : ");
		int a = scan.nextInt();
		
		for(int i=1;i<20; i++ ) {
			if (i*a>=100) {
				break;
			}
			else if ((i*a)%10==0) {
			System.out.print(i*a);
				break;
			}
			System.out.print(i*a+" ");
		}
		
	}
	
	

}
