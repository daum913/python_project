//년도를 입력받아 평년인지 윤년인지 구분하는 프로그램을 만들어라.

package java_assignment3;

import java.util.Scanner;
import java.lang.ClassNotFoundException;

public class number_6 {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("연도를 입력하세요.");
	int year = scan.nextInt();

		// 년/100 || 년/4 == 윤년
	if (year%100==year%4) {
		System.out.println("윤년입니다."); }
	else {
		System.out.println("평년입니다.");
	}
	}
}
