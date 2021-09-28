package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon2417 {

    static long n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Long.parseLong(br.readLine());
        if ((long)Math.sqrt(n) < n) {
            System.out.println((long)Math.sqrt(n) + 1);
        } else {
            System.out.println((long)Math.sqrt(n));
        }
    }
}
