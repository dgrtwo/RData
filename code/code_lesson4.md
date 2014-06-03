---
layout: default
---

Lesson 4: Exploratory Data Analysis With data.table
===========



Segment 1: R Scripts
-----------


{% highlight r %}
3 + 5
{% endhighlight %}



{% highlight text %}
## [1] 8
{% endhighlight %}



{% highlight r %}

x = 4
y = x + 6

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



{% highlight r %}
print(y)
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}



{% highlight r %}

library("ggplot2")
data(mtcars)
ggplot(mtcars, aes(wt, mpg)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson4/segment_11.png) 

{% highlight r %}

print(ggplot(mtcars, aes(wt, mpg)) + geom_point())
{% endhighlight %}

![center](/../figs/code_lesson4/segment_12.png) 


Segment 2: Reading Data
--------------


{% highlight r %}
data(mtcars)

# download Salaries.csv from
# http://dgrtwo.github.io/pages/lahman/Salaries.csv

salaries = read.csv("Salaries.csv")
head(salaries)
{% endhighlight %}



{% highlight text %}
##   yearID teamID lgID  playerID  salary
## 1   1985    BAL   AL murraed02 1472819
## 2   1985    BAL   AL  lynnfr01 1090000
## 3   1985    BAL   AL ripkeca01  800000
## 4   1985    BAL   AL  lacyle01  725000
## 5   1985    BAL   AL flanami01  641667
## 6   1985    BAL   AL boddimi01  625000
{% endhighlight %}



{% highlight r %}

salaries = read.csv("http://dgrtwo.github.io/pages/lahman/Salaries.csv")
head(salaries)
{% endhighlight %}



{% highlight text %}
##   yearID teamID lgID  playerID  salary
## 1   1985    BAL   AL murraed02 1472819
## 2   1985    BAL   AL  lynnfr01 1090000
## 3   1985    BAL   AL ripkeca01  800000
## 4   1985    BAL   AL  lacyle01  725000
## 5   1985    BAL   AL flanami01  641667
## 6   1985    BAL   AL boddimi01  625000
{% endhighlight %}



{% highlight r %}

# help(read.csv)
{% endhighlight %}


Segment 3: Introduction to data.table
-------------


{% highlight r %}
# install.packages('data.table')

library(data.table)
salaries = as.data.table(salaries)

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



{% highlight r %}

head(salaries$salary)
{% endhighlight %}



{% highlight text %}
## [1] 1472819 1090000  800000  725000  641667  625000
{% endhighlight %}



{% highlight r %}

salaries[1, ]
{% endhighlight %}



{% highlight text %}
##    yearID teamID lgID  playerID  salary
## 1:   1985    BAL   AL murraed02 1472819
{% endhighlight %}



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



{% highlight r %}

head(salaries[, yearID])
{% endhighlight %}



{% highlight text %}
## [1] 1985 1985 1985 1985 1985 1985
{% endhighlight %}



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



{% highlight r %}

salaries[lgID == "AL" & yearID > 1990, ]
{% endhighlight %}



{% highlight text %}
##       yearID teamID lgID  playerID  salary
##    1:   1991    BAL   AL davisgl01 3275000
##    2:   1991    BAL   AL ripkeca01 2566667
##    3:   1991    BAL   AL davisst02 2366666
##    4:   1991    BAL   AL orsuljo01 1100000
##    5:   1991    BAL   AL evansdw01  800000
##   ---                                     
## 9549:   2013    TOR   AL perezlu01  500000
## 9550:   2013    TOR   AL drabeky01  499500
## 9551:   2013    TOR   AL delabst01  498900
## 9552:   2013    TOR   AL jeffrje01  495900
## 9553:   2013    TOR   AL  loupaa01  494200
{% endhighlight %}



{% highlight r %}

salaries[yearID > 2010 | yearID < 1990, ]
{% endhighlight %}



