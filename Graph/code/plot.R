library(ggplot2)
## Date:Time VS Letters -- Prison
data <- read.csv('/Users/apple/Desktop/week8/letter_prison.csv')
data$start_date <- as.Date(data$start_date, format="%Y/%m/%d")
ggplot(data, aes(x=start_date, y=total)) +
  geom_line() +
  scale_x_date(date_breaks = "2 month", date_labels = "%Y/%m/%d") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) + 
  xlab("Start Date") +
  ylab("Total") +
  ggtitle("time vs letters(Prison)")

## No.Week:Time VS Letters -- Prison
data <- read.csv('/Users/apple/Desktop/week8/letter_prison.csv')
data$Week_Number <- factor(data$Week_Number, levels = unique(data$Week_Number))
ggplot(data, aes(x = Week_Number, y = total, group = 1)) +  
  geom_line() + 
  geom_point() +  
  xlab("No. Week") + 
  ylab("Total") +
  ggtitle("Weekly: time vs letters (Prison)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) 

## No.Month: Time VS Letters -- Prison
data <- read.csv("/Users/apple/Desktop/week8/letter_prison.csv")
data$Month_Number <- as.numeric(gsub("Month ", "", data$Month_Number))
data$month_total <- as.numeric(data$month_total)
ggplot(data, aes(x = Month_Number, y = month_total)) +
  geom_line() +
  geom_point() +
  theme_minimal() +
  scale_x_continuous(breaks = data$Month_Number) + 
  labs(x = "No.Month", y = "Monthly Total", title = "Monthly: time vs letters(Prison)")



## Date: Time VS Letters -- Jail
data <- read.csv('/Users/apple/Desktop/week8/letter_jail_weeklytotal.csv')
data$start_date <- as.Date(data$start_date, format="%Y/%m/%d")
ggplot(data, aes(x=start_date, y=total)) +
  geom_line() +
  scale_x_date(date_breaks = "1 month", date_labels = "%Y/%m/%d") + 
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) + 
  xlab("Start Date") +
  ylab("Total") +
  ggtitle("time vs letters(Jail)")

## No.Week:Time VS Letters -- Jail
data <- read.csv('/Users/apple/Desktop/week8/letter_jail.csv')
data$Week_Number <- factor(data$Week_Number, levels = unique(data$Week_Number))
ggplot(data, aes(x = Week_Number, y = total, group = 1)) +  
  geom_line() + 
  geom_point() +  
  xlab("No. Week") + 
  ylab("Total") +
  ggtitle("Weekly: time vs letters (Jail)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

## No.Month: Time VS Letters -- Jail
data <- read.csv("/Users/apple/Desktop/week8/letter_jail.csv")
data$Month_Number <- as.numeric(gsub("Month ", "", data$Month_Number))
data$month_total <- as.numeric(data$month_total)
ggplot(data, aes(x = Month_Number, y = month_total)) +
  geom_line() +
  geom_point() +
  theme_minimal() +
  scale_x_continuous(breaks = data$Month_Number) + 
  labs(x = "No.Month", y = "Monthly Total", title = "Monthly: time vs letters(Jail)")


## Date: Time VS Count -- Prison
data <- read.csv('/Users/apple/Desktop/week8/count_prison_weeklytotal.csv')
data$start_date <- as.Date(data$start_date, format="%Y/%m/%d")
ggplot(data, aes(x=start_date, y=total)) +
  geom_line() +
  scale_x_date(date_breaks = "2 month", date_labels = "%Y/%m/%d") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) + 
  xlab("Start Date") +
  ylab("Total") +
  ggtitle("time vs count(Prison)")

## No.Week: Time VS Count -- Prison
data <- read.csv('/Users/apple/Desktop/week8/count_prison.csv')
data$Week_Number <- factor(data$Week_Number, levels = unique(data$Week_Number))
p <- ggplot(data, aes(x = Week_Number, y = total, group = 1)) +  
  geom_line() + 
  geom_point() +  
  xlab("No. Week") + 
  ylab("Total") +
  ggtitle("Weekly: time vs count (Prison)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
ggsave("/Users/apple/Desktop/plots/W_timeVScount(Prison).png", plot = p, width = 10, height = 6)

## No.Month: Time VS Count -- Prison
data <- read.csv("/Users/apple/Desktop/week8/count_prison.csv")
data$Month_Number <- as.numeric(gsub("Month ", "", data$Month_Number))
data$month_total <- as.numeric(data$month_total)
ggplot(data, aes(x = Month_Number, y = month_total)) +
  geom_line() +
  geom_point() +
  theme_minimal() +
  scale_x_continuous(breaks = data$Month_Number) + 
  labs(x = "No.Month", y = "Monthly Total", title = "Monthly: time vs count(Prison)")

## Date: Time VS Count -- Jail
data <- read.csv('/Users/apple/Desktop/week8/count_jail_weeklytotal.csv')
data$start_date <- as.Date(data$start_date, format="%Y/%m/%d")
ggplot(data, aes(x=start_date, y=total)) +
  geom_line() +
  scale_x_date(date_breaks = "1 month", date_labels = "%Y/%m/%d") + 
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) + 
  xlab("Start Date") +
  ylab("Total") +
  ggtitle("time vs count(Jail)")

