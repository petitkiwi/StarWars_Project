# StarWars_Project
*31/03/2022*

In the outer rim, an unidentified satellite has been spotted in the sky around the planet Tatouine moving in high orbit at very high constant speed. The analysts of the alliance are on the case. This satellite does not respond to any injunction; the first problem is to avoid any collision between this satellite and the fleet of satellites of the alliance already in operation. But above all, it is to prepare for the imminent destruction of the satellite by a pulsed plasma shot. Unfortunately, on the ground, the energy necessary for its atomization is too limited and only one shot will be possible.
You will have to prepare this shot as well as possible with the few means available. The satellite follows an orbit defined as follows:

x(t) = p1 × sin(p2 × t + p3)
y(t) = p4 × sin(p5 × t + p6)

With x(t) and y(t) the position of the satellite at a given time t. The pi (i ∈ [1; 6]) are the parameters that will have to be discovered in order to be able to anticipate as well as possible the movements of the satellite at a given time t (t ∈ [0; 2π]).
With the help of laser scopes, the rebellion was able to record with a certain accuracy the position of the satellite at several moments. This list is provided in the file **position_sample.csv**.

In order to succeed in the mission, this project deploys a general algorithm able to find a good combination of parameters that best explains the satellite trajectory.
