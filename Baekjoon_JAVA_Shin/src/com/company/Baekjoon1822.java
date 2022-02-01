package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Baekjoon1822 {
    static int nA, nB;
    static ArrayList<Integer> finalA;
    static HashSet<Integer> A;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        nA = Integer.parseInt(st.nextToken());
        nB = Integer.parseInt(st.nextToken());
        A = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<nA; i++) {
            A.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<nB; i++) {
            A.remove(Integer.parseInt(st.nextToken()));
        }
        int l = A.size();
        finalA = new ArrayList<>(A);
        Collections.sort(finalA);
        System.out.println(l);
        for (Integer n : finalA) {
            System.out.print(n + " ");
        }
    }
}
