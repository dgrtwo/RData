---
layout: default
---

Lesson 1: Variables and Data Structures
==================



<a name="segment1"></a>

Segment 1: Fundamentals
------------

Hi, my name is Neo Christopher Chung and I am a Ph.D. candidate at Princeton University. Today, I will help you understand the basics of statistical programming in R. R is the de facto standard language for data analysis and development of statistical software. Please make sure that you have already installed R and RStudio on your computer. It will be very important for you to follow each step in R and to make sure you have gotten the correct results.

After opening RStudio, it is essential to set up your working environment. Mainly, we would like to set up the working directory and to remove all objects in the current R session, so we can start fresh. The working directory is a default location on your computer that R is pointing at. If you want to save or load a file, you need to know what the current working directory is.

You can either look right above the console in RStudio, or type in:


{% highlight r %}
getwd()
{% endhighlight %}

To organize different R projects and to have a special directory for this R lesson, I created a directory called ``Rlesson`` on my Desktop. Setting the working directory could be done via graphical user interface (in RStudio) or command line interface:


{% highlight r %}
setwd("~/Desktop/Rlesson")
{% endhighlight %}

If you do not change your working directory, later on you may ended up with a cluttered desktop, lost files, or worse.

We would like know if there are any object in the current R session. In RStudio, we can click on the `Environment` tab to see this list, or simply type:




{% highlight r %}
ls()
{% endhighlight %}



{% highlight text %}
## [1] "base.url" "fig.path" "test1"    "test2"    "test3"
{% endhighlight %}

We see that there are three objects, namely test1, test2, and test3. Note that you may see a different list (or an empty list) if there is no object in your current R session.

You may want to delete an object to clear up the working environment. Let's first delete `test1`:


{% highlight r %}
rm(test1)
{% endhighlight %}

If you want to delete every object currently available, you can use `ls()`:


{% highlight r %}
rm(list=ls())
{% endhighlight %}

Let's make sure all objects have been removed:


{% highlight r %}
ls()
{% endhighlight %}



{% highlight text %}
## character(0)
{% endhighlight %}

The `character(0)` means you do not have any objects in the current R session.

<a name="segment2"></a>

Segment 2: Variables
------------

The most basic and crucial element of R would be a variable, which could be assigned a single number, a vector, a matrix, a data frame, and others. Technically speaking, variables can be thought of as containers which refer to any type of objects, such as data structures.

Let's first assign numbers or characters to variables. We can simply assign a single number, such as 42, to a variable:


{% highlight r %}
my.number = 42
{% endhighlight %}

This gives the variable `my.number` a value of 42. You can show the value of my.number with a print command:


{% highlight r %}
print(my.number)
{% endhighlight %}



{% highlight text %}
## [1] 42
{% endhighlight %}

Note that variable names consist of letters, digits, periods and underscores (_), and cannot start with a digit. Do not use other special characters or space in a variable name.

Not all values you could want to store in R are numeric. You could store a string of characters using either single or double quotation marks.


{% highlight r %}
chv1 = "hello"
chv2 = "world"
{% endhighlight %}

We can print one of these variables:


{% highlight r %}
print(chv1)
{% endhighlight %}



{% highlight text %}
## [1] "hello"
{% endhighlight %}

Primitively, R could be used as a scientific calculator. For example, we can add two numbers:


{% highlight r %}
6+4
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}

and we could assign the result of the calculation to a variable:


{% highlight r %}
x = 6+4
print(x)
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}

A math operation could be done using two numeric variables. For instance, we can create another variable `y`:


{% highlight r %}
y = 4
x / y
{% endhighlight %}



{% highlight text %}
## [1] 2.5
{% endhighlight %}

R has many built-in mathematical and statistical functions that are intuitively named and easy to use. You can use exponentiation:


{% highlight r %}
x^2
{% endhighlight %}



{% highlight text %}
## [1] 100
{% endhighlight %}

or calculate a natural logarithmic value by using a function `log()`:


{% highlight r %}
log(x)
{% endhighlight %}



{% highlight text %}
## [1] 2.303
{% endhighlight %}

