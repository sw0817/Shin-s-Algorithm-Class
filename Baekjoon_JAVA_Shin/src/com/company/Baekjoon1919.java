package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon1919 {

    static int[] first, second;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        first = new int[26];
        second = new int[26];
        String string = br.readLine();
        for (int i=0; i<string.length(); i++) {
            first[(int)string.charAt(i) - 97]++;
        }
        string = br.readLine();
        for (int i=0; i<string.length(); i++) {
            second[(int)string.charAt(i) - 97]++;
        }
        int result = 0;
        for (int i=0; i<26; i++) {
            result += Math.abs(first[i] - second[i]);
        }
        System.out.println(result);
    }
}
