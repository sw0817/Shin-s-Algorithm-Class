package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Baekjoon1874 {

    static int N, idx;
    static int[] nums;
    static Stack<Integer> stack = new Stack<Integer>();
    static Queue<String> result = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new int[N];
        idx = 0;
        for (int i=0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            nums[i] = num;
        }

        for (int i=1; i < N+1; i++) {
            stack.push(i);
            result.add("+");
            while (!stack.empty() && stack.peek() == nums[idx]) {
                stack.pop();
                idx++;
                result.add("-");
            }
        }

        if (idx == N) {
            while (!result.isEmpty()) {
                System.out.println(result.poll());
            }
        } else {
            System.out.println("NO");
        }
    }
}
