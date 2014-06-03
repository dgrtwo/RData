---
layout: default
---

Lesson 3: Statistical Testing and Prediction
===============



Segment 1: Comparing Two Samples
--------------


{% highlight r %}
data("mtcars")

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

# help(mtcars)

mtcars$mpg
{% endhighlight %}



{% highlight text %}
##  [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2
## [15] 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2 13.3 19.2 27.3 26.0 30.4
## [29] 15.8 19.7 15.0 21.4
{% endhighlight %}



{% highlight r %}

mtcars$am
{% endhighlight %}



{% highlight text %}
##  [1] 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 1 1 1 1 1 1 1
{% endhighlight %}



{% highlight r %}

library(ggplot2)
{% endhighlight %}



{% highlight text %}
## Loading required package: methods
{% endhighlight %}



{% highlight r %}

ggplot(mtcars, aes(x = factor(am), y = mpg)) + geom_boxplot()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson3/segment_11.png) 

{% highlight r %}

ggplot(mtcars, aes(x = factor(am), y = mpg)) + geom_boxplot()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson3/segment_12.png) 

{% highlight r %}

t.test(mpg ~ am, data = mtcars)
{% endhighlight %}



{% highlight text %}
## 
## 	Welch Two Sample t-test
## 
## data:  mpg by am
## t = -3.767, df = 18.33, p-value = 0.001374
## alternative hypothesis: true difference in means is not equal to 0
## 95 percent confidence interval:
##  -11.28  -3.21
## sample estimates:
## mean in group 0 mean in group 1 
##           17.15           24.39
{% endhighlight %}



{% highlight r %}

tt = t.test(mpg ~ am, data = mtcars)

tt$p.value
{% endhighlight %}



{% highlight text %}
## [1] 0.001374
{% endhighlight %}



{% highlight r %}

tt$conf.int
{% endhighlight %}



{% highlight text %}
## [1] -11.28  -3.21
## attr(,"conf.level")
## [1] 0.95
{% endhighlight %}



{% highlight r %}

tt$conf.int[1]
{% endhighlight %}



{% highlight text %}
## [1] -11.28
{% endhighlight %}



{% highlight r %}

tt$conf.int[2]
{% endhighlight %}



{% highlight text %}
## [1] -3.21
{% endhighlight %}


Segment 2: Correlation
--------------


{% highlight r %}
ggplot(mtcars, aes(x = wt, y = mpg)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson3/segment_2.png) 

{% highlight r %}

mtcars$mpg
{% endhighlight %}



{% highlight text %}
##  [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2
## [15] 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2 13.3 19.2 27.3 26.0 30.4
## [29] 15.8 19.7 15.0 21.4
{% endhighlight %}



{% highlight r %}
mtcars$wt
{% endhighlight %}



{% highlight text %}
##  [1] 2.620 2.875 2.320 3.215 3.440 3.460 3.570 3.190 3.150 3.440 3.440
## [12] 4.070 3.730 3.780 5.250 5.424 5.345 2.200 1.615 1.835 2.465 3.520
## [23] 3.435 3.840 3.845 1.935 2.140 1.513 3.170 2.770 3.570 2.780
{% endhighlight %}



{% highlight r %}

cor.test(mtcars$mpg, mtcars$wt)
{% endhighlight %}



{% highlight text %}
## 
## 	Pearson's product-moment correlation
## 
## data:  mtcars$mpg and mtcars$wt
## t = -9.559, df = 30, p-value = 1.294e-10
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.9338 -0.7441
## sample estimates:
##     cor 
## -0.8677
{% endhighlight %}



{% highlight r %}

ct = cor.test(mtcars$mpg, mtcars$wt)

ct$p.value
{% endhighlight %}



{% highlight text %}
## [1] 1.294e-10
{% endhighlight %}



{% highlight r %}

ct$estimate
{% endhighlight %}



{% highlight text %}
##     cor 
## -0.8677
{% endhighlight %}



