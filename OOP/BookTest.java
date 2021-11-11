package OOP;
import java.util.*;
import java.lang.ClassNotFoundException;
public class BookTest {
	public static void main (String args[]) {
		book bookArray [] = new book[3] ;
		
		bookArray[0] = new book("SQL Plus",50000,5);
		bookArray[1] = new book("Java 2.0",40000,3);
		bookArray[2] = new book("JSP Servlet", 60000,6);
	
		
		
		for (book Book : bookArray) {
			System.out.println(Book.toString());
			//book.showinfo();
			
		}

		System.out.println("책 가격의 합 : 150000원");
		System.out.println("할인된 책 가격의 합 : 150000원");
	

}
}
