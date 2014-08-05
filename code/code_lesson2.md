---
layout: default
---

Lesson 2: Visualizing Data Using ggplot2
============



<a name="segment1"></a>

Segment 1: Introduction
------------

In data analysis more than anything, a picture really is worth a thousand words. When you start analyzing data in R, your first step shouldn't be to run a complex statistical test: first, you should visualize your data in a graph. This lets you understand the basic nature of the data, so that you know what tests you can perform, and where you should focus your analysis. I'm David Robinson, and in this lesson we'll introduce you to ggplot2, a powerful R package that produces data visualizations easily and intuitively. We will assume you are moderately familiar with basic concepts in R, including variables and functions, and with RStudio, the integrated development environment for programming in R.

So, ggplot2 is a third party package: that means it's code that doesn't come built into the language. This means you have to install it.

You can do that with one line of R code here in your interactive terminal, which is:


{% highlight r %}
install.packages("ggplot2")
{% endhighlight %}

and hit return. Or you can go to the Tools->Install Packages menu, where here you type "ggplot2" and hit install.

Each time you reopen R, you need to load the library using the `library` function before you use it. So here that's:


{% highlight r %}
library("ggplot2")
{% endhighlight %}



{% highlight text %}
## Loading required package: methods
{% endhighlight %}

Now we're ready to use it. ggplot2 comes with some data available to use as a demonstration: particularly, the "diamonds" dataset, containing information about several attributes of 54000 diamonds. We can access it using the `data` function:


{% highlight r %}
data("diamonds")
{% endhighlight %}

See that we've added "diamonds" to our global environment. Once we've loaded the diamonds dataset, we can view it using `View`:


{% highlight r %}
View(diamonds)
{% endhighlight %}

Here we have a view of it kind of like a spreadsheet. Here we have the carat: that's the weight of the diamond; and the cut, color and clarity: each of these are measuring something about the quality of the diamond in various levels. And then we have other attributes including the price of the diamond. You can find out what each of these mean using the "help" function:


{% highlight r %}
help(diamonds)
{% endhighlight %}

Here we get a description of the diamonds dataset, and the details about each of the columns.

<a name="segment2"></a>

Segment 2: Introduction to ggplot2
------------

Let's say that we as scientists are interested in understanding the relationship between those attributes. For example, how does weight, in carats, affect the price? Or how does the quality of the color, or of the diamond's clarity, affect the price? These kinds of questions, where we're looking for interesting relationships among attributes using the observations we have, are common, almost universal, across data analysis.

One common visualization for determining the relationship between attributes is a scatter plot, where each diamond will be represented by one point. This is the point where as graphers, we have to make a few decisions. Let's talk about "aesthetics."

An "aesthetic" is a dimension of a graph that we can perceive visually: the simplest example being the x and y axes. When we make a scatterplot, we choose one attribute to assign to the x axis, and one attribute to assign to the y axis.

Other aesthetics we can use in a scatter plot are the color, size, and shape of the points in the graph: each of these aesthetics lets us communicate some dimension of the data, and understand complex relationships between them.

As an example, let's use ggplot2 to create a scatterplot where we put carat, or weight, on the x axis and price, in dollars, on the y axis. So now we make a ggplot2 call. We start with:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_2a.png) 

Now, there are three parts to a ggplot2 graph. The first is the data we'll be graphing. In this case, we are plotting the diamonds data frame, so we type "diamonds". Second, we show the mapping of aesthetics to the attributes we'll be plotting. We type aes- meaning aesthetics- then open parentheses, and now our assignments: we say "x=carat", saying we want to put carat on the x-axis, then "y=price", saying what we want to put on the y-axis.

Now that we've defined the structure of our graph, we are going to add a "layer" to it: that is, define what time of graph it is. In this case, we want to make a scatter plot: the name for that layer is geom_point. "geom" is a typical start for each of these layers. Now we've defined our graph, and hit return, and we see our scatter plot.

See that we've placed "carat" on the x axis, and "price" on the y-axis. Every one of these points represents one row in our data frame: that is, one diamond. We've now communicated a relationship between those two attributes in the dataset: as weight increases, price increases.

Now, this plot shows two aesthetics- weight and price- but there are many other attributes of the data we can communicate. For example, we might want to see how the quality of the cut, or the color, or the clarity, affects the price. Each of those variables is a factor: that means each value belongs to one of a finite number of categories. We can add this using another aesthetic, for example, the color of the points:

To add an aesthetic, we can hit the up arrow to get to our previous line, and then add into the aes call of the aesthetic, "color=clarity", using clarity, which is a measure of the clarity of each diamond, to color our points. We hit return:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=clarity)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_2b.png) 

Now every point is colored according to the quality of the clarity of each diamond. Notice that it created a legend on the right side. You can see that some of the lighter diamonds are more expensive if they have a high clarity rating, and conversely that some of the heavier diamonds aren't as expensive for having a low clarity rating. This is what leads to this rainbow pattern.

If we would rather see how the quality of the color or cut of the diamond affects the price, we can change the aesthetic. Here in "aes" we change "clarity" to "color".


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=color)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_2c.png) 

Now every item in the color legend is one of the ratings of color. Or we can change it to "cut":


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=cut)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_2d.png) 

This way we can explore the relationship of each of these variables and how it affects the carat/price relationship.