<a name="segment3"></a>

Segment 3: Vectors
-----------

As R is built for analyzing large data, we must learn how to handle a sequence of numbers or a matrix of numbers. Let’s first look at a sequence of numbers stored in a vector. Instead of storing a single numeric value, we can create a vector consisting of multiple numeric values by using a function `c()`.


{% highlight r %}
v1 = c(1, 5.5, 1e2)
v2 = c(0.14, 0, -2)
{% endhighlight %}

This function can also be used to combine two vectors, such as `v1` and `v2`, into a variable `v3`:


{% highlight r %}
v3 = c(v1, v2)
v3
{% endhighlight %}



{% highlight text %}
## [1]   1.00   5.50 100.00   0.14   0.00  -2.00
{% endhighlight %}

When we have a vector with more than one value, we can subset the vector using square brackets. Enter an index within square brackets following a variable to retrieve a single value corresponding to this index. Here we look at `v3`, and we only want to get the second element.


{% highlight r %}
v3[2]
{% endhighlight %}



{% highlight text %}
## [1] 5.5
{% endhighlight %}

Similarly, you may use a sequence of indices to retrieve a sequence of values corresponding to those indices. Here we look at the second and third elements of vector `v3`.


{% highlight r %}
v3[c(2,3)]
{% endhighlight %}



{% highlight text %}
## [1]   5.5 100.0
{% endhighlight %}

Lastly, you can store the output of subsetting into another variable:


{% highlight r %}
v3_sub = v3[c(2,3)]
{% endhighlight %}

A lot of statistical programming in R relies on mathematical operations applied to a vector or a matrix. Basic calculator-like functions may apply to all elements in a given vector. We could add the numeric value 2 to a vector `v1`:


{% highlight r %}
v1 + 2
{% endhighlight %}



{% highlight text %}
## [1]   3.0   7.5 102.0
{% endhighlight %}

We could also take the trigonometric function `sin` and apply it to the vector `v1`:


{% highlight r %}
sin(v1)
{% endhighlight %}



{% highlight text %}
## [1]  0.8415 -0.7055 -0.5064
{% endhighlight %}

Now, we have a vector which consists of multiple numeric values and math operations that work element-wise. If needed, we may apply an operation on a subset of a vector:


{% highlight r %}
sin(v1[2])
{% endhighlight %}



{% highlight text %}
## [1] -0.7055
{% endhighlight %}

Note that an equivalent result can be obtained by firstly applying a desired math operation to a vector and retrieving a subset of the result:


{% highlight r %}
sin(v1)[2]
{% endhighlight %}



{% highlight text %}
## [1] -0.7055
{% endhighlight %}

You can also perform operations between two vectors. If two vectors are of the same length, corresponding elements will be used. We could multiply `v1` and `v2`:


{% highlight r %}
v1 * v2
{% endhighlight %}



{% highlight text %}
## [1]    0.14    0.00 -200.00
{% endhighlight %}

See that the first element of v1


{% highlight r %}
v1
{% endhighlight %}



{% highlight text %}
## [1]   1.0   5.5 100.0
{% endhighlight %}

and the first element of v2


{% highlight r %}
v2
{% endhighlight %}



{% highlight text %}
## [1]  0.14  0.00 -2.00
{% endhighlight %}

were multiplied, resulting in the first element of the output. The second element of v1 and the second element of v2 were multiplied, resulting in the second element of the output, and so on.

A dot product, or an inner product, which is a sum of the products of corresponding elements in two vectors, can be computed by


{% highlight r %}
v1 %*% v2
{% endhighlight %}



{% highlight text %}
##        [,1]
## [1,] -199.9
{% endhighlight %}

Dot products requires that two vectors must have a same length. Otherwise, you will get an error:


{% highlight r %}
v1 %*% v3
{% endhighlight %}



{% highlight text %}
## Error: non-conformable arguments
{% endhighlight %}

When in doubt, check the length of a vector. We can look at the length of `v1`, or of `v3`:


{% highlight r %}
length(v1)
{% endhighlight %}



{% highlight text %}
## [1] 3
{% endhighlight %}


