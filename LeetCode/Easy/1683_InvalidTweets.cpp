/**
 * Problem Link : https://leetcode.com/problems/invalid-tweets/
 * Platform     : LeetCode
 * Difficulty   : Easy
 */

#include <bits/stdc++.h>
using namespace std;

# Write your MySQL query statement below
SELECT
    tweet_id
FROM
    Tweets
WHERE
    LENGTH(content) > 15
