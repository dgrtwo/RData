---
layout: default
---

Lesson 1: Variables and Data Structures
==================

<a name="segment1"></a>

Segment 1: Fundamentals
------------





{% highlight r %}
# getwd()

# setwd('~/Desktop/lesson1')

ls()

rm(test1)

ls()

rm(list = ls())

ls()
{% endhighlight %}

<a name="segment2"></a>

Segment 2: Variables
------------


{% highlight r %}
my.number = 42

my.number
{% endhighlight %}



{% highlight text %}
## [1] 42
{% endhighlight %}



{% highlight r %}

print(my.number)
{% endhighlight %}



{% highlight text %}
## [1] 42
{% endhighlight %}



{% highlight r %}

chv1 = "hello"
chv2 = "world"

print(chv1)
{% endhighlight %}



{% highlight text %}
## [1] "hello"
{% endhighlight %}



{% highlight r %}

6 + 4
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}



{% highlight r %}

x = 6 + 4
print(x)
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}



{% highlight r %}

y = 4
x/y
{% endhighlight %}



{% highlight text %}
## [1] 2.5
{% endhighlight %}



{% highlight r %}

x^2
{% endhighlight %}



{% highlight text %}
## [1] 100
{% endhighlight %}



{% highlight r %}
log(x)
{% endhighlight %}



{% highlight text %}
## [1] 2.303
{% endhighlight %}

<a name="segment3"></a>

Segment 3: Vectors
-----------


{% highlight r %}
v1 = c(1, 5.5, 100)
v2 = c(0.14, 0, -2)

v3 = c(v1, v2)
v3
{% endhighlight %}



{% highlight text %}
## [1]   1.00   5.50 100.00   0.14   0.00  -2.00
{% endhighlight %}



{% highlight r %}

v3[2]
{% endhighlight %}



{% highlight text %}
## [1] 5.5
{% endhighlight %}



{% highlight r %}

v3[c(2, 3)]
{% endhighlight %}



{% highlight text %}
## [1]   5.5 100.0
{% endhighlight %}



{% highlight r %}

v3_sub = v3[c(2, 3)]

v1 + 2
{% endhighlight %}



{% highlight text %}
## [1]   3.0   7.5 102.0
{% endhighlight %}



{% highlight r %}
sin(v1)
{% endhighlight %}



{% highlight text %}
## [1]  0.8415 -0.7055 -0.5064
{% endhighlight %}



{% highlight r %}

sin(v1[2])
{% endhighlight %}



{% highlight text %}
## [1] -0.7055
{% endhighlight %}



{% highlight r %}
sin(v1)[2]
{% endhighlight %}



{% highlight text %}
## [1] -0.7055
{% endhighlight %}



{% highlight r %}

v1 * v2
{% endhighlight %}



{% highlight text %}
## [1]    0.14    0.00 -200.00
{% endhighlight %}



{% highlight r %}
v1
{% endhighlight %}



{% highlight text %}
## [1]   1.0   5.5 100.0
{% endhighlight %}



{% highlight r %}
v2
{% endhighlight %}



{% highlight text %}
## [1]  0.14  0.00 -2.00
{% endhighlight %}



{% highlight r %}

v1 %*% v2
{% endhighlight %}



{% highlight text %}
##        [,1]
## [1,] -199.9
{% endhighlight %}



{% highlight r %}

v1 %*% v3
{% endhighlight %}



{% highlight text %}
## Error: non-conformable arguments
{% endhighlight %}



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



{% highlight r %}

chv2
{% endhighlight %}



{% highlight text %}
## [1] "world"
{% endhighlight %}



{% highlight r %}
chv2 + 10
{% endhighlight %}



{% highlight text %}
## Error: non-numeric argument to binary operator
{% endhighlight %}



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



{% highlight r %}

v4 = c("10", "42")
v4/10
{% endhighlight %}



{% highlight text %}
## Error: non-numeric argument to binary operator
{% endhighlight %}



{% highlight r %}

v4 = as.numeric(v4)
class(v4)
{% endhighlight %}



{% highlight text %}
## [1] "numeric"
{% endhighlight %}