{% highlight r %}
length(v3)
{% endhighlight %}



{% highlight text %}
## [1] 6
{% endhighlight %}

You may wonder what happens when you apply a math function to a character variable we made previously. Conveniently, R will prohibit you from using math operations on a character vector, since it simply does not make sense. For example, we created the character vector `chv2` earlier, and we get an error if we try adding a number to it.


{% highlight r %}
chv2 + 10
{% endhighlight %}



{% highlight text %}
## Error: non-numeric argument to binary operator
{% endhighlight %}

However, it may not be obvious whether a variable is numeric or not. You can verify the class of a variable using the function `class`.


{% highlight r %}
class(v2)
{% endhighlight %}



{% highlight text %}
## [1] "numeric"
{% endhighlight %}



{% highlight r %}
class(chv2)
{% endhighlight %}



{% highlight text %}
## [1] "character"
{% endhighlight %}

Some numeric values may be stored in a character vector. For example, patient numbers could be simply stored for an identification purpose and years may be used as ordinal categories. Whether to assign a number 42 versus a character “42” depends entirely on the context. For example, we could create a variable `v4`, and assign `"10"` and `"42"` as its contents:


{% highlight r %}
v4 = c("10", "42")
{% endhighlight %}

Note that double quotation marks make it a character vector. And since R thinks `v4` is a character vector, an attempt to apply a math operation will give an error.


{% highlight r %}
v4 / 10
{% endhighlight %}



{% highlight text %}
## Error: non-numeric argument to binary operator
{% endhighlight %}

If you would like to use numeric values in a character vector, we can tell R to treat `v4` as numbers.


{% highlight r %}
v4 = as.numeric(v4)
{% endhighlight %}

Now we can check the class of `v4`, which has changed to numeric, and we can perform numeric operations on it.


{% highlight r %}
class(v4)
{% endhighlight %}



{% highlight text %}
## [1] "numeric"
{% endhighlight %}



{% highlight r %}
v4 / 10
{% endhighlight %}



{% highlight text %}
## [1] 1.0 4.2
{% endhighlight %}

Of course, this forcefully changes the class and therefore you should be careful in using this function.

The function `summary` provides an easy way to get the feel of data. For a numeric vector, we get six descriptive statistics. For instance, `summary` of `v3`


{% highlight r %}
summary(v3)
{% endhighlight %}



{% highlight text %}
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   -2.00    0.04    0.57   17.40    4.38  100.00
{% endhighlight %}

calculates the mean, median, minimum, max, and other summary statistics.

Depending on the class, `summary` provides different outputs.


{% highlight r %}
summary(chv2)
{% endhighlight %}



{% highlight text %}
##    Length     Class      Mode 
##         1 character character
{% endhighlight %}

R includes a number of built-in functions to compute various statistics. Many of these are only applicable to numeric values. For instance, we could get the mean or variance:


{% highlight r %}
mean(v3)
{% endhighlight %}



{% highlight text %}
## [1] 17.44
{% endhighlight %}



{% highlight r %}
var(v3)
{% endhighlight %}



{% highlight text %}
## [1] 1642
{% endhighlight %}

The quantile function provides the 0, 25th, 50th, 75th, and 100th quantile of the vector:


{% highlight r %}
quantile(v3)
{% endhighlight %}



{% highlight text %}
##      0%     25%     50%     75%    100% 
##  -2.000   0.035   0.570   4.375 100.000
{% endhighlight %}

Other widely used functions include `sum`, `median`, `sd`, `max`, `min`, and others.


{% highlight r %}
sum(v3)
{% endhighlight %}



{% highlight text %}
## [1] 104.6
{% endhighlight %}



{% highlight r %}
median(v3)
{% endhighlight %}



{% highlight text %}
## [1] 0.57
{% endhighlight %}



{% highlight r %}
sd(v3)  # standard deviation
{% endhighlight %}



{% highlight text %}
## [1] 40.52
{% endhighlight %}



{% highlight r %}
max(v3)
{% endhighlight %}



{% highlight text %}
## [1] 100
{% endhighlight %}



