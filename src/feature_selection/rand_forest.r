# Load library
library(randomForest)
## Read data
#termCrosssell<-read.csv(file="C:/Users/mensejev/Downloads/bank/bank.csv",header = T, sep=";")
termCrosssell<-read.csv(file="C:/Users/mensejev/ttu/dip/fpin.csv",header = T, sep=",")
names(termCrosssell)

varNames <- names(termCrosssell)
# Exclude ID or Response variable
varNames <- varNames[!varNames %in% c("Reoperatsioon roSaabumine", "J2relkontroll.id")]
# add + sign between exploratory variables
varNames1 <- paste(varNames, collapse = "+")
# Add response variable and convert to a formula object
rf.form <- as.formula(paste("Reoperatsioon roSaabumine", varNames1, sep = " ~ "))

print(rf.form)

cross.sell.rf <- randomForest(rf.form,
                              termCrosssell,
                              ntree=100,
                              importance=T)

plot(cross.sell.rf)

varImpPlot(cross.sell.rf,
           sort = T,
           main="Variable Importance",
           n.var=10)