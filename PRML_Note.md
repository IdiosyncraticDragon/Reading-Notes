# Pattern Recognition and Machine Learning
> Author:Christopher M. Bishop
> Year: 2006

## Introduction
- the field of pattern recognition is concerned with the automatic discovery of regularities in data through the use of computer algorithms and with the use of these regularities to take actions such as classifying the data into different categories.
- the ability to categorize correctly new examples that differ from those used in training is known as generalization.
- the original input variables are typically preprocessed to Transform them into some new space of variables where, it is hoped, the pattern recognition problem will be easier to solve.
- pre-processing will also be preformed in order to speed up computation.
- some kinds of pre-processing represent a form of dimensionality reduction.
- functions, such as polynomial, which are linear in the unkown parameters have important properties and are called linear models.
- root-mean-square error (RMS)

Overfitting
- intuitively, over-fitting means that the more flexible parts of the model are incresingly tuned to the random noise on the target values.
- one technique which is often used to control the over-fitting phenomenon in such case is that of regularization, which involves adding a penalty term to the error function.
- 用权值来计算regularization项的时候，bias的权值一般是不算进去的，因为如果算进去了，就会导致结果依赖于目标变量的原点位置（就不是bias了）
- the particular case of a quadratic regularizer is called ridge regression. In the context of nueral networks, this approach is called weight decay.

Probability Theory
- prior probability p(a) is the probability available before we observe the identity of a.
- posterior probability p(a|f) of a is the probability obtained after we have observed f.
- the average value of a some function f(x) under a probability distribution p(x) is called the expection of f(x).

- The maximum of a distribution is known as its mode. For Gaussian, the mode coincides with the mean.
- Data points that are drawn independently from the same distribution are said to be independent and identically distributed, which is often abbreviated to i.i.d
- It is called marginal probability, because it is obtained by marginalizing, or summing out, the other variables
-  In practice, it is more convenient to maximize the log of the likelihood function. 1)(可以换). the logarithm is a monotonically increasing function of its argument, maximization of the log of a function is equivalent to maximization of the function itself. 2)(换了有啥好处). it simplifies the subsequent mathematical analysis and also helps numerically because the product of a large number of small probabilities can easily underflow the numerical precision of the computer, and this is resolved by computing instead the sum of the log probabilities.
- 当通过调整均值和方差来最大化高斯分布的likelihood值时，应该是要同时调整这两个值的，但是通过对高斯分布求ln后发现，这两个值互不相干，所以可以分别调整。（非常好的性质）
- the significant limitations of the maximum likelihood approach for univariate Gaussian distribution: This approach underestimates （biased variance, need divide by (N-1) to be the unbiased one, page 27~28） the variance of the distribution. This is an example of a phenomenon called bias and is related to the problem of over-fitting.  
- Note that the bias of the maximum likelihood solution becomes less significant as the number N of data points increases, and in the limit N to infinite the maximum likelihood solution for the variance equals the true variance of the distribution that generated the data. In practice, for anything other than small N, this bias will not prove to be a serious problem.
- In fact, as we shall see, the issue of bias in maximum likelihood lies at the root of the over-fitting problem.
- 高斯模型有些性质非常好，当以高斯建模likelihood函数的时候，使用maximum likelihood estimator进行优化时，可以利用均值方差可以分布调节的特性来简化求解过程，实际上这会转化成最小化 sum-of-squares error函数（只要在建模时均值和方差无不相关）；而在给定参数的先验的情况下，用maximum posterior (MAP方法)来最大化参数的后验（即给定数据情况下，参数的可能性），从而求解参数，因为参数后验正比于参数先验与参数的likelihood函数的乘积，当先验和likelihood都是高斯时，定义良好的情况下，这可以转成最小化带正则想sum-of-squares函数。（页29~30）

Model selection
- one major drawback of cross-validation is the number of training runs that must be performed is increased by a factor of S (S-folder cross-validation, separate the data into S buckets), this can prove problematic for models in which the training is itself computationally expensive. A further problem with techniques such as cross-validation that use separate data to assess performance is that we might have multiple complexity parameters for a single model(for instances, several regularization parameters), exploring combinations of settings for such parameters could, in the worst case, require a number of training runs that is exponential in the number of parameters.

The curse of dimensionality
- although the curse of dimensionality certainly raises important issuses for pattern recognition apllications, it does not prevent us from finding effective techniques applicable to high-dimensional spaces. The reasons for this are twofold.
  - First, real data will often be confined to a region of the space having lower effective dimensionality, and in particular the directions over which important variantions in the target variables occur may be so confined.
  - Second, real data will typically exhibit some smoothness properties (at least locally) so that for the most part small changes in the input variables will produce small changes in the target variables, and so we can exploit local interpolation-like techniques to allow us to make rpedictions of the target variables for new values of the input variables.

## Chapter 2 Probability distributions

### Phrase
```
As well as being of great interest in their own right.
```

### Basic concepts
__density estimation__: Model the probability distribution $$p(x)$$ of a random varable x, given a finite set $$x_1,...,x_N$$ of observations

__parametric distributions__: so-called because they are governed by a small number of adaptive parameters, such as the mean and variance in the case of a Gaussian for example

__正交矩阵（orthonormal matrix）__: n阶方阵A为正交矩阵的充要条件为A的行（列）向量组为正交单位向量组，即行（列）向量组是n维向量空间的一组基。

__正交单位向量组__: 见书籍80页 2.46,2.47式．

__antisymmetric matrix__:又称反对称矩阵或是斜对称矩阵，其转置矩阵和自身的加法逆元相等．既：AT = −A

### Gaussian distribution
