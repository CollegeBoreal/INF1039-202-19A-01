#!/bin/sh

LESSONS=(
6.Capstone-I
A.Capstone-II
1.Python
4.Variables
7.Strings
8.Tuples
9.Conditions
C.Loops
D.Functions
)

for id in "${LESSONS[@]}"
do
   cd ${id}
   sh .scripts/run.sh
   cd ../
done
