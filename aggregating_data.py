 1/1:
list_1 = [1,2.3]
print(list_1)
 1/2: import numpy as np
 1/3:
numpy_1 = np.array(list_1)
print numpy_1
 1/4:
numpy_1 = np.array[(list_1)]
print numpy_1
 1/5:
numpy_1 = np.array[(list_1)]
print(numpy_1)
 1/6:
numpy_1 = np.array(list_1)
print(numpy_1)
 1/7:
list_1 = [1, 2, 3]
print(list_1)
 1/8:
numpy_1 = np.array(list_1)
print(numpy_1)
 1/9:
list_1 = [1, 2. 3]
print(list_1)
1/10:
list_1 = [1, 2, 3]
print(list_1)
1/11:
zeros_array = np.zeros(5)
print (zeros_array)
1/12:
ones_array = np.ones(10)
print (ones_array)
1/13:
range_array1 = np.arange(0, 10)
print(range_array1)
1/14:
range_array2 = np.arange(10, 20, 2)
print(range_array2)
1/15:
range_array2 = np.arange(10, 22, 2)
print(range_array2)
1/16:
range_array2 = np.arange(10, 20, 2)
print(range_array2)
1/17:
range_array3 = np.arange(0, 20, 3)
print(range_array3)
1/18:
range_array2 = np.arange(10, 20)
print(range_array2)
1/19:
linspace_Array = np.linspace(0, 10, 5)
print(linspace_array)
1/20:
linspace_array = np.linspace(0, 10, 5)
print(linspace_array)
1/21:
linspace_array = np.linspace(0, 10, 50)
print(linspace_array)
1/22: Creating Numpy Arrays
 2/1: an_array = np.arange(0,10)
 2/2: import numpy as np
 2/3: an_array = np.arange(0,10)
 2/4: an_array = np.arange(0,11)
 2/5:
an_array = np.arange(0,11)
print(an_array)
 2/6:
first_el = an_array[0]
print(first_el)
 2/7:
first_el = an_array[0]
print(first_el)
last_el = an_array[10]
print(last_el)
 2/8:
first_five = an_array[0:5]
print(first_five)
 2/9:
