
//0이 입력될 때 까지 정수를 계속 입력받아 3의 배수와 5의 배수를 제외한 수들의 개수를 출력허시오.
package java_loop;
import java.util.* ;
import java.lang.ClassNotFoundException;
public class number_5 {
	@SuppressWarnings("removal")
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	ArrayList <Integer> list = new ArrayList<Integer>();
    while(true) { 
        System.out.print("정수를 입력하세요. "); 
        int n = scan.nextInt();
        if (n==0) {break;}
        
        else if (n%3!=0 & n%5!=0) {
        	list.add(n);

        }
       
			
        	}
    
    System.out.println(list.size()+" 개");
		
	}

	
    }
