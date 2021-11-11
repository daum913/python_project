//삼각형의 밑변의 길이와 높이를 입력받아 넓이를 출력하고, "Continue?"에서 하나의 문자를 입력받아
//그 문자가'Y'나 y'이면 작업를 반복하고 다른 문자이면 종료하는 프로그램을 작성하세요.

package java_loop;
import java.util.*;
import java.lang.ClassNotFoundException;
class Something{
	static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.print("삼각형의 높이 입력하세요.");
	int height = scan.nextInt() ;
	System.out.print("삼각형의 밑변의 길이를 입력하세요.");
	int width = scan.nextInt() ;
	
	System.out.print("삼각형의 넓이는 "+height*width+" 입니다.");
	
	System.out.print("Contunue?");
	String answer = scan.next(); }
}

//public class number_6 {
	//public static void main(String[] args) {
	//Something s = new Something() ;
	//Scanner scan = new Scanner(System.in);
	//System.out.print("삼각형의 높이 입력하세요.");
	//int height = scan.nextInt() ;
	//System.out.print("삼각형의 밑변의 길이를 입력하세요.");
	//int width = scan.nextInt() ;
	
	//System.out.print("삼각형의 넓이는 "+height*width+" 입니다. \nContinue?");
	//String answer = scan.next();}
	//switch (s.answer) {
	//case "y" : something
	
		
	//case "Y" :
		
	//default : 
		//break;
		//
	