Now, what if we want to see the effect of both color and cut? We can use a fourth aesthetic, such as the size of the points. So here we have color representing the clarity. Let's add another aesthetic- let's say "size=cut."


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=clarity, size=cut)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment 2e.png) 

Now the size of every point is determined by the cut even while the color is still determined by the clarity. Similarly, we could use the shape to represent the cut:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=clarity, shape=cut)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment 2f.png) 

Now every shape represents a different cut of the diamond.

Now, this scatter plot is one "layer", which means we can add additional layers besides the scatter plot using the plus sign. For example, what if we want to add a smoothing curve that shows the general trend of the data? That's a layer called geom_smooth.

So let's take this plot, take out the color, and add a smoothing trend:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + geom_smooth()
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment 2g.png) 

The gray area around the curve is a confidence interval, suggesting how much uncertainty there is in this smoothing curve. If we want to turn off the confidence interval, we can add an option to the geom_smooth later; specifically "se=FALSE", where "s.e." stands for "standard error."


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + geom_smooth(se=FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment 2h.png) 

This gets rid of the gray area and now we can just see the smoothing curve.

Similarly, if we would rather show a best fit straight line rather than a curve, we can change the "method" option in the geom_smooth layer. In this case it's method="lm", where "lm" stands for "Linear model".


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + geom_smooth(se=FALSE, method="lm")
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment 2i.png) 

There we fit a best fit line to the relationship between carat and price with this geom_smooth layer.

If you used a color aesthetic, ggplot will create one smoothing curve for each color. For example, if we add "color=clarity":


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=clarity)) + geom_point() + geom_smooth(se=FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment 2j.png) 

Now we see it actually fits one curve for each of these colors. This is a useful way to compare and contrast multiple trends. Note that you can show this smoothing curve layer *without* showing your scatter plot layer, simply by removing the geom_point() layer:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=clarity)) + geom_smooth(se=FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment 2k.png) 

This might be a bit clearer: we can see just the fit curves without seeing the actual points.

<a name="segment3"></a>

Segment 3: Faceting and Additional Options
-------------

Another way that you can communicate information about an attribute in your data is to divide your plot up into multiple plots, one for each level, letting you view them separately. This is called "faceting", and ggplot makes it very easy with the "facet_wrap" function.

To do that, we go to a plot like this, and add "facet_wrap(". Now here we put a tilde (~), and then the attribute we would like to divide the plots by, here "clarity."


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=cut)) + geom_point() + facet_wrap(~ clarity)
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_3a.png) 

Now let's zoom in on this. You can see that now we've divided it into eight subplots, each of which has a different "clarity" value, and you can see how the trend differs between each of those subplots. We can still see that the color is representing the quality of the cut of the diamond.

You can even divide your graph based on two different attributes, such as both color and clarity, using facet_grid. In this case that would be "facet_grid(", then you put "color ~ clarity", where the tilde (~) means "explained by."


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price, color=cut)) + geom_point() + facet_grid(color ~ clarity)
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_3b.png) 

Now you can see that each column represents one of the clarity ratings, and each row represents one of the color ratings, and within the combination you can see only those that match that color and that clarity. Faceting like this gives another way to communicate the relationships within your data.

There are many other ways to customize a plot. For starters, you might want to set a title, or set the x or y axis labels manually. You change these options by *adding* to the end of the line of code. To set the title, you would use the ggtitle function:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + ggtitle("My scatter plot")
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_3c.png) 

This adds a title to the top of your graph. If you'd like to change the x- or y- axis labels, you would add "xlab" for "x label", then your custom label:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + ggtitle("My scatter plot") + xlab("Weight (carats)")
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_3d.png) 

You might also want to limit the range of the x or the y axes. You can do this with the xlim or ylim options, which are also added to the end of the line. In this case, say we only want to look at the weights from 0 to 2 carats. We would do:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + ggtitle("My scatter plot") + xlab("Weight (carats)") + xlim(0, 2)
{% endhighlight %}



{% highlight text %}
## Warning: Removed 1889 rows containing missing values (geom_point).
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_3e.png) 

Each of these options gets added on after the last one. Now we can see that the x-axis ranges only from 0 to 2. Similarly, if we wanted to show only the y-axis from 0 to 10000, we could put


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + ggtitle("My scatter plot") + xlab("Weight (carats)") + ylim(0, 10000)
{% endhighlight %}



{% highlight text %}
## Warning: Removed 5222 rows containing missing values (geom_point).
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_3f.png) 

Another possibility is to put one of the axes on a log scale. You can do this with the scale_y_log10() function.


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + ggtitle("My scatter plot") + xlab("Weight (carats)") + ylim(0, 10000)
{% endhighlight %}



{% highlight text %}
## Warning: Removed 5222 rows containing missing values (geom_point).
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_3g.png) 

Now you've put the y-axis on a log scale.

There are many other available options and customizations: each gets added to the end of the plot just like these.

<a name="segment4"></a>

Segment 4: Histograms and Density Plots
-------------

We've seen a lot of ways to customize scatter plots. But scatter plots are just one kind of graph. Sometimes we want to look at just one dimension of our data and observe its distribution: for that, we'll use a histogram.

All you need to do to make a histogram is to change your layer from geom_point() to geom_histogram(). For example, we do


{% highlight r %}
ggplot(diamonds, aes(x=price)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4a.png) 

This creates a histogram. Notice that we've on the x-axis we've placed price. On the y-axis is the frequency within each bin. This is a visualization of the density of the distribution of price.

