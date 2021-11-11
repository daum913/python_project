package mini_project;
import java.util.* ;
import java.lang.ClassNotFoundException;
import java.util.Scanner;

public class join {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		

		User[] users = new User[10];

		while(true) {
			int menu = viewMenu(scan);			
			switch(menu) {
			case 1:
				signUp(users, scan);break;
			case 2:
				login(users, scan);break;
			case 3:
				printUsers(users);break;
			case 4:

				System.out.println("종료");
				System.exit(0);
			}
		}
	}
	

	public static int viewMenu(Scanner scan) {

		int menu;
		

		do{
			//메뉴출력
			System.out.println("==================================");
			System.out.println("1. Sign Up");
			System.out.println("2. Login");
			System.out.println("3. Print All Users");
			System.out.println("4. Exit");
			System.out.println("==================================");
			System.out.print("번호: ");
	

			menu = scan.nextInt();
		}while(menu < 0 || menu > 4);


		return menu;
	}
	

	public static void signUp(User[] users, Scanner scan) {

		System.out.print("Id: ");
		String id = scan.next();
		

		System.out.print("Password: ");
		String pw = scan.next();
		

		User user = new User(id,pw);
		

		users[User.count++] = user;
	}
	

	public static void login(User[] users, Scanner scan) {

		if(User.count <= 0) {
			System.out.println("등록된 User가 없습니다.");
			return;
		}
		

		System.out.print("Id: ");
		String id = scan.next();

		System.out.print("Password: ");
		String pw = scan.next();
		

		for(int i=0; i<User.count; i++) {

			if(id.equals(users[i].userId) && pw.equals(users[i].password)) {
				System.out.println("로그인 성공");
				return;
			}
		}
		System.out.println("로그인 실패");
	}
	

	public static void printUsers(User[] users) {

		for(int i=0; i<User.count; i++)
			System.out.println("{ "+users[i].userId+", "+users[i].password+" }");
	}
}

class User{
	String userId, password;
	static int count;
	
	public User(String userId, String password) {
		this.userId = userId;
		this.password = password;
	}
}