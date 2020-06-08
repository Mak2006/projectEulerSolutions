# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
Solved using excel , the algo is quite nice
COUNT	FACTors 	FINAL NUMBER	CHECK		divisior	quotient
1	1		1		232792560	1		232792560
2	2		2		232792560	2		116396280
3	3		6		232792560	3		77597520
4	2		12		232792560	4		58198140
5	5		60		232792560	5		46558512
6	1		60		232792560	6		38798760
7	7		420		232792560	7		33256080
8	2		840		232792560	8		29099070
9	3		2520		232792560	9		25865840
10	1		2520		232792560	10		23279256
11	11		27720		232792560	11		21162960
12	1		27720		232792560	12		19399380
13	13		360360		232792560	13		17907120
14	1		360360		232792560	14		16628040
15	1		360360		232792560	15		15519504
16	2		720720		232792560	16		14549535
17	17		12252240	232792560	17		13693680
18	1		12252240	232792560	18		12932920
19	19		232792560	232792560	19		12252240


In words,

fac =list =  the numbers whose * will give use the required numner
for each new numbers k from 1 to 20
    if  k is not there in fac
        if k is prime add to fac
        else
            check if k can be made from numbers withi the factor, if so ignore
            if not
                find the smallest number s which when multiplied with any
                ... numbers in  fac will give k, add that.
    return fac

next multiply all of fac to get the number.
"""
