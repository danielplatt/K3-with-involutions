# quartic-k3-with-involution
## What is this?
In this repository we provide the code that was used in the writing of the article *D. Festi, W. Nijgh, D. Platt: K3 surfaces with two involutions and low Picard rank*.
The article exhibits examples of K3 surfaces with two involutions and Picard rank 2, which is the lowest Picard rank possible.
All code is written in [Magma (link)](magma.maths.usyd.edu.au).

## How to use this repository?
Use the code `ConstructionQuartic` to generate random quartic surfaces with Picard rank at most 2 and an involution coming from a curve C of genus 2 and degree 5.
(It is shown in the article that this implies that the quartic surface has Picard rank *equal* to 2.)

Run the code `EquationsInvolution` to get the equation of the involution on the quartic which is defined in the article, and to compute the equations of the K3 surface viewed as an intersection of an intersection of three quadrics.
