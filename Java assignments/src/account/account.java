package account;
import java.util.* ;
import java.lang.ClassNotFoundException;
class account_1 {
 private String account;
 private int balance;
 private double intcrestRate;
 int money;

 

public account_1() {}
public account_1(String account, int balance, double intcrestRate) {
	this.account = account;
	this.balance = balance;
	this.intcrestRate = intcrestRate;}
	

	
public void setAccount(String account) {
	this.account = account ;	
}
public String getAccount(String account) {
	return account ;
}
public void setBalance(int balance) {
	this.balance = balance ;	
}
public int getBalance(int balance) {
		return balance ;
}
public void deposit(int money) {
	balance = money + balance ;
}
public void withdraw(int money) {
	balance = balance - money;
}
public void setInterestRate() {
	this.intcrestRate = intcrestRate;
}
public double getInterestRate() {
	return  intcrestRate;
}
public double CalculateInterest(double intcrestRate ) {
	return balance*intcrestRate;
}
}

public class account {
	public static void main(String[] args) {
		account_1 account_1 = new account_1("441-0290-1203",500000,7.3/100);
		System.out.println("계좌정보 : " + account_1.getAccount() + " \n현재잔액 : " + account_1.getBalance() );
		 account_1.deposit(20000) ;
		 account_1.CalculateInterest();
		 
		 System.out.println("계좌정보: " + account_1.getAccount() + "\n현재잔액: " + account_1.getBalance() );
			System.out.println("이자: " + account_1.CalculateInterest()); 
		 
		
		
	}
	
}
