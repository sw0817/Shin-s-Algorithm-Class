package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon1871 {

    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; i++) {
            String info = br.readLine();
            int front = 0;
            int back = 0;
            for (int j=0; j<3; j++) {
                front += (info.charAt(j) - 'A') * Math.pow(26, 2-j);
            }
            for (int j=4; j<8; j++) {
                back += (info.charAt(j) - '0') * Math.pow(10, 7-j);
            }
            if (Math.abs(front - back) <= 100) {
                System.out.println("nice");
            } else {
                System.out.println("not nice");
            }
        }
    }
}
