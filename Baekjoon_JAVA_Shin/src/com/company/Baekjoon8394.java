package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon8394 {

    static int a = 1, b = 0, n, c, d;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        for (int i=0; i < n; i++) {
            c = (a + b) % 10;
            d = a % 10;
            a = c;
            b = d;
        }
        System.out.println(a);
    }
}
