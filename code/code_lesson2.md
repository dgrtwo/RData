---
layout: default
---

Lesson 2: Visualizing Data Using ggplot2
============

<a name="segment1"></a>

Segment 1: Introduction
------------




{% highlight r %}
library("ggplot2")
{% endhighlight %}



{% highlight text %}
## Loading required package: methods
{% endhighlight %}



{% highlight r %}

data("diamonds")

head(diamonds)
{% endhighlight %}



{% highlight text %}
##   carat       cut color clarity depth table price    x    y    z
## 1  0.23     Ideal     E     SI2  61.5    55   326 3.95 3.98 2.43
## 2  0.21   Premium     E     SI1  59.8    61   326 3.89 3.84 2.31
## 3  0.23      Good     E     VS1  56.9    65   327 4.05 4.07 2.31
## 4  0.29   Premium     I     VS2  62.4    58   334 4.20 4.23 2.63
## 5  0.31      Good     J     SI2  63.3    58   335 4.34 4.35 2.75
## 6  0.24 Very Good     J    VVS2  62.8    57   336 3.94 3.96 2.48
{% endhighlight %}


<a name="segment2"></a>

Segment 2: Scatter Plots
------------


{% highlight r %}
ggplot(diamonds, aes(x = carat, y = price)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_21.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_22.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = color)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_23.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = cut)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_24.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity, size = cut)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_25.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity, shape = cut)) + 
    geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_26.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + geom_smooth()
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_27.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + geom_smooth(se = FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_28.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + geom_smooth(se = FALSE, 
    method = "lm")
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_29.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity)) + geom_point() + 
    geom_smooth(se = FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_210.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity)) + geom_smooth(se = FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_211.png) 

<a name="segment3"></a>

Segment 3: Faceting and Additional Options
-------------


{% highlight r %}
ggplot(diamonds, aes(x = carat, y = price, color = cut)) + geom_point() + facet_wrap(~clarity)
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_31.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = cut)) + geom_point() + facet_grid(color ~ 
    clarity)
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_32.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot")
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_33.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot") + 
    xlab("Weight (carats)")
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_34.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot") + 
    xlab("Weight (carats)")
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_35.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot") + 
    xlab("Weight (carats)") + xlim(0, 2)
{% endhighlight %}



{% highlight text %}
## Warning: Removed 1889 rows containing missing values (geom_point).
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_36.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot") + 
    xlab("Weight (carats)") + scale_y_log10()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_37.png) 


<a name="segment4"></a>

Segment 4: Histograms and Density Plots
-------------


{% highlight r %}
ggplot(diamonds, aes(x = price)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_41.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_histogram(binwidth = 2000)
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_42.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_histogram(binwidth = 200)
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_43.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_histogram(binwidth = 200) + facet_wrap(~clarity)
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_44.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_histogram(binwidth = 200) + facet_wrap(~clarity, 
    scale = "free_y")
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_45.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price, fill = clarity)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_46.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price, fill = cut)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_47.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_density()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_48.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price, color = cut)) + geom_density()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_49.png) 

<a name="segment5"></a>

Segment 5: Boxplots and Violin Plots
-----------


{% highlight r %}
ggplot(diamonds, aes(x = color, y = price)) + geom_boxplot()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_51.png) 

{% highlight r %}

ggplot(diamonds, aes(x = color, y = price)) + geom_boxplot() + scale_y_log10()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_52.png) 

{% highlight r %}

ggplot(diamonds, aes(x = color, y = price)) + geom_violin() + scale_y_log10()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_53.png) 

{% highlight r %}

ggplot(diamonds, aes(x = color, y = price)) + geom_violin() + scale_y_log10() + 
    facet_wrap(~clarity)
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_54.png) 

<a name="segment6"></a>

Segment 6: Input: Getting Data into the Right Format
-----------


{% highlight r %}
x = rnorm(1000)
x
{% endhighlight %}



