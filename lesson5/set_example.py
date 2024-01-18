v = {'A', 'C', 4, False}
list_v = {'A', 'C', 4, False, 'A'}
another_v = set(list_v)
print(another_v)
first_set = {1,2,3,4,5}
second_set = {3,4,5,6,7}
third_set = {3,4,5}
print(first_set.isdisjoint(second_set))
print(third_set.issubset(first_set))
print(third_set<=first_set)
print(second_set.issuperset(third_set)) #>=
fourth_set = first_set.intersection(second_set)
print(fourth_set)
fifth_set = first_set.union(second_set)
print(fifth_set)
sixth_set = fifth_set.difference(fourth_set, v, first_set)
print(sixth_set)
seventh_set = fifth_set.symmetric_difference(fourth_set)
print(seventh_set)
eighth_set = seventh_set.copy()
print(eighth_set)
eighth_set.update(v, first_set)
print(eighth_set)
third_set.intersection_update(v, second_set,first_set)
print(third_set)
fifth_set.difference_update(v)
print(fifth_set)
second_set.symmetric_difference_update(v)
print(second_set)
second_set.add(17)
second_set.remove(False)
print(second_set)
print(second_set.discard(11)) #безпечніше діскардом бо не буде помилки
print(second_set)
exactly_new_set = second_set.pop()
print(exactly_new_set)
print(second_set.clear())
print(second_set)



