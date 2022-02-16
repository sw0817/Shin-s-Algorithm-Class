package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon1100 {

    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i=0; i<8; i++) {
            String row = br.readLine();
            for (int j=0; j<8; j++) {
                if (row.charAt(j) == 'F' && (i+j) % 2 == 0) {
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}