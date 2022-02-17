package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon1614 {

    static long f, N, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        f = Integer.parseInt(br.readLine());
        N = Integer.parseInt(br.readLine());

        if (f == 1) {
            result = N * 8;
        } else if (f == 2) {
            result = 1 + N / 2 * 8 + (N % 2) * 6;
        } else if (f == 3) {
            result = 2 + N / 2 * 8 + (N % 2) * 4;
        } else if (f == 4) {
            result = 3 + N / 2 * 8 + (N % 2) * 2;
        } else {
            result = N * 8 + 4;
        }
        System.out.println(result);
    }
}