{% highlight r %}
min(v3)
{% endhighlight %}



{% highlight text %}
## [1] -2
{% endhighlight %}

Elements in a vector have names, which you can access using the function `names`:


{% highlight r %}
names(v3)
{% endhighlight %}



{% highlight text %}
## NULL
{% endhighlight %}

`NULL` here implies that the elements in `v3` currently do not have names. We can assign names using `=`:


{% highlight r %}
names(v2) = c("Cat", "Dog", "Rat")
{% endhighlight %}

Now we can look at `v2` and see that the names are part of the output:


{% highlight r %}
v2
{% endhighlight %}



{% highlight text %}
##   Cat   Dog   Rat 
##  0.14  0.00 -2.00
{% endhighlight %}

or we can simply extract the names by themselves:


{% highlight r %}
names(v2)
{% endhighlight %}



{% highlight text %}
## [1] "Cat" "Dog" "Rat"
{% endhighlight %}

<a name="segment4"></a>

Segment 4: Matrix
---------------

Matrices are like two-dimensional vectors, organizing values into rows and columns. For example, each row may represent a patient, whereas each column contains biomedical characteristics. If you pick one row, you would get all information about the particular patient. If you examine one column, you would get one of many biomedical characteristics about all patients in the matrix.

Whereas vectors in previous sections had only one row, indicated by `[1]`, a matrix may contain multiple rows.

Before we create a matrix, let’s quickly look at how a sequence of numbers are generated using a colon. We can create a sequence 1 through 6:


{% highlight r %}
1:6
{% endhighlight %}



{% highlight text %}
## [1] 1 2 3 4 5 6
{% endhighlight %}

To generate a more complicated series of numbers, we could use a function called `seq`, standing for "sequence". For example, to generate the sequence of numbers from 1 to 12, incremented by 4, we would do:


{% highlight r %}
seq(from=1, to=12, by=4)
{% endhighlight %}



{% highlight text %}
## [1] 1 5 9
{% endhighlight %}

We can make a sequence of numbers into a matrix, by using a function `matrix`. For instance, we can create a matrix with three rows and two columns:


{% highlight r %}
ma = matrix(1:6, nrow=3, ncol=2)
ma
{% endhighlight %}



{% highlight text %}
##      [,1] [,2]
## [1,]    1    4
## [2,]    2    5
## [3,]    3    6
{% endhighlight %}

Let's create another matrix `mb`:


{% highlight r %}
mb = matrix(7:9, nrow=3, ncol=1)
mb
{% endhighlight %}



{% highlight text %}
##      [,1]
## [1,]    7
## [2,]    8
## [3,]    9
{% endhighlight %}

Note that a matrix cannot contain multiple data types. In our case, `ma` and `mb` exclusively contain numeric values.

Sometimes we'd like to combine different matrices and vectors. `cbind` and `rbind` functions stand for column binding and row binding. It could be used to combine any combination of vectors and matrices, as long as their lengths and dimensions are comparable. Here, we can bind rows of `ma` with a new vector:


{% highlight r %}
rbind(ma, c(100, 200, 300))
{% endhighlight %}



{% highlight text %}
## Warning: number of columns of result is not a multiple of vector length
## (arg 2)
{% endhighlight %}



{% highlight text %}
##      [,1] [,2]
## [1,]    1    4
## [2,]    2    5
## [3,]    3    6
## [4,]  100  200
{% endhighlight %}

Or we can combine `ma` and `mb` into a new matrix:


{% highlight r %}
m = cbind(ma, mb)
m
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    4    7
## [2,]    2    5    8
## [3,]    3    6    9
{% endhighlight %}

See that the matrix `m` has columns of `ma` followed by columns of `mb`.

Try to row-bind `ma` and `mb`. Because `ma` is a 3-by-2 matrix and `mb` is a 3-by-1 matrix, R returns an error stating that two matrices do not have the same number of columns.


{% highlight r %}
rbind(ma, mb)
{% endhighlight %}



{% highlight text %}
## Error: number of columns of matrices must match (see arg 2)
{% endhighlight %}

