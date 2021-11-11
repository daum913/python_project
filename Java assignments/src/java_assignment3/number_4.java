//1-12사이의 정수를 입력받아 평년의 경우 입력받은 해당 월의 날수를 출력하는 프로그램을 작성하시오.



package java_assignment3;
import java.util.* ;
import java.lang.ClassNotFoundException;
public class number_4 {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("연도를 입력하세요.");
	int year = scan.nextInt();
	System.out.println("1부터 12 사이의 정수를 입력하세요.");
	int month = scan.nextInt();
	
	// 년/100 || 년/4 == 윤년
if (year%100==year%4) {
	System.out.println("윤년입니다."); }

else
{
	
	switch(month) {
	
	case 1 :
		System.out.println(31) ;
		break ;
	case 2 : 
		System.out.println(28) ;
		break ;
	case 4 : 
		System.out.println(30) ;	
	case 6 :
		System.out.println(30) ;	
	case 9 :
		System.out.println(30) ;	
		break ;
	case 11 : 
		System.out.println(30) ;	
		break;
	default :
		System.out.println(31) ;
	

};
}

}
	}