last_five = an_array[6:]
print(last_five)
2/10:
last_five = an_array[6::2]
print(last_five)
2/11:
first_five_rev = an_array[4:0:-1]
print(first_five_rev)
2/12: last_two = an_array[-2:]
2/13:
last_two = an_array[-2:]
print(last_two)
2/14: print(an_array.size)
2/15: print(np.amax(an_array)
2/16:
print(np.amax(an_array))
print(np.amin(an_array))
print(np.average(an_array))
 5/1:
an_array = np.arange(0, 6)
print(an_array)
 5/2: import numpy as np
 5/3:
an_array = np.arange(0, 6)
print(an_array)
 5/4:
an_array[3] = 25
print(an_array)
 5/5: print(np.append(an_array),32)
 5/6: print(np.append(an_array,32))
 5/7:
print(np.append(an_array,32))
print(an_array)
 5/8:
an_array = [0,6]
print(np.append(an_array, 7))
print(an_array)
 5/9:
an_array = np.arange[0, 6]
print(np.append(an_array, 7))
print(an_array)
5/10:
an_array = np.arange(0, 6)
print(np.append(an_array, 7))
print(an_array)
5/11:
an_array = np.arange(0, 6)
print(np.append(an_array, 6))
print(an_array)
5/12:
print(np.append(an_array, [6,7]))
print(an_array)
5/13:
np.append(an_array, [6,7])
print(an_array)
5/14:
append_array = np.append(an_array, [6,7])
print(append_array)
5/15:
insert_array = np.insert(an_array, [3:50])
print(append_array)
5/16:
insert_array = np.insert(an_array, [3,50])
print(append_array)
5/17:
insert_array = np.insert(an_array, (3,50)
print(append_array)
5/18:
insert_array = np.insert(an_array, (3,50))
print(append_array)
5/19:
insert_array = np.insert(an_array, [3,50])
print(append_array)
5/20:
insert_array = np.insert(an_array, 3, [50, 60])
print(append_array)
5/21:
insert_array = np.insert(an_array, 3, [50, 60])
print(insert_array)
5/22:
del_array = np.delete(an_array, 3)
print(del_array)
5/23: print(an_array * 3)
5/24:
print(an_array * 3)
print(an_array + 3)
print(an_array - 2)
print(an_array / 10)
5/25:
print(an_array * 3)
print(an_array + 3)
print(an_array - 2)
print(an_array / 10)
print(an_array % 3)
5/26:
print(an_array * 3)     # multiple each element by 3
print(an_array + 3)
print(an_array - 2)
print(an_array / 10)
print(an_array % 3)
5/27:
print(an_array * 3)     # multiple each element by 3
print(an_array + 3)     # add each element by 3
print(an_array - 2)     # subtract each element by 2
print(an_array / 10)    # divide each element by 3
print(an_array % 3)     # modulus of each element
5/28:
sort_array = np.array([3, 5, 1, 23, 45, 32, 87])
print(sort_array)
print(np.sort(sort_array))
5/29:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
print(np.sort(sort_array))
5/30:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
print(np.sort(sort_array)) # default is ascending
print(np.sort(-sort_array)) #
5/31:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
print(np.sort(sort_array)) # default is ascending
print(np.sort(-sort_array)) # ascending negative values
print(-np.sort(sort_array)) # default is ascending
5/32:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
print(np.sort(sort_array)) # default is ascending
print(np.sort(-sort_array)) # descending negative values
print(-np.sort(-sort_array)) # default is ascending
5/33:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
print(np.sort(sort_array)) # default is ascending
print(np.sort(-sort_array)) # ascending negative values
print(-np.sort(-sort_array)) # descending values
5/34:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
print(np.sort(sort_array)) # default is ascending
print(-np.sort(sort_array)) # ascending negative values
print(np.sort(-sort_array)) # descending values
5/35:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
print(np.sort(sort_array)) # default is ascending
print(np.sort(-sort_array)) # ascending negative values
print(-np.sort(-sort_array)) # descending values
5/36:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
# how do you reverse sort an array
print(np.sort(sort_array)) # default is ascending
print(np.sort(-sort_array)) # ascending negative values
print(-np.sort(-sort_array)) # descending values
5/37:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
# how do you reverse sort an array
print(np.sort(sort_array)) 
# first step is to negate the array values
print(np.sort(-sort_array))
# then negate the np sort and this will display in descending order 
print(-np.sort(-sort_array))
5/38:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
# how do you reverse sort an array
print(-(np.sort(sort_array)) 
# first step is to negate the array values
print(np.sort(-sort_array))
# then negate the np sort and this will display in descending order 
print(-np.sort(-sort_array))
5/39:
sort_array = np.array([3, 5, 1, 23, 1, 45, 100, 5, 32, 3, 87])
print(sort_array)
# how do you reverse sort an array
print(np.sort(sort_array)) 
# first step is to negate the array values
print(np.sort(-sort_array))
# then negate the np sort and this will display in descending order 
print(-np.sort(-sort_array))
 6/1: import numpy as np
 6/2:
student_grades = np.array([56, 78, 98, 90, 58, 64, 67, 72, 93, 51])
print(student_grades)
 6/3:
class_average = np.average(student_grades)
print(class_average)
 6/4:
highest_grade = np.average(student_grades)
print(highest_grade)
 6/5:
highest_grade = np.max(student_grades)
print(highest_grade)
 6/6:
lowest_grade = np.min(student_grades)
print(lowest_grade)
 6/7:
# highest grade in class
highest_grade = np.max(student_grades)
print(highest_grade)
#lowest grade in clasee
lowest_grade = np.min(student_grades)
print(lowest_grade)
 6/8:
print(np.argmax(student_grades))
print(np.argmin(student_grades))
 6/9:
print(np.sort(student_grades))
print(-np.sort(-student_grades))
6/10:
# argmax is the index of the max value - so where in the array does the max value sit
print(np.argmax(student_grades))
# argmax is the index of the min value  - so where in the array does the min value sit
print(np.argmin(student_grades))
6/11:
inc_grades = student_grade * 1.1
print (inc_grades)
6/12:
inc_grades = student_grades * 1.1
print (inc_grades)
6/13:
increased_grades = student_grades + 5
print(increased_grades)
6/14:
print(np.sort(student_grades))
print(-np.sort(-student_grades))
6/15: print(np.add(student_grades, np.array([1,2,3,4,5,6,7,8,9,10])))
6/16:
print(
    np.add(
        student_grades, np.array([1,2,3,4,5,6,7,8,9,10])
    )
)
6/17:
# add value in np.array to the corresponding element in student grades
print(
    np.add(
        student_grades, np.array([1,2,3,4,5,6,7,8,9,10])
    )
)
6/18:
# add value in np.array to the corresponding element in student grades
print(
    np.add(
        student_grades, np.ones([5])
    )
)
6/19:
# add value in np.array to the corresponding element in student grades
print(
    np.add(
        student_grades, np.ones([10])
    )
)
6/20:
# add value in np.array to the corresponding element in student grades
print(student_grades)
print(
    np.add(
        student_grades, np.ones([10])
    )
)
6/21:
# add 5 to the corresponding element in student grades
print(student_grades)
print(
    np.add(
        student_grades, np.fives([10])
    )
)
 7/1: import numpy as np
 7/2:
# create a 2 x 2 array
two_by_two = np.matrix(
                       [[1, 2],
                        [3, 4]]
                      )
print(two_by_two)
 7/3:
# create a matix to represent a number 1
num_one = np.matrix(
                     [0,0,1,0,0],
                     [1,1,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [1,1,1,1,1],
)
print(num_one)
 7/4:
# create a matix to represent a number 1
num_one = np.matrix(
                     [0,0,1,0,0],
                     [1,1,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [1,1,1,1,1]
)
print(num_one)
 7/5:
# create a 2 x 3 matrix
two_by_three = np.matrix('1 2; 3 4; 5 6')
print(two_by_three)
 7/6:
# create a 2 x 3 matrix
two_by_three = np.matrix('1 2; 3 4; 5 6')
print(two_by_three)
# create a 3 x 4 matrix
three_by_four = np.matrix('0 0 0; 0 1 0; 0 1 0; 0 1 0')
print(three_by_four)
 7/7:
# create a 2 x 3 matrix
two_by_three = np.matrix('1 2; 3 4; 5 6')
print(two_by_three)
# create a 3 x 4 matrix
three_by_four = np.matrix('0 0 0; 0 1 0; 0 1 0; 0 1 0')
print(three_by_four)
 7/8:
# create a 2 x 3 matrix
two_by_three = np.matrix('1 2; 3 4; 5 6')
print(two_by_three)
print("# ====================================== #")
# create a 3 x 4 matrix
three_by_four = np.matrix('0 0 0; 0 1 0; 0 1 0; 0 1 0')
print(three_by_four)
 7/9:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix("
                     0,0,1,0,0;
                     0,1,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     1,1,1,1,1
)
print(num_one)
print("# ====================================== #")
7/10:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix("
                     0,0,1,0,0;
                     0,1,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     0,0,1,0,0;
                     1,1,1,1,1"
)
print(num_one)
print("# ====================================== #")
7/11:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix('0,0,1,0,0; 0,1,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 1,1,1,1,1')
print(num_one)
print("# ====================================== #")
7/12:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix('0,0,1,0,0; 0,1,1,0,0; 1,1,1,1,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 1,1,1,1,1')
print(num_one)
print("# ====================================== #")
7/13:
two_by_three = np.matrix('1 2; 3 4 5; 6 7 8 9')
print(two_by_three)
7/14:
two_by_three = np.matrix('1 2; 3 4 5; 6 7')
print(two_by_three)
7/15:
two_by_three = np.matrix([1 2]; [3 4 5]; [6 7]')
print(two_by_three)
7/16:
two_by_three = np.matrix([1, 2]; [3, 4, 5]; [6, 7]')
print(two_by_three)
7/17:
two_by_three = np.matrix([1, 2], [3, 4, 5], [6, 7]')
print(two_by_three)
7/18:
two_by_three = np.matrix([[1, 2], [3, 4, 5], [6, 7]]')
print(two_by_three)
7/19:
two_by_three = np.matrix([[1, 2], [3, 4, 5], [6, 7]])
print(two_by_three)
7/20:
# if arrays are not same size the arrays will be converted to an array of lists
two_by_three = np.matrix([[1, 2], [3, 4, 5], [6, 7]])
print(two_by_three)
7/21:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix('0,0,1,0,0; 0,1,1,0,0; 1,1,1,1,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 1,1,1,1,1')
print(num_one)
print("# ====================================== #")
7/22:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix('0 0 1 0 0; 0,1,1,0,0; 1,1,1,1,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 0,0,1,0,0; 1,1,1,1,1')
print(num_one)
print("# ====================================== #")
7/23:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix('0 0 1 0 0; 0 1 1 0 0; 1 1 1 1 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 1 1 1 1 1')
print(num_one)
print("# ====================================== #")
7/24:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix('00100; 0 1 1 0 0; 1 1 1 1 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 1 1 1 1 1')
print(num_one)
print("# ====================================== #")
7/25:
# create a matix to represent a number 1
print("# ====================================== #")
num_one = np.matrix('0 0 1 0 0; 0 1 1 0 0; 1 1 1 1 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 1 1 1 1 1')
print(num_one)
print("# ====================================== #")
7/26: print(np.zeros([3, 2]))
7/27: print(np.ones([3, 2]))
7/28: print(np.ones([10, 20]))
7/29:
# create a matix to represent a number 2
print("# ====================================== #")
num_one = np.matrix('0 0 1 0 0; 
                    0 1 1 0 0; 
                    1 1 1 1 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 1 1 1 1 1')
print(num_one)
print("# ====================================== #")
7/30:
# create a matix to represent a number 2
print("# ====================================== #")
num_two = np.matrix('0 0 1 0 0; 0 1 1 1 0; 0 0 0 1 0; 0 0 0 1 0; 0 0 1 0 0; 0 0 0 1 0; 0 0 0 1 0; 0 1 1 0 0; 1 1 1 1 1')
print(num_two)
print("# ====================================== #")
7/31:
# create a matix to represent a number 2
print("# ====================================== #")
num_two = np.matrix('0 0 1 0 0; 0 1 1 1 0; 1 0 0 0 1; 0 0 0 0 1; 0 0 0 1 0; 0 0 0 1 0; 0 0 0 1 0; 0 1 1 0 0; 1 1 1 1 1')
print(num_two)
print("# ====================================== #")
7/32:
# create a matix to represent a number 2
print("# ====================================== #")
num_two = np.matrix('0 0 1 0 0; 0 1 1 1 0; 1 0 0 0 1; 0 0 0 0 1; 0 0 0 1 0; 0 0 0 0 1; 0 0 0 1 0; 0 1 1 0 0; 1 1 1 1 1')
print(num_two)
print("# ====================================== #")
7/33:
# create a matix to represent a number 2
print("# ====================================== #")
num_two = np.matrix('0 0 1 0 0; 0 1 1 1 0; 1 0 0 0 1; 0 0 0 0 1; 0 0 0 0 1; 0 0 0 1 0; 0 0 0 1 0; 0 1 1 0 0; 1 1 1 1 1')
print(num_two)
print("# ====================================== #")
7/34:
# create a matix to represent a number 2
print("# ====================================== #")
num_two = np.matrix('0 0 1 0 0; 0 1 1 1 0; 1 0 0 0 1; 0 0 0 0 1; 0 0 0 0 1; 0 0 0 1 0; 0 0 0 1 0; 0 0 1 0 0; 1 1 1 1 1')
print(num_two)
print("# ====================================== #")
7/35:
# create a matix to represent a number 2
print("# ====================================== #")
num_two = np.matrix('0 0 1 0 0; 0 1 1 1 0; 1 0 0 0 1; 0 0 0 0 1; 0 0 0 0 1; 0 0 0 1 0; 0 0 1 0 0; 0 0 1 0 0; 1 1 1 1 1')
print(num_two)
print("# ====================================== #")
7/36:
# create a matix to represent a number 2
print("# ====================================== #")
num_two = np.matrix('0 0 1 0 0; 0 1 1 1 0; 1 0 0 0 1; 0 0 0 0 1; 0 0 0 0 1; 0 0 0 1 0; 0 0 1 0 0; 0 1 1 0 0; 1 1 1 1 1')
print(num_two)
print("# ====================================== #")
 8/1: import numpy as np
 8/2:
a_matrix = np.matrix(
                     [
                         [1, 2, 3], 
                         [4, 5, 6], 
                         [7, 8, 9]
                     ])
print(a_matrix)
 8/3: print(a_matrix(0))
 8/4: print(a_matrix[0])
 8/5:
print(a_matrix[0])
print(a_matrix[1])
print(a_matrix[2])
 8/6:
print("--------------------------------------")
print(a_matrix[0])
print("--------------------------------------")
print(a_matrix[1])
print("--------------------------------------")
print(a_matrix[2])
print("--------------------------------------")
 8/7:
print("# -------------------------------------- #")
print(a_matrix[0])
print("# -------------------------------------- #")
print(a_matrix[1])
print("# -------------------------------------- #")
print(a_matrix[2])
print("# -------------------------------------- #")
 8/8: print(a_matrix([1,2]))
 8/9: print(a_matrix([0:1]))
8/10: print(a_matrix[0,1])
8/11:
print(a_matrix[0,1])
print(a_matrix[3,2])
8/12:
print(a_matrix[0,1])
print(a_matrix[2,2])
8/13:
# print value in 1st array, 2nd position
print(a_matrix[0,1])
# print value in 3rd array, 3rd position
print(a_matrix[2,2])
8/14:
# print value in 1st array, 2nd position
print(a_matrix[0,1])
# print value in 3rd array, 3rd position
print(a_matrix[2,2])
# print value in 2nd array, 1st position
print(a_matrix[1,0])
8/15:
# what size is the matrix 3 x 3 = 9
print(a_matrix.size)
8/16:
# what shape is the matrix 3 x 3
print(a_matrix.shape)
8/17:
print(np.amax(a_matrix))                # whats the max value 9
print(np.amin(a_matrix))                # whats the min value 1
print(np.average(a_matrix))             # whats the average   5
8/18:
print(a_matrix.max)
print(np.a_matrix.min)
print(np.a_matrix.mean)
8/19:
print(a_matrix.max)
print(a_matrix.min)
print(a_matrix.mean)
8/20:
print(a_matrix.max())
print(a_matrix.min())
print(a_matrix.mean())
 9/1: import numpy as np
 9/2:
a_matrix = np.matrix([[1, 2], [3, 4]])
print(a_matrix)
 9/3:
a_matrix = np.matrix(
                    [
                        [1, 2], 
                        [3, 4]
                    ]
)
print(a_matrix)
 9/4:
# initialise the matrix
a_matrix = np.matrix(
                    [
                        [1, 2], 
                        [3, 4]
                    ]
)
print(a_matrix)
 9/5:
a_matrix[1, 0] = 10                # changes 3 to 10
print(a_matrix)
 9/6:
a_matrix[0] = [6, 3]              # changes [1, 2] to [6, 3]
print(a_matrix)
 9/7:
# initialise the matrix again
a_matrix = np.matrix(
                    [
                        [1, 2], 
                        [3, 4]
                    ]
)
print(a_matrix.T)
 9/8:
# initialise the matrix again
a_matrix = np.matrix(
                    [
                        [1, 2], 
                        [3, 4]
                    ]
)
print(a_matrix.T)                        # swap rows and columns
print "#--------------------------------#"

a_matrix = np.matrix(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16], 
                    ]
)
print(a_matrix.T)                        # swap rows and columns
print "#--------------------------------#"
 9/9:
# initialise the matrix again
a_matrix = np.matrix(
                    [
                        [1, 2], 
                        [3, 4]
                    ]
)
print(a_matrix.T)                        # swap rows and columns
print ("#--------------------------------#")

a_matrix = np.matrix(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16], 
                    ]
)
print(a_matrix.T)                        # swap rows and columns
print("#--------------------------------#")
9/10: print(a_matrix.flatten())
9/11: print(a_matrix * 2)                    # multiple each value by a factor of 2
9/12:
print(a_matrix * 2)                    # multiple each value by a factor of 2
print(a_matrix.T * 2)                    # multiple each value by a factor of 2
9/13:
print(a_matrix * 2)                    # multiple each value by a factor of 2
print("#--------------------------------#")
print(a_matrix.T * 2)                  # swap rows and columns and then multiple each value by a factor of 2
9/14: print(np.matmul(a_matrix, a_matrix))  # multiple each value by itself 2x2, 4x4, 6x6 8x8
9/15: print(np.matmul(a_matrix, a_matrix))  # ????
9/16:
a_array = [[1,2],[3,4]]
print(np.matmul(a_matrix, a_matrix))  # ????
9/17:
a_matrix = [[1,2],[3,4]]
print(np.matmul(a_matrix, a_matrix))  # ????
9/18:
a_matrix = [[1,2],[3,4]]
b_matrix = [[1,1],[1,1]]
print(np.matmul(a_matrix, b_matrix))  # ????

1 2 3 4    1 2 3 4
9/19:
a_matrix = [[1,2],[3,4]]
b_matrix = [[1,1],[1,1]]
print(np.matmul(a_matrix, b_matrix))  # ????
9/20:
a_matrix = [[1,2],[3,4]]
b_matrix = [[1,2],[1,2]]
print(np.matmul(a_matrix, b_matrix))  # 4 6 7 14
9/21:
a_matrix = [[1,2],[3,4]]                  # b1xa1 + b1*a2 (3) b2xa1 + b2*a2 (3) 
b_matrix = [[1,1],[1,1]]                  #b1xa1 + b1*a2 (3) b1xa1 + b1*a2 (3) 
c_matrix = np.matmul(a_matrix, b_matrix)
print(c_matrix)
9/22:
a_matrix = [[1,2],[3,4]]                  # b1xa1 + b1*a2 (3) b2xa1 + b2*a2 (6) 
b_matrix = [[1,2],[1,2]]                  # b3xa3 + b1*a4 (7) b4xa3 + b4*a4 (14) 
c_matrix = np.matmul(a_matrix, b_matrix)
print(c_matrix)
9/23: print(np.matmul(a_matrix, a_matrix)
9/24: print(np.matmul(a_matrix, a_matrix))
9/25:
x_matrix = [[1,2],[3,4]]                  # b1xa1 + b1*a2 (3) b2xa1 + b2*a2 (6) 
y_matrix = [[1,2],[1,2]]                  # b3xa3 + b1*a4 (7) b4xa3 + b4*a4 (14) 
z_matrix = np.matmul(x_matrix, y_matrix)
print(z_matrix)
9/26: print(np.matmul(a_matrix, a_matrix))
9/27:
# initialise the matrix again
a_matrix = np.matrix(
                    [
                        [1, 2], 
                        [3, 4]
                    ]
)
print(a_matrix.T)                        # swap rows and columns
print ("#--------------------------------#")

a_matrix = np.matrix(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16], 
                    ]
)
print(a_matrix.T)                        # swap rows and columns
print("#--------------------------------#")
9/28: print(np.matmul(a_matrix, a_matrix))
9/29:
print(a_matrix)
print(np.matmul(a_matrix, a_matrix))    # 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16],
9/30:
print(a_matrix)
print(a_matrix)

print(np.matmul(a_matrix, a_matrix))    # 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16],
9/31:
a_matrix = np.matrix(
                    [
                        [1, 2, 3, 4]
                    ]
)
b_matrix = np.matrix(
                    [
                        [1, 2, 3, 4]
                    ]
)

print(np.matmul(a_matrix, b_matrix))    # 1+5+3+4+5+6+7+8+9+10+11+12+13+14+15+16], 10 + 26 + 30 + 40
9/32:
d_matrix = np.matrix(
                        [1, 2, 3, 4]
)
e_matrix = np.matrix(
                        [1, 2, 3, 4]
)

print(np.matmul(d_matrix, e_matrix))    # 1+5+3+4+5+6+7+8+9+10+11+12+13+14+15+16], 10 + 26 + 30 + 40
9/33:
# initialise the matrix again
a_matrix = np.matrix(
                    [
                        [1, 2], 
                        [3, 4]
                    ]
)
print(a_matrix.T)                        # swap rows and columns
print ("#--------------------------------#")

a_matrix = np.matrix(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16], 
                    ]
)
print(a_matrix.T)                        # swap rows and columns
print("#--------------------------------#")
9/34:
d_matrix = np.matrix(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16], 
                    ]
)
e_matrix = np.matrix(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16], 
                    ]
)
print(np.matmul(d_matrix, e_matrix))    # 1+5+3+4+5+6+7+8+9+10+11+12+13+14+15+16], 10 + 26 + 30 + 40
9/35:
d_matrix = np.matrix(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8]
                    ]
)
e_matrix = np.matrix(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8]                    ]
)
print(np.matmul(d_matrix, e_matrix))    # 1+5+3+4+5+6+7+8+9+10+11+12+13+14+15+16], 10 + 26 + 30 + 40
9/36:
d_matrix = [[1, 2, 3, 4],[5, 6, 7, 8]]
e_matrix = [[1, 2, 3, 4],[5, 6, 7, 8]]

