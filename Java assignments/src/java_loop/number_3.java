//한 개의 자연수를 입력받아 그 수의 배수를 차례로 10개 출력하는 프로그램을 작성.

package java_loop;
import java.util.* ;
import java.lang.ClassNotFoundException;
public class number_3 {
public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("자연수를 입력하세요. ");
	int num = scan.nextInt();
	for (int a = 1; a<= 10; a++) {
		
		System.out.println(num * a );
		
	}

	
	
}
	

}
