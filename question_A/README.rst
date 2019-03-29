###Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

To compare whether two lines overlap, you can check if the first starts before the end of the second, and the first ends after the start of the second.