print(np.matmul(d_matrix, e_matrix))    # 1+5+3+4+5+6+7+8+9+10+11+12+13+14+15+16], 10 + 26 + 30 + 40
9/37:
d_matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[1, 2, 3, 4],[5, 6, 7, 8]]
e_matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[1, 2, 3, 4],[5, 6, 7, 8]]

print(np.matmul(d_matrix, e_matrix))
9/38:
d_matrix = [[1, 2],[5, 6],[1, 2],[5, 6]]  # 10 + 16 + 30
e_matrix = [[1, 2],[5, 6],[1, 2],[5, 6]]

print(np.matmul(d_matrix, e_matrix))
9/39:
d_matrix = [[1, 2],[5, 6],[1, 2],[5, 6]]  # 10 + 16 + 30
e_matrix = [[1, 2],[5, 6],[1, 2],[5, 6]]
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/40:
d_matrix = np.matrix([1, 2],[5, 6],[1, 2],[5, 6])  # 10 + 16 + 30
e_matrix = [[1, 2],[5, 6],[1, 2],[5, 6]]
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/41:
d_matrix = np.matrix([
                     [1, 2],[5, 6],[1, 2],[5, 6]
                     ])  # 10 + 16 + 30
e_matrix = [[1, 2],[5, 6],[1, 2],[5, 6]]
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/42:
d_matrix = np.matrix([
                     [1, 2],[5, 6],[1, 2],[5, 6]
                     ])  # 10 + 16 + 30