To extract one value, or a set of values, from a matrix, use square brackets with both row and column indices such as [index of row, index of column].
If we would like to know the element in the first row and the third column:


{% highlight r %}
m[1, 3]
{% endhighlight %}



{% highlight text %}
## [1] 7
{% endhighlight %}

We can also use a sequence of numbers generated with a colon operator within square brackets. Here I would like to know the values in the first row:


{% highlight r %}
m[1, 1:3]
{% endhighlight %}



{% highlight text %}
## [1] 1 4 7
{% endhighlight %}

Leaving the "row" spot or the "column" spot empty will extract, respectively, an entire column or an entire row.


{% highlight r %}
m[1, ]
{% endhighlight %}



{% highlight text %}
## [1] 1 4 7
{% endhighlight %}

We could also get multiple rows or columns. Here I can retrieve the first and second columns


{% highlight r %}
m[, 1:2]
{% endhighlight %}



{% highlight text %}
##      [,1] [,2]
## [1,]    1    4
## [2,]    2    5
## [3,]    3    6
{% endhighlight %}

Importantly, you will get an error if you enter an index of row or column that is out of bounds.


{% highlight r %}
m[5, ]
{% endhighlight %}



{% highlight text %}
## Error: subscript out of bounds
{% endhighlight %}

The matrix `m` does not have a fifth row, which leads to an error.

Of course, if you have a large matrix or have recently loaded a matrix, you may want to ask R the number of rows or the number of columns for your matrix. `nrow` is a function that computes the number of rows of a matrix, `ncol` computes the number of columns.


{% highlight r %}
nrow(m)
{% endhighlight %}



{% highlight text %}
## [1] 3
{% endhighlight %}



{% highlight r %}
ncol(m)
{% endhighlight %}



{% highlight text %}
## [1] 3
{% endhighlight %}

You can also use the function `dim`, short for dimensions, to return both the number of rows and the number of columns.


{% highlight r %}
dim(m)
{% endhighlight %}



{% highlight text %}
## [1] 3 3
{% endhighlight %}

Matrices being two-dimensional, we could flip the columns and the rows. Such operation is called transpose and is used often in statistics. Simply use the `t` function to transpose a matrix:


{% highlight r %}
t(m)
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    4    5    6
## [3,]    7    8    9
{% endhighlight %}

Compare it with the original matrix `m`:


{% highlight r %}
m
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    4    7
## [2,]    2    5    8
## [3,]    3    6    9
{% endhighlight %}

We see that the first row has become the first column in the transposed matrix.

Sometimes the diagonal elements, which are located at [1,1], [2,2], and so on, may contain significant information about the data. Therefore, R provides a quick way to extract those values, using the function `diag`.


{% highlight r %}
diag(m)
{% endhighlight %}



{% highlight text %}
## [1] 1 5 9
{% endhighlight %}

The `diag` function behaves differently based on an input. As we just saw, with a matrix, `diag` will return a vector of diagonal elements.

For a single numeric value, it will create an identity matrix, which is a square matrix with 1s in the diagonal positions.


{% highlight r %}
diag(3)
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    0    0
## [2,]    0    1    0
## [3,]    0    0    1
{% endhighlight %}

For a vector, it will create a diagonal matrix whose diagonal elements are derived from an input vector. The square matrix then would have both the number of rows and columns matching the length of an input vector.


{% highlight r %}
diag(c(1,2,3))
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    0    0
## [2,]    0    2    0
## [3,]    0    0    3
{% endhighlight %}

Basic math functions from the beginning of this course can be readily applied to matrices. You can add, subtract, multiply, or divide each element in a matrix by a single numeric value.


{% highlight r %}
m + 3
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    4    7   10
## [2,]    5    8   11
## [3,]    6    9   12
{% endhighlight %}



{% highlight r %}
m * 2
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    2    8   14
## [2,]    4   10   16
## [3,]    6   12   18
{% endhighlight %}

You can also perform matrix multiplication. Let's create a new matrix, `m2`, with 3 rows:


{% highlight r %}
m2 = matrix(21:32, nrow=3)
m2
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3] [,4]
## [1,]   21   24   27   30
## [2,]   22   25   28   31
## [3,]   23   26   29   32
{% endhighlight %}

