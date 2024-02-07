package invoice;

public class Invoice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int Qty = 4;
		int unitPrice = 20;
		float amount = (float)Qty * (float)unitPrice;
		float total = amount;
		String line = new String(new char[25]).replace('\0', '*');
		System.out.println(line + "Adamson Computer Ltd" + line + "**");
		
		System.out.println("#99 ACS Building Gilmore Ave. New Mla.. Quezon City  * Tel. No: 123-4567");
		System.out.println("                 VAT REG. TIN 098-765-4321-0000");
		System.out.println("                          SALES INVOICE");
		System.out.println("Sold to: WALTER ONYANGO                              Date: 28/04/2020");
		System.out.println("Address: C026-01-0978/2022                           Contact Number:0100100100");
		String sums = new String(new char[70]).replace('\0', '=');
		System.out.println(sums);
		System.out.println("Qty     |    Item Description   |      Unit Price   |      Amount");
		String ton = new String(new char[70]).replace('\0', '-');
		System.out.println(sums);
		System.out.println(Qty + "       |    Pencil             |      " + unitPrice + "           |      " + amount + "0");
		System.out.println(ton);
		Qty = 10;
		unitPrice = 50;
		amount = (float)Qty * (float)unitPrice;
		total += amount;
		System.out.println(Qty + "      |    Duster             |      " + unitPrice + "           |      " + amount + "0");
		System.out.println(ton);
		Qty = 9;
		unitPrice = 30;
		amount = (float)Qty * (float)unitPrice;
		total += amount;
		System.out.println(Qty + "       |    Pens               |      " + unitPrice + "           |      " + amount + "0");
		System.out.println(ton);
		Qty = 10;
		unitPrice = 80;
		amount = (float)Qty * (float)unitPrice;
		total += amount;
		System.out.println(Qty + "      |    Crayon             |      " + unitPrice + "           |      " + amount +"0");
		System.out.println(sums);
		System.out.println("                                       |Sub Total   |" + total + "0");
		System.out.println(sums);
		System.out.println("                                       |VAT(16%)    |" + total * 0.16 + "0");
		System.out.println(sums);
		System.out.println("                                       |Total Amount|" + (total + (total * 0.16)) + "0");
		System.out.println(sums);
		
	}

}
