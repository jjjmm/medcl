x <- data.frame(read.csv("C:/Users/mensejev/ttu/dip/medcl/data/df_90p_80p_filled.csv", header = T))[,-1]
d  <- as.matrix(daisy(x, metric="gower"))
print(d) 

#hc
hc <- hclust(dist(d), "ward")
print(hc)
plot(hc)

#db-scan
db = dbscan(dist(d), 0.15, MinPts = 1, scale = FALSE, 
       method = 'dist')
plot(db, d, main = "DBSCAN", frame = FALSE)