{% highlight r %}
v4/10
{% endhighlight %}



{% highlight text %}
## [1] 1.0 4.2
{% endhighlight %}



{% highlight r %}

summary(v3)
{% endhighlight %}



{% highlight text %}
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   -2.00    0.04    0.57   17.40    4.38  100.00
{% endhighlight %}



{% highlight r %}
summary(chv2)
{% endhighlight %}



{% highlight text %}
##    Length     Class      Mode 
##         1 character character
{% endhighlight %}



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



{% highlight r %}
quantile(v3)
{% endhighlight %}



{% highlight text %}
##      0%     25%     50%     75%    100% 
##  -2.000   0.035   0.570   4.375 100.000
{% endhighlight %}



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
sd(v3)
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



{% highlight r %}

names(v3)
{% endhighlight %}



{% highlight text %}
## NULL
{% endhighlight %}



{% highlight r %}
names(v2) = c("Cat", "Dog", "Rat")
v2
{% endhighlight %}



{% highlight text %}
##   Cat   Dog   Rat 
##  0.14  0.00 -2.00
{% endhighlight %}



{% highlight r %}
names(v2)
{% endhighlight %}



{% highlight text %}
## [1] "Cat" "Dog" "Rat"
{% endhighlight %}

<a name="segment4"></a>

Segment 4: Matrix
---------------


{% highlight r %}
1:6
{% endhighlight %}



{% highlight text %}
## [1] 1 2 3 4 5 6
{% endhighlight %}



{% highlight r %}

seq(from = 1, to = 12, by = 4)
{% endhighlight %}



{% highlight text %}
## [1] 1 5 9
{% endhighlight %}



{% highlight r %}

ma = matrix(1:6, nrow = 3, ncol = 2)
ma
{% endhighlight %}



{% highlight text %}
##      [,1] [,2]
## [1,]    1    4
## [2,]    2    5
## [3,]    3    6
{% endhighlight %}



{% highlight r %}

mb = matrix(7:9, nrow = 3, ncol = 1)
mb
{% endhighlight %}



{% highlight text %}
##      [,1]
## [1,]    7
## [2,]    8
## [3,]    9
{% endhighlight %}



{% highlight r %}

rbind(ma, c(100, 200))
{% endhighlight %}



{% highlight text %}
##      [,1] [,2]
## [1,]    1    4
## [2,]    2    5
## [3,]    3    6
## [4,]  100  200
{% endhighlight %}



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



{% highlight r %}

rbind(ma, mb)
{% endhighlight %}



{% highlight text %}
## Error: number of columns of matrices must match (see arg 2)
{% endhighlight %}



{% highlight r %}

m[1, 3]
{% endhighlight %}



{% highlight text %}
## [1] 7
{% endhighlight %}



{% highlight r %}
m[1, 1:3]
{% endhighlight %}



{% highlight text %}
## [1] 1 4 7
{% endhighlight %}



{% highlight r %}
m[1, ]
{% endhighlight %}



{% highlight text %}
## [1] 1 4 7
{% endhighlight %}



{% highlight r %}
m[, 1:2]
{% endhighlight %}



{% highlight text %}
##      [,1] [,2]
## [1,]    1    4
## [2,]    2    5
## [3,]    3    6
{% endhighlight %}



{% highlight r %}
m[5, ]
{% endhighlight %}



{% highlight text %}
## Error: subscript out of bounds
{% endhighlight %}



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



{% highlight r %}
dim(m)
{% endhighlight %}



{% highlight text %}
## [1] 3 3
{% endhighlight %}



{% highlight r %}

t(m)
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    4    5    6
## [3,]    7    8    9
{% endhighlight %}



{% highlight r %}
m
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    4    7
## [2,]    2    5    8
## [3,]    3    6    9
{% endhighlight %}



{% highlight r %}

diag(m)
{% endhighlight %}



{% highlight text %}
## [1] 1 5 9
{% endhighlight %}



{% highlight r %}
diag(3)
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    0    0
## [2,]    0    1    0
## [3,]    0    0    1
{% endhighlight %}



