- algorithm idea:
+ Step 1: init k centroids
+ Step 2: Assign each point to one of k centroid
+ Step 3: Update centroid
+ Step 4: Check that centroid change or not from step 2 to step 3,
if change, back to step 2, other wise finish

- Advantage:
+ Unsupervised learning algorithm
+ Easy to understand


- Disadvantage:
+ Depend on step 1 (init centroid), it can be long to converge, or just get to local minimum
==> run the algorithm more times with different init centroid and choose the best result
+ A cluster inside other cluster (can not seperate)
+ Choose k (elbow method), the elbow in the chart of cost function and number of centroid
