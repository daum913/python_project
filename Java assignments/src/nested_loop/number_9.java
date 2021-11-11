package nested_loop;
import java.util.*;
public class number_9 {
	public static void main(String[] args) {
		Scanner scan = new Scanner (System.in);
		System.out.print("자연수를 입력하세요 ");
		int a = scan.nextInt();
		int b= 1 ;
		
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < a; j++) {
				System.out.print(b+" ");
				b=(b+2) % 10 ;
			}
			System.out.println();
		}
		
		
		
	}

}
