
// import java.io.*;
// import java.util.*;

// public class PassOne {
//     Hashtable<String, MnemonicTable> is = new Hashtable<>();
//     ArrayList<String> symtab = new ArrayList<>();
//     ArrayList<Integer> symaddr = new ArrayList<>();
//     ArrayList<String> littab = new ArrayList<>();
//     ArrayList<Integer> litaddr = new ArrayList<>();
//     ArrayList<Integer> pooltab = new ArrayList<>();
//     int LC = 0;

//     public void createIS() {
//         MnemonicTable m = new MnemonicTable("STOP", "00", 0);
//         is.put("STOP", m);
//         m = new MnemonicTable("ADD", "01", 0);
//         is.put("ADD", m);
//         m = new MnemonicTable("SUB", "02", 0);
//         is.put("SUB", m);
//         m = new MnemonicTable("MULT", "03", 0);
//         is.put("MULT", m);
//         m = new MnemonicTable("MOVER", "04", 0);
//         is.put("MOVER", m);
//         m = new MnemonicTable("MOVEM", "05", 0);
//         is.put("MOVEM", m);
//         m = new MnemonicTable("COMP", "06", 0);
//         is.put("COMP", m);
//         m = new MnemonicTable("BC", "07", 0);
//         is.put("BC", m);
//         m = new MnemonicTable("DIV", "08", 0);
//         is.put("DIV", m);
//         m = new MnemonicTable("READ", "09", 0);
//         is.put("READ", m);
//         m = new MnemonicTable("PRINT", "10", 0);
//         is.put("PRINT", m);
//     }

//     public void generateIC() throws Exception {
//         BufferedWriter wr = new BufferedWriter(new FileWriter("intermediate.txt"));
//         BufferedReader br = new BufferedReader(new FileReader("input.txt"));
//         String line = " ";
//         pooltab.add(0, 0);
//         while ((line = br.readLine()) != null) {
//             String[] split = line.split("\\s+");
//             if (split[0].length() > 0) {
//                 // it is a label
//                 if (!symtab.contains(split[0])) {
//                     symtab.add(split[0]);
//                     symaddr.add(LC);
//                 } else {
//                     int index = symtab.indexOf(split[0]);
//                     symaddr.remove(index);
//                     symaddr.add(index, LC);
//                 }
//             }
//             if (split[1].equals("START")) {
//                 LC = Integer.parseInt(split[2]);
//                 wr.write("(AD,01)(C," + split[2] + ") \n");
//             } else if (split[1].equals("ORIGIN")) {
//                 if (split[2].contains("+") || split[2].contains("-")) {
//                     LC = getAddress(split[2]);
//                 } else {
//                     LC = symaddr.get(symtab.indexOf(split[2]));
//                 }
//             } else if (split[1].equals("EQU")) {
//                 int addr = 0;
//                 if (split[2].contains("+") || split[2].contains("-")) {
//                     addr = getAddress(split[2]);
//                 } else {
//                     addr = symaddr.get(symtab.indexOf(split[2]));
//                 }
//                 if (!symtab.contains(split[0])) {
//                     symtab.add(split[0]);
//                     symaddr.add(addr);
//                 } else {
//                     int index = symtab.indexOf(split[0]);
//                     symaddr.remove(index);
//                     symaddr.add(index, addr);
//                 }
//             } else if (split[1].equals("LTORG") || split[1].equals("END")) {
//                 if (litaddr.contains(0)) {
//                     for (int i = pooltab.get(pooltab.size() - 1); i < littab.size(); i++) {
//                         if (litaddr.get(i) == 0) {
//                             litaddr.remove(i);
//                             litaddr.add(i, LC);
//                             LC++;
//                         }
//                     }
//                     if (!split[1].equals("END")) {
//                         pooltab.add(littab.size());
//                         wr.write("(AD,05) \n");
//                     } else
//                         wr.write("(AD,04) \n");
//                 }
//             } else if (split[1].contains("DS")) {
//                 LC += Integer.parseInt(split[2]);
//                 wr.write("(DL,01) (C," + split[2] + ") \n");
//             } else if (split[1].equals("DC")) {
//                 LC++;
//                 wr.write("(DL,02) (C," + split[2].replace("'", "").replace("'", "") + ") \n");
//             } else if (is.containsKey(split[1])) {
//                 wr.write("(IS," + is.get(split[1]).opcode + ") ");
//                 if (split.length > 2 && split[2] != null) {
//                     String reg = split[2].replace(",", "");
//                     if (reg.equals("AREG")) {
//                         wr.write("(1) ");
//                     } else if (reg.equals("BREG")) {
//                         wr.write("(2) ");
//                     } else if (reg.equals("CREG")) {
//                         wr.write("(3) ");
//                     } else if (reg.equals("DREG")) {
//                         wr.write("(4) ");
//                     } else {
//                         if (symtab.contains(reg)) {
//                             wr.write("(S," + symtab.indexOf(reg) + ") ");
//                         } else {
//                             symtab.add(reg);
//                             symaddr.add(0);
//                             wr.write("(S," + symtab.indexOf(reg) + ") ");
//                         }
//                     }
//                 }
//                 if (split.length > 3 && split[3] != null) {
//                     if (split[3].contains("=")) {
//                         String norm = split[3].replace("=", "").replace("'", "").replace("'", "");
//                         if (!littab.contains(norm)) {
//                             littab.add(norm);
//                             litaddr.add(0);
//                             wr.write("(L," + littab.indexOf(norm) + ") \n");
//                         } else {
//                             wr.write("L," + littab.indexOf(norm) + ") \n");
//                         }
//                     } else if (symtab.contains(split[3])) {
//                         wr.write("(S," + symtab.indexOf(split[3]) + ")");
//                     } else {
//                         symtab.add(split[3]);
//                         symaddr.add(0);
//                         wr.write("(S," + symtab.indexOf(split[3]) + ")");
//                     }
//                 }
//                 LC++;
//             }
//         }
//         wr.flush();
//         wr.close();
//         BufferedWriter br1 = new BufferedWriter(new FileWriter("symtab.txt"));
//         BufferedWriter br2 = new BufferedWriter(new FileWriter("littab.txt"));
//         BufferedWriter br3 = new BufferedWriter(new FileWriter("pool.txt"));
//         for (int i = 0; i < symtab.size(); i++)
//             br1.write(symtab.get(i) + " " + symaddr.get(i) + "\n");
//         for (int i = 0; i < littab.size(); i++)
//             br2.write(littab.get(i) + " " + litaddr.get(i) + "\n");
//         for (int i = 0; i < pooltab.size(); i++)
//             br3.write(pooltab.get(i) + "\n");
//         br1.flush();
//         br2.flush();
//         br3.flush();
//         br1.close();
//         br2.close();
//         br3.close();
//     }

