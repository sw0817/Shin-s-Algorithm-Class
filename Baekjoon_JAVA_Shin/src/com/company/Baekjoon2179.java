package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon2179 {

    static int N, l, max;
    static String[] strings;
    static String S, T;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        strings = new String[N];
        for (int i=0; i<N; i++) {
            strings[i] = br.readLine();
        }
        max = 0;
        for (int i=0; i<N; i++) {
            for (int j=i+1; j<N; j++) {
                l = 0;
                for (int k=0; k<Math.min(strings[i].length(), strings[j].length()); k++) {
                    if (strings[i].charAt(k) == strings[j].charAt(k)) {
                        l++;
                    } else {
                        break;
                    }
                }
                if (max < l) {
                    max = l;
                    S = strings[i];
                    T = strings[j];
                }
            }
        }
        System.out.println(S);
        System.out.println(T);
    }
}
