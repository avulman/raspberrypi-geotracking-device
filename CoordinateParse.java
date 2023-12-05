import java.io.*;
import java.util.*;

public class Coordinate {
  public static void main(String[] args) {
    String coordinates;
    String filePath;
    filePath = args[0];
    parseIt(filePath);
    
    
  }
public static void parseIt(String filePath){
 try {
      File myObj = new File("Coordinate.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String tmp = myReader.nextLine();
        tmp = tmp.replace("(", "");
        tmp = tmp.replace(")", "");
        tmp = tmp.replace(" ", "");
        String[] tmp1 = tmp.split(",");
        String a = tmp1[1];
        String b = tmp2[2];
        DecimalFormat df = new DecimalFormat("#.####");
        double c = Double.parseDouble(df.format(a));
        double d = Double.parseDouble(df.format(b));
        coordinates = c + "," + d; 
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
}

  
public static void toFile(){
    BufferedWriter out = new BufferedWriter(new FileWriter("pCor.txt"));
    try {
    out.write(coordinates);}
    catch (IOException e){System.out.println("Exception ");}
    finally{
    out.close();
    }
  }
}