You can change the width of each bin as an option to the geom_histogram layer. You can make them wider:


{% highlight r %}
ggplot(diamonds, aes(x=price)) + geom_histogram(binwidth=2000)
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4b.png) 

Or you can change it to be thinner:


{% highlight r %}
ggplot(diamonds, aes(x=price)) + geom_histogram(binwidth=200)
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4c.png) 

Other than that, you can do most of the same things with a histogram that you could with a scatter plot. You can again facet histograms into multiple subplots using facet_wrap. For instance, take a plot and use `facet_wrap`, and let's divide it by `clarity`:


{% highlight r %}
ggplot(diamonds, aes(x=price)) + geom_histogram(binwidth=200) + facet_wrap(~ clarity)
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4d.png) 

Notice that we've created 8 subplots, one for each level of clarity. Note that each subplot shares the same y axis, which might make it hard to interpret the frequencies: some subplots have far more points than others. So to free up the y axis so they can be different between the graphs, we add an argument to facet_wrap. In this case, we add `scale="free_y"`:


{% highlight r %}
ggplot(diamonds, aes(x=price)) + geom_histogram(binwidth=200) + facet_wrap(~ clarity, scale="free_y")
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4e.png) 

Notice that each of the subplots now has a different y-axis; some of them going up to 50, some up to 1000, depending on what is appropriate for that subplot.

Let's say you want to add another attribute to this histogram to see its effect on the density: for example, to make a stacked histogram based on the clarity attribute. Try adding the "fill" aesthetic:


{% highlight r %}
ggplot(diamonds, aes(x=price, fill=clarity)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4f.png) 

This creates a stacked histogram where each color represents the distribution of a different clarity attribute.

You could set this to any other attribute as well, for example the cut:


{% highlight r %}
ggplot(diamonds, aes(x=price, fill=cut)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4g.png) 

Now you can see how the distribution is composed within each of those variables.

Another way to view the distribution is as a density curve. You can do this by changing `geom_histogram` to `geom_density`. Remove the `fill` attribute.


{% highlight r %}
ggplot(diamonds, aes(x=price)) + geom_density()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4h.png) 

Notice it looks smoother than a histogram. If you want to divide this density curve up based on one of your attributes, you can use the `color` aesthetic instead of `fill`. For example, you can add `color=cut`.


{% highlight r %}
ggplot(diamonds, aes(x=price, color=cut)) + geom_density()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_4i.png) 

This provides a good way to compare multiple distributions.

<a name="segment5"></a>

Segment 5: Boxplots and Violin Plots
-----------

One common method in statistics for comparing multiple densities is to use a boxplot. A boxplot has two attributes: an x, which is usually a classification into categories, and y, the actual variable that you're comparing.

In this case, let's say that you want to compare the distribution of the price within each color. You would do:


{% highlight r %}
ggplot(diamonds, aes(x=color, y=price)) + geom_boxplot()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_5a.png) 

The boxplot provides some information in a compact form: you can see the median as a thick black line, the edges of the box show the 25th and 75th quantiles of the data respectively, and these points are outliers that lie far outside the expected range of the data. In this particular case, since there are a large number of outliers you might want to try putting the y-axis on a log scale. Recall that we do that by adding an option:


{% highlight r %}
ggplot(diamonds, aes(x=color, y=price)) + geom_boxplot() + scale_y_log10()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_5b.png) 

This is a better behaved boxplot that gets a better sense of how the distribution of price differs across multiple colors.

One problem with the boxplot is that it doesn't show details of the distribution besides these quantiles. This works well when the data follows a Normal distribution, or a "bell curve," but it might not work well for stranger distributions. For example, the distribution might have not one but two frequency peaks, what we call "bimodality." However strange the distribution, a box plot will always look like a square. We can instead view the distribution as a density using what's called a "violin plot". To do that, all we do is change `geom_boxplot` to `geom_violin`.


{% highlight r %}
ggplot(diamonds, aes(x=color, y=price)) + geom_violin() + scale_y_log10()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_5c.png) 

The width at each point in this violin plot represents the frequency of that price. So these bumps show the prices that are more common, and we can see that indeed within some colors there is bimodality- there are multiple points that are common- that a boxplot did not represent.

Just like in scatter plots or histograms, if we want to see whether another variable is involved, we can use `facet_wrap` to divide our plot into multiple subplots. For example, we could divide this into subgroups based on clarity. To do that, we would do


{% highlight r %}
ggplot(diamonds, aes(x=color, y=price)) + geom_violin() + scale_y_log10() + facet_wrap(~ clarity)
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_5d.png) 

Now you can see that we've divided it into eight smaller violin plots showing the distribution within each of those levels of clarity.

<a name="segment6"></a>

Segment 6: Input- Getting Data into the Right Format
-----------

So far all of our analyses have started with a data frame: one row per observation, one column for each attribute. But let's say you have just one vector of numbers and you want to create a histogram, or you have two vectors and want to make a scatterplot. It may not be worth it to construct a data frame with those values just so you can graph it. To make your life easier, ggplot2 provides a simple way to plot one or two vectors, which is the `qplot` function.

Let's generate some random numbers we want to plot. The rnorm function generates random values from a normal distribution, or "bell curve." So if we create a variable `x` with `rnorm`, saying how many random values we want, for example `1000`:


{% highlight r %}
x = rnorm(1000)
{% endhighlight %}