{% highlight text %}
##       yearID teamID lgID  playerID  salary
##    1:   1985    BAL   AL murraed02 1472819
##    2:   1985    BAL   AL  lynnfr01 1090000
##    3:   1985    BAL   AL ripkeca01  800000
##    4:   1985    BAL   AL  lacyle01  725000
##    5:   1985    BAL   AL flanami01  641667
##   ---                                     
## 5787:   2013    WAS   NL matthry01  504500
## 5788:   2013    WAS   NL lombast02  501250
## 5789:   2013    WAS   NL ramoswi01  501250
## 5790:   2013    WAS   NL rodrihe03  501000
## 5791:   2013    WAS   NL moorety01  493000
{% endhighlight %}



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



{% highlight r %}

salaries.filtered = salaries[lgID == "AL" & yearID >= 1990, ]
salaries.filtered.sorted = salaries.filtered[order(salary), ]
{% endhighlight %}


Segment 4: Summarizing Data Within Groups
--------------


{% highlight r %}
head(salaries$salary)
{% endhighlight %}



{% highlight text %}
## [1] 1472819 1090000  800000  725000  641667  625000
{% endhighlight %}



{% highlight r %}

mean(salaries$salary)
{% endhighlight %}



{% highlight text %}
## [1] 1864357
{% endhighlight %}



{% highlight r %}

head(salaries[yearID == 2000, ]$salary)
{% endhighlight %}



{% highlight text %}
## [1] 11166667  6000000  5600000  4600000  4000000  3250000
{% endhighlight %}



{% highlight r %}

mean(salaries[yearID == 2000, ]$salary)
{% endhighlight %}



{% highlight text %}
## [1] 1992985
{% endhighlight %}



{% highlight r %}

summarized.year = salaries[, mean(salary), by = "yearID"]
{% endhighlight %}



{% highlight text %}
## Warning: Group 21 summed to more than type 'integer' can hold so the
## result has been coerced to 'numeric' automatically, for convenience.
{% endhighlight %}



{% highlight r %}
summarized.year
{% endhighlight %}



{% highlight text %}
##     yearID      V1
##  1:   1985  476299
##  2:   1986  417147
##  3:   1987  434729
##  4:   1988  453171
##  5:   1989  506323
##  6:   1990  511974
##  7:   1991  894961
##  8:   1992 1047521
##  9:   1993  976967
## 10:   1994 1049589
## 11:   1995  964979
## 12:   1996 1027909
## 13:   1997 1218687
## 14:   1998 1280845
## 15:   1999 1485317
## 16:   2000 1992985
## 17:   2001 2279841
## 18:   2002 2392527
## 19:   2003 2573473
## 20:   2004 2491776
## 21:   2005 2633831
## 22:   2006 2834521
## 23:   2007 2941436
## 24:   2008 3136517
## 25:   2009 3277647
## 26:   2010 3278747
## 27:   2011 3318838
## 28:   2012 3458421
## 29:   2013 3723344
##     yearID      V1
{% endhighlight %}



{% highlight r %}

summarized.year = salaries[, list(Average = mean(salary)), by = "yearID"]
{% endhighlight %}



{% highlight text %}
## Warning: Group 21 summed to more than type 'integer' can hold so the
## result has been coerced to 'numeric' automatically, for convenience.
{% endhighlight %}



{% highlight r %}
summarized.year
{% endhighlight %}



{% highlight text %}
##     yearID Average
##  1:   1985  476299
##  2:   1986  417147
##  3:   1987  434729
##  4:   1988  453171
##  5:   1989  506323
##  6:   1990  511974
##  7:   1991  894961
##  8:   1992 1047521
##  9:   1993  976967
## 10:   1994 1049589
## 11:   1995  964979
## 12:   1996 1027909
## 13:   1997 1218687
## 14:   1998 1280845
## 15:   1999 1485317
## 16:   2000 1992985
## 17:   2001 2279841
## 18:   2002 2392527
## 19:   2003 2573473
## 20:   2004 2491776
## 21:   2005 2633831
## 22:   2006 2834521
## 23:   2007 2941436
## 24:   2008 3136517
## 25:   2009 3277647
## 26:   2010 3278747
## 27:   2011 3318838
## 28:   2012 3458421
## 29:   2013 3723344
##     yearID Average
{% endhighlight %}



{% highlight r %}

summarized.year = salaries[, list(Average = mean(salary), Maximum = max(salary)), 
    by = "yearID"]
summarized.year
{% endhighlight %}