e_matrix = np.matrix([
                     [1, 2],[5, 6],[1, 2],[5, 6]
                     ])  # 10 + 16 + 30
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/43:
d_matrix = np.matrix([
                     [1, 2, 3. 4],[5, 6, 7, 8],[1, 2, 3, 4],[5, 6, 7, 8]
                     ])  # 10 + 16 + 30
e_matrix = np.matrix([
                     [1, 2, 3. 4],[5, 6, 7, 8],[1, 2, 3, 4],[5, 6, 7, 8]
                     ])  # 10 + 16 + 30
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/44:
d_matrix = np.matrix([
                     [1, 2, 3, 4],[5, 6, 7, 8],[1, 2, 3, 4],[5, 6, 7, 8]
                     ])  # 10 + 16 + 30
e_matrix = np.matrix([
                     [1, 2, 3, 4],[5, 6, 7, 8],[1, 2, 3, 4],[5, 6, 7, 8]
                     ])  # 10 + 16 + 30
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/45:
x_matrix = [[1,2],[3,4]]                  # b1xa1 + b1*a2 (3) b2xa1 + b2*a2 (3) 
y_matrix = [[1,1],[1,1]]                  # b3xa3 + b1*a4 (7) b4xa3 + b4*a4 (7) 
z_matrix = np.matmul(x_matrix, y_matrix)
print(z_matrix)
print("#------------------------------------#")
z_matrix = np.matmul.add(x_matrix, y_matrix)
print(z_matrix)
9/46:
x_matrix = [[1,2],[3,4]]                  # b1xa1 + b1*a2 (3) b2xa1 + b2*a2 (3) 
y_matrix = [[1,1],[1,1]]                  # b3xa3 + b1*a4 (7) b4xa3 + b4*a4 (7) 
z_matrix = np.matmul(x_matrix, y_matrix)
print(z_matrix)
print("#------------------------------------#")
z_matrix = np.add(x_matrix, y_matrix)
print(z_matrix)
9/47:
x_matrix = [[1,2],[3,4]]                  # b1xa1 + b1*a2 (3) b2xa1 + b2*a2 (3) 
y_matrix = [[1,1],[1,1]]                  # b3xa3 + b1*a4 (7) b4xa3 + b4*a4 (7) 
z_matrix = np.matmul(x_matrix, y_matrix)
print(z_matrix)
print("#----- Add matrix values -------------------------------#")
z_matrix = np.add(x_matrix, y_matrix)
print(z_matrix)
9/48:
d_matrix = np.matrix([
                     [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]
                     ])  