We have created a variable containing 1000 values. Here we can see:


{% highlight r %}
x
{% endhighlight %}



{% highlight text %}
##    [1] -0.7959696 -1.5781027  0.0773569  0.5741992  0.4241290 -0.0308448
##    [7]  0.0019698 -1.4836228 -0.1936896 -1.8217849  0.1308407  0.3536961
##   [13] -1.1248386 -1.2835912 -0.5197232  1.6342223 -0.3623886 -0.3167862
##   [19] -0.5354058 -0.4174116  1.4643429 -0.3483456  0.1367558  0.4226802
##   [25]  0.1545329  0.3926258  0.3430607 -0.6780351  0.9364956 -1.6722821
##   [31] -2.0394362 -0.8239917  1.4688713 -0.6387756  0.4652744 -1.0144235
##   [37] -0.4304354 -1.0845220 -0.8550870 -0.2891349  0.7620406  0.6593881
##   [43] -0.5593859  0.8817869 -1.2114166  0.3655444 -0.4974011 -0.2844669
##   [49]  0.3477334 -1.3246290  0.9449256  2.2602721 -0.4652058  2.0223930
##   [55] -0.9741220 -2.0036181 -0.3321661  2.4028739 -0.2841932 -0.0028120
##   [61]  0.3484321  0.6093935  0.9812512  1.5278250  0.9703586 -1.4168706
##   [67] -2.2008279 -0.3125171  0.2685887  1.1383113 -0.5726550 -1.6779272
##   [73] -0.2342121 -0.8076935 -0.6867322  0.4363610  0.5239006 -1.7578964
##   [79] -1.7582496 -0.4021688  1.5032641 -1.5379724  1.0002962  1.7021732
##   [85]  1.0097385  1.3581171  1.3564881 -0.8898941 -1.0528272  0.2099831
##   [91] -0.7866511  1.8270255  1.3862985  2.5968134  0.1562721 -0.0105200
##   [97] -2.5604857  0.5452795  0.8878745  1.4361878  0.5299330  0.6133065
##  [103]  0.6556744  1.6100314 -2.8660154 -0.4482302 -0.4485881 -0.3289870
##  [109] -0.4056053 -0.8801217 -0.4670084  1.0707935 -0.1916639 -0.9894449
##  [115]  1.2976009 -0.6689716 -1.1498471  0.9013003  1.2594086 -0.5267253
##  [121] -0.7213677  2.0553964 -1.0668172  0.7419988  0.5643351  0.8105255
##  [127]  0.4955311 -0.1611881 -0.3468598  0.4456445  0.4996216  0.1541034
##  [133] -0.8135348 -1.1708218  0.5175897  1.2293175 -1.1036401 -0.8107780
##  [139]  0.7322602 -0.0425832  1.5670989  0.7884926  0.1615738  0.0690910
##  [145] -0.1736764 -0.9658104  0.1161025 -0.2902115  0.5733875 -0.3000646
##  [151] -0.2953446  0.2291009 -0.6757646 -0.7610283  0.4809699 -0.0851359
##  [157]  1.8103378 -0.4748433  0.4845448  0.1551554 -0.2789510  1.2946662
##  [163]  0.7789801 -0.5669838 -0.7042507  2.4072074  1.0882675  0.2658584
##  [169] -0.0366035  0.2333007 -0.9085864 -1.5507462 -0.6458023  1.6233180
##  [175] -1.6731588 -1.6736690 -0.0784647 -1.1972694  0.1615443  0.9015466
##  [181] -0.9306812  0.3557063 -0.7210208  1.8941173 -1.6399701 -0.0581072
##  [187]  0.0009342 -0.2339161  0.5449176  0.3880994 -0.0035344  0.4930497
##  [193] -0.9248505  0.1321949 -0.9643252  0.4392572  0.2239731  0.8912434
##  [199]  0.6960063 -0.5287149  0.4760224 -0.1868170  1.1477952  0.0922831
##  [205]  1.4314905  1.1670866 -1.8605910 -0.1650971  1.2155777 -1.1035837
##  [211]  0.5442406 -1.8791965  2.0770247  0.2317476 -1.1622901  0.5095880
##  [217]  1.3104410  1.5752885  0.9728386  0.1185939  1.6036004  0.3793261
##  [223]  0.3672832 -0.5355303 -1.3160212  1.5385731  0.3306754 -0.8205976
##  [229]  0.5302628  0.1953363 -0.6371132 -0.8073217  0.4631549 -0.1710797
##  [235]  0.0157574 -1.5128082 -0.5827663 -0.2838363 -2.2164454 -0.0584162
##  [241]  0.0154599  0.5636060  0.7941731  1.4969582 -0.4106554 -1.2172106
##  [247]  1.4939839 -0.9814031  1.9500624 -0.4161861 -0.5189286  0.2385414
##  [253] -0.2658256  0.0580943 -0.2871514  1.6945038 -0.1983610  0.1449367
##  [259]  0.4629220 -0.2632544 -0.0170717  1.0597111 -0.7171665  0.7649328
##  [265] -0.1305133 -1.9046690 -0.9639378 -1.3189566 -1.2195106 -0.4598309
##  [271] -1.4567044 -0.9192561 -1.2229143 -0.6928483  0.5026728  1.4802040
##  [277]  1.3074409 -0.3906403  1.2289658 -0.7081951  0.1729308  0.7297977
##  [283] -0.3372331  0.4573929 -0.7033719 -0.5212837  0.1627424 -0.4580351
##  [289]  1.1752984 -0.5175327  0.7430194 -0.0701175 -0.8066119  0.0770441
##  [295]  0.3106499  1.1108179 -0.2478867  0.7381671 -1.6349591 -0.2670197
##  [301] -0.0697006  0.4186534 -1.6591740 -2.0412920 -0.5534740 -1.3857845
##  [307]  1.4382271 -0.4213972 -1.5665922  0.1997553  0.9536411 -1.3198176
##  [313]  0.0051833  0.4950181 -0.0227172  0.0651840  0.1827238 -0.5890935
##  [319]  0.4766168  0.1651913  0.9607531 -1.9976346  0.3648324 -1.2649263
##  [325] -0.2539187  1.3877908  0.0258309 -1.0172024 -0.5698280  2.4066689
##  [331] -1.7565462 -0.1381034 -0.6789023  0.3048554 -1.2854784 -3.4561399
##  [337] -1.2557576 -0.3614945  0.3173806 -0.5280646  1.2384646 -0.5578981
##  [343] -0.9888988 -0.4898498  1.2245865 -0.3967616 -0.0960928  0.2344128
##  [349] -0.9406002 -1.1490017  0.4714183  0.1638662  0.6161755 -0.5448228
##  [355] -1.1038452  1.4281864 -1.1168529  1.1382163  0.6806825 -0.4606020
##  [361]  1.8179969  0.3939587  0.1697833  0.9236168 -0.2499475 -1.3494251
##  [367]  0.7023061 -0.0101574  0.3761681 -1.6850077 -0.2518556  0.7607298
##  [373] -0.7786369  1.9814064 -0.4056633  0.5164120  0.5019247 -0.2691312
##  [379] -1.9122820  1.3438623  0.6644667 -1.3027011  1.4019832 -0.5955636
##  [385]  0.4057616 -0.0996711  1.0713066 -0.3639151  0.4417273 -1.5672654
##  [391] -0.7355268  0.5490882  0.8364842  0.5333652  1.0067147  1.2662324
##  [397]  1.8209087  0.2685291  0.3272133  1.4113609 -1.7016117  0.7101363
##  [403]  0.0764861 -0.1240923 -0.0475662  0.0729718 -0.6540267  0.6924168
##  [409]  0.4023190  0.6935248 -1.0229800  0.5254000  0.2762314  0.6254588
##  [415] -0.8814278 -1.4878836  2.0528547  0.4835311 -0.7149752  0.1605815
##  [421] -1.3318942 -0.7619222  1.3389150 -1.4911029 -1.0635662  0.2410386
##  [427] -0.7394026 -0.5787024  0.7588994 -0.5621596  0.2243590 -0.3530418
##  [433]  0.9982618  0.3651078 -0.2662563  0.2091071  1.0458849  0.8061993
##  [439] -1.1343919 -1.6731618  0.9596076 -2.3474382  1.1655948  1.8605481
##  [445]  0.2371966  1.9318505 -0.7585905  1.0484409 -0.1756034  1.5656422
##  [451]  1.0700829 -0.3152995 -0.5021952  1.2212882 -1.6458220 -0.0756803
##  [457]  0.5527260 -0.2192107 -0.6182502 -1.3995478 -0.1366260 -0.6844818
##  [463]  0.6792151 -0.1824573 -1.0601737  0.2073563 -0.5464228 -0.3911327
##  [469]  0.0599890  0.0864043 -0.4542024 -0.9127650  0.3149915  0.1194921
##  [475] -0.0119400 -1.2604168  0.6499639  0.5269140  1.1469915 -0.2502982
##  [481]  0.1720555  0.2275240  0.1102851 -1.2199585 -0.8247373 -0.4516681
##  [487] -1.0116354 -0.5182339  1.0081597 -0.3823185  0.1312324  0.1601619
##  [493]  1.3132113  0.3709994  0.0994834 -0.3741564  0.9341911 -0.1251261
##  [499] -0.5864120 -0.1011348  1.2710626  0.3561442 -0.4502933 -0.5446722
##  [505]  0.0817528  0.9991236  0.9723431  0.5996503  0.7532817  0.4514813
##  [511]  0.9269643 -2.3839179 -0.0015413  0.9405023  0.8177168 -0.1436319
##  [517]  1.2169901  0.5984728  0.6933118  0.2356280  0.0071713 -0.8833332
##  [523]  1.6640609  0.6331902 -0.9175146 -0.0755754 -0.3016752 -0.2963791
##  [529]  1.2066106  0.1207884 -1.9386344  0.2030906 -0.2453188 -0.7381502
##  [535] -0.5985358 -2.2609837  0.5789543 -0.4465293 -0.1529817  0.2851158
##  [541]  0.3361356 -0.3139253 -1.0726641 -0.9920186 -0.5298825 -0.4467652
##  [547]  1.0429467  1.2719007  0.0641635  0.4334872 -0.3920964  0.5622662
##  [553] -1.1581628 -1.0088331  0.9101525  0.2804658 -1.8797857  1.0430460
##  [559] -0.1085009  0.6840760  1.9289173  1.7821432 -0.9078835  1.8637786
##  [565]  0.7937357  0.2232815 -0.0436762 -1.9408911 -0.8822978 -1.0313850
##  [571]  2.6009822 -1.0688087 -1.2772096 -0.5757484  1.4396158 -0.6482138
##  [577] -1.2603033 -1.1055559  0.2632248  0.1739259  1.9750507 -1.5913846
##  [583] -0.9289474  0.6858719 -2.5010881 -0.2182136 -0.0632617 -1.3124499
##  [589] -1.3844668  0.3769476 -0.1909042 -1.2368659  1.2389751 -0.9196813
##  [595] -1.6357869 -0.8947227 -2.5924789  0.9285055 -0.6408357  0.1137773
##  [601] -1.7858566 -1.4970594  1.1418125  0.7482900  0.4923332 -0.0521817
##  [607] -1.4982573 -0.3961875  0.3749247 -0.9768471 -0.4183443 -0.6469223
##  [613]  0.4048045  1.1039160 -1.8708913  0.8961362  0.4605882  0.1240127
##  [619] -0.3613662  0.7661748  1.3317553 -0.0802866  0.3571114  0.6077125
##  [625]  0.5438402  0.2321132 -0.9564967 -1.2855578 -0.2560647 -1.5479697
##  [631] -0.8186957  1.7856338 -2.0446786 -1.6818063 -0.7249508  0.7634781
##  [637] -0.7777191  1.3372142  0.5445573 -2.8633809 -0.0947172 -1.9362567
##  [643] -1.0742445  0.0859539  1.2691950 -2.4208150 -0.6154097 -0.3776206
##  [649]  2.4977093 -0.7138744 -1.0313338 -0.8506096  1.7158942  0.0514725
##  [655]  0.2825389 -2.3177690  0.4286867 -0.5635598 -0.8214304  0.5944007
##  [661]  0.7520281 -0.8083618 -0.4207512  0.7577409  0.5794520 -1.9013283
##  [667]  2.2157084 -1.9713692 -0.2094732 -0.1578188 -1.4611580 -0.4499962
##  [673]  0.4810249  1.2226222  1.4305586  0.1461979  1.7451837 -1.6168864
##  [679] -0.0821023  0.4250598  0.6808770 -0.0615436 -1.2437122 -0.6646736
##  [685] -0.5256406 -0.3921907  1.1538069  0.9462768 -0.5083542  0.8629368
##  [691]  0.9677885 -0.9966305 -0.7090351  0.4327263  0.7052198  0.9687270
##  [697] -1.1142635 -0.2116047  0.9761222 -0.8871873 -0.9351028 -0.8805307
##  [703]  1.0735520  0.1832443  1.4514285 -1.7979825  0.4984923 -0.2948293
##  [709] -0.7545790  1.2397852  0.7497205 -1.0738702  0.7156939 -0.3687188
##  [715] -1.2972443  1.1758758  0.7077582  1.3228423  0.5050577 -0.8111382
##  [721] -1.1394155 -0.9255640 -0.2976690  0.0932202  1.5529407  0.2158833
##  [727]  0.0630541 -0.3104202  1.3645663  1.6987160  0.5372674 -0.4690046
##  [733] -0.6186480  0.0930111  2.1452773 -3.0474625  0.9936195 -0.2813650
##  [739]  0.6266195  0.4222955 -0.8727745 -0.7708401 -0.2275086  0.2552709
##  [745]  1.5016438  0.9009767 -1.5317976  1.5350996 -1.8685429  0.3407366
##  [751] -1.4741355  0.0972189 -0.2900540 -0.3085321  0.1686151  0.2644461
##  [757]  1.3819852  0.2264180 -0.1274267 -0.0309100  0.6776867  0.8747074
##  [763] -1.3088647 -0.7136597  1.6943141 -0.1601561 -0.4444478 -1.6772519
##  [769] -0.6347682  2.0797751  1.9094730  0.7224333  0.2250256 -0.3648466
##  [775] -0.7850596  1.6737621  0.0553754 -1.2916920 -1.2885634 -1.4859141
##  [781]  0.2095971  0.6555120 -0.2833232  1.1776222  0.3465987 -0.8394890
##  [787] -0.6423873 -1.1708297  0.4751014 -2.0843548 -1.2889121  0.2150840
##  [793]  1.6857093  0.2585215  0.9257383 -1.2918755  0.8577682  0.4591877
##  [799] -1.5904097 -0.0226334  0.2971865  2.1206966 -0.0372117  0.6024643
##  [805]  0.9600513  1.6267097 -0.8341628 -0.4759493  0.0722821 -0.7641559
##  [811] -0.7608000 -0.0507294  0.3722444 -0.0629532  0.0845653  0.6134444
##  [817] -0.5275465  1.7846734  0.3946040 -1.5852374  1.8657393  0.3780863
##  [823] -0.4287512  0.3171629 -1.0713242  0.5000237  0.3798040  0.6804081
##  [829]  0.4312137 -0.6972537  0.9568730  1.1444938  1.1451046  0.5104907
##  [835] -1.3494255 -0.6075723 -0.4011800 -1.1891128  0.8104861 -0.7485158
##  [841] -0.3845334  0.9119230 -1.5185417 -0.3001786 -0.4165641 -0.4705531
##  [847] -1.1204902 -1.6882171  1.3028017 -0.1395134  0.1097571 -1.0477069
##  [853]  0.5403735 -2.0040482 -0.8760552 -0.0512592 -1.0248825  0.5270786
##  [859]  0.2074175 -0.2918015 -0.9602403 -0.2914667  0.6517496 -0.1685919
##  [865]  0.7358465 -0.3916408 -1.2745749 -1.1618241 -1.9048893  0.0048323
##  [871]  0.5378039 -1.3327357 -2.2125845 -0.2430774 -0.6872183  0.4163604
##  [877]  0.9133725  0.4894407  0.7707523  0.0331379  0.7568571 -0.2803711
##  [883] -1.2257037  1.4051833 -1.0006694 -0.0683342 -1.2624433  2.4176588
##  [889]  0.5827521  0.1717654  0.4281814 -0.3366657  0.0342182  1.3135897
##  [895]  0.9689126  0.0403641 -0.2233126  0.4696852  0.6397890 -0.8080816
##  [901] -0.1627909 -0.1592106 -0.3370667 -1.0658286  1.3636601 -0.0056849
##  [907]  0.8147852  1.0329586 -0.6213366 -1.0852029  0.2764135  0.4241839
##  [913]  0.8129962  2.9733043 -0.4763169 -0.3247213  0.2417909  0.8503745
##  [919]  0.1469487  1.6000540  0.0942319  0.0203613  0.9217261  0.7923837
##  [925] -2.8549554 -0.5101153 -2.6928276 -0.4644623 -1.1882081 -0.3526219
##  [931] -2.1588853  0.7940608 -0.2221722 -0.9688465 -1.4149667 -2.2838381
##  [937] -0.9802587 -1.5807696  0.7256216  1.4987596 -1.3368146 -0.5270321
##  [943]  0.7746961 -1.3754252 -1.0470384  0.1498009 -0.8302360 -1.0261066
##  [949] -0.9339966 -0.6136165 -0.5960490  0.1326510  0.7728312  0.7027687
##  [955] -0.0106936  0.1859549  0.7134753 -0.7566696  0.2084880 -0.7736654
##  [961] -0.0430100 -0.9991800 -0.4787656  0.0308086  0.6167382  0.8045252
##  [967] -1.1814552 -1.4003856  2.4060265 -0.7530418 -1.1388702  0.4050619
##  [973]  0.6646614 -1.0152346  0.4205101 -1.5459098 -0.7519205 -0.8506437
##  [979] -0.2349367 -2.3214679 -1.2035366 -1.0084677  0.4935949 -1.0577813
##  [985] -0.6475429  0.8315596  0.7958631 -0.0974068  1.1911219 -1.1734990
##  [991]  0.3312814  0.8046973  0.3026710 -1.8783915 -0.6662570 -0.0349693
##  [997] -2.4678798  0.6427397 -0.0224606  0.0759496
{% endhighlight %}

