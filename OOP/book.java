package OOP;
import java.util.*;
import java.lang.ClassNotFoundException;
public class book{
	
	private String bookName ;
	private int bookPrice ;
	private double bookDiscountRate;
	

	
	public book() {}
	public book(String bookName, int bookPrice, double bookDiscountRate) {
		
		this.bookName = bookName ;
		this.bookPrice = bookPrice ;
		this.bookDiscountRate = bookDiscountRate ;
			
		}
	
 
 
 
public String getbookName() {
	return bookName;
}
public void setBookName(String bookName) {
	this.bookName = bookName ;
}

public int getBookPrice() {
	//System.out.println(bookPrice+"");
	return bookPrice;
}
public void setBookPrice(int bookPrice) {
	this.bookPrice = bookPrice ;
}
public double getBookDiscountRate() {
	//System.out.println(bookDiscountRate+"%");
	return bookDiscountRate;
}
public void setBookDiscountRate(double bookDiscountRate) {
	this.bookDiscountRate= bookDiscountRate;
}


@Override

	public String toString() {

		return this.bookName+" "+this.bookPrice+"원 "+this.bookDiscountRate+"%";

}


//bookDiscountRate = bookDiscountRate.toString ;
//bookPrice = bookPrice.toString ;
//bookName = bookName.toString ;
public static void showinfo() {
	// TODO Auto-generated method stub
	
}
}
