Minimum operations -> intro to dynamic programming

Given an integer N, the task is to obtain N, starting from 1 using minimum number of operations;

    If minimum operations to obtain any number smaller than N is known, then minimum operations to obtain N can be calculated.
    Create the following lookup table:

     dp[i] = Minimum number of operations to obtain i from 1 

    So for any number x, minimum operations required to obtain x can be calculated as:

     dp[x] = min(dp[x-1], dp[x/2], dp[x/3])