Each of these values was generated from a normal distribution.

Let's say we want to histogram those values. We can give them to the function `qplot`:


{% highlight r %}
qplot(x)
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6c.png) 

This creates a histogram without having to create a data frame or specify `geom_histogram`.

This shortcut also lets us set options easily. For example, we can change the binwidth of the histogram by giving the binwidth argument to qplot:


{% highlight r %}
qplot(x, binwidth=1)
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6d.png) 

We can also set the x and y axis labels easily. We can do that either by adding the `xlab` and `ylab` options like we did before:


{% highlight r %}
qplot(x, binwidth=1) + xlab("Random Variable")
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6e.png) 

Or we can add the `xlab` argument to the `qplot` function.


{% highlight r %}
qplot(x, binwidth=1, xlab="Random Variable")
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6e2.png) 

Histograms aren't the only thing we can plot with qplot. Let's create a y variable so that we can construct a scatter plot comparing x to y. Let's make y also be a random normal distribution:


{% highlight r %}
y = rnorm(1000)
{% endhighlight %}

If we want to scatterplot x vs why, we can simply give them to `qplot`.


{% highlight r %}
qplot(x, y)
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6g.png) 

Note that we can still add layers to this basic plot just like we could to a regular ggplot call. For example, we could add a smoothing curve with the `geom_smooth` layer:


{% highlight r %}
qplot(x, y) + geom_smooth()
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6g2.png) 

This layer ends up on top of the scatterplot created by `qplot`.

Now, so far we've been working with the built-in diamonds dataset. These plots were really easy because the data were given in the format of one observation per row- that is, one diamond per row- which we call "tall" format. But many datasets come in a "wide"" format: that means there is more than one observation- more than one point on your scatterplot- in each row. For example, let's look at the WorldPhones dataset, which comes built into R. Just like we did for diamonds, we use data to load it:


{% highlight r %}
data("WorldPhones")
{% endhighlight %}

You can see it got added to our global environment. You can then view it using the `View` function.


{% highlight r %}
View(WorldPhones)
{% endhighlight %}

You can also get more information about WorldPhones using the `help` function:


{% highlight r %}
help(WorldPhones)
{% endhighlight %}

This dataset shows the number of telephones, measured in thousands, in each continent in each of several years in the 1950s.

Notice that each column is one continent, and each row is one year. Now, that sounds like a reasonable way to store your data. But imagine if we want to compare increases in phone usage between continents, with time on the x axis. That means each point on our plot is going to be one continent in one year. We don't have one observation per row: we have seven! That makes it very difficult to plot using ggplot2.

Luckily, there is an easy way to turn this into tall format, called "melting" the data. To do this, we'll have to install another third party package, called reshape2. Recall that you can do this with