{% highlight text %}
##    [1] -7.673e-01  1.172e+00  6.142e-01  1.032e+00  5.774e-01 -9.300e-02
##    [7] -8.576e-01 -8.127e-01  3.621e-01  2.489e-01  4.275e-01 -9.555e-01
##   [13]  5.077e-01 -7.031e-01  6.151e-01 -7.495e-02 -1.546e+00 -4.522e-01
##   [19]  7.483e-02  7.502e-01  2.900e-01 -9.064e-02 -8.348e-01 -1.154e+00
##   [25]  3.206e-01 -1.290e+00  1.167e-01  8.236e-01  6.217e-01  4.299e-01
##   [31] -2.558e-01  6.166e-01  1.665e+00 -1.391e+00 -1.267e+00  8.655e-01
##   [37] -7.582e-01  6.748e-01 -2.734e-01 -3.875e-01  8.947e-01 -5.603e-01
##   [43] -9.159e-01 -8.237e-01 -1.267e+00  9.513e-01 -1.914e+00 -1.217e-01
##   [49] -9.968e-01  1.667e-01 -1.488e+00  8.083e-01 -1.168e+00 -2.362e-01
##   [55] -4.467e-01 -5.175e-01  8.193e-02 -7.065e-01  1.164e+00 -2.010e+00
##   [61] -1.038e+00 -2.514e+00 -1.242e+00 -1.769e+00 -3.028e-02  1.293e+00
##   [67] -8.951e-01 -5.411e-01  7.597e-01 -3.056e-01 -1.560e+00  2.334e-01
##   [73] -8.224e-01 -2.120e+00  8.038e-01  6.885e-01 -1.072e+00  1.497e+00
##   [79] -3.883e-02 -9.559e-01  3.990e-01  4.200e-01  3.933e-01  8.873e-01
##   [85]  2.475e-01 -5.561e-01  6.325e-01  1.230e+00 -5.141e-01 -1.558e+00
##   [91] -2.383e-01  1.619e-01  6.658e-01 -6.733e-02  8.565e-02 -9.429e-01
##   [97] -3.864e-01  5.243e-01 -1.141e-01  4.207e-01 -6.180e-01 -1.829e+00
##  [103]  1.364e+00 -5.067e-01 -1.666e+00  2.141e-02 -4.236e-01 -2.350e+00
##  [109]  1.839e-01  2.524e-01  1.421e+00  1.052e+00 -2.115e-01 -1.164e+00
##  [115] -2.881e-01 -4.646e-01 -1.406e+00  5.612e-01 -1.489e+00  1.880e+00
##  [121] -4.289e-01  1.765e+00 -6.563e-01 -9.956e-01 -3.484e-01  4.394e-01
##  [127]  2.125e+00  1.202e+00 -1.235e+00  1.180e+00 -3.439e-01  1.093e+00
##  [133] -1.413e+00 -1.333e+00  1.117e+00  1.325e+00  2.263e-06 -6.261e-01
##  [139] -2.994e-01 -1.104e+00  6.884e-01  3.432e-01 -1.497e+00 -1.244e+00
##  [145]  1.454e-01  2.748e-01 -6.255e-01  7.986e-01  1.596e+00  1.337e+00
##  [151]  1.339e+00  1.268e+00 -5.684e-01  1.261e+00 -5.173e-01  1.796e-01
##  [157] -1.404e-02  6.211e-01 -1.012e+00  1.165e+00 -1.559e+00  1.168e+00
##  [163] -9.416e-01 -1.034e+00 -7.969e-01  1.157e+00  9.717e-01 -2.167e+00
##  [169] -1.883e-01  1.267e+00 -5.732e-01 -2.332e-01  1.188e+00  5.758e-01
##  [175] -1.130e-01  8.849e-01 -2.240e+00  3.983e-01  4.506e-01 -2.414e-01
##  [181]  3.219e-01  1.270e-01  2.290e-01  4.791e-01  9.058e-01 -1.719e+00
##  [187] -4.448e-01 -7.465e-01 -7.491e-01  1.410e-01  2.648e-01 -1.480e+00
##  [193] -1.570e+00  4.447e-01 -4.967e-01  1.755e-01 -1.903e+00  3.284e-01
##  [199]  8.140e-01 -3.203e-01 -4.988e-02 -5.159e-01 -2.545e-01 -1.216e+00
##  [205] -2.225e+00  2.677e+00 -7.772e-01 -3.102e+00 -1.439e+00  1.239e+00
##  [211] -1.240e+00  2.333e+00  1.529e+00 -5.247e-01  1.398e+00  3.378e-01
##  [217] -1.878e+00  6.545e-01 -1.022e-01 -1.628e+00 -1.986e-02 -4.255e-01
##  [223]  5.007e-01 -5.100e-01 -4.152e-01 -6.862e-01  6.438e-01  2.492e+00
##  [229] -9.409e-01  8.918e-01 -1.961e+00 -9.564e-01  3.253e-02  8.862e-02
##  [235] -2.077e-01  7.937e-01 -2.315e+00 -1.170e+00  1.032e-02 -3.066e-01
##  [241] -1.740e+00 -1.501e-02  3.361e-01  8.457e-01  8.911e-02 -2.715e-01
##  [247] -1.109e-01 -9.746e-01 -3.138e-01  7.255e-01 -6.146e-01  1.408e+00
##  [253]  6.338e-02 -2.660e-01  1.425e+00  9.482e-01 -5.258e-02 -2.640e+00
##  [259]  1.066e-01  1.667e+00  9.272e-01 -5.272e-01  4.247e-01 -1.159e-01
##  [265]  9.715e-01 -6.385e-01  1.668e-01 -2.264e-01  6.066e-01  7.243e-02
##  [271] -4.219e-01 -8.002e-01 -5.208e-01  1.288e+00 -4.409e-01  1.097e+00
##  [277] -2.377e-01 -1.630e+00 -8.338e-01 -4.089e-01  2.707e-01  4.657e-01
##  [283] -1.534e+00 -5.807e-01  1.465e+00 -2.160e+00  6.022e-01  5.214e-01
##  [289]  1.666e+00  5.781e-01 -8.807e-02 -1.004e+00 -3.032e-01 -8.800e-01
##  [295]  2.928e-01 -1.064e+00 -3.861e-01 -1.753e+00 -4.143e-01 -1.627e+00
##  [301]  1.020e+00 -9.387e-01 -2.659e-01 -2.424e-02  1.339e+00 -3.788e-01
##  [307]  1.566e+00  4.727e-01 -9.232e-01  3.206e-01  2.427e+00  1.163e-01
##  [313]  5.956e-01 -2.221e-01 -3.682e-01  1.942e-01  1.550e+00  5.125e-01
##  [319]  3.483e-01  1.089e+00 -2.721e+00  7.640e-01 -5.130e-01 -2.354e-02
##  [325] -1.076e+00 -6.147e-01  1.953e+00 -1.184e+00 -1.635e+00  2.098e+00
##  [331]  1.464e+00 -1.283e+00  2.763e-01  1.075e-02  7.092e-01 -1.021e+00
##  [337] -5.211e-01  5.553e-01 -4.072e-02  4.293e-01  8.677e-01  2.198e-01
##  [343] -6.545e-01 -9.324e-01 -1.863e+00 -2.525e-01 -1.688e+00  7.246e-01
##  [349]  1.377e+00  1.474e+00  1.175e+00  2.242e-01 -5.443e-01 -1.455e+00
##  [355] -8.637e-01 -4.170e-01 -4.852e-01  1.660e-01  6.801e-03 -4.885e-01
##  [361] -2.230e+00 -2.147e+00 -1.406e+00  4.167e-01  2.382e+00  8.398e-01
##  [367] -4.438e-01  3.101e-01 -4.598e-01 -3.116e-01 -3.828e-01 -9.013e-01
##  [373]  1.665e-01  9.120e-01  9.465e-02  2.977e-01 -4.727e-01 -1.037e+00
##  [379] -1.254e+00 -3.543e-01 -2.027e-01  8.959e-01 -1.763e+00  1.559e+00
##  [385] -1.519e-01 -1.551e+00 -1.022e+00 -6.580e-01  8.763e-01 -1.423e+00
##  [391] -4.702e-01 -2.328e+00  6.541e-01 -1.998e+00 -1.459e+00 -1.197e+00
##  [397] -5.926e-01 -7.711e-01  9.208e-01  1.747e+00 -1.623e+00  2.785e-01
##  [403]  7.215e-01  1.005e+00 -1.789e+00 -1.427e+00 -4.507e-01  8.398e-01
##  [409]  1.096e+00 -3.461e-01  7.564e-01  1.151e+00  3.808e-02 -1.613e+00
##  [415] -9.962e-02 -1.184e+00  2.222e+00  3.892e-02  1.452e+00 -5.027e-01
##  [421] -7.807e-01 -1.044e+00  1.705e-01  1.081e+00  1.755e+00  4.465e-01
##  [427] -9.458e-01  4.453e-01  1.399e+00 -1.293e+00  1.617e-01 -9.206e-02
##  [433] -6.318e-01 -2.553e-01  1.008e+00  8.557e-01 -3.252e-01 -1.518e+00
##  [439]  1.772e-02 -7.187e-01  4.832e-01 -4.947e-01 -4.119e-01  1.141e+00
##  [445] -6.945e-01 -5.661e-01 -9.634e-01  7.229e-01 -2.035e+00  2.525e-02
##  [451] -2.260e+00 -2.353e-01  7.003e-01 -6.678e-01  7.186e-01  3.271e+00
##  [457] -5.796e-01  8.807e-01  1.237e+00 -1.543e+00  6.485e-01  7.233e-01
##  [463]  1.732e-01 -3.504e-01 -9.842e-01  9.748e-01  4.298e-01 -2.446e+00
##  [469] -4.245e-02  9.184e-01  3.176e-01  6.529e-01 -7.064e-01  1.883e-01
##  [475]  1.059e-01  1.788e+00  3.827e-01  1.097e+00 -1.133e-01  3.021e-02
##  [481] -4.478e-01 -1.799e+00 -6.319e-01  9.260e-01  1.702e-01 -1.582e+00
##  [487] -1.184e+00  5.992e-01  9.673e-01  6.909e-01  1.985e+00 -7.903e-01
##  [493] -1.497e+00 -1.773e-01  9.859e-01  1.833e-01  9.229e-01  3.668e-01
##  [499] -1.413e-01 -5.039e-01 -1.177e-01  5.783e-01 -1.233e+00 -8.451e-01
##  [505]  9.594e-01 -4.477e-02  8.260e-02 -1.867e-01  9.935e-02 -2.483e+00
##  [511] -2.313e-02 -2.151e+00 -1.098e+00 -8.475e-01  1.856e+00  1.032e+00
##  [517] -5.513e-01  2.436e-01 -1.078e+00 -4.938e-01  2.863e-01 -1.087e+00
##  [523]  1.192e+00 -4.270e-01 -1.240e+00  5.629e-01  1.592e+00 -6.161e-01
##  [529]  1.490e+00  4.378e-01 -6.947e-01  9.164e-01 -2.043e+00  8.355e-01
##  [535]  3.341e-01 -4.756e-01 -1.482e+00  6.328e-01 -7.751e-01  7.643e-02
##  [541] -3.999e-01  1.648e-01 -9.254e-03 -3.109e-01  4.336e-01  3.184e-01
##  [547] -1.103e+00 -1.173e+00 -1.216e+00  1.272e+00 -8.024e-01 -5.209e-01
##  [553] -1.810e-01 -8.348e-01 -9.825e-01  1.477e+00 -6.509e-01  1.854e+00
##  [559]  3.707e-02  4.890e-01 -8.972e-01  1.929e+00 -1.711e-01 -2.505e-01
##  [565]  1.714e+00  2.541e-01  1.329e+00 -1.192e+00  1.458e-01  4.255e-01
##  [571]  1.059e-01 -1.422e+00 -1.188e+00 -5.482e-01  4.496e-01 -3.159e-02
##  [577]  1.757e+00  9.948e-01  1.715e+00  7.775e-01 -1.821e+00 -1.048e+00
##  [583]  1.042e+00 -7.846e-01  1.192e-01 -5.568e-02 -6.784e-02  4.106e-01
##  [589] -6.265e-01 -5.705e-01  1.121e+00 -1.407e+00 -2.252e-01 -8.427e-01
##  [595]  1.712e+00 -8.418e-01 -1.661e-01 -8.693e-01 -1.019e+00  7.276e-01
##  [601] -1.230e+00  2.958e-01 -6.504e-01 -7.573e-01  2.811e-01 -5.573e-01
##  [607]  5.096e-01  2.440e+00  1.891e-01 -1.339e-01  1.787e-02  1.018e-01
##  [613] -3.046e-01 -2.599e-01  4.053e-01 -1.467e+00 -1.005e+00  1.603e+00
##  [619]  1.038e+00  7.983e-02 -9.050e-01 -1.464e+00 -1.819e+00 -1.499e+00
##  [625]  1.079e+00  2.307e-01 -2.735e-01 -1.666e+00  7.726e-01 -1.078e+00
##  [631] -1.086e+00  1.022e+00  1.066e+00 -1.724e+00  1.375e+00 -8.794e-01
##  [637]  3.992e-01  1.611e+00  5.093e-01 -8.512e-01  8.347e-01 -1.074e+00
##  [643]  4.563e-01 -6.913e-01  1.988e-01 -5.702e-02  1.502e-02 -1.695e+00
##  [649]  1.909e-01 -1.745e+00  4.910e-01  1.012e+00 -1.361e-01 -2.914e-02
##  [655] -1.135e+00 -5.436e-01  1.514e+00 -9.221e-01  2.664e-01 -1.085e+00
##  [661] -9.465e-01  6.115e-01 -1.181e+00 -6.549e-02  7.848e-01  1.402e+00
##  [667]  6.537e-01  1.234e+00 -6.172e-02 -7.002e-01  5.071e-01  1.666e-01
##  [673] -5.302e-01 -7.260e-01  1.360e+00  1.793e-01  1.079e+00 -4.353e-01
##  [679] -1.023e+00 -1.392e+00 -6.131e-01 -2.558e-02  6.745e-01  4.465e-02
##  [685]  3.797e-01 -1.340e+00 -2.823e-01 -6.814e-02  2.272e+00  9.155e-01
##  [691]  6.490e-01  5.481e-04 -6.911e-01 -1.336e-01  1.047e-01  1.849e-01
##  [697] -1.192e-01 -2.044e+00 -1.183e+00  7.309e-01 -1.874e+00  5.916e-01
##  [703]  6.787e-01 -3.340e-01  4.173e-01 -2.634e-01 -2.043e-01  1.385e+00
##  [709] -1.522e+00 -3.819e-01 -6.205e-01  3.831e-01  6.032e-01  1.142e+00
##  [715]  1.122e+00  1.466e+00 -2.989e-01  8.526e-01 -2.711e-01  1.011e+00
##  [721] -2.231e-01 -8.944e-01 -6.953e-01 -1.227e+00  1.170e+00 -1.875e+00
##  [727] -1.007e-01 -1.269e-02  1.083e+00 -5.407e-01  4.267e-01 -1.440e+00
##  [733]  1.315e+00  1.302e+00 -4.643e-01  5.568e-01 -2.050e+00 -1.079e+00
##  [739]  7.234e-01  8.621e-02 -2.709e+00  1.908e-02  1.639e-01  1.660e+00
##  [745] -1.238e-01  1.546e+00  7.775e-01  1.051e+00 -8.437e-01  4.797e-01
##  [751]  5.384e-01  2.953e-01 -1.869e+00 -3.716e-01  1.360e+00  3.966e-01
##  [757]  6.466e-01  1.070e+00 -2.124e-01  8.894e-01 -1.887e-01 -1.588e+00
##  [763] -1.573e-01  7.903e-01  1.118e+00 -8.546e-01  3.108e-02 -1.612e-01
##  [769]  2.483e-01  9.258e-01  2.515e-02 -1.799e+00 -8.677e-01  8.552e-01
##  [775] -1.576e-02 -8.346e-01 -4.221e-01  9.160e-02 -2.863e-01  3.797e-01
##  [781] -8.337e-01 -3.224e-01  5.686e-02 -4.273e-01 -7.892e-01 -1.784e-02
##  [787]  1.593e-01  2.413e-01 -8.465e-01  7.947e-01  8.069e-02  1.376e+00
##  [793] -5.552e-01 -1.086e+00 -5.170e-02  1.100e+00 -6.607e-01  7.249e-01
##  [799] -2.896e-01  4.652e-01 -5.807e-01  5.142e-01  3.435e-01 -4.471e-01
##  [805]  3.113e-01  1.343e+00  7.303e-01  9.086e-01 -1.303e+00  1.982e-01
##  [811] -2.675e+00  2.134e-01  1.648e+00 -2.209e-01 -7.743e-01 -2.183e-01
##  [817]  1.580e-01 -1.204e+00 -5.523e-01 -1.672e+00  1.338e+00 -2.384e-01
##  [823]  2.723e-01 -1.312e+00 -1.123e+00 -1.614e-01  3.176e-01  3.190e-01
##  [829]  9.872e-02 -4.935e-01 -2.862e-01  1.152e-01  8.781e-01 -1.057e+00
##  [835] -2.795e-01 -6.424e-01  1.454e+00  3.777e-01  1.109e+00  1.519e+00
##  [841]  3.726e-01 -8.490e-01  2.921e-01  1.017e+00 -3.499e-01  8.635e-01
##  [847]  6.384e-01 -9.609e-02 -6.097e-01 -2.177e-01  9.311e-01 -2.656e-01
##  [853] -2.791e-01 -6.738e-01  9.661e-01  1.413e+00  6.177e-01 -2.962e-01
##  [859] -5.873e-01 -1.051e+00  4.457e-02 -3.343e-01 -2.038e+00 -1.614e+00
##  [865]  5.899e-01 -8.830e-01  1.372e+00 -4.645e-01  3.279e-01 -1.079e+00
##  [871]  7.753e-01 -1.283e+00  3.995e-01 -1.718e+00 -4.648e-01 -3.323e-01
##  [877] -5.607e-01  2.082e+00  7.123e-01 -1.208e-01  6.656e-01 -8.723e-01
##  [883] -4.966e-01 -9.763e-01 -1.192e+00 -5.070e-01 -7.090e-01 -1.052e+00
##  [889]  6.029e-01 -1.676e+00 -4.006e-01  3.018e-01  2.183e+00 -4.145e-01
##  [895]  3.860e-01  7.558e-01 -6.920e-01 -1.016e-01  9.134e-01 -1.199e+00
##  [901]  5.717e-01  1.576e+00 -7.446e-01  1.445e+00  1.273e+00  1.314e+00
##  [907]  1.479e-01  1.001e-01 -4.836e-01 -3.114e-01  1.258e+00 -9.903e-01
##  [913]  2.391e+00 -3.236e-01  6.364e-01  9.207e-01  9.238e-03  1.570e+00
##  [919] -7.545e-01 -9.736e-03  5.795e-02 -1.605e+00 -2.810e+00 -1.675e+00
##  [925]  4.113e-01 -1.450e+00 -4.188e-01 -1.096e+00  9.323e-01  5.764e-01
##  [931]  1.105e+00 -3.004e-01 -9.953e-01  4.491e-01  6.731e-01 -9.843e-02
##  [937] -8.163e-01  1.318e+00 -7.760e-02 -7.520e-01 -2.604e-01  5.614e-01
##  [943] -5.695e-01 -9.986e-01  2.421e-01  1.094e+00 -7.750e-01  1.299e+00
##  [949] -2.240e+00 -5.785e-01 -1.124e+00 -7.298e-01 -1.771e+00  1.215e+00
##  [955] -1.215e+00  9.748e-01  1.384e+00  5.810e-01  1.836e-01  1.718e-01
##  [961] -1.278e-01  7.155e-01 -8.693e-01  1.372e+00  2.484e-01  1.270e+00
##  [967] -2.235e-01 -1.570e+00 -8.332e-01 -8.832e-01  1.357e+00 -2.329e-03
##  [973]  5.368e-01 -1.464e+00 -1.296e+00  2.326e+00 -1.916e+00 -2.020e+00
##  [979] -9.286e-01  1.900e-01 -2.442e-02  3.452e-03 -2.881e-01  8.914e-01
##  [985]  1.332e+00  5.278e-01 -8.015e-01 -9.896e-01 -2.526e-01 -6.514e-01
##  [991] -5.722e-02 -1.035e+00  5.660e-01 -2.229e+00  3.495e-02  2.062e+00
##  [997]  2.701e-01 -1.109e+00 -6.510e-01  1.809e-01
{% endhighlight %}



