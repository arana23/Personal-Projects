import java.util.*;
class personalfinance_track {
Map<String, Integer> im = new HashMap<String, Integer>(); 
Map<String, Integer> hm = new HashMap<String, Integer>(); 

  public void display_menu() {
    System.out.println ( "1) Enter Expense\n2) Enter Income\n3) Print total" );
    System.out.print ( "Selection: " );
  }

  public void enter_expense(){
    Scanner sc= new Scanner(System.in);
    System.out.println("Please select the subcategory of your expenseive: (Food, Shopping, Personal)");
    String name = sc.nextLine();
    System.out.println("Please enter the expensive amount as a decimal value: ");
    double val = sc.nextDouble();
    if(hm.containsKey(name)){
      double temp = hm.get(name);
      hm.put(name,temp+val);
    }
    else{
      hm.put(name,val);
    }

    public void enter_income(){
    Scanner sc= new Scanner(System.in);
    System.out.println("Please select the means of your income: (Work, Gift, etc.)");
    String name = sc.nextLine();
    System.out.println("Please enter the income amount as a decimal value: ");
    double val = sc.nextDouble();
    if(im.containsKey(name)){
      double temp = im.get(name);
      im.put(name,temp+val);
    }
    else{
      im.put(name,val);
    }
  }

  public void print_vals(){
    System.out.println("Income:");
    for (Map.Entry<String, Integer> entry : im.entrySet()) {
            String k = entry.getKey();
            int v = entry.getValue();
            System.out.println("Key: " + k + ", Value: " + v);
        }
    System.out.println("Expenses: ");
    for (Map.Entry<String, Integer> entry : hm.entrySet()) {
            String k = entry.getKey();
            int v = entry.getValue();
            System.out.println("Key: " + k + ", Value: " + v);
        }
  }

  public personalfinance_track() {
    Scanner in = new Scanner ( System.in );
    
    display_menu();
    switch ( in.nextInt() ) {
      case 1:
        System.out.println ( "You picked Enter Expense" );
        enter_expense();
        break;
      case 2:
        System.out.println ( "You picked option 2" );
        enter_income();
        break;
      case 3:
        System.out.println ( "You picked option 3" );
        break;
      default:
        System.err.println ( "Unrecognized option" );
        break;
    }
  }
  
  public static void main ( String[] args ) {
    new personalfinance_track();
  }
}