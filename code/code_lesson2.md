---
layout: default
---

Lesson 2: Visualization Using ggplot2
============

Segment 1: Introduction
------------




{% highlight r %}
library("ggplot2")

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


Segment 2: Introduction to ggplot2
------------


{% highlight r %}
ggplot(diamonds, aes(x = carat, y = price)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_21.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_22.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = color)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_23.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = cut)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_24.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity, size = cut)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_25.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity, shape = cut)) + 
    geom_point()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_26.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + geom_smooth()
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_27.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + geom_smooth(se = FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_28.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + geom_smooth(se = FALSE, 
    method = "lm")
{% endhighlight %}

![center](/../figs/code_lesson2/segment_29.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity)) + geom_point() + 
    geom_smooth(se = FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_210.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = clarity)) + geom_smooth(se = FALSE)
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_211.png) 


Segment 3: Facetting and Additional Options
-------------


{% highlight r %}
ggplot(diamonds, aes(x = carat, y = price, color = cut)) + geom_point() + facet_wrap(~clarity)
{% endhighlight %}

![center](/../figs/code_lesson2/segment_31.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price, color = cut)) + geom_point() + facet_grid(color ~ 
    clarity)
{% endhighlight %}

![center](/../figs/code_lesson2/segment_32.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot")
{% endhighlight %}

![center](/../figs/code_lesson2/segment_33.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot") + 
    xlab("Weight (carats)")
{% endhighlight %}

![center](/../figs/code_lesson2/segment_34.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot") + 
    xlab("Weight (carats)")
{% endhighlight %}

![center](/../figs/code_lesson2/segment_35.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot") + 
    xlab("Weight (carats)") + xlim(0, 2)
{% endhighlight %}



{% highlight text %}
## Warning: Removed 1889 rows containing missing values (geom_point).
{% endhighlight %}

![center](/../figs/code_lesson2/segment_36.png) 

{% highlight r %}

ggplot(diamonds, aes(x = carat, y = price)) + geom_point() + ggtitle("My scatter plot") + 
    xlab("Weight (carats)") + scale_y_log10()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_37.png) 


Segment 4: Histograms and Density Plots
-------------


{% highlight r %}
ggplot(diamonds, aes(x = price)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_41.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_histogram(binwidth = 2000)
{% endhighlight %}

![center](/../figs/code_lesson2/segment_42.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_histogram(binwidth = 200)
{% endhighlight %}

![center](/../figs/code_lesson2/segment_43.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_histogram(binwidth = 200) + facet_wrap(~clarity)
{% endhighlight %}

![center](/../figs/code_lesson2/segment_44.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_histogram(binwidth = 200) + facet_wrap(~clarity, 
    scale = "free_y")
{% endhighlight %}

![center](/../figs/code_lesson2/segment_45.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price, fill = clarity)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_46.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price, fill = cut)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_47.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price)) + geom_density()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_48.png) 

{% highlight r %}

ggplot(diamonds, aes(x = price, color = cut)) + geom_density()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_49.png) 


Segment 5: Boxplots and Violin Plots
-----------


{% highlight r %}
ggplot(diamonds, aes(x = color, y = price)) + geom_boxplot()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_51.png) 

{% highlight r %}

ggplot(diamonds, aes(x = color, y = price)) + geom_boxplot() + scale_y_log10()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_52.png) 

{% highlight r %}

ggplot(diamonds, aes(x = color, y = price)) + geom_violin() + scale_y_log10()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_53.png) 

{% highlight r %}

ggplot(diamonds, aes(x = color, y = price)) + geom_violin() + scale_y_log10() + 
    facet_wrap(~clarity)
{% endhighlight %}

![center](/../figs/code_lesson2/segment_54.png) 


Segment 6: Input: Getting Data into the Right Format
-----------


{% highlight r %}
x = rnorm(1000)
x
{% endhighlight %}