{% highlight text %}
##     yearID Average  Maximum
##  1:   1985  476299  2130300
##  2:   1986  417147  2800000
##  3:   1987  434729  2127333
##  4:   1988  453171  2340000
##  5:   1989  506323  2766667
##  6:   1990  511974  3200000
##  7:   1991  894961  3800000
##  8:   1992 1047521  6100000
##  9:   1993  976967  6200000
## 10:   1994 1049589  6300000
## 11:   1995  964979  9237500
## 12:   1996 1027909  9237500
## 13:   1997 1218687 10000000
## 14:   1998 1280845 14936667
## 15:   1999 1485317 11949794
## 16:   2000 1992985 15714286
## 17:   2001 2279841 22000000
## 18:   2002 2392527 22000000
## 19:   2003 2573473 22000000
## 20:   2004 2491776 22500000
## 21:   2005 2633831 26000000
## 22:   2006 2834521 21680727
## 23:   2007 2941436 23428571
## 24:   2008 3136517 28000000
## 25:   2009 3277647 33000000
## 26:   2010 3278747 33000000
## 27:   2011 3318838 32000000
## 28:   2012 3458421 30000000
## 29:   2013 3723344 29000000
##     yearID Average  Maximum
{% endhighlight %}



{% highlight r %}

summarized.lg = salaries[, list(Average = mean(salary), Maximum = max(salary)), 
    by = "lgID"]
summarized.lg
{% endhighlight %}



{% highlight text %}
##    lgID Average  Maximum
## 1:   AL 1891850 33000000
## 2:   NL 1837917 25000000
{% endhighlight %}



{% highlight r %}

summarized.team = salaries[, list(Average = mean(salary), Maximum = max(salary)), 
    by = "teamID"]
summarized.team
{% endhighlight %}



{% highlight text %}
##     teamID Average  Maximum
##  1:    BAL 1785712 17000000
##  2:    BOS 2692114 22500000
##  3:    CAL  739073  5375000
##  4:    CHA 1992654 17000000
##  5:    CLE 1525795 15000000
##  6:    DET 1980835 23000000
##  7:    KCA 1299026 13000000
##  8:    MIN 1525032 23000000
##  9:    ML4  613244  5875000
## 10:    NYA 3608860 33000000
## 11:    OAK 1303095 13500000
## 12:    SEA 1932289 20557143
## 13:    TEX 1874652 22000000
## 14:    TOR 1768711 19700000
## 15:    ATL 2130475 16061802
## 16:    CHN 2185519 19000000
## 17:    CIN 1568035 18910655
## 18:    HOU 1705561 19369019
## 19:    LAN 2346983 23854494
## 20:    MON  707459 11500000
## 21:    NYN 2317350 23145011
## 22:    PHI 2092231 25000000
## 23:    PIT 1077990 16500000
## 24:    SDN 1317960 15505142
## 25:    SFN 2044199 22250000
## 26:    SLN 1928833 16333327
## 27:    COL 1945628 20275000
## 28:    FLO 1147986 14936667
## 29:    ANA 1895109 13166667
## 30:    TBA 1528400 10125000
## 31:    ARI 2428196 16000000
## 32:    MIL 2095009 15500000
## 33:    LAA 4151107 26187500
## 34:    WAS 2243755 16571429
## 35:    MIA 2974116 19000000
##     teamID Average  Maximum
{% endhighlight %}



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



{% highlight r %}
summarized.team[order(Average), ]
{% endhighlight %}



