//실수의 yard(야드)를 입력받아 cm(센티터)로 환산하여 입력값과 환산한 값을
//출력 예와 같이 소수 둘쩃자리에서 반올림하여 첫째자리까지 출력하는 프로그램을 작성하라.
//단 1야드 = 91.4cm
//입력은 "yard?" 라고먼저 출력하, 실수를 입력받는다. 실수는 double로 한다.

package java_assignment1;
import java.util.* ;
import java.lang.ClassNotFoundException;


public class number_5 {
public static void main(String[] args) {
	
	Scanner scan = new Scanner(System.in);
	System.out.println("yard?");
	double a = scan.nextDouble();
	double b = 91.4 * a;
	System.out.println(a+"yard = "+Math.round(b*10)/10.0+"cm");
	
}
}