# type this (change path) to run this file:
 source("C:/users/mensejev/ttu/dip/medcl/src/r_scripts/data_sort.r")

# remember initial directory
initialdir <- getwd()
setwd("C:/Users/mensejev/ttu/dip/medcl/data/")

# read the data in
med <- read.table("Sulling_data_allstring_v2.csv", header=FALSE, sep=",", fileEncoding="UTF-8")

# count NA values per column
naorder <- apply(med,2,function(x){sum(is.na(x))})
#naorder <- sort(naorder, decreasing=TRUE)
#naorder <- sort(naorder)

# reorder columns by more NA last
#med_sorted <- med[,names(naorder)]

# count NA-s in rows
#rownaorder <- apply(med,1,function(x){sum(is.na(x))})

# reorder rows by more NA last
#med_sorted <-med_sorted[order(rownaorder),]

#write.csv(med_sorted, "Sulling_sorted_by_NA.csv", fileEncoding="UTF-8")

# remove columns where all values are the same
#med_sorted <- med_sorted[sapply(med_sorted, function(x) !is.factor(x) | length(unique(x))>1 )]
#write.csv(med_sorted, "Sulling_sorted_by_NA_allsame_removed.csv", fileEncoding="UTF-8")

# change back to initial directory
setwd(initialdir)
