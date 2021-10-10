package com.company;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon21758 {

    static int N, result;
    static int[] info, prefixSum;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        info = new int[N];
        for (int i=0; i < N; i++) {
            info[i] = Integer.parseInt(st.nextToken());
        }

        prefixSum = new int[N+1];
        for (int i=1; i < N+1; i++) {
            prefixSum[i] += prefixSum[i-1] + info[i-1];
        }

        result = 0;
        // 경우의 수

        // 1. 양쪽 끝 벌 중앙 벌집
        // 양쪽 끝 뺀 누접합 + 벌집
        int center = prefixSum[N-1] - info[0];
        for (int i=1; i < N-1; i++) {
            result = Math.max(result, center + info[i]);
        }

        // 2. 양쪽 끝 벌집
        // 반대 편 벌 확정 + 나머지 벌 위치 조정
        // 2-1. 왼쪽 벌집
        // 2-2. 오른쪽 벌집
        int leftPrefixSum = center + info[0];
        int rightPrefixSum = center + info[N-1];
        for (int i=1; i < N-1; i++) {
            result = Math.max(result, leftPrefixSum - info[i] + prefixSum[i]);
            result = Math.max(result, rightPrefixSum - info[i] + prefixSum[N] - prefixSum[i+1]);
        }
        System.out.println(result);
    }
}
