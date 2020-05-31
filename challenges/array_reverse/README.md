# Reverse an Array

## Challenge

Write a function which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Approach & Efficiency

I've decided to approach this problem creating an empty list, popping the last element of a given array and appending it to the new one. It seems to be relatively memory efficient as we don't have to create a new DS in memory for each new elenemt.
This method is O(n) space and complexity

## Solution

<img src="https://github.com/LeoKuhorev/data-structures-and-algorithms/blob/array-reverse/assets/reverse_array_1.jpg" alt="Whiteboard Solution" style="max-width:100%;">
<img src="https://github.com/LeoKuhorev/data-structures-and-algorithms/blob/array-reverse/assets/reverse_array_2.jpg" alt="Whiteboard Solution" style="max-width:100%;">
