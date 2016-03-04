library(ggplot2)
total <- read.table("bench_output.tsv", header=TRUE, sep='\t')
sorted <- subset(total, total$algorithm=="SortedListSet")
unsorted <- subset(total, total$algorithm=="UnsortedListSet")
# Time(s) to time(milliseconds)
total$time <- total$time * 1000

# Color palette
cbPalette <- c("#ff9cb0", "#ff2450", "#86d8d6", "#009a96")
cbPalette_insertion <- c(cbPalette[3:4])
cbPalette_contains <- c(cbPalette[1:2])

insertion_sorted <- subset(sorted, sorted$operation=="insertion_random")
insertion_sorted_nonrandom <- subset(sorted, sorted$operation=="insertion_nonrandom")
insertion_unsorted <- subset(unsorted, unsorted$operation=="insertion_random")
insertion_unsorted_nonrandom <- subset(unsorted, unsorted$operation=="insertion_nonrandom")
insertion <- rbind(insertion_unsorted, insertion_unsorted_nonrandom,
                   insertion_sorted, insertion_sorted_nonrandom)
insertion$time <- insertion$time*1000

contains_sorted <- subset(sorted, sorted$operation=="contains_random")
contains_sorted_nonrandom <- subset(sorted, sorted$operation=="contains_nonrandom")
contains_unsorted <- subset(unsorted, unsorted$operation=="contains_random")
contains_unsorted_nonrandom <- subset(unsorted, unsorted$operation=="contains_nonrandom")
contains <- rbind(contains_unsorted, contains_unsorted_nonrandom,
                   contains_sorted, contains_sorted_nonrandom)
contains$time <- contains$time*1000

# For plot with the entire data.
ggplot(total, aes(x = as.character(log2(n_size)), y = log2(time))) +
  geom_boxplot(aes(colour = operation), outlier.size=0.7) +
  facet_wrap(~ algorithm) +
  scale_x_discrete(limits=c("4", "8", "12", "16")) + 
  ylab("log2 of time (milliseconds)") +
  xlab("log2 of n_size") +
  ggtitle("Time Taken for Each Operation\n") + 
  scale_colour_manual(values=cbPalette)

# For plotting just the insertion data.
ggplot(insertion, aes(x = as.character(log2(n_size)), y = log2(time))) +
  geom_boxplot(aes(colour = operation), outlier.size=0.7) +
  facet_wrap(~ algorithm) +
  scale_x_discrete(limits=c("4", "8", "12", "16")) + 
  ylab("log2 of time (milliseconds)") +
  xlab("log2 of n_size") +
  ggtitle("Time Taken for Insertion\n") +  
  scale_colour_manual(values=cbPalette_insertion)

# For plotting just the contains data.
ggplot(contains, aes(x = as.character(log2(n_size)), y = log2(time))) +
  geom_boxplot(aes(colour = operation), outlier.size=0.5) +
  facet_wrap(~ algorithm) +
  scale_x_discrete(limits=c("4", "8", "12", "16")) + 
  ylab("log2 of time (milliseconds)") +
  xlab("log2 of n_size") +
  ggtitle("Time Taken for Checking Containment\n") + 
  scale_colour_manual(values=cbPalette_contains)

# Removing outliers.
contains_ordered <- contains[order(contains$time, decreasing=TRUE), ]
contains_ordered_nooutlier <- contains_ordered[-1,]
contains_ordered_nooutlier <- contains_ordered_nooutlier[-1,]

# For plotting contains data without outliers.
ggplot(contains_ordered_nooutlier, aes(x = as.character(log2(n_size)), y = log2(time))) +
  geom_boxplot(aes(colour = operation), outlier.size=0.5) +
  facet_wrap(~ algorithm) +
  scale_x_discrete(limits=c("4", "8", "12", "16")) + 
  ylab("log2 of time (milliseconds)") +
  xlab("log2 of n_size") +
  ggtitle("Time Taken for Checking Containment\nWithout Outliers") + 
  scale_colour_manual(values=cbPalette_contains)