---
layout: page
title: Quizzes
---

Each video segment is associated with one or more exercises intended for you to test your own understanding, which are provided as [Swirl](http://swirlstats.com/) interactive R quizzes.

### Installing Swirl

To install Swirl, go to any interactive R terminal and type

    install.packages("swirl")
    library("swirl")

Then install this class's quizzes with the line:

    install_course_github("dgrtwo", "RData", branch="quizzes", multi=TRUE)

### Taking a Quiz

Once you've finished one of the videos and you wish to take the associated quiz, you simply start swirl:

    library("swirl")
    swirl()

You'll be prompted for your name and informed of the basics of how Swirl works. Soon you'll reach a page that looks like:

    | Please choose a course, or type 0 to exit swirl.

    1: 1. Variables and Data Structures
    2: 2. Visualizing Data Using ggplot2
    3: 3. Statistical Testing and Prediction
    4: 4. Exploratory Data Analysis with data.table
    5: Take me to the swirl course repository!

Choose whichever lesson you are currently taking, and you'll get to choose which quiz to take:

    1: 2.2 Scatter Plots
    2: 2.3 Faceting and Additional Options
    3: 2.4 Histograms and Density Plots
    4: 2.5 Boxplots and Violin Plots
    5: 2.6 Input- Getting Data into the Right Format
    6: 2.7 Output- Saving Your Plots

Each of these is a quiz corresponding to one video segment. Simply select the quiz you wish to take and it will start.

For more information on Swirl, please see [here](http://swirlstats.com/help.html).