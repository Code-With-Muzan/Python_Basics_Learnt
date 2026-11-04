# Can you change the value inside a list which is contained in set s ?
#          s = {8, 7, 12, "Muzamil", [1,2]}

# Answer - 1] No we can't change a value in a set as sets are immutable 
#          2] We can't have list in a set as they are mutable and unhashable, as sets contain only immutable and hashable elements 
#                   Therefore will display a typeError - cannot use 'list' as a set element (unhashable type: 'list')