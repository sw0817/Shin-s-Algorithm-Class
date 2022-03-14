package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Baekjoon1484 {

    static int G, l, r;
    static int[] P, Q;
    static ArrayList<Integer> answer = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        G = Integer.parseInt(br.readLine());
        P = new int[100000];
        Q = new int[100000];
        for (int i=0; i<100000; i++) {
            P[i] = i+1;
            Q[i] = i+1;
        }
        l = 0;
        r = 0;
        while (l < 100000 && r < 100000) {
            int tmp = (P[l] + Q[r]) * (P[l] - Q[r]);
            if (tmp == G) {
                answer.add(P[l]);
            }
            if (tmp < G) {
                l++;
                continue;
            }
            r++;
        }
        if (answer.size() == 0) {
            System.out.println(-1);
        } else {
            for (Integer integer : answer) {
                System.out.println(integer);
            }
        }
    }
}
