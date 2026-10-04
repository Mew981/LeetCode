/**
 * Problem Link : https://leetcode.com/problems/big-countries/
 * Platform     : LeetCode
 * Difficulty   : Easy
 */

#include <bits/stdc++.h>
using namespace std;

# Write your MySQL query statement below
SELECT
    name, population, area
FROM
    World
WHERE
    area >= 3000000 OR population >= 25000000
