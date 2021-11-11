//자연수 n을 입력받아 "출력 예"와 같이 공백으로 구분하여 출력하는 프로그램을 작성하시오.
//주의 : 숫자를 공백으로 구분하되 줄사이에 빈줄은 없다.

package nested_loop;
import java.util.*;
public class number_7 {
public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.print("자연수 n을 입력하세요.");
	int n = scan.nextInt();
	for (int a=0 ; a<n; a++) {
		int b=1;
	
		for(int c=0; c<n-1-a; c++) {
			System.out.print(" ");
	}
		for(int c=0; c<a+1; c++) {
			System.out.print(b++ + " ");
			
		}
		System.out.println();
	
}
	
}
}
