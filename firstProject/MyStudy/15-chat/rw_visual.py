import matplotlib.pyplot as plt

from MyStudy.random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_value, rw.y_value, s=15)
plt.show()

