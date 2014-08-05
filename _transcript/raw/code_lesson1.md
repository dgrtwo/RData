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



To organize different R projects and to have a special directory for this R lesson, I created a directory called ``Rlesson`` on my Desktop. Setting the working directory could be done via graphical user interface (in RStudio) or command line interface:



If you do not change your working directory, later on you may ended up with a cluttered desktop, lost files, or worse.

We would like know if there are any object in the current R session. In RStudio, we can click on the `Environment` tab to see this list, or simply type:





We see that there are three objects, namely test1, test2, and test3. Note that you may see a different list (or an empty list) if there is no object in your current R session.

You may want to delete an object to clear up the working environment. Let's first delete `test1`:



If you want to delete every object currently available, you can use `ls()`:



Let's make sure all objects have been removed:



The `character(0)` means you do not have any objects in the current R session.

<a name="segment2"></a>

Segment 2: Variables
------------

The most basic and crucial element of R would be a variable, which could be assigned a single number, a vector, a matrix, a data frame, and others. Technically speaking, variables can be thought of as containers which refer to any type of objects, such as data structures.

Let's first assign numbers or characters to variables. We can simply assign a single number, such as 42, to a variable:



This gives the variable `my.number` a value of 42. You can show the value of my.number with a print command:



Note that variable names consist of letters, digits, periods and underscores (_), and cannot start with a digit. Do not use other special characters or space in a variable name.

Not all values you could want to store in R are numeric. You could store a string of characters using either single or double quotation marks.



We can print one of these variables:



Primitively, R could be used as a scientific calculator. For example, we can add two numbers:



and we could assign the result of the calculation to a variable:



A math operation could be done using two numeric variables. For instance, we can create another variable `y`:



R has many built-in mathematical and statistical functions that are intuitively named and easy to use. You can use exponentiation:



or calculate a natural logarithmic value by using a function `log()`:



<a name="segment3"></a>

Segment 3: Vectors
-----------

As R is built for analyzing large data, we must learn how to handle a sequence of numbers or a matrix of numbers. Let’s first look at a sequence of numbers stored in a vector. Instead of storing a single numeric value, we can create a vector consisting of multiple numeric values by using a function `c()`.



This function can also be used to combine two vectors, such as `v1` and `v2`, into a variable `v3`:



When we have a vector with more than one value, we can subset the vector using square brackets. Enter an index within square brackets following a variable to retrieve a single value corresponding to this index. Here we look at `v3`, and we only want to get the second element.



Similarly, you may use a sequence of indices to retrieve a sequence of values corresponding to those indices. Here we look at the second and third elements of vector `v3`.



Lastly, you can store the output of subsetting into another variable:



A lot of statistical programming in R relies on mathematical operations applied to a vector or a matrix. Basic calculator-like functions may apply to all elements in a given vector. We could add the numeric value 2 to a vector `v1`:



We could also take the trigonometric function `sin` and apply it to the vector `v1`:



Now, we have a vector which consists of multiple numeric values and math operations that work element-wise. If needed, we may apply an operation on a subset of a vector:



Note that an equivalent result can be obtained by firstly applying a desired math operation to a vector and retrieving a subset of the result:



You can also perform operations between two vectors. If two vectors are of the same length, corresponding elements will be used. We could multiply `v1` and `v2`:



See that the first element of v1



and the first element of v2



were multiplied, resulting in the first element of the output. The second element of v1 and the second element of v2 were multiplied, resulting in the second element of the output, and so on.

A dot product, or an inner product, which is a sum of the products of corresponding elements in two vectors, can be computed by



Dot products requires that two vectors must have a same length. Otherwise, you will get an error:



When in doubt, check the length of a vector. We can look at the length of `v1`, or of `v3`:





You may wonder what happens when you apply a math function to a character variable we made previously. Conveniently, R will prohibit you from using math operations on a character vector, since it simply does not make sense. For example, we created the character vector `chv2` earlier, and we get an error if we try adding a number to it.



However, it may not be obvious whether a variable is numeric or not. You can verify the class of a variable using the function `class`.



Some numeric values may be stored in a character vector. For example, patient numbers could be simply stored for an identification purpose and years may be used as ordinal categories. Whether to assign a number 42 versus a character “42” depends entirely on the context. For example, we could create a variable `v4`, and assign `"10"` and `"42"` as its contents:



