//행과 열의 수를 입력받아 다음과 같이 출력하는 프로그램을 작성하세요.

package nested_loop;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_3 {
public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.print("행의 수를 입력하세요. : ");
	int n = scan.nextInt();
	System.out.print("열의 수를 입력하세요. : ");
	int m = scan.nextInt();
	
	for(int i = 1; i<=n; i++) {

		for (int j = 1; j<=m; j++) {
		System.out.print(i*j+" ");
	}
		System.out.print( " \n");
}
	
	

}

}