{% highlight r %}

qplot(x)
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_61.png) 

{% highlight r %}

qplot(x, binwidth = 1)
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_62.png) 

{% highlight r %}

qplot(x, binwidth = 1) + xlab("Random Variable")
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_63.png) 

{% highlight r %}

qplot(x, binwidth = 1, xlab = "Random Variable")
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_64.png) 

{% highlight r %}

y = rnorm(1000)

qplot(x, y)
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_65.png) 

{% highlight r %}

qplot(x, y) + geom_smooth()
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_66.png) 

{% highlight r %}

data("WorldPhones")
head(WorldPhones)
{% endhighlight %}



{% highlight text %}
##      N.Amer Europe Asia S.Amer Oceania Africa Mid.Amer
## 1951  45939  21574 2876   1815    1646     89      555
## 1956  60423  29990 4708   2568    2366   1411      733
## 1957  64721  32510 5230   2695    2526   1546      773
## 1958  68484  35218 6662   2845    2691   1663      836
## 1959  71799  37598 6856   3000    2868   1769      911
## 1960  76036  40341 8220   3145    3054   1905     1008
{% endhighlight %}



{% highlight r %}
# help(WorldPhones)

library(reshape2)

WorldPhones.m = melt(WorldPhones)

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



{% highlight r %}

colnames(WorldPhones.m) = c("Year", "Continent", "Phones")

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



{% highlight r %}

ggplot(WorldPhones.m, aes(x = Year, y = Phones, color = Continent)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_67.png) 

{% highlight r %}

ggplot(WorldPhones.m, aes(x = Year, y = Phones, color = Continent)) + geom_line()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_68.png) 

{% highlight r %}

ggplot(WorldPhones.m, aes(x = Year, y = Phones, color = Continent)) + geom_line() + 
    scale_y_log10()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_69.png) 

<a name="segment7"></a>

Segment 7: Output: Saving Your Plots
-------------


{% highlight r %}
ggplot(diamonds, aes(x = carat, y = price)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_71.png) 

{% highlight r %}

p = ggplot(diamonds, aes(x = carat, y = price)) + geom_point()

ggsave(filename = "diamonds.png", p)
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}



{% highlight r %}

ggsave(filename = "diamonds.pdf", p)
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}



{% highlight r %}

ggsave(filename = "diamonds.jpeg", p)
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}



{% highlight r %}

# help(ggsave)

ggplot(diamonds, aes(x = carat, y = price)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson2/segment_72.png) 

{% highlight r %}

ggsave("diamonds.png")
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}