{% highlight text %}
##    [1]  0.277447  0.666760  0.294562  2.749031  0.401433 -0.447626
##    [7] -0.595484  0.686948  0.387455 -1.662636 -1.325506  0.602650
##   [13] -0.072771 -0.243952 -1.213285  0.124940 -0.316175 -0.141491
##   [19]  0.829292  0.978558 -0.364291 -1.307131  1.165355 -1.711577
##   [25]  0.354778 -0.238379  1.575359 -0.045905  0.121310 -0.670606
##   [31] -0.276909  1.048080  3.012673  2.210501  0.185988 -0.775151
##   [37] -1.120998 -1.042094  0.121825 -1.306542 -0.086619 -1.441362
##   [43]  0.646865 -0.928767  1.056695 -0.308386  0.304982 -0.250303
##   [49]  1.434924 -0.402436  2.275436 -0.035960  0.838477  1.157681
##   [55] -0.049846  0.368189 -0.323932  1.109981  0.728653 -0.607762
##   [61]  0.239530 -0.222562 -1.751765 -0.699894  1.665830 -0.022035
##   [67]  0.673544 -0.228970 -0.952631  1.351651  1.711812  0.505505
##   [73]  0.126097 -0.950167  0.154977  0.522855 -0.649024  0.406823
##   [79] -0.224163 -0.061809 -0.890746 -0.772311  0.402146  1.652282
##   [85]  0.170086  0.438960  0.127151 -0.368189  0.207980  0.399277
##   [91]  0.309639 -0.010773 -0.906713  0.842619  1.461469  0.979648
##   [97] -0.923949 -0.555880  0.797913  0.657687 -0.190398  0.118125
##  [103]  0.361083 -2.602072  0.240206  0.908099 -0.340104 -0.699998
##  [109]  0.337580  1.645560  1.822067 -0.794045 -1.016944 -1.685878
##  [115] -1.009466 -0.421229 -0.057410 -0.684956  0.252429  0.350710
##  [121]  0.662310  0.137164  0.137750 -0.088502 -0.769679 -0.775876
##  [127]  2.486597 -1.188069  1.232669 -2.648981 -0.994439  0.438149
##  [133]  0.566265  0.404998  0.948291 -2.061414  1.499298 -1.129167
##  [139]  0.463067 -0.740884 -0.231420 -1.275512 -0.237617 -1.372488
##  [145] -0.498202  2.038186  0.799342 -0.125820 -2.284853  0.149271
##  [151] -0.229675 -2.257238 -0.272417 -0.493513  0.249081 -0.455022
##  [157] -0.306961 -0.313637 -0.775246 -1.188801  0.690686  0.585693
##  [163]  0.630881 -1.399962  1.761903 -1.353123 -1.156897 -0.571149
##  [169] -1.541311  0.194459  1.009768 -1.237064 -0.566960 -1.419553
##  [175] -0.934136 -0.885159  0.500198 -0.683426  0.245077  0.382970
##  [181] -0.422626 -1.198297  0.649427 -1.292695 -0.562615 -0.518142
##  [187]  0.895339  1.109807  0.026682 -0.610459 -0.458021 -0.741095
##  [193] -1.202258 -1.312886 -2.760791  0.543749 -0.383061 -1.287870
##  [199]  0.910220 -0.209620  0.652363 -0.414397  1.207305 -0.326787
##  [205] -0.280638  0.912106  0.283036 -1.444621  1.549898 -1.020500
##  [211]  1.740290 -1.394574 -0.594613 -0.751037  1.187950  0.868422
##  [217]  0.315418  0.177822  0.550466 -0.768220  0.010748  0.305084
##  [223] -1.434145 -0.652742  1.521991 -0.868327 -1.329254 -0.597288
##  [229] -0.131990 -1.492505  0.275424  0.686865 -0.809936 -0.743087
##  [235] -0.371303 -0.309932 -0.182512 -1.355547  0.998268 -0.434299
##  [241]  0.096485 -0.080930  0.088277 -0.884840 -2.624554 -1.241547
##  [247]  0.352579  0.416216 -0.371538 -0.235654  0.699293 -1.126453
##  [253] -1.328075  0.391719 -0.326964 -1.138589 -0.400833  0.404710
##  [259] -0.750509 -1.182891 -0.200944 -2.392596  0.317171 -0.815048
##  [265] -0.037508 -0.380707 -0.795083  0.165134 -1.052990  0.570292
##  [271] -2.407222 -0.070248  0.311354 -0.343813 -0.195888  1.860314
##  [277] -0.153560 -1.930901 -1.547059 -1.570431  0.155805  0.358733
##  [283]  0.331482 -1.693965 -1.338570 -0.539631 -1.449933  0.037213
##  [289] -0.124609  0.543822  0.028280  0.291281  2.000358 -0.076106
##  [295]  1.567277  0.067910 -0.002207 -0.665755  1.437198  1.748886
##  [301] -0.358002 -0.348160  0.298714  1.514530  0.387062  0.990344
##  [307]  2.766104  1.344012  1.646934 -0.614337  1.571559  0.019859
##  [313]  0.720116  0.947531  0.715094 -0.614125 -0.809449 -0.593496
##  [319]  0.065279  0.528248  1.196829  1.105916  0.862438 -0.152358
##  [325] -0.067989 -1.011601  0.179231  0.836225 -0.473756 -0.862847
##  [331] -0.173357  0.709428  0.850884 -0.882571 -0.743089 -1.481409
##  [337] -0.473371 -0.476726  0.521254  0.199413  0.282298  1.750350
##  [343] -0.760654  1.106249 -0.767620 -1.631504 -0.801076 -0.903398
##  [349] -0.327284  0.980103 -0.345554 -0.525820 -0.147133 -0.249329
##  [355] -2.072783 -1.923145  2.099577  0.066564  0.089320  0.940845
##  [361] -0.161426  0.859653  1.030338 -2.045405  0.483018  0.661759
##  [367]  1.054172 -0.160631 -1.262920  1.879693 -1.136118 -0.102033
##  [373] -1.202458  0.211415  1.675677 -0.470417  0.867528 -0.147959
##  [379]  1.498920  2.269080 -1.271795  0.449431  1.198413  0.409825
##  [385] -1.443894 -0.778285  0.468183  0.477423 -0.553442 -0.753790
##  [391]  0.397516  0.319714 -1.621636 -0.353696 -0.115858 -0.581399
##  [397] -2.092570  0.771714 -0.171405 -0.019611 -1.075868  0.940154
##  [403]  0.174736 -2.163234  1.331799 -0.759110 -1.304543 -1.135252
##  [409]  1.355600  1.003021 -0.796202  0.392700 -0.189545  0.084745
##  [415] -1.112941 -0.880895  0.394195  0.497691  0.765927  0.192071
##  [421] -0.106187  0.949004 -0.439767  0.311838  0.128369 -1.251875
##  [427]  1.106995 -1.714093 -1.312980  1.985591  0.339125 -0.104583
##  [433]  0.949193  1.394430  0.793113  0.297990  0.296735 -1.959393
##  [439]  0.062946  0.454953  0.524767 -0.474812 -0.765595  1.547331
##  [445]  0.509127 -0.083452  1.642849 -1.251228 -1.711204  0.110273
##  [451]  0.263749  1.802552 -0.677349 -0.364153 -0.535768  0.163188
##  [457] -0.219969  0.193551 -1.229178  0.191068 -0.557785 -3.082045
##  [463]  1.936542 -0.525808  0.398537 -0.957593 -0.059458 -0.374970
##  [469]  1.366898  0.295904 -0.900723 -0.257240  0.070929 -0.941787
##  [475]  1.038247 -0.613946  1.166910  2.157431 -0.356440 -0.090100
##  [481]  0.804615  0.594891  1.984466 -2.200138  0.002954  0.754152
##  [487]  0.013972 -0.053754  0.157520 -0.984188  0.759009 -2.023992
##  [493] -1.596149 -0.302365  0.215769  0.359010 -0.005409 -1.114051
##  [499]  0.367175  0.175328 -2.099746  0.406136  2.634071  0.575749
##  [505]  1.805993  1.639239  0.337449  1.235391  0.531949 -1.839600
##  [511]  0.217076  0.446563 -0.373204  0.026287  0.188948 -0.028833
##  [517] -0.265155  1.045970  0.456876  0.495240 -1.342889  0.054080
##  [523] -0.955193 -2.139416  0.746828  1.024390  0.633598 -0.251697
##  [529]  0.522608  0.157474  1.403782 -0.681953  1.261763  1.917339
##  [535] -2.251241  1.143121 -1.073260  0.091574  0.610790 -0.692420
##  [541] -1.335326  1.614769 -0.818448  1.584093  0.497172  0.326318
##  [547] -0.430444 -0.294343  1.698191 -1.085647  0.469047 -0.151979
##  [553] -0.038396 -1.005778 -0.874675 -0.658967 -0.656512 -0.525082
##  [559]  0.586567  2.276833 -1.536405 -1.000646 -1.198523 -0.162473
##  [565] -0.944220 -1.036707  1.200083  1.221752 -0.018483  0.593974
##  [571] -0.609445  0.417514  0.160877 -0.959505  1.233177 -0.623027
##  [577]  1.747225 -0.294375  1.031457 -1.490823  0.161401  0.583673
##  [583]  0.317697  1.188870 -1.257531  0.016232  1.858576 -1.369602
##  [589] -0.906306 -1.407759 -0.780460 -0.555821 -0.450541 -0.473131
##  [595]  0.259277 -0.099424 -1.254685 -0.338448  0.811797 -1.079643
##  [601]  1.162458  0.446067  1.146208 -0.101273  0.803047  0.667132
##  [607] -0.076045 -0.255955 -0.319351  0.852673  2.042663  1.053762
##  [613]  0.537015  0.596315 -0.212316  0.753944  1.934453  1.152591
##  [619]  0.838213 -0.525081  0.872319  0.673449 -0.724607 -1.817928
##  [625]  2.000104  0.230267  0.276990  0.018493 -0.499272  1.017250
##  [631]  0.452702 -0.746864  0.212515 -1.176918 -0.024475 -0.606071
##  [637] -1.509001 -0.543942 -0.070582  0.657558  0.615597 -1.349613
##  [643]  0.654127 -1.435441 -0.436494 -1.304577 -0.168099  0.657843
##  [649]  0.895387  0.314762 -0.943943  0.452845 -0.233463 -1.217333
##  [655] -0.581402  1.114310  1.062862  0.774293 -0.533669  0.524901
##  [661] -1.139315  0.677226  0.926740  1.249991  0.939974  1.097791
##  [667] -0.755240 -0.440020  0.708002 -0.920511  1.981083 -0.946812
##  [673]  0.463202 -0.265444  0.047277 -0.787201 -0.246046 -2.230021
##  [679]  0.197147 -0.645709 -0.137491 -0.464414 -0.955841  0.840917
##  [685]  1.807061 -0.838241  2.238869 -0.543228  0.629199  0.216481
##  [691] -0.964906  0.559986 -3.051244  0.687532  1.562077  1.507432
##  [697]  0.530839  0.344624 -0.983244  0.045015  0.827472  0.593926
##  [703] -1.100693  1.381756  0.425727 -0.299966  0.297209  1.390877
##  [709] -0.291837  0.220044 -0.028244 -0.419032 -1.411360 -1.044913
##  [715] -0.407282  0.440342 -0.141056  0.963740 -0.622599 -1.479937
##  [721]  0.218299 -0.844540  0.426479 -1.302205  0.387626  0.838199
##  [727]  1.833808 -1.031616  0.799784 -0.968048 -0.881463  1.263917
##  [733]  0.241423 -0.560430  0.477930 -0.609183  1.211117  1.259969
##  [739] -0.900973 -0.204864  0.047258  1.533390 -0.133258  1.172616
##  [745]  0.711185  2.161618  1.630228  1.528720  0.808281 -1.481746
##  [751]  0.556465  1.048583 -1.300015  1.222882  0.567799  0.889960
##  [757] -0.750047 -1.702683 -0.802229  0.666449 -0.571184  0.177319
##  [763]  1.190517 -0.845606 -1.611476 -0.462911 -1.052166 -0.970516
##  [769] -0.558375  0.565388 -0.602593 -0.657607 -1.409394  0.931933
##  [775]  1.080766 -0.402524  1.142764  2.105053  0.671092 -0.086074
##  [781]  0.147113 -0.533418 -1.472669 -0.169224 -0.181583 -2.572211
##  [787]  0.493464 -0.870288 -2.868819  0.366074  0.927891 -1.511368
##  [793]  0.124986  0.077309 -0.478284  0.713850 -0.397806 -0.494104
##  [799] -1.199957  0.560911  1.929011 -1.149754 -0.153777 -1.502105
##  [805]  0.250195  0.269739 -0.113632  1.567524 -0.614713  1.425485
##  [811]  0.176886  1.045199  1.055560 -0.719893 -0.303200  0.371980
##  [817] -0.526568  0.858958  0.532542  0.541841  0.902412  0.662987
##  [823] -1.648070  1.148585 -1.295935  0.915556  1.529968  0.683609
##  [829]  1.055459 -0.555922  1.257527 -0.311494 -0.392001  1.311824
##  [835] -1.346365  0.676806 -0.204242  0.261404  1.191377 -1.071405
##  [841] -0.286080  0.283330 -1.544531  1.021410 -0.162104  0.578587
##  [847] -1.289660  2.196639 -1.974888  0.175081  0.330590  2.293960
##  [853] -0.227448 -0.771434 -1.589249 -0.218761 -1.022978 -0.675114
##  [859]  0.807560 -0.170375 -1.543451  1.080520  0.316092 -0.849479
##  [865]  0.247698  0.026405  0.160422 -0.746107  2.001501 -1.077593
##  [871] -0.831637 -0.387783  0.620876 -0.122067  0.168562 -0.928809
##  [877]  0.605845  1.916840 -0.342923  0.167549  0.238759  0.441677
##  [883]  0.173217 -0.622736 -2.196021 -0.729880  0.742199  2.389252
##  [889] -1.459515 -0.436211 -0.499795 -0.139051 -0.318910 -0.067859
##  [895] -1.895900 -0.093454 -0.260653  1.087773 -0.008291  0.865171
##  [901]  1.998232  0.177110  0.307643 -1.146393 -0.946267 -0.553259
##  [907] -1.014337  1.237914 -0.894305 -0.267923 -1.718001 -0.519519
##  [913]  0.868850 -0.702347  0.798146  1.681227  0.205073  1.478547
##  [919]  0.010796  0.282835  0.570679 -2.574812 -0.240416 -1.117251
##  [925]  0.785988 -0.785394 -0.039358 -0.748901 -2.909437 -0.026006
##  [931] -0.751201  2.272502 -0.084811 -1.657362 -1.070174 -0.817293
##  [937] -1.119133  0.783901 -1.270835  0.287633 -0.826895 -0.389490
##  [943]  0.595933 -0.842967 -0.165619  0.619558 -0.238894 -1.494006
##  [949]  0.143228 -1.726893  0.541883  3.145785  1.243248  1.232734
##  [955] -0.629343  0.207375  0.202188  0.555789  0.579815 -1.727485
##  [961] -0.826616  1.494396 -0.378652 -0.641371  1.010794 -0.461152
##  [967]  0.433852 -1.143147 -0.213694  0.121737  0.556117 -0.946688
##  [973] -1.126067  0.964424  0.368196  0.450408 -1.081623  0.048359
##  [979]  1.214440 -0.600719  0.140972 -0.909652  1.766286  1.180145
##  [985]  0.736189  0.378255  0.622790  0.973394 -1.188109 -0.033816
##  [991] -0.515934  3.205213 -1.966088 -0.295262  0.608641 -0.268121
##  [997]  0.671013  2.459280 -1.533294 -0.933020
{% endhighlight %}