{% highlight r %}

ct$conf.int
{% endhighlight %}



{% highlight text %}
## [1] -0.9338 -0.7441
## attr(,"conf.level")
## [1] 0.95
{% endhighlight %}


Segment 3: Linear Regression
-----------------


{% highlight r %}
fit = lm(mpg ~ wt, mtcars)

fit
{% endhighlight %}



{% highlight text %}
## 
## Call:
## lm(formula = mpg ~ wt, data = mtcars)
## 
## Coefficients:
## (Intercept)           wt  
##       37.29        -5.34
{% endhighlight %}



{% highlight r %}

summary(fit)
{% endhighlight %}



{% highlight text %}
## 
## Call:
## lm(formula = mpg ~ wt, data = mtcars)
## 
## Residuals:
##    Min     1Q Median     3Q    Max 
## -4.543 -2.365 -0.125  1.410  6.873 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)   37.285      1.878   19.86  < 2e-16 ***
## wt            -5.344      0.559   -9.56  1.3e-10 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 3.05 on 30 degrees of freedom
## Multiple R-squared:  0.753,	Adjusted R-squared:  0.745 
## F-statistic: 91.4 on 1 and 30 DF,  p-value: 1.29e-10
{% endhighlight %}



{% highlight r %}

coef(summary(fit))
{% endhighlight %}



{% highlight text %}
##             Estimate Std. Error t value  Pr(>|t|)
## (Intercept)   37.285     1.8776  19.858 8.242e-19
## wt            -5.344     0.5591  -9.559 1.294e-10
{% endhighlight %}



{% highlight r %}

co = coef(summary(fit))
co[, 1]
{% endhighlight %}



{% highlight text %}
## (Intercept)          wt 
##      37.285      -5.344
{% endhighlight %}



{% highlight r %}

co[, 4]
{% endhighlight %}



{% highlight text %}
## (Intercept)          wt 
##   8.242e-19   1.294e-10
{% endhighlight %}



{% highlight r %}

predict(fit)
{% endhighlight %}



{% highlight text %}
##           Mazda RX4       Mazda RX4 Wag          Datsun 710 
##              23.283              21.920              24.886 
##      Hornet 4 Drive   Hornet Sportabout             Valiant 
##              20.103              18.900              18.793 
##          Duster 360           Merc 240D            Merc 230 
##              18.205              20.236              20.450 
##            Merc 280           Merc 280C          Merc 450SE 
##              18.900              18.900              15.533 
##          Merc 450SL         Merc 450SLC  Cadillac Fleetwood 
##              17.350              17.083               9.227 
## Lincoln Continental   Chrysler Imperial            Fiat 128 
##               8.297               8.719              25.527 
##         Honda Civic      Toyota Corolla       Toyota Corona 
##              28.654              27.478              24.111 
##    Dodge Challenger         AMC Javelin          Camaro Z28 
##              18.473              18.927              16.762 
##    Pontiac Firebird           Fiat X1-9       Porsche 914-2 
##              16.736              26.944              25.848 
##        Lotus Europa      Ford Pantera L        Ferrari Dino 
##              29.199              20.343              22.481 
##       Maserati Bora          Volvo 142E 
##              18.205              22.427
{% endhighlight %}



{% highlight r %}

summary(fit)
{% endhighlight %}



{% highlight text %}
## 
## Call:
## lm(formula = mpg ~ wt, data = mtcars)
## 
## Residuals:
##    Min     1Q Median     3Q    Max 
## -4.543 -2.365 -0.125  1.410  6.873 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)   37.285      1.878   19.86  < 2e-16 ***
## wt            -5.344      0.559   -9.56  1.3e-10 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 3.05 on 30 degrees of freedom
## Multiple R-squared:  0.753,	Adjusted R-squared:  0.745 
## F-statistic: 91.4 on 1 and 30 DF,  p-value: 1.29e-10
{% endhighlight %}



{% highlight r %}

