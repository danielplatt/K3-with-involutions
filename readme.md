# quartic-k3-with-involution
## What is this?
In this repository we provide the code that was used in the writing of the article *D. Festi, W. Nijgh, D. Platt: K3 surfaces with two involutions and low Picard rank*.
The article exhibits examples of K3 surfaces with two involutions and Picard rank 2, which is the lowest Picard rank possible.
All code is written in [Magma (link)](magma.maths.usyd.edu.au).

## How to use this repository?
Run the code `Quarticswithinvolution.txt` to generate the quartic surface from the article and check computationally that it has Picard rank at most 2. 
(It is shown in the article that this implies that the quartic surface has Picard rank *equal* to 2.)

TODO: (1) Make this file runnable (2) Is everything under `// Original code and comments for random K3 by Ronald:` in that file not needed anymore? 

Run the code `EquationsInvolution` to get the equation of the involution on the quartic from the first file, and to compute the equations of the K3 surface viewed as an intersection of an intersection of three quadrics.