{% highlight r %}

qplot(x)
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_61.png) 

{% highlight r %}

qplot(x, binwidth = 1)
{% endhighlight %}

![center](/../figs/code_lesson2/segment_62.png) 

{% highlight r %}

qplot(x, binwidth = 1) + xlab("Random Variable")
{% endhighlight %}

![center](/../figs/code_lesson2/segment_63.png) 

{% highlight r %}

qplot(x, binwidth = 1, xlab = "Random Variable")
{% endhighlight %}

![center](/../figs/code_lesson2/segment_64.png) 

{% highlight r %}

y = rnorm(1000)

qplot(x, y)
{% endhighlight %}

![center](/../figs/code_lesson2/segment_65.png) 

{% highlight r %}

qplot(x, y) + geom_smooth()
{% endhighlight %}



{% highlight text %}
## geom_smooth: method="auto" and size of largest group is >=1000, so using gam with formula: y ~ s(x, bs = "cs"). Use 'method = x' to change the smoothing method.
{% endhighlight %}

![center](/../figs/code_lesson2/segment_66.png) 

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

![center](/../figs/code_lesson2/segment_67.png) 

{% highlight r %}

ggplot(WorldPhones.m, aes(x = Year, y = Phones, color = Continent)) + geom_line()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_68.png) 

{% highlight r %}

ggplot(WorldPhones.m, aes(x = Year, y = Phones, color = Continent)) + geom_line() + 
    scale_y_log10()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_69.png) 


Segment 7: Output: Saving Your Plots


{% highlight r %}
ggplot(diamonds, aes(x = carat, y = price)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson2/segment_71.png) 

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

![center](/../figs/code_lesson2/segment_72.png) 

{% highlight r %}

ggsave("diamonds.png")
{% endhighlight %}



{% highlight text %}
## Saving 7 x 7 in image
{% endhighlight %}

