package com.company;

import java.util.Stack;

public class Programmers42584 {

    static class Solution {
        public int[] solution(int[] prices) {
            int l = prices.length;
            int[] answer = new int[l];
            for (int i=0; i<l; i++) {
                answer[i] = l-1-i;
            }
            Stack<Node> stack = new Stack<>();
            for (int i=0; i<l; i++) {
                if (stack.empty()) {
                    stack.push(new Node(i, prices[i]));
                } else {
                    while (!stack.empty() && stack.peek().price > prices[i]) {
                        int idx = stack.pop().idx;
                        answer[idx] = i - idx;
                    }
                    stack.add(new Node(i, prices[i]));
                }
            }
            return answer;
        }

        static class Node {
            int idx;
            int price;

            Node(int _idx, int _price) {
                this.idx = _idx;
                this.price = _price;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Programmers42584.Solution s = new Programmers42584.Solution();
    }
}
