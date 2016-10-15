# Markov Chain Monte Carlo (MCMC)
>Source link: https://nicercode.github.io/guides/mcmc/

>Source link: http://mp.weixin.qq.com/s?__biz=MzA5ODUxOTA5Mg==&mid=2652549929&idx=1&sn=b774997faf139ddba296cdc1cb171d81&scene=2&srcid=0812Gcot4umIh53aGHZKKgP1&from=timeline&isappinstalled=0#wechat_redirect

## What's the purpose
__MCMC is simply an algorithm for sampling from a distribution.__ It’s only one of many algorithms for doing so.

 It is a type of “Monte Carlo” (i.e., a random) method that uses “Markov chains” .

 Monte Carlo 抽样计算随机变量的期望值：X 表示随即变量，服从概率分布 p(x), 那么要计算 f(x) 的期望，只需要我们不停从 p(x) 中抽样xi，然后对这些f（xi）取平均即可近似f(x)的期望。

## Why it works
原理是马氏链的收敛定律。

使用方法是接受-拒绝采样法。

## Markov Process
Markov过程：
一个随机过程如果给定了当前时刻t的值$X_t$, 未来 $X_s (s>t)$的值不受过去的值$X_u (u<t)$的影响就称为是有Markov性。

随机变量的值被称为随机过程所处的状态， 而从状态i转移到j的的条件概率P{X_{n+1}=j|X_n=i}称作改Markov链的一部转移概率。当这一概率与n无关时，称Markov链有平稳转移概率。 通常转移概率构成的矩阵P是一个无穷维的方阵，但因为Markov链的状态总数是有限的，则P就是有限阶的方阵，其阶数正好是状态空间中状态的总数。

## How it works
通过马氏链的细致平稳条件，通过随机的初始状态进行转移，直至稳定。这里的状态是指某种指定的随机分布的状态（比如高斯分布）， 然后头改过稳定下来的随机分布作为盖在待生成分布上方的一个分布，通过不断的接受-拒绝稳定分布中采样的样本，来产生待采样分布中的样本。

## Hints

马尔科夫链是一条随机变量的链，也就是下一个变量值的概率只与上一个变量相关。
