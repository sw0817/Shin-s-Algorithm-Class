package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Baekjoon1918 {

    static String input;
    static char[] list;
    static Stack<Character> stack = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine();
        list = input.toCharArray();
        StringBuilder sb = new StringBuilder();

        for (int i=0; i<list.length; i++) {
            char cur = list[i];

            if ('A' <= cur && cur <= 'Z') {
                sb.append(cur);
            } else {
                if (cur == '(') {
                    stack.push(cur);
                } else if (cur == ')') {
                    while (!stack.isEmpty() && stack.peek() != '(') {
                        sb.append(stack.pop());
                    }

                    if (!stack.isEmpty()) {
                        stack.pop();
                    }
                } else {
                    while (!stack.isEmpty() && checkCur(cur) <= checkCur(stack.peek())) {
                        sb.append(stack.pop());
                    }
                    stack.push(cur);
                }
            }
        }

        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        System.out.println(sb.toString());
    }

    static int checkCur(char cur) {
        if (cur == '*' || cur == '/') {
            return 2;
        } else if (cur == '+' || cur == '-') {
            return 1;
        } return 0;
    }
}
