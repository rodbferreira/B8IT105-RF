'
Rodolfo Ferreira
Programming for Big Data
Id 10540987
CA5 - RStudio Data
github https://github.com/rodbferreira/B8IT105-RF
'


library(lubridate)
library(ggplot2)

#Load data
setwd('C:/Users/Rodolfo Laptop/Documents/GitHub/B8IT105-RF/CA5')
data<-read.csv('premierleague.csv',header = TRUE)

#examine data
head(data)
tail(data)
summary(data)
str(data)


table1<-table(data$club, data$age)

# Get Age average per Club
aggregate(data[,3:3], list(data$club), mean)

# Get Market Value average per Club
aggregate(data[,6:6], list(data$club), mean)

#Get Club Market Value
aggregate(data[,6:6], list(data$club), sum)

#Plot
ggplot(data,aes(age,club)) + geom_point()

ggplot(data,aes(market_value,club)) + geom_boxplot()

hist(data$age)

hist(data$page_views)

ggplot(data,aes(age, color = club)) + geom_histogram(binwidth = 10)