{% highlight text %}
##     teamID Average  Maximum
##  1:    ML4  613244  5875000
##  2:    MON  707459 11500000
##  3:    CAL  739073  5375000
##  4:    PIT 1077990 16500000
##  5:    FLO 1147986 14936667
##  6:    KCA 1299026 13000000
##  7:    OAK 1303095 13500000
##  8:    SDN 1317960 15505142
##  9:    MIN 1525032 23000000
## 10:    CLE 1525795 15000000
## 11:    TBA 1528400 10125000
## 12:    CIN 1568035 18910655
## 13:    HOU 1705561 19369019
## 14:    TOR 1768711 19700000
## 15:    BAL 1785712 17000000
## 16:    TEX 1874652 22000000
## 17:    ANA 1895109 13166667
## 18:    SLN 1928833 16333327
## 19:    SEA 1932289 20557143
## 20:    COL 1945628 20275000
## 21:    DET 1980835 23000000
## 22:    CHA 1992654 17000000
## 23:    SFN 2044199 22250000
## 24:    PHI 2092231 25000000
## 25:    MIL 2095009 15500000
## 26:    ATL 2130475 16061802
## 27:    CHN 2185519 19000000
## 28:    WAS 2243755 16571429
## 29:    NYN 2317350 23145011
## 30:    LAN 2346983 23854494
## 31:    ARI 2428196 16000000
## 32:    BOS 2692114 22500000
## 33:    MIA 2974116 19000000
## 34:    NYA 3608860 33000000
## 35:    LAA 4151107 26187500
##     teamID Average  Maximum
{% endhighlight %}



{% highlight r %}

summarized.year.lg = salaries[, list(Average = mean(salary), Maximum = max(salary)), 
    by = c("yearID", "lgID")]
summarized.year.lg
{% endhighlight %}



{% highlight text %}
##     yearID lgID Average  Maximum
##  1:   1985   AL  455597  1795704
##  2:   1985   NL  500249  2130300
##  3:   1986   AL  402338  1984423
##  4:   1986   NL  433925  2800000
##  5:   1987   AL  441847  2110000
##  6:   1987   NL  427858  2127333
##  7:   1988   AL  453901  2305000
##  8:   1988   NL  452374  2340000
##  9:   1989   AL  502052  2766666
## 10:   1989   NL  511116  2766667
## 11:   1990   AL  500416  3200000
## 12:   1990   NL  525914  2513703
## 13:   1991   AL  908127  3791667
## 14:   1991   NL  879588  3800000
## 15:   1992   AL 1017651  5300000
## 16:   1992   NL 1085609  6100000
## 17:   1993   AL 1028576  5550000
## 18:   1993   NL  923883  6200000
## 19:   1994   AL 1130703  5550000
## 20:   1994   NL  971003  6300000
## 21:   1995   AL 1039865  9237500
## 22:   1995   NL  890699  8166666
## 23:   1996   AL 1055235  9237500
## 24:   1996   NL 1000407  8416667
## 25:   1997   AL 1267830 10000000
## 26:   1997   NL 1169651  8666667
## 27:   1998   AL 1364397 10000000
## 28:   1998   NL 1207658 14936667
## 29:   1999   AL 1503986 11949794
## 30:   1999   NL 1468881 10714286
## 31:   2000   AL 2004402 12868670
## 32:   2000   NL 1983097 15714286
## 33:   2001   AL 2333184 22000000
## 34:   2001   NL 2232801 15714286
## 35:   2002   AL 2449016 22000000
## 36:   2002   NL 2342579 15714286
## 37:   2003   AL 2524940 22000000
## 38:   2003   NL 2614933 17166667
## 39:   2004   AL 2517280 22500000
## 40:   2004   NL 2469003 18000000
## 41:   2005   AL 2681581 26000000
## 42:   2005   NL 2590987 22000000
## 43:   2006   AL 3088942 21680727
## 44:   2006   NL 2616446 19369019
## 45:   2007   AL 3304391 23428571
## 46:   2007   NL 2623749 16600000
## 47:   2008   AL 3449574 28000000
## 48:   2008   NL 2870790 18622809
## 49:   2009   AL 3380833 33000000
## 50:   2009   NL 3184369 23854494
## 51:   2010   AL 3431360 33000000
## 52:   2010   NL 3142161 20144707
## 53:   2011   AL 3505557 32000000
## 54:   2011   NL 3156655 21644707
## 55:   2012   AL 3662264 30000000
## 56:   2012   NL 3277278 23145011
## 57:   2013   AL 3757664 29000000
## 58:   2013   NL 3688940 25000000
##     yearID lgID Average  Maximum
{% endhighlight %}



{% highlight r %}

summarized.year.team = salaries[, list(Average = mean(salary), Maximum = max(salary)), 
    by = c("yearID", "teamID")]
summarized.year.team
{% endhighlight %}