e_matrix = np.matrix([
                     [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]
                     ])  
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/49:
d_matrix = np.matrix([
                     [1, 2, 3, 4],[2, 3, 4, 5],[1, 2, 3, 4],[1, 2, 3, 4]
                     ])  
e_matrix = np.matrix([
                     [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]
                     ])  
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/50:
d_matrix = np.matrix([
                     [1, 2, 3, 4],[2, 3, 4, 5],[1, 2, 3, 4],[2, 3, 4, 5]
                     ])  
e_matrix = np.matrix([
                     [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]
                     ])  
print(d_matrix)
print(e_matrix)
print(np.matmul(d_matrix, e_matrix))
9/51:
d_matrix = np.matrix([
                     [1, 2, 3, 4],[2, 3, 4, 5],[1, 2, 3, 4],[2, 3, 4, 5]
                     ])  
e_matrix = np.matrix([
                     [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]
                     ])  
print(d_matrix)
print(e_matrix)
f_matrix=np.matmul(d_matrix, e_matrix)
print(f_matrix)
9/52:
d_matrix = np.matrix([
                     [1, 2, 3, 4],[2, 3, 4, 5],[1, 2, 3, 4],[2, 3, 4, 5]
                     ])  
e_matrix = np.matrix([
                     [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]
                     ])  
