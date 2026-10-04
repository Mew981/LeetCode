/**
 * Problem Link : https://leetcode.com/problems/find-customer-referee/
 * Platform     : LeetCode
 * Difficulty   : Easy
 */

#include <bits/stdc++.h>
using namespace std;

# Write your MySQL query statement below
SELECT
    name
FROM
    Customer
WHERE 
    referee_id != 2 OR referee_id is null

