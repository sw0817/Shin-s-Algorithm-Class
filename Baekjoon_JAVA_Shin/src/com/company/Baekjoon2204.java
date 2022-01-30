package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon2204 {
    static int[] cur, result;
    static String answer, str;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int T = Integer.parseInt(br.readLine());
            if (T == 0) {
                break;
            }
            result = new int[20];
            for (int i=0; i<20; i++) {
                result[i] = 28;
            }
            for (int i=0; i<T; i++) {
                cur = new int[20];
                str = br.readLine();
                int l = str.length();
                for (int j=0; j<l; j++) {
                    char c = str.charAt(j);
                    cur[j] = (c - 'A') % 32 + 1;
                }
                for (int j=0; j<20; j++) {
                    if (result[j] < cur[j]) {
                        break;
                    } else if (result[j] > cur[j]) {
                        result = cur;
                        answer = str;
                        break;
                    }
                }
            }
            System.out.println(answer);
        }
    }
}
