package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Baekjoon1041 {

    static long N, sum, min1, min2, min3, max;
    static long[] dice, minSum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Long.parseLong(br.readLine());
        sum = 0;
        max = 0;
        dice = new long[6];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<6; i++) {
            dice[i] = Long.parseLong(st.nextToken());
            sum += dice[i];
            max = Math.max(max, dice[i]);
        }
        minSum = new long[3];
        minSum[0] = Math.min(dice[0], dice[5]);
        minSum[1] = Math.min(dice[1], dice[4]);
        minSum[2] = Math.min(dice[2], dice[3]);
        Arrays.sort(minSum);
        min1 = minSum[0];
        min2 = min1 + minSum[1];
        min3 = min2 + minSum[2];
        if (N == 1) {
            System.out.println(sum - max);
        } else {
            long n1 = 4 * (N - 2) * (N - 1) + (long)Math.pow(N-2, 2);
            long n2 = 4 * (N - 2) + (N - 1) * 4;
            long n3 = 4;

            System.out.println(min1 * n1 + min2 * n2 + min3 * n3);
        }
    }
}
