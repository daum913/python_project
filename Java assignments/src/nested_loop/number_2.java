//2부터 9까지의 수 중 2개를 입력받아 입력받은 수 사이의 구구단을 출력하는 프로그램을 작성하시오.
// 반드시 먼저 입력된 수의 구구단부터 아래의 형식에 맞게 출력하여야 한다.

package nested_loop;
import java.util.*;
import java.lang.ClassNotFoundException;
public class number_2 {
	public static void main(String[] args) {
Scanner scan = new Scanner(System.in);
System.out.print("2부터 9까지의 수를 입력하세요.");
int n = scan.nextInt();

System.out.print("2부터 9까지의 수를 입력하세요.");
int n_2 = scan.nextInt();

if (n>=n_2) {
	for(int g = 1; g<=9; g++) {
for(int i = n; i>= n_2; i--) {
	System.out.println(g+"   x   "+i+"   =   "+g*i);
}
System.out.println();
}
	}

else {
for(int g = 1; g <=9; g++ ) {
	for(int i = n; i<=n_2; i++) {
		System.out.println(i+"   x   "+g+"   =   "+g*i);
	}
	System.out.println();
}
}

	scan.close();
	
	}
}