//     private int getAddress(String string) {
//         int temp = 0;
//         if (string.contains("+")) {
//             String sp[] = string.split("\\+");
//             int ad = symaddr.get(symtab.indexOf(sp[0]));
//             temp = ad + Integer.parseInt(sp[1]);
//         } else if (string.contains("-")) {
//             String sp[] = string.split("\\-");
//             int ad = symaddr.get(symtab.indexOf(sp[0]));
//             temp = ad - Integer.parseInt(sp[1]);
//         }
//         return temp;
//     }

//     public static void main(String[] args) throws Exception {
//         PassOne p = new PassOne();
//         p.createIS();
//         p.generateIC();
//     }
// }

import java.io.*;
import java.util.*;

class Pass2 {
    public static void main(String[] Args) throws IOException {
        BufferedReader b1 = new BufferedReader(new FileReader("intermediate.txt"));
        BufferedReader b2 = new BufferedReader(new FileReader("symtab.txt"));
        BufferedReader b3 = new BufferedReader(new FileReader("littab.txt"));
        FileWriter f1 = new FileWriter("Pass2.txt");
        HashMap<Integer, String> symSymbol = new HashMap<Integer, String>();
        HashMap<Integer, String> litSymbol = new HashMap<Integer, String>();
        HashMap<Integer, String> litAddr = new HashMap<Integer, String>();
        String s;
        int symtabPointer = 1, littabPointer = 1, offset;
        while ((s = b2.readLine()) != null) {
            String word[] = s.split("\t");
            symSymbol.put(symtabPointer++, word[1]);
        }
        while ((s = b3.readLine()) != null) {
            String word[] = s.split("\t");
            litSymbol.put(littabPointer, word[0]);
            litAddr.put(littabPointer++, word[1]);
        }
        while ((s = b1.readLine()) != null) {
            if (s.substring(1, 6).compareToIgnoreCase("IS,00") == 0) {
                f1.write("+ 00 0 000\n");
            } else if (s.substring(1, 3).compareToIgnoreCase("IS") == 0) {
                f1.write("+ " + s.substring(4, 6) + " ");
                if (s.charAt(9) == ')') {
                    f1.write(s.charAt(8) + " ");
                    offset = 3;
                } else {
                    f1.write("0 ");
                    offset = 0;
                }
                if (s.charAt(8 + offset) == 'S')
                    f1.write(symSymbol.get(Integer.parseInt(s.substring(10 + offset, s.length() - 1))) +
                            "\n");
                else
                    f1.write(litAddr.get(Integer.parseInt(s.substring(10 + offset, s.length() - 1))) + "\n");
            } else if (s.substring(1, 6).compareToIgnoreCase("DL,01") == 0) {
                String s1 = s.substring(10, s.length() - 1), s2 = "";
                for (int i = 0; i < 3 - s1.length(); i++)
                    s2 += "0";
                s2 += s1;
                f1.write("+ 00 0 " + s2 + "\n");
            } else {
                f1.write("\n");
            }
        }
        f1.close();
        b1.close();
        b2.close();
        b3.close();
    }
}