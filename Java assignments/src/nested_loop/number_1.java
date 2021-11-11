//자연수 n을 입력받고 1부터 홀수를 차례대로 더해나가면서 합이 n이상이면 그 떄 까지 더해진
//홀수의 개수와 그 합을 출력하는 프로그램을 작성하시오.
package nested_loop;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_1 {
	public static void main(String[] args) {

	Scanner scan = new Scanner(System.in) ;
	System.out.print("자연수를 입력하세");
	int n = scan.nextInt();
	int sum = 0 ; int count =0;
	
	for(int i=1; sum<n ; i++){
		if(i%2==1) {
			sum+=i;
			count++;
		}
	
	System.out.printf("d% ,d%" ,sum,count);
		
	}
}
}