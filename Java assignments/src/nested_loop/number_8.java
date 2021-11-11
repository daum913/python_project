//자연수n을 입력받아 출력 예와 같이 공백으로 구분하여 출력되는 프로그램을 작성하시오.
//주의 : 숫자는 공백으로 구분하되 줄 사이에 빈줄은 없다.
package nested_loop;
import java.util.*;
public class number_8 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("자연수를 입력하세요 : ");
		int x = scan.nextInt();
		
		int y = 1;
		
		for (int a=0; a<x; a++) {
			for (int b=0; b<=x-a-1; b++) {
				System.out.print(" "); }
				for(int b=0; b<=x-a-1;b++) {
					System.out.print(y++ + " ");
				}
				System.out.println();
		}
			}
		
	}
