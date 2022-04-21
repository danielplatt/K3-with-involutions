# quartic-k3-with-involution
## What is this?
In this repository we provide the code that was used in the writing of the article *D. Festi, W. Nijgh, D. Platt: K3 surfaces with two involutions and low Picard number*.
The article exhibits examples of K3 surfaces with two involutions and Picard number 2, which is the lowest Picard number possible for a K3 surface that is not a double cover of P^2 branched over a sextic.
All code is written in [Magma (link)](magma.maths.usyd.edu.au).

## How to use this repository?

On a machine that has Magma installed, run in the command line: `magma` and then, once Magma has started, run `load <file>;`, where you replace `<file>` with one of the files from the repository. The runnable Magma files are explained below.

### `ExampleBranchedDoublePlane`

This code computes the Picard number of the double cover of P^2, branched over the sextic defined by the equation `f:=7*x^6+x^5*y-x^4*y^2-9*x^3*y^3+2*x^2*y^4-6*x*y^5+7*y^6+3*x^5*z
    +7*x^4*y*z+6*x^3*y^2*z-4*x^2*y^3*z-4*x*y^4*z+9*y^5*z+2*x^4*z^2
    -4*x^3*y*z^2-6*x^2*y^2*z^2-7*x*y^3*z^2+5*x^2*y*z^3+5*x*y^2*z^3
    -8*y^3*z^3-6*x^2*z^4+5*x*y*z^4+8*y^2*z^4+7*x*z^5-2*y*z^5+z^6`.
This is Example 3.4 from the article.
The program computes the Picard number of the reductions of the K3 surface of primes up to 50. The result of this computation give that modulo 5 and modulo 13 gives upperbound 2. Becuase the values of the ArtinTateFormule do not not differ by a square, this gives an upper bound of 1 for Picard rank of the original complex K3.
As the Picard number of every algebraic K3 is at least 1, this shows that the Picard number of this surface is equal to 1.

### `ExampleNodalK3`

This code computes the Picard number of the blowup of the nodal K3 defined by the equation f4+f3*w+f2*w^2=0 as a subset of P^3, where 
`f2:=3*x^2+9*x*y+9*y^2+7*x*z+8*y*z+8*z^2`,
`f3:=-8*x^3+8*x^2*y-8*x*y^2-5*y^3-9*x^2*z-x*y*z-6*y^2*z+5*x*z^2-9*y*z^2-7*z^3`,
`f4:=-5*x^4+5*x^3*y+4*x^2*y^2+x*y^3-4*x^3*z+8*x^2*y*z-8*x*y^2*z+7*y^3*z+
    +9*x^2*z^2-4*x*y*z^2+2*y^2*z^2-6*x*z^3+3*y*z^3-4*z^4`.
This is example 4.5 from the article.
In the article, the blowup of the nodal quartic is recognised as the double cover of P^2 branched over the sextic `f:=f3^2-4*f2*f4`, and the program computes the Picard number of the K3 surface using this model.
The program computes the Picard number of the reductions of the K3 surface modulo 5 and it is found that this rank is 2, which gives an upper bound for the Picard number.
We also have a lower bound 2, because the exceptional divisor and the hyperplane section are independent divisors, so the Picard number of this K3 surface is equal to 2.

### `ConstructionQuartic`

Use the code `ConstructionQuartic` to generate random quartic surfaces with Picard number at most 2 and an involution coming from a curve C of genus 2 and degree 5. 
(It is shown in the article that this implies that the quartic surface has Picard number *equal* to 2.)
It also gives back the model as a double cover. The function can take quite some time to find an example. 

The code of `ConstructionQuartic2` is an alternative which has the same output as the original function. The difference is that it only checks the upperbound for the reduction mod 2. While it finds less surfaces of Picard number 2, the upside is that the code is way faster!

### `ExampleQuartic`

Run the code `ExampleQuartic` to get the equation of the involution on the quartic which is defined in the article. It also computes the model as double cover of P^2 and the model viewed as an intersection of an intersection of three quadrics.

### `ConstructionK3Degree6`

Use the code `ConstructionK3Degree6` to generate random K3 surfaces of degree 6 in P^4 of Picard number 2 and an involution coming from a curve C of genus 2. It also gives back the model as a double cover.

### `ExampleK3Degree6`

Run the code `ExampleK3Degree6` to get the model as double cover of P^2 of the example in paragraph 8 in the article. It also shows that the Picard number of this surface is 2.