## No.Week: Time VS Count -- Jail
data <- read.csv('/Users/apple/Desktop/week8/count_jail.csv')
data$Week_Number <- factor(data$Week_Number, levels = unique(data$Week_Number))
ggplot(data, aes(x = Week_Number, y = total, group = 1)) +  
  geom_line() + 
  geom_point() +  
  xlab("No. Week") + 
  ylab("Total") +
  ggtitle("Weekly: time vs count (Jail)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

## No.Month: Time VS Count -- Jail
data <- read.csv("/Users/apple/Desktop/week8/count_jail.csv")
data$Month_Number <- as.numeric(gsub("Month ", "", data$Month_Number))
data$month_total <- as.numeric(data$month_total)
ggplot(data, aes(x = Month_Number, y = month_total)) +
  geom_line() +
  geom_point() +
  theme_minimal() +
  scale_x_continuous(breaks = data$Month_Number) + 
  labs(x = "No.Month", y = "Monthly Total", title = "Monthly: time vs count(Jail)")


## No.Week: Time VS positive ratio --Prison
data <- read.csv('/Users/apple/Desktop/week8/new_weekly_ratio_prison.csv')
data$Week_Number <- as.numeric(gsub("Week ", "", data$Week_Number))
min_ratio <- min(data$positive_ratio, na.rm = TRUE)
max_ratio <- max(data$positive_ratio, na.rm = TRUE)
ggplot(data, aes(x = Week_Number, y = positive_ratio)) +
  geom_line() + 
  geom_point() + 
  scale_y_continuous(limits = c(min_ratio, max_ratio), breaks = seq(min_ratio, max_ratio, length.out = 5)) +
  xlab("No.Week") + 
  ylab("Positive_Ratio") +
  ggtitle("Weekly: time vs positive_ratio(Prison)")


## No.Week: Time VS negetive ratio --Prison
data <- read.csv('/Users/apple/Desktop/week8/new_weekly_ratio_prison.csv')
data$Week_Number <- as.numeric(gsub("Week ", "", data$Week_Number))
min_ratio <- min(data$negative_ratio, na.rm = TRUE)
max_ratio <- max(data$negative_ratio, na.rm = TRUE)
ggplot(data, aes(x = Week_Number, y = negative_ratio)) +
  geom_line() + 
  geom_point() + 
  scale_y_continuous(limits = c(min_ratio, max_ratio), breaks = seq(min_ratio, max_ratio, length.out = 5)) +
  xlab("No.Week") + 
  ylab("Negative_Ratio") +
  ggtitle("Weekly: time vs negative_ratio(Prison)")

## No.Week: Time VS positive ratio -- Jail
data <- read.csv('/Users/apple/Desktop/week8/new_weekly_ratio_jail.csv')
data$Week_Number <- as.numeric(gsub("Week ", "", data$Week_Number))
min_ratio <- min(data$positive_ratio, na.rm = TRUE)
max_ratio <- max(data$positive_ratio, na.rm = TRUE)
ggplot(data, aes(x = Week_Number, y = positive_ratio)) +
  geom_line() + 
  geom_point() + 
  scale_y_continuous(limits = c(min_ratio, max_ratio), breaks = seq(min_ratio, max_ratio, length.out = 5)) +
  xlab("No.Week") + 
  ylab("Positive_Ratio") +
  ggtitle("Weekly: time vs positive_ratio(Jail)")

## No.Week: Time VS negetive ratio --Jail
data <- read.csv('/Users/apple/Desktop/week8/new_weekly_ratio_jail.csv')
data$Week_Number <- as.numeric(gsub("Week ", "", data$Week_Number))
min_ratio <- min(data$negative_ratio, na.rm = TRUE)
max_ratio <- max(data$negative_ratio, na.rm = TRUE)
ggplot(data, aes(x = Week_Number, y = negative_ratio)) +
  geom_line() + 
  geom_point() + 
  scale_y_continuous(limits = c(min_ratio, max_ratio), breaks = seq(min_ratio, max_ratio, length.out = 5)) +
  xlab("No.Week") + 
  ylab("Negative_Ratio") +
  ggtitle("Weekly: time vs negative_ratio(Jail)")









