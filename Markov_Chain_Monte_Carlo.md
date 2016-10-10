# Markov Chain Monte Carlo (MCMC)
>Source link: https://nicercode.github.io/guides/mcmc/

>Source link: http://mp.weixin.qq.com/s?__biz=MzA5ODUxOTA5Mg==&mid=2652549929&idx=1&sn=b774997faf139ddba296cdc1cb171d81&scene=2&srcid=0812Gcot4umIh53aGHZKKgP1&from=timeline&isappinstalled=0#wechat_redirect

## What's the purpose
__MCMC is simply an algorithm for sampling from a distribution.__ It’s only one of many algorithms for doing so.

 It is a type of “Monte Carlo” (i.e., a random) method that uses “Markov chains” .

 Monte Carlo 抽样计算随机变量的期望值：X 表示随即变量，服从概率分布 p(x), 那么要计算 f(x) 的期望，只需要我们不停从 p(x) 中抽样xi，然后对这些f（xi）取平均即可近似f(x)的期望。

## Why it works
原理是马氏链的收敛定律。

## How it works