Now we can multiply `m` with `m2`:


{% highlight r %}
m3 = m %*% m2
m3
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3] [,4]
## [1,]  270  306  342  378
## [2,]  336  381  426  471
## [3,]  402  456  510  564
{% endhighlight %}

Note that each element in `m3` is a dot product between a row in `m` and a column in `m2`.

<a name="segment5"></a>

Segment 5: Lists and Data Frames
-------------

While matrices are extremely useful for processing and storing a large dataset, matrices have several limitations that may not suit our needs. For example, what do we do if we would like to put together columns of numeric values and of characters in the same structure? Matrices will force numeric values into characters because only one data type is allowed. Both lists and data frames are more flexible data structures and will allow different data types to be assigned to a single variable.

In R, a list is a vector containing other objects which may be of different data types and of different lengths. Let’s combine multiple variables we have created into a single list. To do this we use a function called `list`, and give it items we have created before:


{% highlight r %}
list(v1,chv2,ma)
{% endhighlight %}



{% highlight text %}
## [[1]]
## [1]   1.0   5.5 100.0
## 
## [[2]]
## [1] "world"
## 
## [[3]]
##      [,1] [,2]
## [1,]    1    4
## [2,]    2    5
## [3,]    3    6
{% endhighlight %}

We could also assign names to objects within a list:


{% highlight r %}
my.list = list(numeric=v1, character=chv2, matrix=ma)
{% endhighlight %}

We can slice a list by its index:


{% highlight r %}
my.list[1]
{% endhighlight %}



{% highlight text %}
## $numeric
## [1]   1.0   5.5 100.0
{% endhighlight %}

This output is still a list containing the first member:


{% highlight r %}
class(my.list[1])
{% endhighlight %}



{% highlight text %}
## [1] "list"
{% endhighlight %}

If you would like to extract the content, you need to use *two* sets of square brackets


{% highlight r %}
my.list[[1]]
{% endhighlight %}



{% highlight text %}
## [1]   1.0   5.5 100.0
{% endhighlight %}



{% highlight r %}
class(my.list[[1]])
{% endhighlight %}



{% highlight text %}
## [1] "numeric"
{% endhighlight %}

Alternatively, the content of a member in a list can be accessed by its name. We can learn the names of a list with the `names` function:


{% highlight r %}
names(my.list)
{% endhighlight %}



{% highlight text %}
## [1] "numeric"   "character" "matrix"
{% endhighlight %}

And can use a dollar sign ($) to extract one member of the list:


{% highlight r %}
my.list$matrix
{% endhighlight %}



{% highlight text %}
##      [,1] [,2]
## [1,]    1    4
## [2,]    2    5
## [3,]    3    6
{% endhighlight %}



{% highlight r %}
class(my.list$matrix)
{% endhighlight %}



{% highlight text %}
## [1] "matrix"
{% endhighlight %}

Data frames are lists with a set of restrictions. Most precisely, a data frame is a list of vectors which are conveniently arranged as columns. All vectors or columns in a data frame must have the same length. With statistical programming in mind, data frames mimic matrices when needed and appropriate. Most functions, such as `colnames`, `cbind`, and `dim`, used for a matrix are also applicable to data frames.

R comes with built-in datasets that can be retrieved by name, using `data` function. In this class, we are going to utilize `mtcars`, a dataset built into R.


{% highlight r %}
data(mtcars)
class(mtcars)
{% endhighlight %}



{% highlight text %}
## [1] "data.frame"
{% endhighlight %}

`mtcars` contains statistics about 32 cars in 1974, including miles per gallon, weight, number of cylinders, and others. Each row is one car, and each column one of characteristics.

You can see a help file about `mtcars` with:


{% highlight r %}
?mtcars
{% endhighlight %}

RStudio provides a functionality to display the data in a spreadsheet, using the `View(function)`.


{% highlight r %}
View(mtcars)
{% endhighlight %}

