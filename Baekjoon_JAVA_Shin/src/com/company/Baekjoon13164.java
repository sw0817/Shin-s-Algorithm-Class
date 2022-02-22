package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Baekjoon13164 {

    static int N, K;
    static int[] info, diff;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        info = new int[N];
        diff = new int[N-1];

        st = new StringTokenizer(br.readLine());
        info[0] = Integer.parseInt(st.nextToken());

        for (int i=1; i<N; i++) {
            info[i] = Integer.parseInt(st.nextToken());
            diff[i-1] = info[i] - info[i-1];
        }
        Arrays.sort(diff);

        int result = 0;

        for (int i=0; i<N-K; i++) {
            result += diff[i];
        }

        System.out.println(result);
    }
}
