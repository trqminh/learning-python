+ Algorithm idea:
- when you want to predict an test point label, choose k nearest neighbors of that point in
the training set, then vote for the label from those k
- There are some kind of vote:
+ choose the most appear label in those k
+ in k point, the nearer has the bigger weight

- Advantage:
+ No need for training :(((
+ Easy to predict new test point
+ ...

- Disadvantage:
+ noise when k is small
+ Basically, all the compute in the test session, and the compute base on distance
so it can be slow when the dimension is high.