However, you might not want to look at all the data points in a data frame. One of the most useful functions is `head`, which shows the first 6 rows of a data frame. Since the data may be very large, it is a good way to get an idea of its contents:


{% highlight r %}
head(mtcars)
{% endhighlight %}



{% highlight text %}
##                    mpg cyl disp  hp drat    wt  qsec vs am gear carb
## Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
## Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
## Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
## Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
## Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
{% endhighlight %}

Just how we obtained summary statistics of a vector, we can apply `summary` function to a data frame:


{% highlight r %}
summary(mtcars)
{% endhighlight %}



{% highlight text %}
##       mpg            cyl            disp             hp       
##  Min.   :10.4   Min.   :4.00   Min.   : 71.1   Min.   : 52.0  
##  1st Qu.:15.4   1st Qu.:4.00   1st Qu.:120.8   1st Qu.: 96.5  
##  Median :19.2   Median :6.00   Median :196.3   Median :123.0  
##  Mean   :20.1   Mean   :6.19   Mean   :230.7   Mean   :146.7  
##  3rd Qu.:22.8   3rd Qu.:8.00   3rd Qu.:326.0   3rd Qu.:180.0  
##  Max.   :33.9   Max.   :8.00   Max.   :472.0   Max.   :335.0  
##       drat            wt            qsec            vs       
##  Min.   :2.76   Min.   :1.51   Min.   :14.5   Min.   :0.000  
##  1st Qu.:3.08   1st Qu.:2.58   1st Qu.:16.9   1st Qu.:0.000  
##  Median :3.69   Median :3.33   Median :17.7   Median :0.000  
##  Mean   :3.60   Mean   :3.22   Mean   :17.8   Mean   :0.438  
##  3rd Qu.:3.92   3rd Qu.:3.61   3rd Qu.:18.9   3rd Qu.:1.000  
##  Max.   :4.93   Max.   :5.42   Max.   :22.9   Max.   :1.000  
##        am             gear           carb     
##  Min.   :0.000   Min.   :3.00   Min.   :1.00  
##  1st Qu.:0.000   1st Qu.:3.00   1st Qu.:2.00  
##  Median :0.000   Median :4.00   Median :2.00  
##  Mean   :0.406   Mean   :3.69   Mean   :2.81  
##  3rd Qu.:1.000   3rd Qu.:4.00   3rd Qu.:4.00  
##  Max.   :1.000   Max.   :5.00   Max.   :8.00
{% endhighlight %}

See that each column is summarized independently, and for each column, we get the six summary statistics, such as `min`, `max`, `median`, and `mean`.

As a data frame can be thought of as a list of vectors that have the same length, we can also access each column by their names.


{% highlight r %}
names(mtcars)
{% endhighlight %}



{% highlight text %}
##  [1] "mpg"  "cyl"  "disp" "hp"   "drat" "wt"   "qsec" "vs"   "am"   "gear"
## [11] "carb"
{% endhighlight %}

Note that this is equivalent to looking at the column names:


{% highlight r %}
colnames(mtcars)
{% endhighlight %}



{% highlight text %}
##  [1] "mpg"  "cyl"  "disp" "hp"   "drat" "wt"   "qsec" "vs"   "am"   "gear"
## [11] "carb"
{% endhighlight %}

You can retrieve a specific column by name. For instance, we could look just at miles per gallon (`mpg`):


{% highlight r %}
mtcars$mpg
{% endhighlight %}



{% highlight text %}
##  [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2
## [15] 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2 13.3 19.2 27.3 26.0 30.4
## [29] 15.8 19.7 15.0 21.4
{% endhighlight %}

Rather than using the dollar sign ($), we could also access the column like


{% highlight r %}
mtcars[, "mpg"]
{% endhighlight %}



{% highlight text %}
##  [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2
## [15] 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2 13.3 19.2 27.3 26.0 30.4
## [29] 15.8 19.7 15.0 21.4
{% endhighlight %}

Alternatively, we can use the column index within square brackets to subset a column from a data frame. This is identical to how we subset a matrix. To get just the first column:


{% highlight r %}
mtcars[, 1]
{% endhighlight %}



