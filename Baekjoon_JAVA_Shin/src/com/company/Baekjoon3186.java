package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon3186 {
    static int K, L, N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        String info = br.readLine();
        int t1 = 0;
        int t2 = 0;
        boolean ready = false;
        boolean flush = false;
        for (int i=0; i<N; i++) {
            int cur = info.charAt(i) - '0';
            if (cur == 1) {

                t1 += 1;
            }
        }
    }
}

// 아직 미완성