{% highlight text %}
##      yearID teamID Average  Maximum
##   1:   1985    BAL  525487  1472819
##   2:   1985    BOS  435902  1075000
##   3:   1985    CAL  515282  1100000
##   4:   1985    CHA  468866  1242333
##   5:   1985    CLE  327583  1100000
##  ---                               
## 824:   2013    PIT 2752214 16500000
## 825:   2013    SDN 2342339  9500000
## 826:   2013    SFN 5006440 22250000
## 827:   2013    SLN 3295004 16272110
## 828:   2013    WAS 4548131 16571429
{% endhighlight %}



{% highlight r %}

library(ggplot2)
ggplot(salaries, aes(yearID, salary)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson4/segment_41.png) 

{% highlight r %}

summarized.year
{% endhighlight %}



{% highlight text %}
##     yearID Average  Maximum
##  1:   1985  476299  2130300
##  2:   1986  417147  2800000
##  3:   1987  434729  2127333
##  4:   1988  453171  2340000
##  5:   1989  506323  2766667
##  6:   1990  511974  3200000
##  7:   1991  894961  3800000
##  8:   1992 1047521  6100000
##  9:   1993  976967  6200000
## 10:   1994 1049589  6300000
## 11:   1995  964979  9237500
## 12:   1996 1027909  9237500
## 13:   1997 1218687 10000000
## 14:   1998 1280845 14936667
## 15:   1999 1485317 11949794
## 16:   2000 1992985 15714286
## 17:   2001 2279841 22000000
## 18:   2002 2392527 22000000
## 19:   2003 2573473 22000000
## 20:   2004 2491776 22500000
## 21:   2005 2633831 26000000
## 22:   2006 2834521 21680727
## 23:   2007 2941436 23428571
## 24:   2008 3136517 28000000
## 25:   2009 3277647 33000000
## 26:   2010 3278747 33000000
## 27:   2011 3318838 32000000
## 28:   2012 3458421 30000000
## 29:   2013 3723344 29000000
##     yearID Average  Maximum
{% endhighlight %}



{% highlight r %}
ggplot(summarized.year, aes(yearID, Average)) + geom_line()
{% endhighlight %}

![center](/../figs/code_lesson4/segment_42.png) 

{% highlight r %}

ggplot(summarized.year.lg, aes(yearID, Average, color = lgID)) + geom_line()
{% endhighlight %}

![center](/../figs/code_lesson4/segment_43.png) 


Segment 5: Merging Data
-------------


{% highlight r %}
master = read.csv("http://dgrtwo.github.io/pages/lahman/Master.csv")

master = as.data.table(master)

head(master)
{% endhighlight %}



{% highlight text %}
##     playerID birthYear birthMonth birthDay birthCountry birthState
## 1: aardsda01      1981         12       27          USA         CO
## 2: aaronha01      1934          2        5          USA         AL
## 3: aaronto01      1939          8        5          USA         AL
## 4:  aasedo01      1954          9        8          USA         CA
## 5:  abadan01      1972          8       25          USA         FL
## 6:  abadfe01      1985         12       17         D.R.  La Romana
##     birthCity deathYear deathMonth deathDay deathCountry deathState
## 1:     Denver        NA         NA       NA                        
## 2:     Mobile        NA         NA       NA                        
## 3:     Mobile      1984          8       16          USA         GA
## 4:     Orange        NA         NA       NA                        
## 5: Palm Beach        NA         NA       NA                        
## 6:  La Romana        NA         NA       NA                        
##    deathCity nameFirst nameLast        nameGiven weight height bats throws
## 1:               David  Aardsma      David Allan    205     75    R      R
## 2:                Hank    Aaron      Henry Louis    180     72    R      R
## 3:   Atlanta    Tommie    Aaron       Tommie Lee    190     75    R      R
## 4:                 Don     Aase   Donald William    190     75    R      R
## 5:                Andy     Abad    Fausto Andres    184     73    L      L
## 6:            Fernando     Abad Fernando Antonio    220     73    L      L
##         debut  finalGame  retroID   bbrefID
## 1: 2004-04-06 2013-09-28 aardd001 aardsda01
## 2: 1954-04-13 1976-10-03 aaroh101 aaronha01
## 3: 1962-04-10 1971-09-26 aarot101 aaronto01
## 4: 1977-07-26 1990-10-03 aased001  aasedo01
## 5: 2001-09-10 2006-04-13 abada001  abadan01
## 6: 2010-07-28 2013-09-27 abadf001  abadfe01
{% endhighlight %}



