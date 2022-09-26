# Tasks

## Binary Numbers

In the file `src/binary.py`, write the following recursive functions:

1. `den2bin(d)` which takes an integer `d` and converts it to a binary string by first checking whether the number is even or odd (thereby determining the least significant bit) and appending the corresponding bit to the binary representation of `d div 2`.
2. `bin2den(b)` which takes a string `b` representing a binary number and converts it to denary by adding the value of the least significant bit to double the value of the binary string excluding the LSB. 

*It is not acceptable to get results such as `den2bin(10) == "01010"` with leading zeros. Hint: You may need more than one base case.*

## Maths

In the file `src/maths.py`, write the following recursive functions:

1. `factorial(n)` which computes the factorial $n!$ of `n` using the recursive definition of the factorial:
$$n! = \begin{cases}1 & \text{if}\quad n = 0 \\ n \times (n-1)! &\text{if}\quad n \geq 1\end{cases}$$
2. `gcd(a, b)` which computes the greatest common divisor of two numbers `a` and `b` using Euclid's algorithm:
$$\gcd(a,b) = \begin{cases} b & \text{if}\quad a\text{ mod }b = 0 \\ \gcd(b, a\text{ mod }b) &\text{otherwise}\end{cases}$$

## Mystery Function

1. In the file `src/mystery.py`, write a function `qs(l)` which takes a list of numbers, `l` and applies the following algorithm:
    ```vba
    function qs(l)
        if len(l) == 0 then
            return l
        end if
        p = l[0]
        s = []
        g = []
        for i = 1 to len(l)-1
            x = l[i]
            if x <= p then
                s.append(x)
            else
                g.append(x)
            end if
        next i
        ss = qs(s)
        gs = qs(g)
        return concatenate(ss, [p], gs)
    end function
    ```
    Here, `concatenate` means creating a list which contains the elements of the list parameters. For instance, `concatenate([1,2,3], [4,5,6], [7,8,9])` should return `[1,2,3,4,5,6,7,8,9]`.

2. Complete the trace table in the file `trace_mystery.xlsx`.
3. What purpose does the function `qs` serve?
    * **Answer**: ........................................

*Questions 2 and 3 are not automatically graded, I will simply look at them after you make a commit.*.

## Staircases
*This section is harder than the others. View it as a Challenge (capital "c"). There are no automatic tests for this section so as to not show your submission as failing if you do not attempt to solve it or find yourself unable to. You can verify your solution attempts by using the table in `paths.txt`* 

When I go to drink tea after school, I take the tube to Camden Town. At Camden Town station, I walk up the staircase, which has 96 steps in total. At any given point, I can take 1, 2 or 3 steps at once. 

The below shows the different paths I can take to get to the fifth step. As you can see, there are 13 such paths:

|   | Path 1 | Path 2 | Path 3 | Path 4 | Path 5 | Path 6 | Path 7 | Path 8 | Path 9 | Path 10 | Path 11 | Path 12 | Path 13 |
|--:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:-------:|:-------:|:-------:|:-------:|
**Step 5** | $\bullet$ | $\bullet$ | $\bullet$ |$\bullet$  | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ | 
**Step 4** | $\bullet$ | $\bullet$ | $\bullet$ |$\bullet$  | $\bullet$ | $\bullet$ | $\bullet$ |           |           |           |           |           |           |
**Step 3** | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ |           |           |           | $\bullet$ | $\bullet$ | $\bullet$ | $\bullet$ |           |           |
**Step 2** | $\bullet$ | $\bullet$ |           |           | $\bullet$ | $\bullet$ |           | $\bullet$ | $\bullet$ |           |           | $\bullet$ | $\bullet$ |
**Step 1** | $\bullet$ |           | $\bullet$ |           | $\bullet$ |           | $\bullet$ | $\bullet$ |           | $\bullet$ |           | $\bullet$ |           |

In the above table, a $\bullet$ in a particular row means that in that particular path, I step on that step while a blank cell means that I step over that step in this path. 

How many paths are there to step 4?

How many paths are there to step 3?

How many paths are there to step 2?

How does the number of paths to step 5 relate to the three numbers above? Can you explain why?

In `src/staircases.py`, write a recursive function `recursive_paths(n)` which calculates the number of paths I can take to step `n`. 

Try using your function to calculate the number of paths that I can follow to reach ground level at Camden Town station (step 96). It is highly unlikely that you will have the patience to run it to completion: my Surface Pro took hours to run a naïve recursive algorithm. 

Let's look at two alternative ways to make this algorithm more efficient. 

### Memoisation
The reason for the naïve recursion to be so slow is that a lot of the work is repeated a lot of times, as we saw with the Fibonacci numbers. While in "pure" recursion, each recursive call is independent of the others, it makes little sense to make the same recursive calls over and over and over again. We can therefore memorise what we have computed before. To do this, we'll exploit that lists (arrays in iGCSE terminology) in Python are passed by *by reference*. If you don't know what this means in general, please review the material on suroutines and parameter passing. 

We start by  modifying our existing function to use a second parameter, a list called `cache`. `cache[i] == 0` will indicate that we do not yet know the number of paths to step `i`. Now, at the beginning of the function, check whether `cache[n]` is `0`. If so, we have to follow our recursion, but we pass the same list cache into any recursive calls. As the recursive calls (and their recursive calls) return, the values will start populating the list `cache` because `cache` is passed by reference in Python. When we have calculated the value of `recursive_paths(n)`, before returning it, set the value of `cache[n]` to the number you just calculated. 

If the entry `cache[n]` is not `0`, you can simply look up what the value is and return that, because clearly, at some point, you have already calculated `recursive_paths(n)`, saving you some recursive calls (and a lot of time!).

### Making The Function Iterative

What if instead of the staircase at Camden Town Station I wanted to walk up the Niesen-Treppenlauf staircase in Switzerland, which has the most steps in the world? 

There are 11,674 steps in it. Try calculating the number of paths for that staircase. You should get a stack overflow error. :(

Try rewriting the function in an iterative way! *Hint: try to remember (or look up) how the Fibonacci function is typically made iterative!*