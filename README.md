# Recursion

Recursion is a programming technique that many people find difficult to wrap their heads around at first. However, once you have succeeded in doing so, it is often a more intutive way of solving a problem as well as an elegant solution. 

It relies on the basic idea that you can write an algorithm that follows three steps:
1. break the given problem into two or more chunks, unless you can solve the problem easily immediately.
2. apply this algorithm to at least one of the smaller chunks that can be viewed as smaller versions of the same problem
3. combine the solutions to the smaller problems to get an overall solution. 

## Self-similar Problems

While *technically*, recursion can solve any computational problems that are solveable with the other techniques we have so far discussed, it is often a convoluted and somewhat forced way of doing so unless the problem particularly lends itself to applying recursion. 

The core question one needs to ask oneself when writing a recursive algorithm to solve a problem is the following:

*Can I break down the given problem so that I get a smaller version of itself out of one of the parts?*

If this is the case, then you can assume that you can solve the smaller version of the problem and simply focus on how you go from the solution of the smaller problem to a solution for the overall problem together with any of the other pieces you got from breaking the problem down. 

Here is an example that illustrates the way recursion can be pplied to solve problems:

### Russian Nesting Dolls
Russian Nesting Dolls are wood figurines that you can unscrew, open up and retrieve a slightly smaller doll from within. The innermost doll won't let itself be opened up, though. 

If now you wanted to count how many dolls there are when you are holding a nested doll, as soon as you open up the outermost layer, you have reached a situation in which you are holding an empty doll and a smaller nested doll. To count the overall number of dolls, you need to count the number of dolls in the smaller nested one and add the empty doll you just opened up. 

However, if you found that that smaller nesting doll had a post-it stuck on it saying "this doll has five layers", you wouldn't need to open it up to determine that the overall number of dolls is 6. Once you see the post-it saying that there are five more layers, you no longer care about *how* you arrived at the overall number of layers: all that is important is that you figured out the number of layers in the interior doll *somehow*, and can use this knowledge to solve your initial problem.

Here is a formulation of how to count the layers of a Russian nesting doll recursively:

1) If you can screw open the doll you see:
    * open the doll up
    * count the layers of the interior doll
    * in total, there are that many dolls plus 1.
2) Else:
    * There is just that doll because there can't be anything hidden inside it; the number of dolls is 1. 

## Base Cases

The above example requires that there is an end to the dolls; there must be a doll somewhere that does not unscrew. 

Effectively, recursion only works if we reach some point at which we can simply... solve the problem at hand after breaking it down far enough. This is what is known as a base case. Usually, base cases are shown in recursive subroutines as if-statements: "If we have reached a/the base case: apply simple solution. Else: apply recursive solution." 

The presence of a base case is one of three conditions that the OCR exam board have to count something as a "recursive routine", so you may be asked "Which of these is a recursive subroutine?": One without base case would not be counted.

These conditions are:
1. The presence of a base case.
2. The routine must make a recursive call.
3. For any given input, the base case must eventually be reached; that is, if some input causes infinite recursion it does not count as a recursive routine.

## Recursion vs Iteration
Recursion is a very powerful programming technique, in that it can be used to solve many problems. In fact, if you had just recursion without iterations, you would still be able to solve all problems you could solve before! In fact, you can rewrite any recursive code to use iteration and vice versa. You are also expected to be able to give advantages and disadvantages of recursion against iteration. Here's a recap:

|  | Recursion | Iteration |
|--:|:--------|:---------|
| **Advantages**   | code often considered easier to follow | tends to be more efficient as work is never duplicated |
| **Disadvantages**| recursive calls may lead to *stack overflow* | typically requires more lines of code |