# 1*1+1*2+1*3+1*4=10 2*2+2*3+2*4+2*5=

print(d_matrix)
print(e_matrix)
f_matrix=np.matmul(d_matrix, e_matrix)
print(f_matrix)
10/1: import numpy as np
10/2:
image_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
print(image_matrix)
10/3:
image_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [1, 1, 1, 1, 1], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
print(image_matrix)
10/4:
# need to get no of rows and number of columns
# .shape returns a tuple (r, c)
rows = image_matrix.shape[0]
cols = image-matrix.shape[1]

print(rows)
print(cols)
10/5:
# need to get no of rows and number of columns
# .shape returns a tuple (r, c)
rows = image_matrix.shape[0]
cols = image_matrix.shape[1]

print(rows)
print(cols)
10/6:
for r in range(rows)
    print(rows[r])
10/7:
for r in range(rows):
    print(rows[r])
10/8:
for r in range(rows):
    print(str(rows[r])
10/9:
for r in range(rows):
    print(rows(r))
10/10:
for r in range(rows):
    print(rows[r])
10/11:
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if c = 0:
            image_matrix[r,c] = 1
        else:
            image_matrix[r,c] = 0
10/12:
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if c == 0:
            image_matrix[r,c] = 1
        else:
            image_matrix[r,c] = 0
10/13:
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if c == 0:
            image_matrix[r,c] = 1
        else:
            image_matrix[r,c] = 0

print(image_matrix)
10/14:
print(image_matrix)
print("#--------------------------------#")
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if c == 0:
            image_matrix[r,c] = 1
        else:
            image_matrix[r,c] = 0

print(image_matrix)
10/15:
image_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [1, 1, 1, 1, 1], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
print(image_matrix)
10/16:
# need to get no of rows and number of columns
# .shape returns a tuple (r, c)
rows = image_matrix.shape[0]
cols = image_matrix.shape[1]

print(rows)
print(cols)
10/17:
print(image_matrix)
print("#--------------------------------#")
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if c == 0:
            image_matrix[r,c] = 1
        else:
            image_matrix[r,c] = 0

print(image_matrix)
10/18:
image_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [1, 1, 1, 1, 1], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
print(image_matrix)
print("#--------------------------------#")
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if image_matrix[r,c] == 0:
            image_matrix[r,c] = 1
        else:
            image_matrix[r,c] = 0

print(image_matrix)
10/19:
print("#------- BEFORE -------------------------#")
image_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [1, 1, 1, 1, 1], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
print(image_matrix)
print("#-------- AFTER ------------------------#")
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if image_matrix[r,c] == 0:
            image_matrix[r,c] = 1
        else:
            image_matrix[r,c] = 0

print(image_matrix)
10/20:
print("#------- BEFORE -------------------------#")
one_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [1, 1, 1, 1, 1], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
rows = one_matrix.shape[0]
cols = one_matrix.shape[1]

print(one_matrix)
print("#-------- AFTER ------------------------#")
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if one_matrix[r,c] == 0:
            one_matrix[r,c] = 1
        else:
            one_matrix[r,c] = 0

print(one_matrix)
10/21:
print("#------- BEFORE -------------------------#")
one_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
rows = one_matrix.shape[0]
cols = one_matrix.shape[1]

print(one_matrix)
print("#-------- AFTER ------------------------#")
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if one_matrix[r,c] == 0:
            one_matrix[r,c] = 1
        else:
            one_matrix[r,c] = 0

print(one_matrix)
10/22:
print("#------- BEFORE -------------------------#")
one_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
rows = one_matrix.shape[0]
cols = one_matrix.shape[1]

print(one_matrix)
print("#-------- AFTER ------------------------#")
for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if one_matrix[r,c] == 0:
            one_matrix[r,c] = 1
        else:
            one_matrix[r,c] = 0

print(one_matrix)

print("#-------- TRANSPOSE ------------------------#")
print(one_matrix.T)
10/23:
print("#-------- TRANSPOSE ------------------------#")
print(one_matrix.T)

print("#-------- FLATTENED ------------------------#")
print(one_matrix.flatten())
10/24:
print("#------- BEFORE -------------------------#")
one_matrix = np.matrix(
    [
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0]
    ]
)
rows = one_matrix.shape[0]
cols = one_matrix.shape[1]