Note that double quotation marks make it a character vector. And since R thinks `v4` is a character vector, an attempt to apply a math operation will give an error.



If you would like to use numeric values in a character vector, we can tell R to treat `v4` as numbers.



Now we can check the class of `v4`, which has changed to numeric, and we can perform numeric operations on it.



Of course, this forcefully changes the class and therefore you should be careful in using this function.

The function `summary` provides an easy way to get the feel of data. For a numeric vector, we get six descriptive statistics. For instance, `summary` of `v3`



calculates the mean, median, minimum, max, and other summary statistics.

Depending on the class, `summary` provides different outputs.



R includes a number of built-in functions to compute various statistics. Many of these are only applicable to numeric values. For instance, we could get the mean or variance:



The quantile function provides the 0, 25th, 50th, 75th, and 100th quantile of the vector:



Other widely used functions include `sum`, `median`, `sd`, `max`, `min`, and others.



Elements in a vector have names, which you can access using the function `names`:



`NULL` here implies that the elements in `v3` currently do not have names. We can assign names using `=`:



Now we can look at `v2` and see that the names are part of the output:



or we can simply extract the names by themselves:



<a name="segment4"></a>

Segment 4: Matrix
---------------

Matrices are like two-dimensional vectors, organizing values into rows and columns. For example, each row may represent a patient, whereas each column contains biomedical characteristics. If you pick one row, you would get all information about the particular patient. If you examine one column, you would get one of many biomedical characteristics about all patients in the matrix.

Whereas vectors in previous sections had only one row, indicated by `[1]`, a matrix may contain multiple rows.

Before we create a matrix, let’s quickly look at how a sequence of numbers are generated using a colon. We can create a sequence 1 through 6:



To generate a more complicated series of numbers, we could use a function called `seq`, standing for "sequence". For example, to generate the sequence of numbers from 1 to 12, incremented by 4, we would do:



We can make a sequence of numbers into a matrix, by using a function `matrix`. For instance, we can create a matrix with three rows and two columns:



Let's create another matrix `mb`:



Note that a matrix cannot contain multiple data types. In our case, `ma` and `mb` exclusively contain numeric values.

Sometimes we'd like to combine different matrices and vectors. `cbind` and `rbind` functions stand for column binding and row binding. It could be used to combine any combination of vectors and matrices, as long as their lengths and dimensions are comparable. Here, we can bind rows of `ma` with a new vector:



Or we can combine `ma` and `mb` into a new matrix:



See that the matrix `m` has columns of `ma` followed by columns of `mb`.

Try to row-bind `ma` and `mb`. Because `ma` is a 3-by-2 matrix and `mb` is a 3-by-1 matrix, R returns an error stating that two matrices do not have the same number of columns.



To extract one value, or a set of values, from a matrix, use square brackets with both row and column indices such as [index of row, index of column].
If we would like to know the element in the first row and the third column:



We can also use a sequence of numbers generated with a colon operator within square brackets. Here I would like to know the values in the first row:



Leaving the "row" spot or the "column" spot empty will extract, respectively, an entire column or an entire row.



We could also get multiple rows or columns. Here I can retrieve the first and second columns



Importantly, you will get an error if you enter an index of row or column that is out of bounds.



The matrix `m` does not have a fifth row, which leads to an error.

Of course, if you have a large matrix or have recently loaded a matrix, you may want to ask R the number of rows or the number of columns for your matrix. `nrow` is a function that computes the number of rows of a matrix, `ncol` computes the number of columns.



You can also use the function `dim`, short for dimensions, to return both the number of rows and the number of columns.



Matrices being two-dimensional, we could flip the columns and the rows. Such operation is called transpose and is used often in statistics. Simply use the `t` function to transpose a matrix:



Compare it with the original matrix `m`:



We see that the first row has become the first column in the transposed matrix.

Sometimes the diagonal elements, which are located at [1,1], [2,2], and so on, may contain significant information about the data. Therefore, R provides a quick way to extract those values, using the function `diag`.



The `diag` function behaves differently based on an input. As we just saw, with a matrix, `diag` will return a vector of diagonal elements.

For a single numeric value, it will create an identity matrix, which is a square matrix with 1s in the diagonal positions.



For a vector, it will create a diagonal matrix whose diagonal elements are derived from an input vector. The square matrix then would have both the number of rows and columns matching the length of an input vector.