37.2851 + (-5.3445) * 4.5
{% endhighlight %}



{% highlight text %}
## [1] 13.23
{% endhighlight %}



{% highlight r %}

newcar = data.frame(wt = 4.5)

predict(fit, newcar)
{% endhighlight %}



{% highlight text %}
##     1 
## 13.24
{% endhighlight %}



{% highlight r %}

ggplot(mtcars, aes(wt, mpg)) + geom_point() + geom_smooth(method = "lm")
{% endhighlight %}

![center](/RData/code/../figs/code_lesson3/segment_3.png) 


Segment 4: Multiple Linear Regression
-----------------


{% highlight r %}
ggplot(mtcars, aes(x = wt, y = mpg, col = cyl, size = disp)) + geom_point()
{% endhighlight %}

![center](/RData/code/../figs/code_lesson3/segment_4.png) 

{% highlight r %}

mfit = lm(mpg ~ wt + disp + cyl, mtcars)
summary(mfit)
{% endhighlight %}



{% highlight text %}
## 
## Call:
## lm(formula = mpg ~ wt + disp + cyl, data = mtcars)
## 
## Residuals:
##    Min     1Q Median     3Q    Max 
## -4.403 -1.403 -0.495  1.339  6.072 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 41.10768    2.84243   14.46  1.6e-14 ***
## wt          -3.63568    1.04014   -3.50   0.0016 ** 
## disp         0.00747    0.01184    0.63   0.5332    
## cyl         -1.78494    0.60711   -2.94   0.0065 ** 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.59 on 28 degrees of freedom
## Multiple R-squared:  0.833,	Adjusted R-squared:  0.815 
## F-statistic: 46.4 on 3 and 28 DF,  p-value: 5.4e-11
{% endhighlight %}



{% highlight r %}

mco = coef(summary(mfit))

mco[, 1]
{% endhighlight %}



{% highlight text %}
## (Intercept)          wt        disp         cyl 
##   41.107678   -3.635677    0.007473   -1.784944
{% endhighlight %}



{% highlight r %}
mco[, 4]
{% endhighlight %}



{% highlight text %}
## (Intercept)          wt        disp         cyl 
##   1.620e-14   1.596e-03   5.332e-01   6.512e-03
{% endhighlight %}



{% highlight r %}

predict(mfit)
{% endhighlight %}



{% highlight text %}
##           Mazda RX4       Mazda RX4 Wag          Datsun 710 
##               22.07               21.14               26.34 
##      Hornet 4 Drive   Hornet Sportabout             Valiant 
##               20.64               17.01               19.50 
##          Duster 360           Merc 240D            Merc 230 
##               16.54               23.47               23.57 
##            Merc 280           Merc 280C          Merc 450SE 
##               19.14               19.14               14.09 
##          Merc 450SL         Merc 450SLC  Cadillac Fleetwood 
##               15.33               15.15               11.27 
## Lincoln Continental   Chrysler Imperial            Fiat 128 
##               10.55               10.68               26.56 
##         Honda Civic      Toyota Corolla       Toyota Corona 
##               28.66               27.83               25.90 
##    Dodge Challenger         AMC Javelin          Camaro Z28 
##               16.41               16.61               15.48 
##    Pontiac Firebird           Fiat X1-9       Porsche 914-2 
##               15.84               27.52               27.09 
##        Lotus Europa      Ford Pantera L        Ferrari Dino 
##               29.18               17.93               21.41 
##       Maserati Bora          Volvo 142E 
##               16.10               24.76
{% endhighlight %}



{% highlight r %}

newcar = data.frame(wt = 4.5, disp = 300, cyl = 8)
newcar
{% endhighlight %}



{% highlight text %}
##    wt disp cyl
## 1 4.5  300   8
{% endhighlight %}



{% highlight r %}

predict(mfit, newcar)
{% endhighlight %}



{% highlight text %}
##     1 
## 12.71
{% endhighlight %}

