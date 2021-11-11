//남자는 m, 여자는 f, 18세 이상을 성인이라고 하자.
//성별과 나이를 입력받아 구분하여 출력하는 프로그램을 만들자.


package java_assignment3;
import java.util.* ;
import java.lang.ClassNotFoundException;
public class number_5 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("성별을 f또는 m으로 입력하세요.");
		String sex = scan.next();
		System.out.println("나이를 입력하세요.");
		int age = scan.nextInt();
		
		if (sex=="f" ) {
				if (age>=18) {
				System.out.println("성인여자");}
				else {
				System.out.println("미성년여자");}
			}
			
		else {		
			if (age>=18) {
			System.out.println("성인남자");}
			else {
			System.out.println("미성년남자");
			}
			
		}
		
				
	}

}
