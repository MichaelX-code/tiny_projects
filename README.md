# tiny_projects
Just a space to store my tiny projects... Hopefully somebody will enjoy them.

---
## Complex Fibonacci numbers

First of all, it's not my idea. It was taken from [Matt Parker's video](https://www.youtube.com/watch?v=ghxQA3vvhsk).
#### So, what the hell is it?
- We all know what Fibonacci numbers are. It is a sequence of numbers where every number equals the sum of two previous numbers:  `0, 1, 1, 2, 3, 5, 8, 13, ...` and so on.
- But... Why do we start with *0* and *1*? What if want to put a number before? Let's do that! We need a number which will give *1* if we add *0* to it. _It's *1*_. Ok, let's do one more. `x + 1 = 0`. _It's *-1*_. So, what will we get if we continue? This:
`... -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, ...`
- Now we know every *n*th element of Fibonacci sequence where *n* - any integer. To go beyond integers  we should use Binet's formula.
- Now, we should be able to calculate for any decimal *n*. But as you can see, *-1 / golden ratio* is negative, so, if you raise it to a fractional power you will get a complex result. Now, we done! Just draw a graph on a complex plane to see the beauty of complex numbers. _And yeah, I know... You should be a real nerd to call the graphic beautiful_.