{% highlight r %}

salaries[playerID == "aardsda01"]
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



{% highlight r %}

merged.salaries = merge(salaries, master, by = "playerID")
merged.salaries[, `:=`(name, paste(nameFirst, nameLast))]
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



{% highlight r %}

batting = read.csv("http://dgrtwo.github.io/pages/lahman/Batting.csv")
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



{% highlight r %}

merged.batting = merge(batting, salaries, by = c("playerID", "teamID", "lgID", 
    "yearID"))

merged.batting
{% endhighlight %}



{% highlight text %}
##         playerID teamID lgID yearID stint   G G_batting  AB  R   H X2B X3B
##     1: aardsda01    BOS   AL   2008     1  47         5   1  0   0   0   0
##     2: aardsda01    CHA   AL   2007     1  25         2   0  0   0   0   0
##     3: aardsda01    NYA   AL   2012     1   1        NA  NA NA  NA  NA  NA
##     4: aardsda01    SEA   AL   2009     1  73         3   0  0   0   0   0
##     5: aardsda01    SEA   AL   2010     1  53         4   0  0   0   0   0
##    ---                                                                    
## 22867: zumayjo01    DET   AL   2009     1  29         3   0  0   0   0   0
## 22868: zumayjo01    DET   AL   2010     1  31         4   0  0   0   0   0
## 22869: zupcibo01    BOS   AL   1991     1  18        18  25  3   4   0   0
## 22870: zupcibo01    BOS   AL   1992     1 124       124 392 46 108  19   1
## 22871: zupcibo01    BOS   AL   1993     1 141       141 286 40  69  24   2
##        HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old  salary
##     1:  0   0  0  0  0  1   0   0  0  0    0     5  403250
##     2:  0   0  0  0  0  0   0   0  0  0    0     2  387500
##     3: NA  NA NA NA NA NA  NA  NA NA NA   NA    NA  500000
##     4:  0   0  0  0  0  0   0   0  0  0    0    NA  419000
##     5:  0   0  0  0  0  0   0   0  0  0    0    NA 2750000
##    ---                                                    
## 22867:  0   0  0  0  0  0   0   0  0  0    0    NA  735000
## 22868:  0   0  0  0  0  0   0   0  0  0    0    NA  915000
## 22869:  1   3  0  0  1  6   0   0  1  0    0    18  100000
## 22870:  3  43  2  2 25 60   1   4  7  4    6   124  109000
## 22871:  2  26  5  2 27 54   2   2  8  3    7   141  222000
{% endhighlight %}



{% highlight r %}

merged.batting = merge(batting, salaries, by = c("playerID", "teamID", "lgID", 
    "yearID"), all.x = TRUE)

merged.batting
{% endhighlight %}



{% highlight text %}
##         playerID teamID lgID yearID stint   G G_batting  AB  R   H X2B X3B
##     1: aardsda01    BOS   AL   2008     1  47         5   1  0   0   0   0
##     2: aardsda01    CHA   AL   2007     1  25         2   0  0   0   0   0
##     3: aardsda01    CHN   NL   2006     1  45        43   2  0   0   0   0
##     4: aardsda01    NYA   AL   2012     1   1        NA  NA NA  NA  NA  NA
##     5: aardsda01    NYN   NL   2013     1  43        43   0  0   0   0   0
##    ---                                                                    
## 97885: zuverge01    DET   AL   1955     1  14        14   4  0   0   0   0
## 97886: zwilldu01    CHA   AL   1910     1  27        27  87  7  16   5   0
## 97887: zwilldu01    CHF   FL   1914     1 154       154 592 91 185  38   8
## 97888: zwilldu01    CHF   FL   1915     1 150       150 548 65 157  32   7
## 97889: zwilldu01    CHN   NL   1916     1  35        35  53  4   6   1   0
##        HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary
##     1:  0   0  0  0  0  1   0   0  0  0    0     5 403250
##     2:  0   0  0  0  0  0   0   0  0  0    0     2 387500
##     3:  0   0  0  0  0  0   0   0  1  0    0    45     NA
##     4: NA  NA NA NA NA NA  NA  NA NA NA   NA    NA 500000
##     5:  0   0  0  0  0  0   0   0  0  0    0    NA     NA
##    ---                                                   
## 97885:  0   0  0  0  0  2   0   0  0  0    0    14     NA
## 97886:  0   5  1 NA 11 NA  NA   1  1 NA   NA    27     NA
## 97887: 16  95 21 NA 46 68  NA   1 10 NA   NA   154     NA
## 97888: 13  94 24 NA 67 65  NA   2 18 NA   NA   150     NA
## 97889:  1   8  0 NA  4  6  NA   0  2 NA   NA    35     NA
{% endhighlight %}



