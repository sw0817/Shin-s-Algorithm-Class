package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon1332 {

    static int N, V, result;
    static int[] interest;
    static boolean alwaysInterest = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());
        interest = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i < N; i++) {
            interest[i] = Integer.parseInt(st.nextToken());
        }
        result = Integer.MAX_VALUE;
        check(0, interest[0], interest[0], 1);
        if (alwaysInterest) {
            result = N;
        }
        System.out.println(result);
    }

    static void check(int idx, int max, int min, int cnt) {
        if (idx == N) {
            result = Math.min(result, cnt-1);
            return;
        }

        max = Math.max(max, interest[idx]);
        min = Math.min(min, interest[idx]);

        if (V <= max - min || idx+1 == N) {
            result = Math.min(result, cnt);
            if (V <= max - min) {
                alwaysInterest = false;
            }
            return;
        }

        if (idx + 1 < N && interest[idx+1] < min || idx + 1 < N && max < interest[idx+1]) {
            check(idx+1, max, min, cnt+1);
        }

        if (idx + 2 <= N) {
            check(idx + 2, max, min, cnt+1);
        }
    }
}