print(one_matrix)
print("#-------- AFTER ------------------------#")

for r in range(rows):                  # for r in range 0->no of rows 
    for c in range(cols):              # for c in range 0 -> cols
        if one_matrix[r,c] == 0:
            one_matrix[r,c] = 1
        else:
            one_matrix[r,c] = 0

print(one_matrix)
10/25:
print("#-------- TRANSPOSE ------------------------#")
print(one_matrix.T)

print("#-------- FLATTENED ------------------------#")
print(one_matrix.flatten())
13/1: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/2: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/3: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/4: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/5: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/6: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/7: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/8: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/9: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/10: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/11: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/12: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/13: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/14: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/15: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/16: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/17: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
13/18: runfile('C:/Zenva/courses/pandas/intro.py', wdir='C:/Zenva/courses/pandas')
14/1: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/2: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/3: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/4: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/5: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/6: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/7: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/8: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/9: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/10: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/11: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/12: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/13: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/14: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/15: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/16: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/17: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/18: flights.columns
14/19: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
14/20: flights.columns
14/21: flights.rows
14/22: runfile('C:/Zenva/courses/pandas/reading_in_data.py', wdir='C:/Zenva/courses/pandas')
15/1: import pandas as pd
15/2: flights = pd.read_excel('flights.xlsx', 'Flights')
15/3: flights = pd.read_excel('flights.xlsx', 'flights')
15/4: flights = pd.read_excel('flights.xls', 'flights')
15/5: flights = pd.read_excel('flights.xlsx', 'flights')
16/1: import panda as pd
16/2: import pandas as pd
16/3: flights = pd.read_csv('flights.csv')
16/4: flights = pd.read_csv('flights.csv', index_col=False)
16/5: color NoColor
16/6: colors NoColor
16/7: flights = pd.read_csv('flights.csv')
16/8: flights = pd.read_csv('flights.csv', index_col=False)
16/9: flights
14/23: flights
16/10: flights.columns
16/11: flights.DAY_OF_WEEK
16/12: flights.ORIGIN
16/13: flights.columns
16/14: flights.ORIGIN
16/15: flights.ORIGIN_CITY
16/16: flights.columns
16/17: flights.ORIGIN_CITY_NAME
14/24: flights.ORIGIN_CITY_NAME
14/25: flights['DAY_OF_WEEK']
14/26: flights.DAY_OF_WEEK
14/27: runcell(0, 'C:/Zenva/courses/pandas/reading_in_data.py')
16/18: flights.ORIGIN_CITY_NAME
16/19: # Data Manipulation with Panda
16/20: flights
16/21: # get all of the origin column
16/22: flights.ORIGIN
16/23: # check the column names again
16/24: flights.columns
16/25: # select the origin and destination airports
16/26: flights[['ORIGIN','DEST']]
16/27: # selct first 3 rows - remember slice doesnt include the upper bound
16/28: flights[:3]
16/29: # select a row and col entry in the Dataframe
16/30: # iloc integer location
16/31: flights.iloc[0,0]
16/32: # get value from 3rd row 2nd col
16/33: flights.iloc[2,1]
16/34: # get value from 2nd row  3rd col
16/35: flights.iloc[1,2]
16/36: # mixing row indices with string column names
16/37: flights.iloc[1, flights.columns.get_loc['DISTANCE']]
16/38: flights.iloc[1, flights.columns.get_loc('DISTANCE')]
16/39: # can specify a range of rows to get
16/40: flights.iloc[:3, flights.columns.get_loc('DISTANCE')]
16/41: # can get multiple columns by converting it into a list
16/42: flights.iloc[:3, [flights.columns.get_loc('DISTANCE'), flights.columns.get_loc('ORIGIN_CITY_NAME')]]
16/43: flights.iloc[0, [flights.columns.get_loc('DISTANCE'), flights.columns.get_loc('ORIGIN_CITY_NAME')]]
16/44: # save session history to file
16/45: %history -g -f selecting_data.py
17/1: # Sorting Date
17/2: ipot pandas as pd
17/3: import pandas as pd
17/4: flights = pd.read_cs('flights.csv', index_col=False)
17/5: flights = pd.read_csv('flights.csv', index_col=False)
17/6: print(flights)
17/7: #sort values by column
17/8: flights.sort_values(by=['DISTANCE'])
17/9: # sort descending
17/10: flights.sort_values(by=['DISTANCE'], ascending=False)
17/11: # sort by AIR_TIME
17/12: flights.sort_values(by=['AIR_TIME'], ascending=False)
17/13: # sort values by mutiple columns
17/14: flights.sort_values(by=['DISTANCE','AIR_TIME'], ascending=False)
17/15: # export history
17/16: %history -g -f sorting_data.py
18/1: # Filtering Data
18/2: import pandas as pd
18/3: flights = pd.read_csv('flights.csv', index_col=False)
19/1: # Filtering Data
19/2: import pandas as pd
19/3: flights = pd.read_csv('flights.csv', index_col=False)
19/4: flights
19/5: flights['MONTH'==1]
19/6: flights('MONTH'==1)
19/7: flights(['MONTH'] == 1)
19/8: flights[['MONTH'] == 1]
19/9: flights['MONTH'] == 1
19/10: flights[flights['MONTH'] == 1]
19/11: flights[flights['MONTH'] == 1 and flights['DAY_OF_MONTH'] == 1]
19/12: flights[flights['MONTH']  and flights['DAY_OF_MONTH'] == 1]
20/1: # Data Sorting
20/2: import pandas as pd
20/3: flights = pd read_csv('flights.csv', index_col=False)
20/4: flights = pd.read_csv('flights.csv', index_col=False)
20/5: flights.sort_values(by==['DISTANCE'])
20/6: flights.sort_values(by=['DISTANCE'])
20/7: flights.sort_values(by=['DISTANCE', ascending=False])
20/8: flights.sort_values(by=['DISTANCE'], ascending=False)
20/9: # sort values by AIR_TIME
20/10: flights.sort_values(by=['AIR_TIME'], ascending=False)
20/11: # Sorting by multiple columns
20/12: flights.sort_values(by=['DISTANCE', 'AIR_TIME'], ascending=False)
21/1: # Filtering data in DataFrames
21/2: import pandas as pd
21/3: flights = pd.read_csv('flights.csv', index_col=False)
21/4: # filters use a boolean value to check values against and return all rows satisfying the expression
21/5: # fetch all flights in January
21/6: flights.columns
21/7: flights[MONTH == 1]
21/8: flights['MONTH' == 1]
21/9: flights['MONTH'] == 1
21/10: # returns a true or false value for all rows showing if they match the expression
21/11: # to just return the rows that are true
21/12: flights[flights['MONTH'] == 1]
21/13: # fetch all flighst leaving New York State
21/14: flights[flights['ORGIN_STATE_NM'] == 'New York']
21/15: flights[flights['ORiGIN_STATE_NM'] == 'New York']
21/16: flights[flights['ORIGIN_STATE_NM'] == 'New York']
21/17: # can also other expressions like comparision operators
21/18: long_flights = flights[flights['DISTANCE'] > 4000]
21/19: long_flights
21/20: #long_flights is a dataframe s we can add more fliters
21/21: # if we want all long flights that start in Hawaii
21/22: long_flights = flights[flights['ORIGIN_STATE_NM'] == 'Hawaii']
21/23: long_flights
21/24: long_flights = flights[flights['DISTANCE'] > 4000]
21/25: long_flights
21/26: long_flights[long_flights['ORIGIN_STATE_NM'] == 'Hawaii']
21/27: # can use python and or NOT - as there is more than one true/false value returned
21/28: # can use bitwise operators | & ~
21/29: # need to enclose each expression in ()
21/30:
long_flights[(long_flights['ORIGIN_STATE_NM'] == "Hawaii") | (long_flights['DEST_STAT
E_NM'] == "Hawaii")]
21/31: long_flights[(long_flights['ORIGIN_STATE_NM'] == "Hawaii") | (long_flights['DEST_STATE_NM'] == "Hawaii")]
21/32: long_flights[(long_flights['ORIGIN_STATE_NM'] == "Hawaii") | (long_flights['DEST_STATE_NM'] == "Hawaii")]
21/33: flight[(flights['DISTANCE'] > 4000) & (flights['MONTH'] == 1)]
21/34: flights[(flights['DISTANCE'] > 4000) & (flights['MONTH'] == 1)]
21/35: # all flights more than 4000 but not in March
21/36: flights[(flights['DISTANCE'] > 4000) & ~(flights['MONTH'] == 3)]
21/37: # export history
21/38: %history -g -f filtering.py
23/1: ?
23/2: ? color
23/3: color ?
24/1: # Data Aggregation
24/2: import pandas as pd
24/3: interactiveShell.colors
24/4: InteractiveShell.colors
24/5: InteractiveShell.colors.nocolor
24/6: @color NoColor
24/7: %colors nocolor
   1: # Data aggregration
   2: # set colors to nocolor
   3: %colors nocolor
   4: # import pandas
   5: import pandas as pd
   6: # import flights data
   7: flights = pd.read_csv('flights.csv', index_col=False)
   8: # import numpy
   9: import numpy as np
  10: # group data by month
  11: flights_by_month = flights.groupby('MONTH')
  12: flights_by_month
  13: # returns a Python representation because this isn’t how we work with groups
  14: # we have to ask for which group we want
  15: # retrieve flight data from December
  16: flights_by_month.get_group(12)
  17: # this is the same as filtering by month
  18: # but if we want to know how many miles were flown in December
  19: flights_by_month.get_group(12).aggregrate(np.sum)
  20: this is wrong - so if we want total distance by month
  21: # this is wrong - so if we want total distance by month
  22: flights_by_month['DISTANCE'].aggregrate(np.sum)
  23: flights_by_month['DISTANCE'].aggregate(np.sum)
  24: # so we used numpy to to calculate the sum for each group
  25: # other numpy functions
  26: flights_by_month['DISTANCE'].aggregate(np.mean)
  27: flights_by_month['DISTANCE'].aggregate(np.max)
  28: flights_by_month['DISTANCE'].aggregate(np.min)
  29: # but which month had the most miles travelled
  30: flights_by_month['DISTANCE'].aggregate(np.sum).max()
  31: # but which month had the least miles travelled
  32: flights_by_month['DISTANCE'].aggregate(np.sum).min()
  33: # these only return values
  34: # which month was it
  35: # use idxmax() - index of the max value
  36: flights_by_month['DISTANCE'].aggregate(np.sum).max()
  37: flights_by_month['DISTANCE'].aggregate(np.sum).idxmax()
  38: # but which month was it that had the least miles travelled
  39: flights_by_month['DISTANCE'].aggregate(np.sum).min()
  40: flights_by_month['DISTANCE'].aggregate(np.sum).idxmin()
  41: # how many flights we cancalled each month
  42: flights_by_month['CANCELLED'].aggregate(np.sum)
  43: flights_by_month['CANCELLED'].aggregate(np.sum).max
  44: flights_by_month['CANCELLED'].aggregate(np.sum).max()
  45: flights_by_month['CANCELLED'].aggregate(np.sum).idxmax()
  46: # ------------------------------------------------------- #
  47: %history -g -f aggregating_data.py