{% highlight r %}

merged.all = merge(merged.batting, master, by = "playerID")
merged.all
{% endhighlight %}



{% highlight text %}
##         playerID teamID lgID yearID stint   G G_batting  AB  R   H X2B X3B
##     1: aardsda01    BOS   AL   2008     1  47         5   1  0   0   0   0
##     2: aardsda01    CHA   AL   2007     1  25         2   0  0   0   0   0
##     3: aardsda01    CHN   NL   2006     1  45        43   2  0   0   0   0
##     4: aardsda01    NYA   AL   2012     1   1        NA  NA NA  NA  NA  NA
##     5: aardsda01    NYN   NL   2013     1  43        43   0  0   0   0   0
##    ---                                                                    
## 97885: zuverge01    DET   AL   1955     1  14        14   4  0   0   0   0
## 97886: zwilldu01    CHA   AL   1910     1  27        27  87  7  16   5   0
## 97887: zwilldu01    CHF   FL   1914     1 154       154 592 91 185  38   8
## 97888: zwilldu01    CHF   FL   1915     1 150       150 548 65 157  32   7
## 97889: zwilldu01    CHN   NL   1916     1  35        35  53  4   6   1   0
##        HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary birthYear
##     1:  0   0  0  0  0  1   0   0  0  0    0     5 403250      1981
##     2:  0   0  0  0  0  0   0   0  0  0    0     2 387500      1981
##     3:  0   0  0  0  0  0   0   0  1  0    0    45     NA      1981
##     4: NA  NA NA NA NA NA  NA  NA NA NA   NA    NA 500000      1981
##     5:  0   0  0  0  0  0   0   0  0  0    0    NA     NA      1981
##    ---                                                             
## 97885:  0   0  0  0  0  2   0   0  0  0    0    14     NA      1924
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


Segment 6: Exploratory Data Analysis
-------------


{% highlight r %}
merged.all = merged.all[AB > 0]
merged.all
{% endhighlight %}



{% highlight text %}
##         playerID teamID lgID yearID stint   G G_batting  AB   R   H X2B
##     1: aardsda01    BOS   AL   2008     1  47         5   1   0   0   0
##     2: aardsda01    CHN   NL   2006     1  45        43   2   0   0   0
##     3: aaronha01    ATL   NL   1966     1 158       158 603 117 168  23
##     4: aaronha01    ATL   NL   1967     1 155       155 600 113 184  37
##     5: aaronha01    ATL   NL   1968     1 160       160 606  84 174  33
##    ---                                                                 
## 84365: zuverge01    DET   AL   1955     1  14        14   4   0   0   0
## 84366: zwilldu01    CHA   AL   1910     1  27        27  87   7  16   5
## 84367: zwilldu01    CHF   FL   1914     1 154       154 592  91 185  38
## 84368: zwilldu01    CHF   FL   1915     1 150       150 548  65 157  32
## 84369: zwilldu01    CHN   NL   1916     1  35        35  53   4   6   1
##        X3B HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary birthYear
##     1:   0  0   0  0  0  0  1   0   0  0  0    0     5 403250      1981
##     2:   0  0   0  0  0  0  0   0   0  1  0    0    45     NA      1981
##     3:   1 44 127 21  3 76 96  15   1  0  8   14   158     NA      1934
##     4:   3 39 109 17  6 63 97  19   0  0  6   11   155     NA      1934
##     5:   4 29  86 28  5 64 62  23   1  0  5   21   160     NA      1934
##    ---                                                                 
## 84365:   0  0   0  0  0  0  2   0   0  0  0    0    14     NA      1924
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



