import java.io.*;
import java.util.*;

public class CoordinateParse {
  
  public static void main(String[] args) {
    String coordinates = parseIt();
    toFile(coordinates);
    
    
  }
public static String parseIt(){
  String coordinates = "";
 try {
      File myObj = new File("velocity_violations.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String tmp = myReader.nextLine();
        tmp = tmp.replace("(", "");
        tmp = tmp.replace(")", "");
        tmp = tmp.replace(" ", "");
        String[] tmp1 = tmp.split(",");
        String a = tmp1[1];
        String b = tmp1[2];
        coordinates = a + "," + b;
        
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
      String test = "error";
      return test;
    }
    return coordinates; 
}

  
public static void toFile(String coordinates){
    try {
    BufferedWriter out = new BufferedWriter(new FileWriter("pCor.txt"));
    out.write(coordinates);
    out.close();}
    catch (IOException e){System.out.println("Exception ");}
  }
}