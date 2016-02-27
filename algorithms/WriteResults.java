import java.io.*;
import java.util.*;
import java.text.*;
import java.lang.*;

public class WriteResults {
    public static void main(String[] args) {
        String filename = args[0];

        if (filename == null) {
            System.err.println("You must provide a vaild file");
            System.exit(1);
        } else{

        String line = null;

        String dir = "../simulations/";

        try {

            Date dnow = new Date();
            SimpleDateFormat ft = new SimpleDateFormat("yyyy.MM.dd_hh:mm:ss");
            String writeFile = dir + ft.format(dnow) + ".csv";

            FileWriter fileWriter = new FileWriter(writeFile);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

            bufferedWriter.write("Threads,CpuTime,UserTime,SystemTime\n");

            FileReader fileReader = new FileReader(filename);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            while ((line = bufferedReader.readLine()) != null) {
                if (line.length() < 5) {
                    continue;
                }

                if (line.substring(0,8).equals("Threads:") ) {
                    int threads = Integer.parseInt(line.substring(8));
                    String cpuTime = null;
                    String userTime = null;
                    String kernelTime = null;
                    while ((line = bufferedReader.readLine()) != null) {
                        if (line == null){
                            break;
                        }
                        else if (line.length() < 12) {
                            continue;
                        } 
                        else if (line.substring(0,4).equals("real")) {
                            cpuTime = line.substring(7,12);
                        }
                        else if (line.substring(0,4).equals("user")) {
                            userTime = line.substring(7,12);
                        }
                        else if (line.substring(0,3).equals("sys")) {
                            kernelTime = line.substring(6,11);
                            String writeLine = String.format("%d,%s,%s,%s\n", threads, cpuTime, userTime,kernelTime);
                            bufferedWriter.write(writeLine);
                            int BUFFER_SIZE = 1000;
                            bufferedReader.mark(BUFFER_SIZE);
                            String next_line = bufferedReader.readLine();
                            bufferedReader.reset();
                            if (line.length() < 12){
                                continue;
                            } else {

                                break;
                            }
                        }

                    }
                }

            }
            bufferedReader.close();
            bufferedWriter.close();

        }
        catch(FileNotFoundException ex){
            System.err.println("Unable to open file " + filename);
            System.exit(1);
        }
        catch(IOException ex) {
            System.err.println("There was a problem reading file " + filename);
            System.exit(1);
        }
        catch(Exception ex) {
            ex.printStackTrace(System.err);
            System.exit(1);
        }

    }
}

}