{% highlight r %}

summarized.batters = merged.all[, list(Total.HR = sum(HR)), by = "playerID"]
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



{% highlight r %}

merged.all[, `:=`(name, paste(nameFirst, nameLast))]
{% endhighlight %}



{% highlight text %}
##         playerID teamID lgID yearID stint   G G_batting  AB   R   H X2B
##     1: aardsda01    BOS   AL   2008     1  47         5   1   0   0   0
##     2: aardsda01    CHN   NL   2006     1  45        43   2   0   0   0
##     3: aaronha01    ATL   NL   1966     1 158       158 603 117 168  23
##     4: aaronha01    ATL   NL   1967     1 155       155 600 113 184  37
##     5: aaronha01    ATL   NL   1968     1 160       160 606  84 174  33
##    ---                                                                 
## 84365: zuverge01    DET   AL   1955     1  14        14   4   0   0   0
## 84366: zwilldu01    CHA   AL   1910     1  27        27  87   7  16   5
## 84367: zwilldu01    CHF   FL   1914     1 154       154 592  91 185  38
## 84368: zwilldu01    CHF   FL   1915     1 150       150 548  65 157  32
## 84369: zwilldu01    CHN   NL   1916     1  35        35  53   4   6   1
##        X3B HR RBI SB CS BB SO IBB HBP SH SF GIDP G_old salary birthYear
##     1:   0  0   0  0  0  0  1   0   0  0  0    0     5 403250      1981
##     2:   0  0   0  0  0  0  0   0   0  1  0    0    45     NA      1981
##     3:   1 44 127 21  3 76 96  15   1  0  8   14   158     NA      1934
##     4:   3 39 109 17  6 63 97  19   0  0  6   11   155     NA      1934
##     5:   4 29  86 28  5 64 62  23   1  0  5   21   160     NA      1934
##    ---                                                                 
## 84365:   0  0   0  0  0  0  2   0   0  0  0    0    14     NA      1924
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



{% highlight r %}
summarized.batters = merged.all[, list(Total.HR = sum(HR)), by = c("playerID", 
    "name")]
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



{% highlight r %}

summarized.batters[order(Total.HR)]
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



{% highlight r %}

summarized.batters = merged.all[, list(Total.HR = sum(HR), Total.R = sum(R), 
    Total.H = sum(H)), by = c("playerID", "name")]
ggplot(summarized.batters, aes(Total.H, Total.R)) + geom_point()
{% endhighlight %}

![center](/../figs/code_lesson4/segment_61.png) 

{% highlight r %}

189/602
{% endhighlight %}



{% highlight text %}
## [1] 0.314
{% endhighlight %}



{% highlight r %}

summarized.batters = merged.all[, list(Total.HR = sum(HR), Total.R = sum(R), 
    Total.H = sum(H), BattingAverage = sum(H)/sum(AB)), by = c("playerID", "name")]
summarized.batters
{% endhighlight %}



{% highlight text %}
##         playerID            name Total.HR Total.R Total.H BattingAverage
##     1: aardsda01   David Aardsma        0       0       0        0.00000
##     2: aaronha01      Hank Aaron      755    2174    3771        0.30500
##     3: aaronto01    Tommie Aaron       13     102     216        0.22881
##     4:  aasedo01        Don Aase        0       0       0        0.00000
##     5:  abadan01       Andy Abad        0       1       2        0.09524
##    ---                                                                  
## 16336: zupcibo01      Bob Zupcic        7      99     199        0.25031
## 16337:  zupofr01      Frank Zupo        0       3       3        0.16667
## 16338: zuvelpa01    Paul Zuvella        2      41     109        0.22200
## 16339: zuverge01 George Zuverink        0       4      21        0.14789
## 16340: zwilldu01  Dutch Zwilling       30     167     364        0.28437
{% endhighlight %}



{% highlight r %}

ggplot(summarized.batters, aes(BattingAverage)) + geom_histogram()
{% endhighlight %}



{% highlight text %}
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
{% endhighlight %}

![center](/../figs/code_lesson4/segment_62.png) 

