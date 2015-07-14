---
layout: default
---

Lesson 4: Exploratory Data Analysis With data.table
===========



<a name="segment1"></a>

Segment 1: R Scripts
-----------

In these lessons so far you've learned a lot about the statistical programming language R: you've learned how to set variables and work with data structures, to create informative visualizations using ggplot2, and how to perform rigorous statistical tests. But datasets from the real world aren't so simple: they might contain dozens of variables across tens of thousands of observations. You might need to filter them based on quality considerations, and they might be spread across multiple datasets, leaving you to combine them together yourself. I'm David Robinson, and in this lesson we're going to tie all your R skills together, by learning how to perform exploratory data analysis using the powerful data.table package. As an example, we'll be analyzing a dataset of historical baseball statistics, learning how to preprocess and filter it, how to combine multiple datasets together, and how to answer interesting questions interactively with your data.

This lesson will assume basic familiarity with R, especially vectors and data frames, with RStudio, and with the ggplot2 package for visualization.

One of the essential functions of computers is to take repetitive, dull tasks and automate them, so they can be easily be performed as many times as you need. Part of being a good programmer is sticking to this philosophy.

So far we've been working in the interactive R terminal. This is useful for writing a line of code quickly and seeing the result.


{% highlight r %}
3 + 5
{% endhighlight %}



{% highlight text %}
## [1] 8
{% endhighlight %}

But most of your analyses will take multiple lines of code and they'll have to be run all in the same order, and it's impractical to have to type them all in sequence in an interactive window. So let's instead write an R script, which will contain a series of commands that you want to run in order. In RStudio, Go to File->New File->New R Script, or you can do CMD+SHIFT+N, to create a new R script. You'll see it pops up above your command prompt. Write a couple lines of R. For example, let's define two variables:


{% highlight r %}
x = 4
y = x + 6
{% endhighlight %}

Now save your new script. First you have to choose a working directory, which you can do with "More->Set as Working Directory" in the file manager in RStudio. Then save your script, which you can do with CMD+S or with the floppy disk icon here. Let's save it as `script.R` in our working directory. Now we can run this script- that is, all our commands in the script all at once- by clicking "Source" at the top of the script. Notice that a command pops up in your interactive terminal, something like


{% highlight r %}
source('~/Desktop/RCourse/script.R')
{% endhighlight %}

That means it ran all the commands in your script in a row. You can see this by checking the values of `x` and `y`:


{% highlight r %}
x
{% endhighlight %}



{% highlight text %}
## [1] 4
{% endhighlight %}



{% highlight r %}
y
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}

So even though you didn't see the commands in the interactive terminal, they did run when you hit Source.

Incidentally, there's a keyboard shortcut for sourcing a current file as well: you can do CMD+SHIFT+S.

Now what if we want some output to our script besides just setting a few variables? Normally we'd be able to view the contents of a variable just by typing that variable by itself. For instance:


{% highlight r %}
y
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}

However, try putting the line `y` by itself in your script, save, and source it. Notice there was no output. That's because when you run outside of the interactive terminal, values don't print unless you explicitly tell them to do so. You do that with the print function. Change your line in the file to `print(y)`, then save and source.


{% highlight r %}
print(y)
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}

*Now* we can see the output in your interactive window. Remember that: when you're running inside a script, if you want to see an output, you have to actually print it.

Importantly, the same is true of a ggplot2 plot. Let's create a basic ggplot:


{% highlight r %}
library(ggplot2)
{% endhighlight %}



{% highlight text %}
## Loading required package: methods
{% endhighlight %}



{% highlight r %}
data(mtcars)
ggplot(mtcars, aes(wt, mpg)) + geom_point()
{% endhighlight %}

![center](../../figs/code_lesson4/unnamed-chunk-7-1.png) 

As soon as we hit return on this line, we created a scatterplot. However, let's put the same lines of code into our script. Then we clear the current plot by hitting Clear All, and hit Source.

Notice that no plot showed up. The reason is that when it's in a file, a ggplot, just like a regular variable, needs to be printed to show up. You do that with:


{% highlight r %}
print(ggplot(mtcars, aes(wt, mpg)) + geom_point())
{% endhighlight %}

![center](../../figs/code_lesson4/unnamed-chunk-8-1.png) 

Finally, there's a useful shortcut for running one line at a time in a script. Put your cursor on a particular line of code, then hit CMD+RETURN in Macs, or CONTROL+ENTER on Windows, you'll run just that line of code in your interactive terminal. This means you don't have to select a line and copy and paste it into your terminal. This is useful for if you want to run a single line of code in your script, but don't want to go through the time of rerunning the whole file.

R scripts can be as long as you like: yours may end up being hundreds or even thousands of lines of code- and they're the only practical way to organize a complicated analysis productively.

<a name="segment2"></a>

Segment 2: Reading Data
--------------

So far we've been working with built-in datasets in R. For example, remember that we can load the `mtcars` dataset by doing


{% highlight r %}
data(mtcars)
{% endhighlight %}

R comes with dozens of useful datasets like this, and they're great for learning and practicing. But of course, whatever data you're actually interested in, chances are it's probably not already built into R. So how can you read your own data into R?

Let's start by downloading some data and reading it in. We're going to be working with a dataset about baseball: specifically the 2013 version of Sean Lahman's Baseball Archive. The statistical analysis of baseball is called sabermetrics, and it has a rich and fascinating history: this dataset can be used to explore lots of extraordinary trends. Don't worry if you're not a fan of baseball, or even if you know nothing about it: we're just using it as an example of data manipulation. I'll explain everything as we go along, and you'll have just as much fun as anyone.