Basic math functions from the beginning of this course can be readily applied to matrices. You can add, subtract, multiply, or divide each element in a matrix by a single numeric value.



You can also perform matrix multiplication. Let's create a new matrix, `m2`, with 3 rows:



Now we can multiply `m` with `m2`:



Note that each element in `m3` is a dot product between a row in `m` and a column in `m2`.

<a name="segment5"></a>

Segment 5: Lists and Data Frames
-------------

While matrices are extremely useful for processing and storing a large dataset, matrices have several limitations that may not suit our needs. For example, what do we do if we would like to put together columns of numeric values and of characters in the same structure? Matrices will force numeric values into characters because only one data type is allowed. Both lists and data frames are more flexible data structures and will allow different data types to be assigned to a single variable.

In R, a list is a vector containing other objects which may be of different data types and of different lengths. Let’s combine multiple variables we have created into a single list. To do this we use a function called `list`, and give it items we have created before:



We could also assign names to objects within a list:



We can slice a list by its index:



This output is still a list containing the first member:



If you would like to extract the content, you need to use *two* sets of square brackets



Alternatively, the content of a member in a list can be accessed by its name. We can learn the names of a list with the `names` function:



And can use a dollar sign ($) to extract one member of the list:



Data frames are lists with a set of restrictions. Most precisely, a data frame is a list of vectors which are conveniently arranged as columns. All vectors or columns in a data frame must have the same length. With statistical programming in mind, data frames mimic matrices when needed and appropriate. Most functions, such as `colnames`, `cbind`, and `dim`, used for a matrix are also applicable to data frames.

R comes with built-in datasets that can be retrieved by name, using `data` function. In this class, we are going to utilize `mtcars`, a dataset built into R.



`mtcars` contains statistics about 32 cars in 1974, including miles per gallon, weight, number of cylinders, and others. Each row is one car, and each column one of characteristics.

You can see a help file about `mtcars` with:



RStudio provides a functionality to display the data in a spreadsheet, using the `View(function)`.



However, you might not want to look at all the data points in a data frame. One of the most useful functions is `head`, which shows the first 6 rows of a data frame. Since the data may be very large, it is a good way to get an idea of its contents:



Just how we obtained summary statistics of a vector, we can apply `summary` function to a data frame:



See that each column is summarized independently, and for each column, we get the six summary statistics, such as `min`, `max`, `median`, and `mean`.

As a data frame can be thought of as a list of vectors that have the same length, we can also access each column by their names.



Note that this is equivalent to looking at the column names:



You can retrieve a specific column by name. For instance, we could look just at miles per gallon (`mpg`):



Rather than using the dollar sign ($), we could also access the column like



Alternatively, we can use the column index within square brackets to subset a column from a data frame. This is identical to how we subset a matrix. To get just the first column:



We can obtain multiple rows at once as well:



<a name="segment6"></a>

Segment 6: Logical Vectors and Operators
-------------

Another type of variable is a logical value: `TRUE` or `FALSE`. We can create a logical vector or matrix, as well as using mathematical operations, such as inequalities, on numbers to dynamically generate logical variables.

Using the function `c`, we can make a vector of logical values. Note that TRUE and FALSE are not wrapped by quotation marks.



Note that the class of `y` is "logical":



Note that `TRUE` and `FALSE`, being capitalized, are reserved and treated specially by R. Therefore, you can not and should not name your variable `TRUE` or `FALSE`.

You can compare numeric values in a vector with any value you choose:



If you apply a logical operator to a matrix, it will work on each element. Here we ask which elements of `m` are greater than or equal to 5.



However, what if you want "all automatic cars" from the `mtcars` dataset, or "all cars with mpg > 20"? We can first ask R which elements of `mtcars$mpg` is greater than 20:



This logical vector can be used to subset rows of the data frame. `TRUE` means "keep the row", `FALSE` means drop it. Place this before the comma in the square brackets:



Alternatively, and more concisely, we could also put the expression directly in front of the comma:



You can combine multiple conditions using `&` (and) or `|` (or), such as looking for automatic gearshift cars with `mpg` > 20. Here we provide two conditions: that the mpg is greater than 20, and that the gearshift is automatic:



Then we can look at the first few rows of `efficient.auto`:



We can confirm they have `mpg` greater than 20 and `am` equal to 0.
