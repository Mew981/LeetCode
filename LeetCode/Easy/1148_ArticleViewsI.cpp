/**
 * Problem Link : https://leetcode.com/problems/article-views-i/
 * Platform     : LeetCode
 * Difficulty   : Easy
 */

#include <bits/stdc++.h>
using namespace std;

# Write your MySQL query statement below
SELECT 
    distinct author_id as id
FROM
    Views
WHERE
    author_id = viewer_id
ORDER BY
    id

