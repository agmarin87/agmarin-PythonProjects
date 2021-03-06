This project is written to understand the meaning of the mean squared displacement (MSD) and how the different parameters and methods can influence to obtain such plot.
As a brief definition for those who are not very familiar with the MSD. Basically it gives information of how far the particle or protein under study has moved during some time.

The code generates a “n” number of 3D array of “N” random-generated points. It is possible to change the number of arrays (trajectories) and the number of points for each trajectory.

After generating the array, the code performs a loop to calculate the MSD through two methods: 1) following the equation MSD=(x(t)-x_0 )^2, and 2) following the explanation found in: https://stackoverflow.com/questions/34222272/computing-mean-square-displacement-using-python-and-fft, and then it averages the MSD values for all trajectories.

The loop stores all the generated data in a list called “alldf”. Finally, it plots all trajectories and the calculated MSD.
Example of results obtained is [this one](https://github.com/agmarin87/agmarin-PythonProjects/blob/master/MSD%20project/Trajectory%20example.png) where a trajectory is plotted and [this figure](https://github.com/agmarin87/agmarin-PythonProjects/blob/master/MSD%20project/MSD%20calculation%20example.png) where the MSD is plotted following both methods.

For any questions or recommendations, please do not hesitate to contact me ;)
