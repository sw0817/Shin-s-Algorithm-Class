package com.company;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Baekjoon1700 {

    static int N, K;
    static int[] info, cntInfo;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        info = new int[K];
        cntInfo = new int[K+1];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i < K; i++) {
            info[i] = Integer.parseInt(st.nextToken());
            cntInfo[info[i]]++;
        }
        List<Integer> list = new ArrayList<>();
        int result = 0;

        for (int i=0; i < K; i++) {
            cntInfo[info[i]]--;
            if (list.contains(info[i])) {
                continue;
            }
            if (list.size() >= N) {
                result++;
                boolean flag = false;
                for (int j=0; j < list.size(); j++) {
                    if (cntInfo[list.get(j)] <= 0) {
                        list.remove(new Integer(list.get(j)));
                        flag = true;
                        break;
                    }
                }
                if (!flag) {
                    boolean [] b = new boolean[N];
                    int check = N;
                    loop:{
                        for (int j=i+1; j < K; j++) {
                            for (int k=0; k < N; k++) {
                                if (list.get(k) == info[j] && !b[k]) {
                                    b[k] = true;
                                    check--;
                                    if (check == 0) {
                                        list.remove(new Integer(info[j]));
                                        break loop;
                                    }
                                    break;
                                }
                            }
                        }
                    }
                }
            }
            list.add(info[i]);
        }
        System.out.println(result);
    }
}