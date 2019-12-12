#!/bin/sh

LESSONS=(
1.Python
4.Variables
6.Capstone-I
7.Strings
8.Tuples
9.Conditions
A.Capstone-II
C.Loops
D.Functions
)

for id in "${LESSONS[@]}"
do
   cd ${id}
   sh .scripts/run.sh
   cd ../
done