{% highlight r %}
install.packages("reshape2")
{% endhighlight %}

just like we did with `ggplot2`. Now we load the reshape2 package, with


{% highlight r %}
library(reshape2)
{% endhighlight %}

Now we can melt our dataset: that is, turn it from this wide format- many observations per row- to a tall format- one observation per row. Let's assign the new, melted data to a variable called WorldPhones.m, where m is for melted. We assign this using the `melt` function on the WorldPhones data.


{% highlight r %}
WorldPhones.m = melt(WorldPhones)
{% endhighlight %}

Now let's view our new, melted data.


{% highlight r %}
head(WorldPhones.m)
{% endhighlight %}



{% highlight text %}
##   Var1   Var2 value
## 1 1951 N.Amer 45939
## 2 1956 N.Amer 60423
## 3 1957 N.Amer 64721
## 4 1958 N.Amer 68484
## 5 1959 N.Amer 71799
## 6 1960 N.Amer 76036
{% endhighlight %}

Notice that there are now only three columns: Var1, Var2, and value. So Var1 is year, in Var2 we see each of the continents, and value is the number of phones. What happened was that every cell- every observation- every number of phones per year per continent- in the original data got its own row in this melted data. We can see that in the year 1951, in North America, there were 45 million, 939 thousand phones. You can see the same value in our original unmelted data. So none of the data changed, it just got "reshaped".

