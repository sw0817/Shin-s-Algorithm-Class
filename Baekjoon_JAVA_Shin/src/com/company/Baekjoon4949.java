package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Baekjoon4949 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String str = br.readLine();
            boolean ans = true;
            if (str.length() == 1 && str.charAt(0) == '.') {
                break;
            }

            Stack<Character> stack = new Stack<>();
            for (int i=0; i<str.length(); i++) {
                char ch = str.charAt(i);
                if (ch == '(' || ch == '[') {
                    stack.add(ch);
                }
                if (ch == ')') {
                    if (!stack.empty() && stack.peek() == '(') {
                        stack.pop();
                    } else {
                        ans = false;
                        break;
                    }
                } else if (ch == ']') {
                    if (!stack.empty() && stack.peek() == '[') {
                        stack.pop();
                    } else {
                        ans = false;
                        break;
                    }
                }
            }
            if (ans && stack.empty()) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
    }
}