{% highlight r %}
diag(c(1, 2, 3))
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    0    0
## [2,]    0    2    0
## [3,]    0    0    3
{% endhighlight %}



{% highlight r %}

m + 2
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    3    6    9
## [2,]    4    7   10
## [3,]    5    8   11
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



{% highlight r %}
m2 = matrix(21:32, nrow = 3)
m3 = m %*% m2
{% endhighlight %}

<a name="segment5"></a>

Segment 5: Lists and Data Frames
-------------


{% highlight r %}
list(v1, chv2, ma)
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



{% highlight r %}

my.list = list(numeric = v1, character = chv2, matrix = ma)

my.list[1]
{% endhighlight %}



{% highlight text %}
## $numeric
## [1]   1.0   5.5 100.0
{% endhighlight %}



{% highlight r %}
class(my.list[1])
{% endhighlight %}



{% highlight text %}
## [1] "list"
{% endhighlight %}



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



{% highlight r %}

names(my.list)
{% endhighlight %}



{% highlight text %}
## [1] "numeric"   "character" "matrix"
{% endhighlight %}



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



{% highlight r %}

data(mtcars)
class(mtcars)
{% endhighlight %}



{% highlight text %}
## [1] "data.frame"
{% endhighlight %}



{% highlight r %}

# ? mtcars

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



{% highlight r %}

names(mtcars)
{% endhighlight %}



{% highlight text %}
##  [1] "mpg"  "cyl"  "disp" "hp"   "drat" "wt"   "qsec" "vs"   "am"   "gear"
## [11] "carb"
{% endhighlight %}



{% highlight r %}
colnames(mtcars)
{% endhighlight %}



{% highlight text %}
##  [1] "mpg"  "cyl"  "disp" "hp"   "drat" "wt"   "qsec" "vs"   "am"   "gear"
## [11] "carb"
{% endhighlight %}



{% highlight r %}

mtcars$mpg
{% endhighlight %}



{% highlight text %}
##  [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2
## [15] 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2 13.3 19.2 27.3 26.0 30.4
## [29] 15.8 19.7 15.0 21.4
{% endhighlight %}



{% highlight r %}
mtcars[, "mpg"]
{% endhighlight %}



{% highlight text %}
##  [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2
## [15] 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2 13.3 19.2 27.3 26.0 30.4
## [29] 15.8 19.7 15.0 21.4
{% endhighlight %}



{% highlight r %}

mtcars[, 1]
{% endhighlight %}



{% highlight text %}
##  [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2
## [15] 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2 13.3 19.2 27.3 26.0 30.4
## [29] 15.8 19.7 15.0 21.4
{% endhighlight %}



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


{% highlight r %}
y = c(TRUE, FALSE, TRUE)
print(y)
{% endhighlight %}



{% highlight text %}
## [1]  TRUE FALSE  TRUE
{% endhighlight %}



{% highlight r %}
class(y)
{% endhighlight %}



{% highlight text %}
## [1] "logical"
{% endhighlight %}



{% highlight r %}

v2 > 0
{% endhighlight %}



{% highlight text %}
##   Cat   Dog   Rat 
##  TRUE FALSE FALSE
{% endhighlight %}



{% highlight r %}
m >= 5
{% endhighlight %}



{% highlight text %}
##       [,1]  [,2] [,3]
## [1,] FALSE FALSE TRUE
## [2,] FALSE  TRUE TRUE
## [3,] FALSE  TRUE TRUE
{% endhighlight %}



{% highlight r %}

mtcars$mpg > 20
{% endhighlight %}



{% highlight text %}
##  [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE  TRUE FALSE FALSE
## [12] FALSE FALSE FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE  TRUE FALSE
## [23] FALSE FALSE FALSE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE
{% endhighlight %}



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



{% highlight r %}

efficient.cars = mtcars[mtcars$mpg > 20, ]

efficient.auto = mtcars[mtcars$mpg > 20 & mtcars$am == 0, ]
head(efficient.auto, 3)
{% endhighlight %}



{% highlight text %}
##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Hornet 4 Drive 21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Merc 240D      24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
## Merc 230       22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
{% endhighlight %}

