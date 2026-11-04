s1 = {2,45,34,37,53,73}
s2 = {2,45,34,73,355,6424,42,442}

print(s1.union(s2)) # This function will combine both the set 
print(s1.intersection(s2)) # This function will intersect both the sets and give the set of common elements found in both s1 and s2 as output 

s3 = s1 - s2 # This method will differentiate both the sets and give the set of s1 which is not present in s2
print(s3)

s4 = s2 - s1 # Same Anology but will give the set of s2 which is not present in s1 
print(s4)