package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Baekjoon9237 {

    static int N;
    static Integer[] trees;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        trees = new Integer[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i < N; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(trees, Collections.reverseOrder());
        int ans = 0;
        for (int i=0; i < N; i++) {
            ans = Math.max(ans, trees[i] + i + 2);
        }
        System.out.println(ans);
    }
}