To make the data a little more intuitive, you can change the column names. You might recall that we can do this as follows:


{% highlight r %}
colnames(WorldPhones.m) = c("Year", "Continent", "Phones")
{% endhighlight %}

So now if we view `WorldPhones.m`, we can see our new column names.


{% highlight r %}
head(WorldPhones.m)
{% endhighlight %}



{% highlight text %}
##   Year Continent Phones
## 1 1951    N.Amer  45939
## 2 1956    N.Amer  60423
## 3 1957    N.Amer  64721
## 4 1958    N.Amer  68484
## 5 1959    N.Amer  71799
## 6 1960    N.Amer  76036
{% endhighlight %}

Now that we have our data in melted format, it is easy to create a plot with ggplot2. We go through our usual steps of a ggplot call, but this time we give it WorldPhones.m. We do:


{% highlight r %}
ggplot(WorldPhones.m, aes(x=Year, y=Phones, color=Continent)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6p.png) 

on the x-axis we're going to put the Year, so we can see how things change over time. On the y-axis we want to put the number of Phones, which is the variable we're interested in graphing. And let's color each point based on the factor of Continent. Then we'll add the `geom_point` layer to make this into a scatterplot.

Now we've worked with scatterplots before, but since this time what we're showing is a trend over time, it might be better to draw lines between the points in continent. This is easy: we can just change the layer to a `geom_line` layer.


{% highlight r %}
ggplot(WorldPhones.m, aes(x=Year, y=Phones, color=Continent)) + geom_line()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6q.png) 

Now we have a plot of the number of phones in each continent by year. Incidentally, one might expect phone service to increase exponentially rather than linearly. Also, a lot of the values here are scrunched in the bottom of the axis. When that's the case, it's a good idea to put the y axis on a log scale. Recall that we can do that by adding `scale_y_log10()`.


{% highlight r %}
ggplot(WorldPhones.m, aes(x=Year, y=Phones, color=Continent)) + geom_line() + scale_y_log10()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_6r.png) 

Now each of the phone trends looks linear, and we can see the lower values more clearly: for example, that Africa overtook Central America in the number of phones in the year 1956.

Notice how easy this plot was to make once we had the data in the correct format: one row for every point- that's every combination of year and continent- on our graph. So if your data's not in that format when you're starting out, melt it.

<a name="segment7"></a>

Segment 7: Output: Saving Your Plots
-------------

So you just created a great ggplot, and now you want to save it to a file, so you can email it, or add it to your paper or poster, or just look at it later. You can do this with the ggsave function.

First, let's create a scatterplot based on our diamonds data.


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_7a.png) 

Now instead of displaying it, let's run that line again, but save it to a variable, called p.


{% highlight r %}
p = ggplot(diamonds, aes(x=carat, y=price)) + geom_point()
{% endhighlight %}

Note that when that happened, the plot did not get recreated: it WAS built but never displayed. We've saved the entire plot into this `p` object. Now we can save that plot to a file, instead of displaying it in our window, by using ggsave:


{% highlight r %}
ggsave(filename="diamonds.png", p)
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}

What just happened is that we created a file called diamonds.png that saved the image. It doesn't have to be a PNG; it can also be a PDF:


{% highlight r %}
ggsave(filename="diamonds.pdf", p)
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}

or a JPEG:


{% highlight r %}
ggsave(filename="diamonds.jpeg", p)
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}

You can read about the formats ggsave supports, and about the other options you can set like figure height and width, by doing `help` on `ggsave`:
    

{% highlight r %}
help(ggsave)
{% endhighlight %}

One useful shortcut is that if you just displayed a plot, like in a line like this:


{% highlight r %}
ggplot(diamonds, aes(x=carat, y=price)) + geom_point()
{% endhighlight %}

![center](/RData/code/lesson2/figures/segment_7g.png) 

Then ggsave will know to save *that* plot by default when you perform ggsave- you don't even have to tell it which plot you're saving.


{% highlight r %}
ggsave("diamonds.png")
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}

Just make sure you're saving the plot you mean to save.

Within RStudio, there's one other choice for saving a plot: you can click on Export, and then "Save Plot As Image," and then select your width, height, filename, and so on.
