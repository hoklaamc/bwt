# bwt

Burrow Wheeler Transform implementation in python.

Solution for [this problem](https://www.spoj.com/problems/BWHEELER/).

## Input Format (from the problem linked above)

The input file consists of multiple testcases.
The first line of each testcase contains one integer, R, indicating the row number containing the original input string in the sorted matrix.
The second line of each testcase contains one string, Col, which is the last column of the grid. (1 <= len(Col) <= 1000)
Col contains only lowercase characters. 1 <= R <= len(Col).
Input terminates with a line containing R=0 which must not be processed.

## Output Format (from the problem linked above)

Print the original input string to the burrow wheeler's algorithm.

## Usage

Run using `python bwheeler.py` to use stdin as input.
Run using `python bwheeler.py testfile` to run using a test file. Example is in the file called `test`.

## Sample Input

```
2
bacab
3
rwlb
11
baaabaaaabbbaba
0
```

## Sample Output

```
abcba
rbwl
baaabbbbaaaaaab
```