So the URL for this file is [http://dgrtwo.github.io/pages/lahman/Salaries.csv](http://dgrtwo.github.io/pages/lahman/Salaries.csv). Take this URL and put it into your favorite web browser. At this point you can see the comma separated values in the dataset. Let's save it to our computer, particularly putting it into your current working directory. Make sure it's saved as a CSV file. We should now have the Salaries.csv file in your file manager in RStudio.

Let's look at the contents of this CSV file a little more closely. This is called CSV, or comma-separated value, format. It contains one header row, and then a series of lines made up of multiple fields separated by commas. This is one of the most common formats data is shared in. For instance, if you have an Excel spreadsheet, note that you can save it into CSV format.

You can read a CSV file into R easily with the `read.csv` function:


{% highlight r %}
salaries = read.csv("Salaries.csv")
{% endhighlight %}

This read in the CSV file as a data frame. You can see this by doing


{% highlight r %}
View(salaries)
{% endhighlight %}

This data is organized into rows: one row per player per year. You can see a column for the year, for the ID of the player, and for the salary in US dollars. You can also see the team that the player was playing on, and the league, either the American League (`AL`) or National League (`NL`) that the team plays in.

I had you download the file just so we could look at it, but note that you don't actually have to download it at all. R can read a CSV file directly from the internet, if you give it the URL. Take that URL we had and put it into `read.csv` directly:


{% highlight r %}
salaries = read.csv("http://dgrtwo.github.io/pages/lahman/Salaries.csv")
{% endhighlight %}

This downloads the file, reads it in, and saves it into the same data.frame.

Now, this was the best way to read this standard CSV file. But what if you didn't have a header row? Or what if your file were separated by spaces, or by tabs, instead of by commas? Take a look at the help page for `read.csv`:


{% highlight r %}
help(read.csv)
{% endhighlight %}

You can see here that there are multiple ways to use `read.csv` with different defaults and options. For example, if you didn't want to have a header, you could change the header option to `header=FALSE`. If you wanted the fields to be separated by spaces, rather than commas, you could add `sep=" "`. Don't do that in this case.

You can also see that R provides other functions such as `read.table` whose defaults are different (space separation with no header). So by choosing the right function, and the right set of specialized option, you can read almost any kind of row/column organized file.

R can't read everything. But for the majority of cases, if your data was prepared responsibly and you set these simple options correctly, you can use the `read.csv` and `read.table` functions to import whatever data you need.

<a name="segment3"></a>

Segment 3: Introduction to data.table
-------------

Now we have downloaded this data on baseball players' salaries, we're interested in filtering and manipulating it. The salary data is currently held in a data.frame, a data structure built into R. data.frame is powerful, but there's an even more powerful alternative in R that makes data manipulation fast, easy and intuitive. Like ggplot2, it's a third party package, which means it doesn't come built in, and we have to install it. So let's install the `data.table` package You can do that with:


{% highlight r %}
install.packages("data.table")
{% endhighlight %}

Now, before we learn to use data.table, let's take one last look at salaries the data.frame. If you type


{% highlight r %}
salaries
{% endhighlight %}

it will print thousands and thousands of lines until it decides to stops. Now, let's convert the data.frame into a data table. First you load the `data.table` package:


{% highlight r %}
library(data.table)
{% endhighlight %}

Then use the `as.data.table` function to replace `salaries` with a data.table version.


{% highlight r %}
salaries = as.data.table(salaries)
{% endhighlight %}

Now, let's print it again:


{% highlight r %}
salaries
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID  salary
##     1:   1985    BAL   AL murraed02 1472819
##     2:   1985    BAL   AL  lynnfr01 1090000
##     3:   1985    BAL   AL ripkeca01  800000
##     4:   1985    BAL   AL  lacyle01  725000
##     5:   1985    BAL   AL flanami01  641667
##    ---                                     
## 23952:   2013    WAS   NL matthry01  504500
## 23953:   2013    WAS   NL lombast02  501250
## 23954:   2013    WAS   NL ramoswi01  501250
## 23955:   2013    WAS   NL rodrihe03  501000
## 23956:   2013    WAS   NL moorety01  493000
{% endhighlight %}

Notice that it contains the same information, but only shows the first five rows, then ---, then the last five rows, which is generally a more convenient representation. This more compact way of printing a data.table is the first benefit of using the package.

Now, a lot of things work just the same way as they do in a data.frame. You can still access a column with a dollar sign. For instance, let's say you want the `salary` column.


{% highlight r %}
salaries$salary
{% endhighlight %}

Or to get a single row of a data.table, you can do:


{% highlight r %}
salaries[1, ]
{% endhighlight %}



{% highlight text %}
##    yearID teamID lgID  playerID  salary
## 1:   1985    BAL   AL murraed02 1472819
{% endhighlight %}

Or you can get a range of rows:


{% highlight r %}
salaries[1:5, ]
{% endhighlight %}



{% highlight text %}
##    yearID teamID lgID  playerID  salary
## 1:   1985    BAL   AL murraed02 1472819
## 2:   1985    BAL   AL  lynnfr01 1090000
## 3:   1985    BAL   AL ripkeca01  800000
## 4:   1985    BAL   AL  lacyle01  725000
## 5:   1985    BAL   AL flanami01  641667
{% endhighlight %}

One thing that did work on data frames but doesn't work on data tables is extracting a column based on an index. In a data.frame, you could extract the first column by putting the index after the comma:


{% highlight r %}
salaries[, 1]
{% endhighlight %}



{% highlight text %}
## [1] 1
{% endhighlight %}

But that doesn't work in data.table. Instead, you can put the name of the column, *without quotes*, after the comma:


{% highlight r %}
salaries[, yearID]
{% endhighlight %}

This retrieves the entire vector of that year.

You can also grab multiple columns (for example, just the year and the salary) using `list`:


{% highlight r %}
salaries[, list(yearID, salary)]
{% endhighlight %}



{% highlight text %}
##        yearID  salary
##     1:   1985 1472819
##     2:   1985 1090000
##     3:   1985  800000
##     4:   1985  725000
##     5:   1985  641667
##    ---               
## 23952:   2013  504500
## 23953:   2013  501250
## 23954:   2013  501250
## 23955:   2013  501000
## 23956:   2013  493000
{% endhighlight %}

Now we've created a new data table with just the two columns `yearID` and `salary`.

Now, let's say we want to filter the rows based on one column, which is a common step in data preprocessing. For example, let's say you want to get only the years after 2000. There is an easy way to do this in data.table. We put a condition before the comma:


{% highlight r %}
salaries[yearID > 2000, ]
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID   salary
##     1:   2001    ANA   AL vaughmo01 13166667
##     2:   2001    ANA   AL salmoti01  6500000
##     3:   2001    ANA   AL anderga01  4500000
##     4:   2001    ANA   AL erstada01  3450000
##     5:   2001    ANA   AL percitr01  3400000
##    ---                                      
## 10853:   2013    WAS   NL matthry01   504500
## 10854:   2013    WAS   NL lombast02   501250
## 10855:   2013    WAS   NL ramoswi01   501250
## 10856:   2013    WAS   NL rodrihe03   501000
## 10857:   2013    WAS   NL moorety01   493000
{% endhighlight %}

Now we've created a subset of the data that contains only years 2001 and after. Similarly, if you wanted to get salaries from a specific year, 2010, you could do


{% highlight r %}
salaries[yearID == 2010, ]
{% endhighlight %}



{% highlight text %}
##      yearID teamID lgID  playerID   salary
##   1:   2010    BAL   AL millwke01 12000000
##   2:   2010    BAL   AL roberbr01 10000000
##   3:   2010    BAL   AL  lugoju01  9250000
##   4:   2010    BAL   AL markani01  7100000
##   5:   2010    BAL   AL gonzami02  6000000
##  ---                                      
## 826:   2010    WAS   NL zimmejo01   401000
## 827:   2010    WAS   NL desmoia01   400000
## 828:   2010    WAS   NL detwiro01   400000
## 829:   2010    WAS   NL englije01   400000
## 830:   2010    WAS   NL taverwi01   400000
{% endhighlight %}

There are two leagues in American Major League Baseball: the American League (`AL`), and the National League (`NL`). If we want to filter for just the American League, we can do:


{% highlight r %}
salaries[lgID == "AL", ]
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID  salary
##     1:   1985    BAL   AL murraed02 1472819
##     2:   1985    BAL   AL  lynnfr01 1090000
##     3:   1985    BAL   AL ripkeca01  800000
##     4:   1985    BAL   AL  lacyle01  725000
##     5:   1985    BAL   AL flanami01  641667
##    ---                                     
## 11740:   2013    TOR   AL perezlu01  500000
## 11741:   2013    TOR   AL drabeky01  499500
## 11742:   2013    TOR   AL delabst01  498900
## 11743:   2013    TOR   AL jeffrje01  495900
## 11744:   2013    TOR   AL  loupaa01  494200
{% endhighlight %}

Now I've selected just the American League teams.

Finally, we can combine multiple filtering conditions using the *and* (`&`) or *or* (`|`) operators. For instance, we can filter for all the rows in the American League that were after 1990.


{% highlight r %}
salaries[lgID == "AL" & yearID >= 1990, ]
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID  salary
##     1:   1990    BAL   AL ripkeca01 1316667
##     2:   1990    BAL   AL bradlph01 1150000
##     3:   1990    BAL   AL tettlmi01  750000
##     4:   1990    BAL   AL orsuljo01  610000
##     5:   1990    BAL   AL melvibo01  350000
##    ---                                     
## 10023:   2013    TOR   AL perezlu01  500000
## 10024:   2013    TOR   AL drabeky01  499500
## 10025:   2013    TOR   AL delabst01  498900
## 10026:   2013    TOR   AL jeffrje01  495900
## 10027:   2013    TOR   AL  loupaa01  494200
{% endhighlight %}

Similarly, we can combine conditions with *or* (`|`). For instance, say we wanted only years before 1990 or after 2010.


{% highlight r %}
salaries[yearID < 1990 & yearID > 2010, ]
{% endhighlight %}



{% highlight text %}
## Empty data.table (0 rows) of 5 cols: yearID,teamID,lgID,playerID,salary
{% endhighlight %}

We can also sort the data easily, using the order function in the area before the comma:


{% highlight r %}
salaries[order(salary), ]
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID   salary
##     1:   1993    NYA   AL jamesdi01        0
##     2:   1999    PIT   NL martija02        0
##     3:   1993    NYA   AL silveda01    10900
##     4:   1994    CHA   AL  carych01    50000
##     5:   1997    FLO   NL  penaal01    50000
##    ---                                      
## 23952:   2013    NYA   AL rodrial01 29000000
## 23953:   2012    NYA   AL rodrial01 30000000
## 23954:   2011    NYA   AL rodrial01 32000000
## 23955:   2009    NYA   AL rodrial01 33000000
## 23956:   2010    NYA   AL rodrial01 33000000
{% endhighlight %}

Now you can see that the pairs of players and years are sorted by salary, with the lower salaries at the top. This gives us an easy way to see the highest and lowest salaries. In case you're wondering, NYA here is the team ID of the New York Yankees: called NYA instead of NYY for historical reasons. We could also sort by year:


{% highlight r %}
salaries[order(yearID), ]
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID  salary
##     1:   1985    BAL   AL murraed02 1472819
##     2:   1985    BAL   AL  lynnfr01 1090000
##     3:   1985    BAL   AL ripkeca01  800000
##     4:   1985    BAL   AL  lacyle01  725000
##     5:   1985    BAL   AL flanami01  641667
##    ---                                     
## 23952:   2013    WAS   NL matthry01  504500
## 23953:   2013    WAS   NL lombast02  501250
## 23954:   2013    WAS   NL ramoswi01  501250
## 23955:   2013    WAS   NL rodrihe03  501000
## 23956:   2013    WAS   NL moorety01  493000
{% endhighlight %}

What if we want to sort first by year, and *then* breaking ties with salary? We can do that by providing two arguments to the order function:


{% highlight r %}
salaries[order(yearID, salary), ]
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID   salary
##     1:   1985    BAL   AL sheetla01    60000
##     2:   1985    CAL   AL clibust02    60000
##     3:   1985    CAL   AL mccaski01    60000
##     4:   1985    CHA   AL guilloz01    60000
##     5:   1985    MIN   AL salasma01    60000
##    ---                                      
## 23952:   2013    NYA   AL teixema01 23125000
## 23953:   2013    NYA   AL sabatcc01 24285714
## 23954:   2013    NYA   AL wellsve01 24642857
## 23955:   2013    PHI   NL   leecl02 25000000
## 23956:   2013    NYA   AL rodrial01 29000000
{% endhighlight %}

Now it's organized with 1985 first, and 2013 last, but within each of those years it is organized by salary.

Note that we can perform multiple operations all in a sequence, by saving the intermediate results. For instance, we can first perform a filtering operation and save it as `salaries.filtered`:


{% highlight r %}
salaries.filtered = salaries[lgID == "AL" & yearID >= 1990, ]
{% endhighlight %}

Then we can sort it by salary and save it into a new data table, which is now both filtered and sorted.


{% highlight r %}
salaries.filtered.sorted = salaries.filtered[order(salary), ]
salaries.filtered.sorted
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID   salary
##     1:   1993    NYA   AL jamesdi01        0
##     2:   1993    NYA   AL silveda01    10900
##     3:   1994    CHA   AL  carych01    50000
##     4:   1990    BAL   AL  bellju01   100000
##     5:   1990    BAL   AL brownma03   100000
##    ---                                      
## 10023:   2013    NYA   AL rodrial01 29000000
## 10024:   2012    NYA   AL rodrial01 30000000
## 10025:   2011    NYA   AL rodrial01 32000000
## 10026:   2009    NYA   AL rodrial01 33000000
## 10027:   2010    NYA   AL rodrial01 33000000
{% endhighlight %}

These operations let us easily explore the data and answer basic questions.

<a name="segment4"></a>

Segment 4: Summarizing Data Within Groups
--------------

In our last segment we learned how to download a dataset on baseball player salaries and turn it into a data table, and then to perform some basic organizations on it like filtering and sorting. Now we're going to learn about a more sophisticated and powerful way of processing the data, namely performing summary operations within groups. This is an important and omnipresent task in data analysis.

Let's look again at our salaries dataset.


{% highlight r %}
salaries
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID  salary
##     1:   1985    BAL   AL murraed02 1472819
##     2:   1985    BAL   AL  lynnfr01 1090000
##     3:   1985    BAL   AL ripkeca01  800000
##     4:   1985    BAL   AL  lacyle01  725000
##     5:   1985    BAL   AL flanami01  641667
##    ---                                     
## 23952:   2013    WAS   NL matthry01  504500
## 23953:   2013    WAS   NL lombast02  501250
## 23954:   2013    WAS   NL ramoswi01  501250
## 23955:   2013    WAS   NL rodrihe03  501000
## 23956:   2013    WAS   NL moorety01  493000
{% endhighlight %}

Right now we have 24 thousand rows, each with a combination of a year and a player. Now, we can perform some general summaries of this data. For example, we can extract the salary column using a dollar sign ($):


{% highlight r %}
salaries$salary
{% endhighlight %}

Then we can find the average salary of all players across all years with the mean function:


{% highlight r %}
mean(salaries$salary)
{% endhighlight %}



{% highlight text %}
## [1] 1864357
{% endhighlight %}

Similarly, we could find the highest salary across all years with `max`:


{% highlight r %}
max(salaries$salary)
{% endhighlight %}



{% highlight text %}
## [1] 33000000
{% endhighlight %}

or the median:


{% highlight r %}
median(salaries$salary)
{% endhighlight %}



{% highlight text %}
## [1] 507950
{% endhighlight %}

We can also find the average salary in a given year by filtering the data before we extract the column. This code extracts the salaries only from the year 2000:


{% highlight r %}
salaries[yearID == 2000, ]$salary
{% endhighlight %}



{% highlight text %}
##   [1] 11166667  6000000  5600000  4600000  4000000  3250000  3225000
##   [8]  2500000  2350000  1512500   925000   900000   850000   600000
##  [15]   550000   375000   275000   275000   225000   222500   215000
##  [22]   210000   210000   210000   207500   207500   202500   200000
##  [29]   200000   200000 12868670  7127199  6786032  6620921  6300000
##  [36]  6000000  4600000  4250000  4209324  4146789  3000000  2500000
##  [43]  2250000  2000000  1750000  1450000  1200000   750000   700000
##  [50]   620000   500000   400000   205000   205000   204000   203500
##  [57]   201000   200000   200000 11500000  6350000  6320000  5750000
##  [64]  5000333  4500000  4500000  4000000  3750000  3700000  3500000
##  [71]  3500000  2500000  2400000  2000000  2000000  1350000   695000
##  [78]   625000   625000   612500   610000   375000   350000   295000
##  [85]   270000   250000   210000   202500   200000  7100000  5400000
##  [92]  4900000  3300000  1400000  1350000  1320000   675000   475000
##  [99]   425000   375000   325000   305000   285000   285000   275000
## [106]   255000   255000   250000   250000   250000   225000   225000
## [113]   212500   210000   206000   200000   200000   200000  8175000
## [120]  7911948  7500000  7196656  7000000  6000000  5550000  5000000
## [127]  4250000  3000000  2700000  1850000  1617667  1600000  1200000
## [134]  1125000  1062500  1000000   550000   247000   237500   232500
## [141]   227500   225000   217500   205000  7500000  7000000  4500000
## [148]  4500000  4425000  4062500  4000000  3950000  3650000  3125000
## [155]  1975000  1816667  1300000  1100000  1000000   950000   700000
## [162]   550000   325000   300000   255000   240000   236000   205000
## [169]   200000   200000   200000  4000000  2300000  2300000  2250000
## [176]  2250000  1500000  1450000  1000000   962500   575000   550000
## [183]   525000   350000   325000   250000   250000   232500   232500
## [190]   225000   225000   220000   220000   215000   210000   205000
## [197]   205000   203000   202500  3500000  2000000  1500000  1200000
## [204]  1115000   875000   825000   700000   500000   500000   322500
## [211]   300000   285000   285000   245000   240000   230000   225000
## [218]   225000   225000   220000   202000   200000   200000   200000
## [225]   200000 12357143 12000000 10000000  7250000  7000000  6500000
## [232]  6350000  6000000  5250000  4800000  2400000  1950000  1916667
## [239]  1400000  1300000  1250000  1000000   800000   750000   350000
## [246]   250000   240000   213000   206650   203800   201000   200000
## [253]   200000  5600000  4000000  3103333  3050000  3050000  2750000
## [260]  2100000  1225000   900000   825000   750000   600000   500000
## [267]   500000   290000   260000   250000   240000   240000   240000
## [274]   228000   221000   219500   217000   211000   201000   200500
## [281]  7500000  6350000  6000000  5400000  4362500  4000000  4000000
## [288]  3950000  2750000  2225000  2000000  1850000  1500000  1450000
## [295]  1425000   950000   580000   500000   325000   290000   285000
## [302]   275000   275000   252500   215000   205000  9000000  7097962
## [309]  6250000  6000000  6000000  5945818  3300000  3000000  2947410
## [316]  2373439  2000000  1850000  1000000   800000   610000   525000
## [323]   425000   375000   350000   300000   295000   270000   265000
## [330]   265000   253000   237500   230000   200000   200000   200000
## [337]   200000  8620921  8600000  7500000  6500000  5000000  5000000
## [344]  4500000  4325000  3750000  3600000  3025000  2650000  2000000
## [351]  1100000   975000   750000   750000   305000   280000   250000
## [358]   245000   230000   220000   220000   200000   200000 10000000
## [365]  6600000  5500000  5500000  3025000  2500000  1800000  1450000
## [372]   900000   800000   800000   733333   700000   683333   500000
## [379]   500000   425000   395000   383333   375000   333333   310000
## [386]   220000   205000   200000 13350000  8500000  8000000  7000000
## [393]  5625000  5375000  5250000  3375000  3333333  2831000  2500000
## [400]  2250000  1916667  1833333  1725000  1500000  1100000  1005000
## [407]  1000000   762500   750000   500000   312500   300000   260000
## [414]   243500   215000   215000 11100000  9463237  8500000  8500000
## [421]  7600000  6250000  4750000  3700000  3700000  3365099  3000000
## [428]  3000000  2975000  1650000  1400000  1000000   750000   650000
## [435]   420000   400000   350000   290000   255000   242000   220000
## [442]   207500   200000   200000   200000   200000 11000000  6000000
## [449]  5737500  5300000  4600000  4500000  3833333  3500000  2500000
## [456]  2000000  1600000  1500000  1100000  1000000  1000000   776000
## [463]   690000   625000   600000   395000   300000   265000   245000
## [470]   235000   217500   210000   205000   205000   200000   200000
## [477]  9329700  7000000  5300000  4750000  3250000  1950000  1950000
## [484]  1700000  1600000  1400000  1400000  1100000   862500   650000
## [491]   630000   600000   500000   400000   400000   375000   300000
## [498]   300000   300000   220000   200000   200000   200000 12142857
## [505]  6350000  6250000  3700000  3600000  3416667  3183333  3000000
## [512]  3000000  2350000  2212500  1750000  1500000  1300000  1200000
## [519]   933333   750000   650000   625000   560000   525000   450000
## [526]   325000   300000   300000   270000   245000   222500  7000000
## [533]  4500000  1500000   500000   390000   380000   324000   318000
## [540]   315000   295000   295000   287000   269000   268000   265000
## [547]   265000   264000   255000   255000   245000   240000   225000
## [554]   208000   204000   203000   201000   201000   200000  6750000
## [561]  6666667  6500000  5250000  5032444  4500000  3200000  2400000
## [568]  1700000  1250000  1100000  1025000   800000   700000   700000
## [575]   500000   500000   350000   330000   300000   275000   260000
## [582]   255000   252500   240000   237500   215000 15714286  9916667
## [589]  9416667  6125000  5383333  5375000  5333333  4000000  3850000
## [596]  3700000  3500000  3000000  2250000  2000000  1450000  1400000
## [603]  1250000  1000000   750000   550000   500000   475000   300000
## [610]   250000   230000   205000  5000000  5000000  4462500  3333333
## [617]  2500000  2400000  2350000  1450000  1025000   900000   835000
## [624]   800000   775000   650000   612500   515000   350000   300000
## [631]   282000   275000   260000   258000   255000   250000   235000
## [638]   215000   210000   205000   201500   200500   200000   200000
## [645]  4125000  4000000  3633333  3500000  3500000  3200000  3000000
## [652]  1350000   825000   700000   600000   355000   350000   340000
## [659]   325000   280000   267500   265000   265000   255000   225000
## [666]   218000   210000   202500   201500   201500   200000   200000
## [673]   200000 12071429  8000000  7750000  5750000  5366667  5000000
## [680]  4375000  4333333  4225000  3633333  3437500  3350000  2250000
## [687]  2200000  2050014  2000000   750000   600000   500000   500000
## [694]   462500   260000   220000   215000   210000  5900000  5650000
## [701]  5066667  4833333  4200000  3000000  2933333  2750000  2016667
## [708]  1885000  1400000  1000000   750000   600000   550000   500000
## [715]   500000   500000   475000   390000   375000   345000   300000
## [722]   280000   250000   240000   210000   205000   203000  5625000
## [729]  3290000  2750000  2250000  2166667  2050000  1816667  1000000
## [736]  1000000   875000   750000   700000   550000   450000   400000
## [743]   400000   380000   335000   320000   300000   300000   285000
## [750]   285000   230000   215000   205000  6916667  6600000  6300000
## [757]  6100000  5750000  4583333  3750000  2600000  1750000  1750000
## [764]   875000   830000   800000   775000   700000   700000   600000
## [771]   450000   370000   360000   250000   250000   250000   230000
## [778]   230000   225000   215000   208000   203000   200000 10658826
## [785]  6000000  5500000  5500000  4750000  4000000  3000000  2450000
## [792]  1550000  1450000  1325000  1325000  1175000  1125000  1000000
## [799]   537500   462500   232000   225000   225000   220000   215000
## [806]   210000   202000   200000   200000  9333333  7600000  7417981
## [813]  6000000  4500000  4420840  2867542  2500000  2300000  2250000
## [820]  1750000  1600000  1366667  1100000   750000   750000   690000
## [827]   650000   600000   595000   550000   550000   400000   250000
## [834]   240000   220000   202500
{% endhighlight %}

We can then find the average salary in the year 2000:


{% highlight r %}
mean(salaries[yearID == 2000, ]$salary)
{% endhighlight %}



{% highlight text %}
## [1] 1992985
{% endhighlight %}

This gives us a good way to ask questions interactively about our data. But what if we want to look for a trend- for example, how baseball player salaries change over time? It would be a huge hassle to repeat this line of code for 1985, 1986, 1987 and so on, and them combine all of those. What we want is a way to perform this summary operation of averaging within each year, for every year in the dataset. It turns out the data.table package makes that easy:

Let's create a new data.table called `summarized.year`, then we subset it using square brackets in a very particular way. Put nothing before the first comma. Now after the second comma, we say we want to take the mean of the salary column- but then we put another comma and `by="yearID"`, which means  we don't want to do it once for the whole dataset- we want to do it within each year. So we're computing the mean salary (`mean(salary)`), within each year (`by="yearID"`).



{% highlight r %}
summarized.year = salaries[, mean(salary), by="yearID"]
{% endhighlight %}



{% highlight text %}
## Warning in gmean(salary): Group 21 summed to more than type 'integer'
## can hold so the result has been coerced to 'numeric' automatically, for
## convenience.
{% endhighlight %}

This message in red is a warning: it's basically complaining that baseball players are paid too much. But you can ignore it, it doesn't have any effect on our results. Let's look at what ended up in `summarized.year`:


{% highlight r %}
summarized.year
{% endhighlight %}



{% highlight text %}
##     yearID        V1
##  1:   1985  476299.4
##  2:   1986  417147.0
##  3:   1987  434729.5
##  4:   1988  453171.1
##  5:   1989  506323.1
##  6:   1990  511973.7
##  7:   1991  894961.2
##  8:   1992 1047520.6
##  9:   1993  976966.6
## 10:   1994 1049588.6
## 11:   1995  964979.1
## 12:   1996 1027909.3
## 13:   1997 1218687.4
## 14:   1998 1280844.6
## 15:   1999 1485316.8
## 16:   2000 1992984.6
## 17:   2001 2279841.1
## 18:   2002 2392526.6
## 19:   2003 2573472.9
## 20:   2004 2491776.1
## 21:   2005 2633830.8
## 22:   2006 2834520.9
## 23:   2007 2941435.9
## 24:   2008 3136517.1
## 25:   2009 3277647.0
## 26:   2010 3278746.8
## 27:   2011 3318838.2
## 28:   2012 3458421.2
## 29:   2013 3723344.4
##     yearID        V1
{% endhighlight %}

We now have two columns: one for year, which we were summarizing by, and one called V1. Every year has its own row, and this V1 was the result of this expression we put between the two commas.

What if we wanted to give it a more useful name, like "Average"? We can do that by changing what we put in our summarizing expression, by placing the `list()` function between the commas.


{% highlight r %}
summarized.year = salaries[, list(Average=mean(salary)), by="yearID"]
{% endhighlight %}



{% highlight text %}
## Warning in gmean(salary): Group 21 summed to more than type 'integer'
## can hold so the result has been coerced to 'numeric' automatically, for
## convenience.
{% endhighlight %}



{% highlight r %}
summarized.year
{% endhighlight %}



{% highlight text %}
##     yearID   Average
##  1:   1985  476299.4
##  2:   1986  417147.0
##  3:   1987  434729.5
##  4:   1988  453171.1
##  5:   1989  506323.1
##  6:   1990  511973.7
##  7:   1991  894961.2
##  8:   1992 1047520.6
##  9:   1993  976966.6
## 10:   1994 1049588.6
## 11:   1995  964979.1
## 12:   1996 1027909.3
## 13:   1997 1218687.4
## 14:   1998 1280844.6
## 15:   1999 1485316.8
## 16:   2000 1992984.6
## 17:   2001 2279841.1
## 18:   2002 2392526.6
## 19:   2003 2573472.9
## 20:   2004 2491776.1
## 21:   2005 2633830.8
## 22:   2006 2834520.9
## 23:   2007 2941435.9
## 24:   2008 3136517.1
## 25:   2009 3277647.0
## 26:   2010 3278746.8
## 27:   2011 3318838.2
## 28:   2012 3458421.2
## 29:   2013 3723344.4
##     yearID   Average
{% endhighlight %}

This means we want to create a column called average that contains the mean salary within each year. (Ignore the warning again). Now you can see that the column is called `Average`, which is more helpful. But our summary operation doesn't have to stop there. We can create two columns at the same time: one for the average, and one for the maximum:


{% highlight r %}
summarized.year = salaries[, list(Average=mean(salary), Maximum=max(salary)), by="yearID"]
{% endhighlight %}



{% highlight text %}
## Warning in gmean(salary): Group 21 summed to more than type 'integer'
## can hold so the result has been coerced to 'numeric' automatically, for
## convenience.
{% endhighlight %}



{% highlight r %}
summarized.year
{% endhighlight %}



{% highlight text %}
##     yearID   Average  Maximum
##  1:   1985  476299.4  2130300
##  2:   1986  417147.0  2800000
##  3:   1987  434729.5  2127333
##  4:   1988  453171.1  2340000
##  5:   1989  506323.1  2766667
##  6:   1990  511973.7  3200000
##  7:   1991  894961.2  3800000
##  8:   1992 1047520.6  6100000
##  9:   1993  976966.6  6200000
## 10:   1994 1049588.6  6300000
## 11:   1995  964979.1  9237500
## 12:   1996 1027909.3  9237500
## 13:   1997 1218687.4 10000000
## 14:   1998 1280844.6 14936667
## 15:   1999 1485316.8 11949794
## 16:   2000 1992984.6 15714286
## 17:   2001 2279841.1 22000000
## 18:   2002 2392526.6 22000000
## 19:   2003 2573472.9 22000000
## 20:   2004 2491776.1 22500000
## 21:   2005 2633830.8 26000000
## 22:   2006 2834520.9 21680727
## 23:   2007 2941435.9 23428571
## 24:   2008 3136517.1 28000000
## 25:   2009 3277647.0 33000000
## 26:   2010 3278746.8 33000000
## 27:   2011 3318838.2 32000000
## 28:   2012 3458421.2 30000000
## 29:   2013 3723344.4 29000000
##     yearID   Average  Maximum
{% endhighlight %}

Now you can see that we've created two columns along with the summarizing year: one with average, one with maximum.

We could add other columns as well, showing, for instance, the minimum or standard deviation or the salary within each year. Anything you put in this list will end up being a column.

You can group your summaries by any column in the data, not just the year. For example, you could summarize within each baseball league- those two leagues being the American League and the National League. Again we put a `list()` of the columns we want to create within the commas, but this time put `by="lgID"`.


{% highlight r %}
summarized.lg = salaries[, list(Average=mean(salary), Maximum=max(salary)), by="lgID"]
{% endhighlight %}



{% highlight text %}
## Warning in gmean(salary): Group 1 summed to more than type 'integer'
## can hold so the result has been coerced to 'numeric' automatically, for
## convenience.
{% endhighlight %}



{% highlight r %}
summarized.lg
{% endhighlight %}



{% highlight text %}
##    lgID Average  Maximum
## 1:   AL 1891850 33000000
## 2:   NL 1837917 25000000
{% endhighlight %}

Now you can see there are only two rows: one for the American League, one for the National League, and we can see the average and maximum salaries within each.

We've already summarized by year, and by league- we could also summarize by team. We would just change `by="lgID"` to `by="teamID"`.


{% highlight r %}
summarized.team = salaries[, list(Average=mean(salary), Maximum=max(salary)), by="teamID"]
{% endhighlight %}



{% highlight text %}
## Warning in gmean(salary): Group 2 summed to more than type 'integer'
## can hold so the result has been coerced to 'numeric' automatically, for
## convenience.
{% endhighlight %}



{% highlight r %}
summarized.team
{% endhighlight %}



{% highlight text %}
##     teamID   Average  Maximum
##  1:    BAL 1785712.3 17000000
##  2:    BOS 2692113.9 22500000
##  3:    CAL  739073.2  5375000
##  4:    CHA 1992653.5 17000000
##  5:    CLE 1525795.0 15000000
##  6:    DET 1980835.0 23000000
##  7:    KCA 1299025.8 13000000
##  8:    MIN 1525031.7 23000000
##  9:    ML4  613243.6  5875000
## 10:    NYA 3608860.1 33000000
## 11:    OAK 1303094.8 13500000
## 12:    SEA 1932288.9 20557143
## 13:    TEX 1874651.6 22000000
## 14:    TOR 1768711.0 19700000
## 15:    ATL 2130474.7 16061802
## 16:    CHN 2185518.7 19000000
## 17:    CIN 1568035.3 18910655
## 18:    HOU 1705561.3 19369019
## 19:    LAN 2346982.7 23854494
## 20:    MON  707458.9 11500000
## 21:    NYN 2317350.0 23145011
## 22:    PHI 2092230.9 25000000
## 23:    PIT 1077989.7 16500000
## 24:    SDN 1317959.6 15505142
## 25:    SFN 2044198.7 22250000
## 26:    SLN 1928832.6 16333327
## 27:    COL 1945628.5 20275000
## 28:    FLO 1147986.4 14936667
## 29:    ANA 1895109.2 13166667
## 30:    TBA 1528399.5 10125000
## 31:    ARI 2428195.9 16000000
## 32:    MIL 2095009.0 15500000
## 33:    LAA 4151107.2 26187500
## 34:    WAS 2243755.2 16571429
## 35:    MIA 2974115.7 19000000
##     teamID   Average  Maximum
{% endhighlight %}

Now we can see one row for each team.

Note that this output is itself a data.table, just like the input was. You can process it or sort it just like you could any other. For example, you could filter it to look only at a particular range of years. Here we look for years after 2000:


{% highlight r %}
summarized.year[yearID > 2000, ]
{% endhighlight %}



{% highlight text %}
##     yearID Average  Maximum
##  1:   2001 2279841 22000000
##  2:   2002 2392527 22000000
##  3:   2003 2573473 22000000
##  4:   2004 2491776 22500000
##  5:   2005 2633831 26000000
##  6:   2006 2834521 21680727
##  7:   2007 2941436 23428571
##  8:   2008 3136517 28000000
##  9:   2009 3277647 33000000
## 10:   2010 3278747 33000000
## 11:   2011 3318838 32000000
## 12:   2012 3458421 30000000
## 13:   2013 3723344 29000000
{% endhighlight %}

Here we get a smaller subset of that summary. Similarly you can sort the output, for instance to find the highest paid and lowest paid teams.


{% highlight r %}
summarized.team[order(Average), ]
{% endhighlight %}



{% highlight text %}
##     teamID   Average  Maximum
##  1:    ML4  613243.6  5875000
##  2:    MON  707458.9 11500000
##  3:    CAL  739073.2  5375000
##  4:    PIT 1077989.7 16500000
##  5:    FLO 1147986.4 14936667
##  6:    KCA 1299025.8 13000000
##  7:    OAK 1303094.8 13500000
##  8:    SDN 1317959.6 15505142
##  9:    MIN 1525031.7 23000000
## 10:    CLE 1525795.0 15000000
## 11:    TBA 1528399.5 10125000
## 12:    CIN 1568035.3 18910655
## 13:    HOU 1705561.3 19369019
## 14:    TOR 1768711.0 19700000
## 15:    BAL 1785712.3 17000000
## 16:    TEX 1874651.6 22000000
## 17:    ANA 1895109.2 13166667
## 18:    SLN 1928832.6 16333327
## 19:    SEA 1932288.9 20557143
## 20:    COL 1945628.5 20275000
## 21:    DET 1980835.0 23000000
## 22:    CHA 1992653.5 17000000
## 23:    SFN 2044198.7 22250000
## 24:    PHI 2092230.9 25000000
## 25:    MIL 2095009.0 15500000
## 26:    ATL 2130474.7 16061802
## 27:    CHN 2185518.7 19000000
## 28:    WAS 2243755.2 16571429
## 29:    NYN 2317350.0 23145011
## 30:    LAN 2346982.7 23854494
## 31:    ARI 2428195.9 16000000
## 32:    BOS 2692113.9 22500000
## 33:    MIA 2974115.7 19000000
## 34:    NYA 3608860.1 33000000
## 35:    LAA 4151107.2 26187500
##     teamID   Average  Maximum
{% endhighlight %}

Finally, we can group by more than one column in our analysis. Let's say we want to see the average salary within each year, separately for the two leagues: so we're summarizing by the league and year combination. To do this, we change the by argument to be a vector `c("yearID", "lgID")`.


{% highlight r %}
summarized.year.lg = salaries[, list(Average=mean(salary), Maximum=max(salary)), by=c("yearID", "lgID")]
summarized.year.lg
{% endhighlight %}



{% highlight text %}
##     yearID lgID   Average  Maximum
##  1:   1985   AL  455597.0  1795704
##  2:   1985   NL  500249.3  2130300
##  3:   1986   AL  402337.9  1984423
##  4:   1986   NL  433925.1  2800000
##  5:   1987   AL  441846.6  2110000
##  6:   1987   NL  427857.8  2127333
##  7:   1988   AL  453901.2  2305000
##  8:   1988   NL  452374.2  2340000
##  9:   1989   AL  502052.4  2766666
## 10:   1989   NL  511116.5  2766667
## 11:   1990   AL  500415.8  3200000
## 12:   1990   NL  525913.7  2513703
## 13:   1991   AL  908126.7  3791667
## 14:   1991   NL  879587.5  3800000
## 15:   1992   AL 1017651.1  5300000
## 16:   1992   NL 1085608.6  6100000
## 17:   1993   AL 1028575.6  5550000
## 18:   1993   NL  923883.0  6200000
## 19:   1994   AL 1130703.1  5550000
## 20:   1994   NL  971003.2  6300000
## 21:   1995   AL 1039864.5  9237500
## 22:   1995   NL  890698.7  8166666
## 23:   1996   AL 1055235.2  9237500
## 24:   1996   NL 1000406.7  8416667
## 25:   1997   AL 1267829.6 10000000
## 26:   1997   NL 1169651.4  8666667
## 27:   1998   AL 1364396.6 10000000
## 28:   1998   NL 1207658.0 14936667
## 29:   1999   AL 1503986.4 11949794
## 30:   1999   NL 1468880.6 10714286
## 31:   2000   AL 2004401.7 12868670
## 32:   2000   NL 1983096.5 15714286
## 33:   2001   AL 2333183.9 22000000
## 34:   2001   NL 2232801.3 15714286
## 35:   2002   AL 2449016.0 22000000
## 36:   2002   NL 2342579.4 15714286
## 37:   2003   AL 2524939.6 22000000
## 38:   2003   NL 2614933.1 17166667
## 39:   2004   AL 2517280.2 22500000
## 40:   2004   NL 2469002.5 18000000
## 41:   2005   AL 2681580.8 26000000
## 42:   2005   NL 2590986.6 22000000
## 43:   2006   AL 3088942.0 21680727
## 44:   2006   NL 2616445.7 19369019
## 45:   2007   AL 3304390.9 23428571
## 46:   2007   NL 2623749.2 16600000
## 47:   2008   AL 3449574.3 28000000
## 48:   2008   NL 2870790.4 18622809
## 49:   2009   AL 3380833.1 33000000
## 50:   2009   NL 3184368.7 23854494
## 51:   2010   AL 3431360.4 33000000
## 52:   2010   NL 3142161.2 20144707
## 53:   2011   AL 3505557.0 32000000
## 54:   2011   NL 3156654.9 21644707
## 55:   2012   AL 3662264.1 30000000
## 56:   2012   NL 3277278.0 23145011
## 57:   2013   AL 3757664.2 29000000
## 58:   2013   NL 3688940.2 25000000
##     yearID lgID   Average  Maximum
{% endhighlight %}

Notice it has one row for each combination of a year and a league- for example, one for the year 1985 within AL (American League), and one for 1985 NL (National League), and has the average and maximum within each of these. You could go even farther and view the analysis within each team, within each year. Just change the `lgID` to `teamID`:


{% highlight r %}
summarized.year.team = salaries[, list(Average=mean(salary), Maximum=max(salary)), by=c("yearID", "teamID")]
summarized.year.team
{% endhighlight %}



{% highlight text %}
##      yearID teamID   Average  Maximum
##   1:   1985    BAL  525486.9  1472819
##   2:   1985    BOS  435902.4  1075000
##   3:   1985    CAL  515281.9  1100000
##   4:   1985    CHA  468865.6  1242333
##   5:   1985    CLE  327583.3  1100000
##  ---                                 
## 824:   2013    PIT 2752214.3 16500000
## 825:   2013    SDN 2342339.3  9500000
## 826:   2013    SFN 5006440.5 22250000
## 827:   2013    SLN 3295003.9 16272110
## 828:   2013    WAS 4548130.8 16571429
{% endhighlight %}

Now, any of these summaries could be used as the result of an analysis, for example as a table in a presentation or paper. But they also make visualizing trends much easier. For example, let's say we want to examine the trend of how salary changes over time. We could produce a plot of all the points in the original salaries dataset, all 24 thousand combinations of players and years. For that we'll use ggplot2, which we covered in a previous segment:


{% highlight r %}
library(ggplot2)
{% endhighlight %}

Perform this on our original dataset `salaries`, putting on the x-axis `yearID` and on the y-axis `salary`.


{% highlight r %}
ggplot(salaries, aes(yearID, salary)) + geom_point()
{% endhighlight %}

![center](../../figs/code_lesson4/unnamed-chunk-53-1.png) 

So in this graph we can see a positive trend in salary over time. However, all we can really see is the range of salaries: within this mass of points it's not possible to tell what the average is for each of these years. If we actually want to see how the average changed over time, we can instead plot the summarized data. We get this from `summarized.year`:


{% highlight r %}
summarized.year
{% endhighlight %}



{% highlight text %}
##     yearID   Average  Maximum
##  1:   1985  476299.4  2130300
##  2:   1986  417147.0  2800000
##  3:   1987  434729.5  2127333
##  4:   1988  453171.1  2340000
##  5:   1989  506323.1  2766667
##  6:   1990  511973.7  3200000
##  7:   1991  894961.2  3800000
##  8:   1992 1047520.6  6100000
##  9:   1993  976966.6  6200000
## 10:   1994 1049588.6  6300000
## 11:   1995  964979.1  9237500
## 12:   1996 1027909.3  9237500
## 13:   1997 1218687.4 10000000
## 14:   1998 1280844.6 14936667
## 15:   1999 1485316.8 11949794
## 16:   2000 1992984.6 15714286
## 17:   2001 2279841.1 22000000
## 18:   2002 2392526.6 22000000
## 19:   2003 2573472.9 22000000
## 20:   2004 2491776.1 22500000
## 21:   2005 2633830.8 26000000
## 22:   2006 2834520.9 21680727
## 23:   2007 2941435.9 23428571
## 24:   2008 3136517.1 28000000
## 25:   2009 3277647.0 33000000
## 26:   2010 3278746.8 33000000
## 27:   2011 3318838.2 32000000
## 28:   2012 3458421.2 30000000
## 29:   2013 3723344.4 29000000
##     yearID   Average  Maximum
{% endhighlight %}

We have the year in one column and the average salary in another. So use that `yearID` as our x-axis and `Average` as our y-axis. Usually when we have one trend we put just a line:


{% highlight r %}
ggplot(summarized.year, aes(yearID, Average)) + geom_line()
{% endhighlight %}

![center](../../figs/code_lesson4/unnamed-chunk-55-1.png) 

Now we can see the trend of the average over time. This comes directly from the summarized data, where we have the average per year.

We can even go farther- since we have it summarized by year *and* league, we can plot `summarized.year.lg` instead. We still put `yearID` on the x-axis and `Average` on the y, but now we color based on the league ID (`lgID`):


{% highlight r %}
ggplot(summarized.year.lg, aes(yearID, Average, col=lgID)) + geom_line()
{% endhighlight %}

![center](../../figs/code_lesson4/unnamed-chunk-56-1.png) 

Now we can see two separate lines- one red for the American League, and one green for the National League.

Notice that data.table and ggplot2 have a natural synergy: data table lets you summarize your data to the extent you need to visualize what you want with `ggplot2`. Together they work as two powerful tools for exploratory data analysis.

<a name="segment5"></a>

Segment 5: Merging Data
-------------

Let's take a closer look at the baseball player salary data that we've downloaded and imported into R. You can do that with


{% highlight r %}
View(salaries)
{% endhighlight %}

Notice that the players are not represented by their actual first and last names- they're represented by some kind of ID. This ID looks pretty unhelpful: why not just put their names in that column?

The first reason is that there are multiple players in history that have the same name, and at that point if you used their names to identify them, it wouldn't be possible to tell them apart in the data. Meanwhile, these IDs are guaranteed to be unique per player. There are other advantages: for example, the player ID is shorter and therefore takes up less storage space- but the uniqueness is the most important. That ID can be used to connect this column to other datasets.

So what do I mean by other datasets? Well, the salary data is just one table within the Lahman baseball dataset. Let's load in a different one, from a slightly different URL. Go back to the line where we read in the salary data, but change `Salary.csv` to `Master.csv`, and save it to a variable called `master`.


{% highlight r %}
master = read.csv("http://dgrtwo.github.io/pages/lahman/Master.csv")
{% endhighlight %}

Before we do anything else, let's turn this data frame into a data table just like we did with `salaries`:


{% highlight r %}
master = as.data.table(master)
{% endhighlight %}

Let's take a look at the table:


{% highlight r %}
View(master)
{% endhighlight %}

This is a master list of the baseball players based on their ID. Here in the first column you can see the playerIDs that appeared in the salaries data. But you can also see a lot of biographical information, like their birthday and birthplace, their weight and height, the date of their death, and most importantly, their full name. So now in one table (`salaries`) we just have the ID, and in another table (`master`) we have a way of getting from that name to their full biographical information. So, let's take the first name on this list: someone named David Aardsma. We could take this players ID, copy it, and extract just this player's salary:


{% highlight r %}
salaries[playerID == "aardsda01", ]
{% endhighlight %}



{% highlight text %}
##    yearID teamID lgID  playerID  salary
## 1:   2004    SFN   NL aardsda01  300000
## 2:   2007    CHA   AL aardsda01  387500
## 3:   2008    BOS   AL aardsda01  403250
## 4:   2009    SEA   AL aardsda01  419000
## 5:   2010    SEA   AL aardsda01 2750000
## 6:   2011    SEA   AL aardsda01 4500000
## 7:   2012    NYA   AL aardsda01  500000
{% endhighlight %}

Based on their ID, we were able to extract the years of their salary. You can see that David Aardsma played in seven years, you can see it rose from 2004 to 2010, before dropping back down again. So this is a way we can get one player's name and team along with his salary each year. But it's very clumsy to have to do it individually for each player. Luckily there's a much easier way to connect these two datasets: we can merge them, using the `merge` function. Let's create a new merged dataset called `merged.salaries`.


{% highlight r %}
merged.salaries = merge(salaries, master, by="playerID")
{% endhighlight %}

The "by" argument defines what column we should use to merge them. In this case, that's what column is shared between them, which is `playerID`.


{% highlight r %}
merged.salaries
{% endhighlight %}



{% highlight text %}
##         playerID yearID teamID lgID  salary birthYear birthMonth birthDay
##     1: aardsda01   2004    SFN   NL  300000      1981         12       27
##     2: aardsda01   2007    CHA   AL  387500      1981         12       27
##     3: aardsda01   2008    BOS   AL  403250      1981         12       27
##     4: aardsda01   2009    SEA   AL  419000      1981         12       27
##     5: aardsda01   2010    SEA   AL 2750000      1981         12       27
##    ---                                                                   
## 23952: zumayjo01   2011    DET   AL 1400000      1984         11        9
## 23953: zupcibo01   1991    BOS   AL  100000      1966          8       18
## 23954: zupcibo01   1992    BOS   AL  109000      1966          8       18
## 23955: zupcibo01   1993    BOS   AL  222000      1966          8       18
## 23956: zuvelpa01   1989    ATL   NL  145000      1958         10       31
##        birthCountry birthState   birthCity deathYear deathMonth deathDay
##     1:          USA         CO      Denver        NA         NA       NA
##     2:          USA         CO      Denver        NA         NA       NA
##     3:          USA         CO      Denver        NA         NA       NA
##     4:          USA         CO      Denver        NA         NA       NA
##     5:          USA         CO      Denver        NA         NA       NA
##    ---                                                                  
## 23952:          USA         CA Chula Vista        NA         NA       NA
## 23953:          USA         PA  Pittsburgh        NA         NA       NA
## 23954:          USA         PA  Pittsburgh        NA         NA       NA
## 23955:          USA         PA  Pittsburgh        NA         NA       NA
## 23956:          USA         CA   San Mateo        NA         NA       NA
##        deathCountry deathState deathCity nameFirst nameLast   nameGiven
##     1:                                       David  Aardsma David Allan
##     2:                                       David  Aardsma David Allan
##     3:                                       David  Aardsma David Allan
##     4:                                       David  Aardsma David Allan
##     5:                                       David  Aardsma David Allan
##    ---                                                                 
## 23952:                                        Joel   Zumaya Joel Martin
## 23953:                                         Bob   Zupcic      Robert
## 23954:                                         Bob   Zupcic      Robert
## 23955:                                         Bob   Zupcic      Robert
## 23956:                                        Paul  Zuvella        Paul
##        weight height bats throws      debut  finalGame  retroID   bbrefID
##     1:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     2:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     3:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     4:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     5:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##    ---                                                                   
## 23952:    215     75    R      R 2006-04-03 2010-06-28 zumaj001 zumayjo01
## 23953:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23954:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23955:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23956:    173     72    R      R 1982-09-04 1991-05-02 zuvep001 zuvelpa01
{% endhighlight %}

Notice that we can still see all the data from the `salaries` dataset- the player ID, year, team, league, and salary. But each player's salary in each year- but we've also combined it with their biographical information- like their birthday and place, and most notably their name. So we've combined these two tables based on this common column: we have them all in one place. If you wanted to look for trends in salary- for instance, a connection of salary to a player's height, weight, or birth country- you now have all the information in one data table.

One note, having their first and last names as different columns is useful, but we'd like to combine them together into a new column, of first name-space-last name. One way we can create a new column in a data.table is with the `:=` operator:


{% highlight r %}
merged.salaries[, name:=paste(nameFirst, nameLast)]
{% endhighlight %}



{% highlight text %}
##         playerID yearID teamID lgID  salary birthYear birthMonth birthDay
##     1: aardsda01   2004    SFN   NL  300000      1981         12       27
##     2: aardsda01   2007    CHA   AL  387500      1981         12       27
##     3: aardsda01   2008    BOS   AL  403250      1981         12       27
##     4: aardsda01   2009    SEA   AL  419000      1981         12       27
##     5: aardsda01   2010    SEA   AL 2750000      1981         12       27
##    ---                                                                   
## 23952: zumayjo01   2011    DET   AL 1400000      1984         11        9
## 23953: zupcibo01   1991    BOS   AL  100000      1966          8       18
## 23954: zupcibo01   1992    BOS   AL  109000      1966          8       18
## 23955: zupcibo01   1993    BOS   AL  222000      1966          8       18
## 23956: zuvelpa01   1989    ATL   NL  145000      1958         10       31
##        birthCountry birthState   birthCity deathYear deathMonth deathDay
##     1:          USA         CO      Denver        NA         NA       NA
##     2:          USA         CO      Denver        NA         NA       NA
##     3:          USA         CO      Denver        NA         NA       NA
##     4:          USA         CO      Denver        NA         NA       NA
##     5:          USA         CO      Denver        NA         NA       NA
##    ---                                                                  
## 23952:          USA         CA Chula Vista        NA         NA       NA
## 23953:          USA         PA  Pittsburgh        NA         NA       NA
## 23954:          USA         PA  Pittsburgh        NA         NA       NA
## 23955:          USA         PA  Pittsburgh        NA         NA       NA
## 23956:          USA         CA   San Mateo        NA         NA       NA
##        deathCountry deathState deathCity nameFirst nameLast   nameGiven
##     1:                                       David  Aardsma David Allan
##     2:                                       David  Aardsma David Allan
##     3:                                       David  Aardsma David Allan
##     4:                                       David  Aardsma David Allan
##     5:                                       David  Aardsma David Allan
##    ---                                                                 
## 23952:                                        Joel   Zumaya Joel Martin
## 23953:                                         Bob   Zupcic      Robert
## 23954:                                         Bob   Zupcic      Robert
## 23955:                                         Bob   Zupcic      Robert
## 23956:                                        Paul  Zuvella        Paul
##        weight height bats throws      debut  finalGame  retroID   bbrefID
##     1:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     2:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     3:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     4:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     5:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##    ---                                                                   
## 23952:    215     75    R      R 2006-04-03 2010-06-28 zumaj001 zumayjo01
## 23953:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23954:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23955:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23956:    173     72    R      R 1982-09-04 1991-05-02 zuvep001 zuvelpa01
##                 name
##     1: David Aardsma
##     2: David Aardsma
##     3: David Aardsma
##     4: David Aardsma
##     5: David Aardsma
##    ---              
## 23952:   Joel Zumaya
## 23953:    Bob Zupcic
## 23954:    Bob Zupcic
## 23955:    Bob Zupcic
## 23956:  Paul Zuvella
{% endhighlight %}

This means assign a new column, `name`, and now we can give it a value based on other columns in the dataset. The `paste` function is a useful function in R for combining two vectors of strings to be separated by spaces. If we put `nameFirst` and `nameLast`, because we're within the data.table, that we want to combine those two names into a new name.


{% highlight r %}
merged.salaries
{% endhighlight %}



{% highlight text %}
##         playerID yearID teamID lgID  salary birthYear birthMonth birthDay
##     1: aardsda01   2004    SFN   NL  300000      1981         12       27
##     2: aardsda01   2007    CHA   AL  387500      1981         12       27
##     3: aardsda01   2008    BOS   AL  403250      1981         12       27
##     4: aardsda01   2009    SEA   AL  419000      1981         12       27
##     5: aardsda01   2010    SEA   AL 2750000      1981         12       27
##    ---                                                                   
## 23952: zumayjo01   2011    DET   AL 1400000      1984         11        9
## 23953: zupcibo01   1991    BOS   AL  100000      1966          8       18
## 23954: zupcibo01   1992    BOS   AL  109000      1966          8       18
## 23955: zupcibo01   1993    BOS   AL  222000      1966          8       18
## 23956: zuvelpa01   1989    ATL   NL  145000      1958         10       31
##        birthCountry birthState   birthCity deathYear deathMonth deathDay
##     1:          USA         CO      Denver        NA         NA       NA
##     2:          USA         CO      Denver        NA         NA       NA
##     3:          USA         CO      Denver        NA         NA       NA
##     4:          USA         CO      Denver        NA         NA       NA
##     5:          USA         CO      Denver        NA         NA       NA
##    ---                                                                  
## 23952:          USA         CA Chula Vista        NA         NA       NA
## 23953:          USA         PA  Pittsburgh        NA         NA       NA
## 23954:          USA         PA  Pittsburgh        NA         NA       NA
## 23955:          USA         PA  Pittsburgh        NA         NA       NA
## 23956:          USA         CA   San Mateo        NA         NA       NA
##        deathCountry deathState deathCity nameFirst nameLast   nameGiven
##     1:                                       David  Aardsma David Allan
##     2:                                       David  Aardsma David Allan
##     3:                                       David  Aardsma David Allan
##     4:                                       David  Aardsma David Allan
##     5:                                       David  Aardsma David Allan
##    ---                                                                 
## 23952:                                        Joel   Zumaya Joel Martin
## 23953:                                         Bob   Zupcic      Robert
## 23954:                                         Bob   Zupcic      Robert
## 23955:                                         Bob   Zupcic      Robert
## 23956:                                        Paul  Zuvella        Paul
##        weight height bats throws      debut  finalGame  retroID   bbrefID
##     1:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     2:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     3:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     4:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##     5:    205     75    R      R 2004-04-06 2013-09-28 aardd001 aardsda01
##    ---                                                                   
## 23952:    215     75    R      R 2006-04-03 2010-06-28 zumaj001 zumayjo01
## 23953:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23954:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23955:    220     76    R      R 1991-09-07 1994-08-04 zupcb001 zupcibo01
## 23956:    173     72    R      R 1982-09-04 1991-05-02 zuvep001 zuvelpa01
##                 name
##     1: David Aardsma
##     2: David Aardsma
##     3: David Aardsma
##     4: David Aardsma
##     5: David Aardsma
##    ---              
## 23952:   Joel Zumaya
## 23953:    Bob Zupcic
## 23954:    Bob Zupcic
## 23955:    Bob Zupcic
## 23956:  Paul Zuvella
{% endhighlight %}

You can see that we've added a new column, `name`.

Merging can sometimes be a bit more complicated. For example, let's bring in one more dataset, this one a history of each player's batting statistics for each year. To do that, take the earlier `read.csv` line, change `Master.csv` to `Batting.csv`, and save it into a variable called `batting`:


{% highlight r %}
batting = read.csv("http://dgrtwo.github.io/pages/lahman/Batting.csv")
{% endhighlight %}

Then let's turn it into a data.table, just like we did for `master`:


{% highlight r %}
batting = as.data.table(batting)
batting
{% endhighlight %}



{% highlight text %}
##         playerID yearID stint teamID lgID   G G_batting  AB  R   H X2B X3B
##     1: aardsda01   2004     1    SFN   NL  11        11   0  0   0   0   0
##     2: aardsda01   2006     1    CHN   NL  45        43   2  0   0   0   0
##     3: aardsda01   2007     1    CHA   AL  25         2   0  0   0   0   0
##     4: aardsda01   2008     1    BOS   AL  47         5   1  0   0   0   0
##     5: aardsda01   2009     1    SEA   AL  73         3   0  0   0   0   0
##    ---                                                                    
## 97885: zimmejo02   2013     1    WAS   NL  32        32  65  4   8   1   0
## 97886: zimmery01   2013     1    WAS   NL 147       147 568 84 156  26   2
## 97887:  zitoba01   2013     1    SFN   NL  30        30  34  3   5   0   0
## 97888: zobribe01   2013     1    TBA   AL 157       157 612 77 168  36   3
## 97889: zuninmi01   2013     1    SEA   AL  52        52 173 22  37   5   0
##        HR RBI SB CS BB  SO IBB HBP SH SF GIDP G_old
##     1:  0   0  0  0  0   0   0   0  0  0    0    11
##     2:  0   0  0  0  0   0   0   0  1  0    0    45
##     3:  0   0  0  0  0   0   0   0  0  0    0     2
##     4:  0   0  0  0  0   1   0   0  0  0    0     5
##     5:  0   0  0  0  0   0   0   0  0  0    0    NA
##    ---                                             
## 97885:  0   2  0  0  1  20   0   0  6  1    0    NA
## 97886: 26  79  6  0 60 133   2   2  0  3   16    NA
## 97887:  0   2  0  0  0   8   0   0  9  0    1    NA
## 97888: 12  71 11  3 72  91   4   7  1  6   18    NA
## 97889:  5  14  1  0 16  49   0   3  0  1    5    NA
{% endhighlight %}

This is the most complex dataset yet. Here, like the salary data, we have one row per player per year, and their team ID and league ID. But we also have many statistics summarizing how well he did at batting that year. For instance, G represents how many games the player played in, AB represents the number of times a player went up to bat (how many chances they had to get a hit), H represents the number of hits, and HR represents the number of home runs he scored (hitting the ball out of the park, which gets a run in just one hit).

Now, let's say we want to combine this data with the salary data- for example so we can see how salary is correlated with performance. First, notice that the salary table and the batting table don't share only one column of player ID: they share four: playerID, teamID, leagueID and yearID. That's because we have multiple batting statistics and salary for each single player. This means we won't just be merging by player: we'll be merging them based on the combination of all four columns.

The way we do that is with the `by` argument to `merged`. Instead of giving just the `playerID` to `by`, we give a vector of the four shared columns.


{% highlight r %}
merged.batting = merge(batting, salaries, by=c("playerID", "yearID", "teamID", "lgID"))
merged.batting
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID stint   G G_batting  AB  R   H X2B X3B
##     1:   2004    SFN   NL aardsda01     1  11        11   0  0   0   0   0
##     2:   2007    CHA   AL aardsda01     1  25         2   0  0   0   0   0
##     3:   2008    BOS   AL aardsda01     1  47         5   1  0   0   0   0
##     4:   2009    SEA   AL aardsda01     1  73         3   0  0   0   0   0
##     5:   2010    SEA   AL aardsda01     1  53         4   0  0   0   0   0
##    ---                                                                    
## 22867:   2009    DET   AL zumayjo01     1  29         3   0  0   0   0   0
## 22868:   2010    DET   AL zumayjo01     1  31         4   0  0   0   0   0
## 22869:   1991    BOS   AL zupcibo01     1  18        18  25  3   4   0   0
## 22870:   1992    BOS   AL zupcibo01     1 124       124 392 46 108  19   1
## 22871:   1993    BOS   AL zupcibo01     1 141       141 286 40  69  24   2
##        HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old  salary
##     1:  0   0  0  0  0  0   0   0  0  0    0    11  300000
##     2:  0   0  0  0  0  0   0   0  0  0    0     2  387500
##     3:  0   0  0  0  0  1   0   0  0  0    0     5  403250
##     4:  0   0  0  0  0  0   0   0  0  0    0    NA  419000
##     5:  0   0  0  0  0  0   0   0  0  0    0    NA 2750000
##    ---                                                    
## 22867:  0   0  0  0  0  0   0   0  0  0    0    NA  735000
## 22868:  0   0  0  0  0  0   0   0  0  0    0    NA  915000
## 22869:  1   3  0  0  1  6   0   0  1  0    0    18  100000
## 22870:  3  43  2  2 25 60   1   4  7  4    6   124  109000
## 22871:  2  26  5  2 27 54   2   2  8  3    7   141  222000
{% endhighlight %}

Now it has all the information that was in the batting dataset, but it also added a column for salary. Another thing to note is that we don't have salary information on every player in every year: in particular, we've lost all information on players before 1985. There is a way we can fix this, by adding the `all.x` option to the `merge` function:


{% highlight r %}
merged.batting = merge(batting, salaries, by=c("playerID", "yearID", "teamID", "lgID"), all.x=TRUE)
merged.batting
{% endhighlight %}



{% highlight text %}
##        yearID teamID lgID  playerID stint   G G_batting  AB  R   H X2B X3B
##     1:   2004    SFN   NL aardsda01     1  11        11   0  0   0   0   0
##     2:   2006    CHN   NL aardsda01     1  45        43   2  0   0   0   0
##     3:   2007    CHA   AL aardsda01     1  25         2   0  0   0   0   0
##     4:   2008    BOS   AL aardsda01     1  47         5   1  0   0   0   0
##     5:   2009    SEA   AL aardsda01     1  73         3   0  0   0   0   0
##    ---                                                                    
## 97885:   1959    BAL   AL zuverge01     1   6         6   0  0   0   0   0
## 97886:   1910    CHA   AL zwilldu01     1  27        27  87  7  16   5   0
## 97887:   1914    CHF   FL zwilldu01     1 154       154 592 91 185  38   8
## 97888:   1915    CHF   FL zwilldu01     1 150       150 548 65 157  32   7
## 97889:   1916    CHN   NL zwilldu01     1  35        35  53  4   6   1   0
##        HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary
##     1:  0   0  0  0  0  0   0   0  0  0    0    11 300000
##     2:  0   0  0  0  0  0   0   0  1  0    0    45     NA
##     3:  0   0  0  0  0  0   0   0  0  0    0     2 387500
##     4:  0   0  0  0  0  1   0   0  0  0    0     5 403250
##     5:  0   0  0  0  0  0   0   0  0  0    0    NA 419000
##    ---                                                   
## 97885:  0   0  0  0  2  0   0   0  0  0    0     6     NA
## 97886:  0   5  1 NA 11 NA  NA   1  1 NA   NA    27     NA
## 97887: 16  95 21 NA 46 68  NA   1 10 NA   NA   154     NA
## 97888: 13  94 24 NA 67 65  NA   2 18 NA   NA   150     NA
## 97889:  1   8  0 NA  4  6  NA   0  2 NA   NA    35     NA
{% endhighlight %}

This means "keep everything in the first dataset we're merging," which is `batting` (`all.y` would mean "keep everything in the second dataset"). Notice now that now all rows have information in the `salary` column: some have NA, which means "missing value," or "not applicable." So notice that all the rows where we have salary data get to keep their value, while all the ones that don't get filled in by the missing value NA.

Now we can take this merged dataset and merge it with our biographical data in the master list. Here that would be


{% highlight r %}
merged.all = merge(merged.batting, master, by="playerID")
merged.all
{% endhighlight %}



{% highlight text %}
##         playerID yearID teamID lgID stint   G G_batting  AB  R   H X2B X3B
##     1: aardsda01   2004    SFN   NL     1  11        11   0  0   0   0   0
##     2: aardsda01   2006    CHN   NL     1  45        43   2  0   0   0   0
##     3: aardsda01   2007    CHA   AL     1  25         2   0  0   0   0   0
##     4: aardsda01   2008    BOS   AL     1  47         5   1  0   0   0   0
##     5: aardsda01   2009    SEA   AL     1  73         3   0  0   0   0   0
##    ---                                                                    
## 97885: zuverge01   1959    BAL   AL     1   6         6   0  0   0   0   0
## 97886: zwilldu01   1910    CHA   AL     1  27        27  87  7  16   5   0
## 97887: zwilldu01   1914    CHF   FL     1 154       154 592 91 185  38   8
## 97888: zwilldu01   1915    CHF   FL     1 150       150 548 65 157  32   7
## 97889: zwilldu01   1916    CHN   NL     1  35        35  53  4   6   1   0
##        HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary birthYear
##     1:  0   0  0  0  0  0   0   0  0  0    0    11 300000      1981
##     2:  0   0  0  0  0  0   0   0  1  0    0    45     NA      1981
##     3:  0   0  0  0  0  0   0   0  0  0    0     2 387500      1981
##     4:  0   0  0  0  0  1   0   0  0  0    0     5 403250      1981
##     5:  0   0  0  0  0  0   0   0  0  0    0    NA 419000      1981
##    ---                                                             
## 97885:  0   0  0  0  2  0   0   0  0  0    0     6     NA      1924
## 97886:  0   5  1 NA 11 NA  NA   1  1 NA   NA    27     NA      1888
## 97887: 16  95 21 NA 46 68  NA   1 10 NA   NA   154     NA      1888
## 97888: 13  94 24 NA 67 65  NA   2 18 NA   NA   150     NA      1888
## 97889:  1   8  0 NA  4  6  NA   0  2 NA   NA    35     NA      1888
##        birthMonth birthDay birthCountry birthState birthCity deathYear
##     1:         12       27          USA         CO    Denver        NA
##     2:         12       27          USA         CO    Denver        NA
##     3:         12       27          USA         CO    Denver        NA
##     4:         12       27          USA         CO    Denver        NA
##     5:         12       27          USA         CO    Denver        NA
##    ---                                                                
## 97885:          8       20          USA         MI   Holland        NA
## 97886:         11        2          USA         MO St. Louis      1978
## 97887:         11        2          USA         MO St. Louis      1978
## 97888:         11        2          USA         MO St. Louis      1978
## 97889:         11        2          USA         MO St. Louis      1978
##        deathMonth deathDay deathCountry deathState    deathCity nameFirst
##     1:         NA       NA                                          David
##     2:         NA       NA                                          David
##     3:         NA       NA                                          David
##     4:         NA       NA                                          David
##     5:         NA       NA                                          David
##    ---                                                                   
## 97885:         NA       NA                                         George
## 97886:          3       27          USA         CA La Crescenta     Dutch
## 97887:          3       27          USA         CA La Crescenta     Dutch
## 97888:          3       27          USA         CA La Crescenta     Dutch
## 97889:          3       27          USA         CA La Crescenta     Dutch
##        nameLast       nameGiven weight height bats throws      debut
##     1:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     2:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     3:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     4:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     5:  Aardsma     David Allan    205     75    R      R 2004-04-06
##    ---                                                              
## 97885: Zuverink          George    195     76    R      R 1951-04-21
## 97886: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 97887: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 97888: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 97889: Zwilling Edward Harrison    160     66    L      L 1910-08-14
##         finalGame  retroID   bbrefID
##     1: 2013-09-28 aardd001 aardsda01
##     2: 2013-09-28 aardd001 aardsda01
##     3: 2013-09-28 aardd001 aardsda01
##     4: 2013-09-28 aardd001 aardsda01
##     5: 2013-09-28 aardd001 aardsda01
##    ---                              
## 97885: 1959-06-15 zuveg101 zuverge01
## 97886: 1916-07-12 zwild101 zwilldu01
## 97887: 1916-07-12 zwild101 zwilldu01
## 97888: 1916-07-12 zwild101 zwilldu01
## 97889: 1916-07-12 zwild101 zwilldu01
{% endhighlight %}

Now we see we still have the same batting information, but we also have the biographical information from the master list- for example, each player's real name. We've created one mega-dataset covering all three kinds of information. The Lahman baseball dataset contains a lot more information, including player's fielding statistics, presence in the Hall of Fame, pitchers, managers, and so on, all sharing these same IDs. By merging these datasets in the right way, you can answer very complex and interesting questions.

<a name="segment6"></a>

Segment 6: Exploratory Data Analysis
-------------

So let's wrap up by taking all these tools together on our mega-merged dataset. Just like any other dataset, we can filter and process this. For example, this dataset includes pitchers, who might never go up to bat in a whole season. That could end up skewing our analysis.


{% highlight r %}
head(merged.all)
{% endhighlight %}



{% highlight text %}
##     playerID yearID teamID lgID stint  G G_batting AB R H X2B X3B HR RBI
## 1: aardsda01   2004    SFN   NL     1 11        11  0 0 0   0   0  0   0
## 2: aardsda01   2006    CHN   NL     1 45        43  2 0 0   0   0  0   0
## 3: aardsda01   2007    CHA   AL     1 25         2  0 0 0   0   0  0   0
## 4: aardsda01   2008    BOS   AL     1 47         5  1 0 0   0   0  0   0
## 5: aardsda01   2009    SEA   AL     1 73         3  0 0 0   0   0  0   0
## 6: aardsda01   2010    SEA   AL     1 53         4  0 0 0   0   0  0   0
##    SB CS BB SO IBB HBP SH SF GIDP G_old  salary birthYear birthMonth
## 1:  0  0  0  0   0   0  0  0    0    11  300000      1981         12
## 2:  0  0  0  0   0   0  1  0    0    45      NA      1981         12
## 3:  0  0  0  0   0   0  0  0    0     2  387500      1981         12
## 4:  0  0  0  1   0   0  0  0    0     5  403250      1981         12
## 5:  0  0  0  0   0   0  0  0    0    NA  419000      1981         12
## 6:  0  0  0  0   0   0  0  0    0    NA 2750000      1981         12
##    birthDay birthCountry birthState birthCity deathYear deathMonth
## 1:       27          USA         CO    Denver        NA         NA
## 2:       27          USA         CO    Denver        NA         NA
## 3:       27          USA         CO    Denver        NA         NA
## 4:       27          USA         CO    Denver        NA         NA
## 5:       27          USA         CO    Denver        NA         NA
## 6:       27          USA         CO    Denver        NA         NA
##    deathDay deathCountry deathState deathCity nameFirst nameLast
## 1:       NA                                       David  Aardsma
## 2:       NA                                       David  Aardsma
## 3:       NA                                       David  Aardsma
## 4:       NA                                       David  Aardsma
## 5:       NA                                       David  Aardsma
## 6:       NA                                       David  Aardsma
##      nameGiven weight height bats throws      debut  finalGame  retroID
## 1: David Allan    205     75    R      R 2004-04-06 2013-09-28 aardd001
## 2: David Allan    205     75    R      R 2004-04-06 2013-09-28 aardd001
## 3: David Allan    205     75    R      R 2004-04-06 2013-09-28 aardd001
## 4: David Allan    205     75    R      R 2004-04-06 2013-09-28 aardd001
## 5: David Allan    205     75    R      R 2004-04-06 2013-09-28 aardd001
## 6: David Allan    205     75    R      R 2004-04-06 2013-09-28 aardd001
##      bbrefID
## 1: aardsda01
## 2: aardsda01
## 3: aardsda01
## 4: aardsda01
## 5: aardsda01
## 6: aardsda01
{% endhighlight %}

An example would be David Aardsma, who in many years never even had a single At Bat (AB is 0). We can start by filtering out all the years in which someone has no At Bats.


{% highlight r %}
merged.all = merged.all[AB > 0, ]
merged.all
{% endhighlight %}



{% highlight text %}
##         playerID yearID teamID lgID stint   G G_batting  AB   R   H X2B
##     1: aardsda01   2006    CHN   NL     1  45        43   2   0   0   0
##     2: aardsda01   2008    BOS   AL     1  47         5   1   0   0   0
##     3: aaronha01   1954    ML1   NL     1 122       122 468  58 131  27
##     4: aaronha01   1955    ML1   NL     1 153       153 602 105 189  37
##     5: aaronha01   1956    ML1   NL     1 153       153 609 106 200  34
##    ---                                                                 
## 84365: zuverge01   1958    BAL   AL     1  45        45   9   0   2   0
## 84366: zwilldu01   1910    CHA   AL     1  27        27  87   7  16   5
## 84367: zwilldu01   1914    CHF   FL     1 154       154 592  91 185  38
## 84368: zwilldu01   1915    CHF   FL     1 150       150 548  65 157  32
## 84369: zwilldu01   1916    CHN   NL     1  35        35  53   4   6   1
##        X3B HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary birthYear
##     1:   0  0   0  0  0  0  0   0   0  1  0    0    45     NA      1981
##     2:   0  0   0  0  0  0  1   0   0  0  0    0     5 403250      1981
##     3:   6 13  69  2  2 28 39  NA   3  6  4   13   122     NA      1934
##     4:   9 27 106  3  1 49 61   5   3  7  4   20   153     NA      1934
##     5:  14 26  92  2  4 37 54   6   2  5  7   21   153     NA      1934
##    ---                                                                 
## 84365:   1  0   2  0  0  1  2   0   0  0  0    0    45     NA      1924
## 84366:   0  0   5  1 NA 11 NA  NA   1  1 NA   NA    27     NA      1888
## 84367:   8 16  95 21 NA 46 68  NA   1 10 NA   NA   154     NA      1888
## 84368:   7 13  94 24 NA 67 65  NA   2 18 NA   NA   150     NA      1888
## 84369:   0  1   8  0 NA  4  6  NA   0  2 NA   NA    35     NA      1888
##        birthMonth birthDay birthCountry birthState birthCity deathYear
##     1:         12       27          USA         CO    Denver        NA
##     2:         12       27          USA         CO    Denver        NA
##     3:          2        5          USA         AL    Mobile        NA
##     4:          2        5          USA         AL    Mobile        NA
##     5:          2        5          USA         AL    Mobile        NA
##    ---                                                                
## 84365:          8       20          USA         MI   Holland        NA
## 84366:         11        2          USA         MO St. Louis      1978
## 84367:         11        2          USA         MO St. Louis      1978
## 84368:         11        2          USA         MO St. Louis      1978
## 84369:         11        2          USA         MO St. Louis      1978
##        deathMonth deathDay deathCountry deathState    deathCity nameFirst
##     1:         NA       NA                                          David
##     2:         NA       NA                                          David
##     3:         NA       NA                                           Hank
##     4:         NA       NA                                           Hank
##     5:         NA       NA                                           Hank
##    ---                                                                   
## 84365:         NA       NA                                         George
## 84366:          3       27          USA         CA La Crescenta     Dutch
## 84367:          3       27          USA         CA La Crescenta     Dutch
## 84368:          3       27          USA         CA La Crescenta     Dutch
## 84369:          3       27          USA         CA La Crescenta     Dutch
##        nameLast       nameGiven weight height bats throws      debut
##     1:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     2:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     3:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##     4:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##     5:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##    ---                                                              
## 84365: Zuverink          George    195     76    R      R 1951-04-21
## 84366: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84367: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84368: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84369: Zwilling Edward Harrison    160     66    L      L 1910-08-14
##         finalGame  retroID   bbrefID
##     1: 2013-09-28 aardd001 aardsda01
##     2: 2013-09-28 aardd001 aardsda01
##     3: 1976-10-03 aaroh101 aaronha01
##     4: 1976-10-03 aaroh101 aaronha01
##     5: 1976-10-03 aaroh101 aaronha01
##    ---                              
## 84365: 1959-06-15 zuveg101 zuverge01
## 84366: 1916-07-12 zwild101 zwilldu01
## 84367: 1916-07-12 zwild101 zwilldu01
## 84368: 1916-07-12 zwild101 zwilldu01
## 84369: 1916-07-12 zwild101 zwilldu01
{% endhighlight %}

Now we can see that all At Bat's are at least 1.

Now, one thing baseball fans like looking for is career records. That means we want to summarize across all the years that a batter played, and find, for example, the total number of home runs each player hit. Recall that we learned to do that with "by". For example:


{% highlight r %}
summarized.batters = merged.all[, list(Total.HR=sum(HR)), by="playerID"]
{% endhighlight %}

Here we create one column, `Total.HR`, which we define as the sum of home runs for each player, and we tell it to perform these summaries on each player individually.


{% highlight r %}
summarized.batters
{% endhighlight %}



{% highlight text %}
##         playerID Total.HR
##     1: aardsda01        0
##     2: aaronha01      755
##     3: aaronto01       13
##     4:  aasedo01        0
##     5:  abadan01        0
##    ---                   
## 16336: zupcibo01        7
## 16337:  zupofr01        0
## 16338: zuvelpa01        2
## 16339: zuverge01        0
## 16340: zwilldu01       30
{% endhighlight %}

Now we can see that we've created a new data.table that contains each player's ID and their total career home runs. But in the process, since the only thing we're summarizing by is the player ID, we lost track of their actual first and last names. There's a simple way around that. First, recall that we can create a new column that combines the players' first and last names using `paste` and `:=`, and let's try the same trick again, this time on `merged.all`:


{% highlight r %}
merged.all[, name:=paste(nameFirst, nameLast)]
{% endhighlight %}



{% highlight text %}
##         playerID yearID teamID lgID stint   G G_batting  AB   R   H X2B
##     1: aardsda01   2006    CHN   NL     1  45        43   2   0   0   0
##     2: aardsda01   2008    BOS   AL     1  47         5   1   0   0   0
##     3: aaronha01   1954    ML1   NL     1 122       122 468  58 131  27
##     4: aaronha01   1955    ML1   NL     1 153       153 602 105 189  37
##     5: aaronha01   1956    ML1   NL     1 153       153 609 106 200  34
##    ---                                                                 
## 84365: zuverge01   1958    BAL   AL     1  45        45   9   0   2   0
## 84366: zwilldu01   1910    CHA   AL     1  27        27  87   7  16   5
## 84367: zwilldu01   1914    CHF   FL     1 154       154 592  91 185  38
## 84368: zwilldu01   1915    CHF   FL     1 150       150 548  65 157  32
## 84369: zwilldu01   1916    CHN   NL     1  35        35  53   4   6   1
##        X3B HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary birthYear
##     1:   0  0   0  0  0  0  0   0   0  1  0    0    45     NA      1981
##     2:   0  0   0  0  0  0  1   0   0  0  0    0     5 403250      1981
##     3:   6 13  69  2  2 28 39  NA   3  6  4   13   122     NA      1934
##     4:   9 27 106  3  1 49 61   5   3  7  4   20   153     NA      1934
##     5:  14 26  92  2  4 37 54   6   2  5  7   21   153     NA      1934
##    ---                                                                 
## 84365:   1  0   2  0  0  1  2   0   0  0  0    0    45     NA      1924
## 84366:   0  0   5  1 NA 11 NA  NA   1  1 NA   NA    27     NA      1888
## 84367:   8 16  95 21 NA 46 68  NA   1 10 NA   NA   154     NA      1888
## 84368:   7 13  94 24 NA 67 65  NA   2 18 NA   NA   150     NA      1888
## 84369:   0  1   8  0 NA  4  6  NA   0  2 NA   NA    35     NA      1888
##        birthMonth birthDay birthCountry birthState birthCity deathYear
##     1:         12       27          USA         CO    Denver        NA
##     2:         12       27          USA         CO    Denver        NA
##     3:          2        5          USA         AL    Mobile        NA
##     4:          2        5          USA         AL    Mobile        NA
##     5:          2        5          USA         AL    Mobile        NA
##    ---                                                                
## 84365:          8       20          USA         MI   Holland        NA
## 84366:         11        2          USA         MO St. Louis      1978
## 84367:         11        2          USA         MO St. Louis      1978
## 84368:         11        2          USA         MO St. Louis      1978
## 84369:         11        2          USA         MO St. Louis      1978
##        deathMonth deathDay deathCountry deathState    deathCity nameFirst
##     1:         NA       NA                                          David
##     2:         NA       NA                                          David
##     3:         NA       NA                                           Hank
##     4:         NA       NA                                           Hank
##     5:         NA       NA                                           Hank
##    ---                                                                   
## 84365:         NA       NA                                         George
## 84366:          3       27          USA         CA La Crescenta     Dutch
## 84367:          3       27          USA         CA La Crescenta     Dutch
## 84368:          3       27          USA         CA La Crescenta     Dutch
## 84369:          3       27          USA         CA La Crescenta     Dutch
##        nameLast       nameGiven weight height bats throws      debut
##     1:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     2:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     3:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##     4:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##     5:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##    ---                                                              
## 84365: Zuverink          George    195     76    R      R 1951-04-21
## 84366: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84367: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84368: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84369: Zwilling Edward Harrison    160     66    L      L 1910-08-14
##         finalGame  retroID   bbrefID            name
##     1: 2013-09-28 aardd001 aardsda01   David Aardsma
##     2: 2013-09-28 aardd001 aardsda01   David Aardsma
##     3: 1976-10-03 aaroh101 aaronha01      Hank Aaron
##     4: 1976-10-03 aaroh101 aaronha01      Hank Aaron
##     5: 1976-10-03 aaroh101 aaronha01      Hank Aaron
##    ---                                              
## 84365: 1959-06-15 zuveg101 zuverge01 George Zuverink
## 84366: 1916-07-12 zwild101 zwilldu01  Dutch Zwilling
## 84367: 1916-07-12 zwild101 zwilldu01  Dutch Zwilling
## 84368: 1916-07-12 zwild101 zwilldu01  Dutch Zwilling
## 84369: 1916-07-12 zwild101 zwilldu01  Dutch Zwilling
{% endhighlight %}

Now we've added to `merged.all` a `name` column:


{% highlight r %}
merged.all
{% endhighlight %}



{% highlight text %}
##         playerID yearID teamID lgID stint   G G_batting  AB   R   H X2B
##     1: aardsda01   2006    CHN   NL     1  45        43   2   0   0   0
##     2: aardsda01   2008    BOS   AL     1  47         5   1   0   0   0
##     3: aaronha01   1954    ML1   NL     1 122       122 468  58 131  27
##     4: aaronha01   1955    ML1   NL     1 153       153 602 105 189  37
##     5: aaronha01   1956    ML1   NL     1 153       153 609 106 200  34
##    ---                                                                 
## 84365: zuverge01   1958    BAL   AL     1  45        45   9   0   2   0
## 84366: zwilldu01   1910    CHA   AL     1  27        27  87   7  16   5
## 84367: zwilldu01   1914    CHF   FL     1 154       154 592  91 185  38
## 84368: zwilldu01   1915    CHF   FL     1 150       150 548  65 157  32
## 84369: zwilldu01   1916    CHN   NL     1  35        35  53   4   6   1
##        X3B HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary birthYear
##     1:   0  0   0  0  0  0  0   0   0  1  0    0    45     NA      1981
##     2:   0  0   0  0  0  0  1   0   0  0  0    0     5 403250      1981
##     3:   6 13  69  2  2 28 39  NA   3  6  4   13   122     NA      1934
##     4:   9 27 106  3  1 49 61   5   3  7  4   20   153     NA      1934
##     5:  14 26  92  2  4 37 54   6   2  5  7   21   153     NA      1934
##    ---                                                                 
## 84365:   1  0   2  0  0  1  2   0   0  0  0    0    45     NA      1924
## 84366:   0  0   5  1 NA 11 NA  NA   1  1 NA   NA    27     NA      1888
## 84367:   8 16  95 21 NA 46 68  NA   1 10 NA   NA   154     NA      1888
## 84368:   7 13  94 24 NA 67 65  NA   2 18 NA   NA   150     NA      1888
## 84369:   0  1   8  0 NA  4  6  NA   0  2 NA   NA    35     NA      1888
##        birthMonth birthDay birthCountry birthState birthCity deathYear
##     1:         12       27          USA         CO    Denver        NA
##     2:         12       27          USA         CO    Denver        NA
##     3:          2        5          USA         AL    Mobile        NA
##     4:          2        5          USA         AL    Mobile        NA
##     5:          2        5          USA         AL    Mobile        NA
##    ---                                                                
## 84365:          8       20          USA         MI   Holland        NA
## 84366:         11        2          USA         MO St. Louis      1978
## 84367:         11        2          USA         MO St. Louis      1978
## 84368:         11        2          USA         MO St. Louis      1978
## 84369:         11        2          USA         MO St. Louis      1978
##        deathMonth deathDay deathCountry deathState    deathCity nameFirst
##     1:         NA       NA                                          David
##     2:         NA       NA                                          David
##     3:         NA       NA                                           Hank
##     4:         NA       NA                                           Hank
##     5:         NA       NA                                           Hank
##    ---                                                                   
## 84365:         NA       NA                                         George
## 84366:          3       27          USA         CA La Crescenta     Dutch
## 84367:          3       27          USA         CA La Crescenta     Dutch
## 84368:          3       27          USA         CA La Crescenta     Dutch
## 84369:          3       27          USA         CA La Crescenta     Dutch
##        nameLast       nameGiven weight height bats throws      debut
##     1:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     2:  Aardsma     David Allan    205     75    R      R 2004-04-06
##     3:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##     4:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##     5:    Aaron     Henry Louis    180     72    R      R 1954-04-13
##    ---                                                              
## 84365: Zuverink          George    195     76    R      R 1951-04-21
## 84366: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84367: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84368: Zwilling Edward Harrison    160     66    L      L 1910-08-14
## 84369: Zwilling Edward Harrison    160     66    L      L 1910-08-14
##         finalGame  retroID   bbrefID            name
##     1: 2013-09-28 aardd001 aardsda01   David Aardsma
##     2: 2013-09-28 aardd001 aardsda01   David Aardsma
##     3: 1976-10-03 aaroh101 aaronha01      Hank Aaron
##     4: 1976-10-03 aaroh101 aaronha01      Hank Aaron
##     5: 1976-10-03 aaroh101 aaronha01      Hank Aaron
##    ---                                              
## 84365: 1959-06-15 zuveg101 zuverge01 George Zuverink
## 84366: 1916-07-12 zwild101 zwilldu01  Dutch Zwilling
## 84367: 1916-07-12 zwild101 zwilldu01  Dutch Zwilling
## 84368: 1916-07-12 zwild101 zwilldu01  Dutch Zwilling
## 84369: 1916-07-12 zwild101 zwilldu01  Dutch Zwilling
{% endhighlight %}

Now when we perform this summary, let's do it not just on the player ID, but also on their name:


{% highlight r %}
summarized.batters = merged.all[, list(Total.HR=sum(HR)), by=c("playerID", "name")]
summarized.batters
{% endhighlight %}



{% highlight text %}
##         playerID            name Total.HR
##     1: aardsda01   David Aardsma        0
##     2: aaronha01      Hank Aaron      755
##     3: aaronto01    Tommie Aaron       13
##     4:  aasedo01        Don Aase        0
##     5:  abadan01       Andy Abad        0
##    ---                                   
## 16336: zupcibo01      Bob Zupcic        7
## 16337:  zupofr01      Frank Zupo        0
## 16338: zuvelpa01    Paul Zuvella        2
## 16339: zuverge01 George Zuverink        0
## 16340: zwilldu01  Dutch Zwilling       30
{% endhighlight %}

By summarizing based on these two columns, we can keep both their ID and their real name.

Now, just like any data.table, we can sort it to find out who the top home-run hitters are. For this we use the `order` function:


{% highlight r %}
summarized.batters[order(Total.HR), ]
{% endhighlight %}



{% highlight text %}
##         playerID           name Total.HR
##     1: aardsda01  David Aardsma        0
##     2:  aasedo01       Don Aase        0
##     3:  abadan01      Andy Abad        0
##     4:  abadfe01  Fernando Abad        0
##     5: abadijo01    John Abadie        0
##    ---                                  
## 16336: rodrial01 Alex Rodriguez      654
## 16337:  mayswi01    Willie Mays      660
## 16338:  ruthba01      Babe Ruth      714
## 16339: aaronha01     Hank Aaron      755
## 16340: bondsba01    Barry Bonds      762
{% endhighlight %}

Baseball fans won't be surprised that at the top we can see Barry Bonds, Hank Aaron, Babe Ruth, and some other legendary baseball hitters. In the same way we can summarize by other statistics, like total number of hits or runs. For instance, here let's add `Total.R` for total number of runs, and `Total.H` for total number of hits.


{% highlight r %}
summarized.batters = merged.all[, list(Total.HR=sum(HR), Total.R=sum(R), Total.H=sum(H)), by=c("playerID", "name")]
summarized.batters
{% endhighlight %}



{% highlight text %}
##         playerID            name Total.HR Total.R Total.H
##     1: aardsda01   David Aardsma        0       0       0
##     2: aaronha01      Hank Aaron      755    2174    3771
##     3: aaronto01    Tommie Aaron       13     102     216
##     4:  aasedo01        Don Aase        0       0       0
##     5:  abadan01       Andy Abad        0       1       2
##    ---                                                   
## 16336: zupcibo01      Bob Zupcic        7      99     199
## 16337:  zupofr01      Frank Zupo        0       3       3
## 16338: zuvelpa01    Paul Zuvella        2      41     109
## 16339: zuverge01 George Zuverink        0       4      21
## 16340: zwilldu01  Dutch Zwilling       30     167     364
{% endhighlight %}

Now we've saved all that career information into `summarized.batters`.

The more a player gets hits in baseball, the more chance they have to actually score runs. That means it's not surprising that there's a correlation between them. We can take a look at that correlation through ggplot. We'll put total hits (`Total.H`) on the x-axis and total runs (`Total.R`) on the y-axis.


{% highlight r %}
ggplot(summarized.batters, aes(Total.H, Total.R)) + geom_point()
{% endhighlight %}

![center](../../figs/code_lesson4/unnamed-chunk-80-1.png) 

Here we can see a clear correlation between the number of hits a player gets and the number of runs.

So far each of these summaries has been of one statistic: the total number of home runs, or the total number of hits. But some baseball statistics are calculated based on several of a player's statistics. For example, consider the batting average, which is the number of hits a player gets, divided by the number of times he goes up to bat.


{% highlight r %}
head(merged.all)
{% endhighlight %}



{% highlight text %}
##     playerID yearID teamID lgID stint   G G_batting  AB   R   H X2B X3B HR
## 1: aardsda01   2006    CHN   NL     1  45        43   2   0   0   0   0  0
## 2: aardsda01   2008    BOS   AL     1  47         5   1   0   0   0   0  0
## 3: aaronha01   1954    ML1   NL     1 122       122 468  58 131  27   6 13
## 4: aaronha01   1955    ML1   NL     1 153       153 602 105 189  37   9 27
## 5: aaronha01   1956    ML1   NL     1 153       153 609 106 200  34  14 26
## 6: aaronha01   1957    ML1   NL     1 151       151 615 118 198  27   6 44
##    RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary birthYear birthMonth
## 1:   0  0  0  0  0   0   0  1  0    0    45     NA      1981         12
## 2:   0  0  0  0  1   0   0  0  0    0     5 403250      1981         12
## 3:  69  2  2 28 39  NA   3  6  4   13   122     NA      1934          2
## 4: 106  3  1 49 61   5   3  7  4   20   153     NA      1934          2
## 5:  92  2  4 37 54   6   2  5  7   21   153     NA      1934          2
## 6: 132  1  1 57 58  15   0  0  3   13   151     NA      1934          2
##    birthDay birthCountry birthState birthCity deathYear deathMonth
## 1:       27          USA         CO    Denver        NA         NA
## 2:       27          USA         CO    Denver        NA         NA
## 3:        5          USA         AL    Mobile        NA         NA
## 4:        5          USA         AL    Mobile        NA         NA
## 5:        5          USA         AL    Mobile        NA         NA
## 6:        5          USA         AL    Mobile        NA         NA
##    deathDay deathCountry deathState deathCity nameFirst nameLast
## 1:       NA                                       David  Aardsma
## 2:       NA                                       David  Aardsma
## 3:       NA                                        Hank    Aaron
## 4:       NA                                        Hank    Aaron
## 5:       NA                                        Hank    Aaron
## 6:       NA                                        Hank    Aaron
##      nameGiven weight height bats throws      debut  finalGame  retroID
## 1: David Allan    205     75    R      R 2004-04-06 2013-09-28 aardd001
## 2: David Allan    205     75    R      R 2004-04-06 2013-09-28 aardd001
## 3: Henry Louis    180     72    R      R 1954-04-13 1976-10-03 aaroh101
## 4: Henry Louis    180     72    R      R 1954-04-13 1976-10-03 aaroh101
## 5: Henry Louis    180     72    R      R 1954-04-13 1976-10-03 aaroh101
## 6: Henry Louis    180     72    R      R 1954-04-13 1976-10-03 aaroh101
##      bbrefID          name
## 1: aardsda01 David Aardsma
## 2: aardsda01 David Aardsma
## 3: aaronha01    Hank Aaron
## 4: aaronha01    Hank Aaron
## 5: aaronha01    Hank Aaron
## 6: aaronha01    Hank Aaron
{% endhighlight %}

So in our batting dataset, for Hank Aaron in 1955, we can see that he had 189 hits out of 602 at-bats. We'd calculate his batting average as


{% highlight r %}
189 / 602
{% endhighlight %}



{% highlight text %}
## [1] 0.3139535
{% endhighlight %}

for that year. What if we wanted to compute each player's career batting average? It turns out that's easy with the summary operation. We add a column `BattingAverage` to the summary data.table, which we put as the sum of all hits divided by the sum of all at-bats.


{% highlight r %}
summarized.batters = merged.all[, list(Total.HR=sum(HR), Total.R=sum(R), Total.H=sum(H), BattingAverage=sum(H) / sum(AB)), by=c("playerID", "name")]
summarized.batters
{% endhighlight %}



{% highlight text %}
##         playerID            name Total.HR Total.R Total.H BattingAverage
##     1: aardsda01   David Aardsma        0       0       0      0.0000000
##     2: aaronha01      Hank Aaron      755    2174    3771      0.3049984
##     3: aaronto01    Tommie Aaron       13     102     216      0.2288136
##     4:  aasedo01        Don Aase        0       0       0      0.0000000
##     5:  abadan01       Andy Abad        0       1       2      0.0952381
##    ---                                                                  
## 16336: zupcibo01      Bob Zupcic        7      99     199      0.2503145
## 16337:  zupofr01      Frank Zupo        0       3       3      0.1666667
## 16338: zuvelpa01    Paul Zuvella        2      41     109      0.2219959
## 16339: zuverge01 George Zuverink        0       4      21      0.1478873
## 16340: zwilldu01  Dutch Zwilling       30     167     364      0.2843750
{% endhighlight %}

This kind of summary operation thus lets us generate any statistic we're interested in. We could then, for instance, put it into a histogram to find out its distribution:


{% highlight r %}
ggplot(summarized.batters, aes(BattingAverage)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](../../figs/code_lesson4/unnamed-chunk-84-1.png) 

We can see that they center around about 25%, with a large number of people with close to 0 batting average, which would mostly be pitchers.

In this way you're able to test hypotheses almost as fast as you can think of them. This loop of asking questions about your data and getting answers back is the core of exploratory data analysis.
