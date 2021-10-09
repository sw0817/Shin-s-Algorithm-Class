package com.company;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Baekjoon1620 {

    static int N, M;
    static String[] poketmons;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        poketmons = new String[N];
        List poketmonsIndex = Arrays.asList(poketmons);
        for (int i=0; i < N; i++) {
            poketmons[i] = br.readLine();
        }
        for (int i=0; i < M; i++) {
            String info = br.readLine();
            int type = (int)info.charAt(0);
            if (49 <= type && type < 58) {
                System.out.println(poketmons[Integer.parseInt(info) - 1]);
            } else {
                System.out.println(poketmonsIndex.indexOf(info) + 1);
            }
        }
    }
}