{% highlight text %}
##  [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2
## [15] 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2 13.3 19.2 27.3 26.0 30.4
## [29] 15.8 19.7 15.0 21.4
{% endhighlight %}

We can obtain multiple rows at once as well:


{% highlight r %}
mtcars[1:3, ]
{% endhighlight %}



{% highlight text %}
##                mpg cyl disp  hp drat    wt  qsec vs am gear carb
## Mazda RX4     21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag 21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
## Datsun 710    22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
{% endhighlight %}

<a name="segment6"></a>

Segment 6: Logical Vectors and Operators
-------------

Another type of variable is a logical value: `TRUE` or `FALSE`. We can create a logical vector or matrix, as well as using mathematical operations, such as inequalities, on numbers to dynamically generate logical variables.

Using the function `c`, we can make a vector of logical values. Note that TRUE and FALSE are not wrapped by quotation marks.


{% highlight r %}
y = c(TRUE, FALSE, TRUE)
y
{% endhighlight %}



{% highlight text %}
## [1]  TRUE FALSE  TRUE
{% endhighlight %}

Note that the class of `y` is "logical":


{% highlight r %}
class(y)
{% endhighlight %}



{% highlight text %}
## [1] "logical"
{% endhighlight %}

Note that `TRUE` and `FALSE`, being capitalized, are reserved and treated specially by R. Therefore, you can not and should not name your variable `TRUE` or `FALSE`.

You can compare numeric values in a vector with any value you choose:


{% highlight r %}
v2 > 0
{% endhighlight %}



{% highlight text %}
##   Cat   Dog   Rat 
##  TRUE FALSE FALSE
{% endhighlight %}

If you apply a logical operator to a matrix, it will work on each element. Here we ask which elements of `m` are greater than or equal to 5.


{% highlight r %}
m >= 5
{% endhighlight %}



{% highlight text %}
##       [,1]  [,2] [,3]
## [1,] FALSE FALSE TRUE
## [2,] FALSE  TRUE TRUE
## [3,] FALSE  TRUE TRUE
{% endhighlight %}

However, what if you want "all automatic cars" from the `mtcars` dataset, or "all cars with mpg > 20"? We can first ask R which elements of `mtcars$mpg` is greater than 20:


{% highlight r %}
mtcars$mpg > 20
{% endhighlight %}



{% highlight text %}
##  [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE  TRUE FALSE FALSE
## [12] FALSE FALSE FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE  TRUE FALSE
## [23] FALSE FALSE FALSE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE
{% endhighlight %}

This logical vector can be used to subset rows of the data frame. `TRUE` means "keep the row", `FALSE` means drop it. Place this before the comma in the square brackets:


{% highlight r %}
v = mtcars$mpg > 20
efficient.cars = mtcars[v, ]
efficient.cars
{% endhighlight %}



{% highlight text %}
##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Mazda RX4      21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag  21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
## Datsun 710     22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
## Hornet 4 Drive 21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Merc 240D      24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
## Merc 230       22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
## Fiat 128       32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
## Honda Civic    30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
## Toyota Corolla 33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
## Toyota Corona  21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
## Fiat X1-9      27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
## Porsche 914-2  26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
## Lotus Europa   30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
## Volvo 142E     21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
{% endhighlight %}

Alternatively, and more concisely, we could also put the expression directly in front of the comma:


{% highlight r %}
efficient.cars = mtcars[mtcars$mpg > 20, ]
{% endhighlight %}

You can combine multiple conditions using `&` (and) or `|` (or), such as looking for automatic gearshift cars with `mpg` > 20. Here we provide two conditions: that the mpg is greater than 20, and that the gearshift is automatic:


{% highlight r %}
efficient.auto = mtcars[mtcars$mpg > 20 & mtcars$am == 0, ]
{% endhighlight %}

Then we can look at the first few rows of `efficient.auto`:


{% highlight r %}
head(efficient.auto, 3)
{% endhighlight %}



{% highlight text %}
##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Hornet 4 Drive 21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Merc 240D      24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
## Merc 230       22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
{% endhighlight %}

We can confirm they have `mpg` greater than 20 and `am` equal to 0.
