package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Baekjoon1793 {

    static BigInteger[] dp = new BigInteger[251];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        dp[0] = new BigInteger("1");
        dp[1] = new BigInteger("1");
        dp[2] = new BigInteger("3");

        for (int i = 2; i < 251; i++) {
            dp[i] = dp[i-1].add(dp[i-2].multiply(BigInteger.valueOf(2)));
        }
        while (true) {
            String line = br.readLine();
            if (line == null) {
                break;
            }
            int n = Integer.parseInt(line);

            System.out.println(dp[n]);
        }
    }
}
