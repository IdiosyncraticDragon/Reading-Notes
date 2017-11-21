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

Decision Theory
- decision theory discussed in this book is, when combined with prbability theory, to make optimal decisions in situations involving uncertainty.
- One intuitive decision is choosing the class having the higher posterior probability when use Bayes' theorem to make decision.
- The joint probability distribution p(x,t) provides a complete summary of the uncertainty associated with these variables.
- Inference: determination of p(x,t) from a set of training data is an example of inference and is typically a very difficult problem.
- 对于class之间没有重要性区别的分类，我们最小化数据的错分率（minimizing the misclassification rate）使我们的目的；而对于class之间有重要性区别的，则要最小化重要性的期望（minimizing the expected loss）。
- Decision region, boundaries, surface: 对于最小化错分率的问题, we need a rule that assigns each value of x to one of the avaiable classes. Such a rule will divide the input space into regions {1...,k} called decision regions, one for each class. The boundaries between decision regions are called decision boundaries or decision surfaces.
- reject option: In some applications, it will be appropriate to avoid making decisions on the difficult cases in anticipation of a lower error rate on those examples for which a classification decision is made. (which 是修饰those examples的，a classification deicion is made for some examples, these examples are expected to have a lower error, by avoid making decisions on other difficult cases)
- Inference and decision: classification can be viewed as inference stage + decision stage. Inference stage: we use training data to learna model for p(c|x). Decision stage: we use these posterior probabilities p(c|x) to make optimal class assignments
- Discriminant function: An alternative of the view of classification is solving both inference and decision together, by simply learning a function that maps inputs x directly into decisions.
- Three distinct approaches to solve decision problems: generative models, discriminative models and discriminant function.
  - generative models: approaches that explicityly or implicityly model the distribution of inputs as well as outputs (joint distribution) are known as generative models, because by sampling from them it is possible to generate synthetic data points in the input space. A example procedure:
    - solve inference problem of determing the class-conditional densities p(x|C).
    - separately infer the prior class probabilities p(C).
    - use bayes' theorem to find posterior class probabilities p(C|x).
    - use decision theory to find decision regions.
  - discriminative models: approaches that model the posterior probabilites directly are called dicriminative models.
    - solve inference problem of determining the posterior class probability p(C|x)
    - use decision theory to find decision regions
  - discriminant function: direction map the x to y, probabilities play no role. (like softmax is not discriminant function, it just predict probabilities)
- generative model最强最全，可以应用面最广但是需要大量的计算资源才能算出来；discriminative models对于单纯的分类问题来说，最有效率；discriminant functiuon 是不依赖概率的分类方式。

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

## Chapter 5 Neural Networks

### basic concepts

- 'multipayer perceptron' is really a misnomeer, because the model comprises multiple layers of logistic regression models (with continuous nonlinearityies) rather than multiple perceptrons (with discontinuous nonlinearityies).
- Our focus in this chapter is therefore on neural networks as efficient models for statistical pattern recognition.
- a feed-forward architecture ensures that the outputs are deterministic functions of the inputs, in other words to one having no closed directed cycles.
- Neural networks are therefore said to be universal approximators. For example, a two-layer network with linear outputs can uniformly approximate any continuous function on a compact input domain to arbitrary accuracy provided the network has a sufficiently large number of hidden units.
- Weight-space symmetries：One property of feed-forward networks, which will play a role when we consider Bayesian model comparison, is that multiple distinct choices for the weight vector w can all give rise to the same mapping function from inputs to outputs.就是说，在模型空间中，有很多近似的模型。这可以通过一个简单的思想实验验证，对于一个两层权值神经网络，隐藏层的激活函数是tanh，tanh是奇函数；当将所有的权值取反时，tanh的值也会取反，但是因为tanh连向输出的权值也取反了，所以整个输出其实没变，那么对于每个隐藏神经元，所有与它的相连的权值取反都不会对网络造成什么印象，那么对于这个网络结构，它的任意一种权值取值方式都起码有2的M次方（M是隐藏层神经元个数）种同样结果的模型。

- 回归问题用sum-of-squares error作为loss函数，分类问题用交叉熵作为误差函数，其实都是从条件概率之积的negtively log 结果得来的，只是因为不同为题的条件概率建模方式不一样，所以得出的loss函数不一样。

- 问题使用什么样的输出函数和怎么样的loss函数，是要根据问题的建模而来的，目的都是最大化分类随机变量在给定网络参数下的likelihood（一般通过将所有数据上likelihood的乘积转换为negtive log来分析问题）。In summary, there is a natural choice of both output unit activation function and matching error function, according to the type of problem being solved.
  - 对于回归问题，通过假设输出结果与标准结果之间有高斯噪声，我们可以自然的推导出，需要用线性回归生成输出，使用sum-of-square error作为loss函数；
  - 对于不相关的多类分类问题，使用sigmoid生成输出，使用交叉熵作为loss函数；
  - 对于相关多类的分类问题，使用softmax生成输出（以为这个保证输出一个概率分布），使用多类相关交叉熵函数作为loss函数。

- softmax函数有种特性，就是输入的x在全部维度上都加上一个常数的话，softmax的值是不变的，这会导致softmax函数权值空间的一些方向上没有曲率，一般通过加正则项的方法来缓解这个问题。这是因为softmax是借助exp函数对x做变化，而exp对指数的加法可以拆借乘法，因此如果x所有维度加了个常数的话，相当于所有exp项前乘个常数，可以通过softmax的除法消去。

- 对于神经网络模型的权值优化，Because there is clearly no hope of finding an analytical solution to the equation ∇E(w) = 0， we resort to iterative numerical procedures.
- Most techniques involve choosing some initial value w(0) for the weight vector and then moving through weight space in a succession of steps of the form w(τ+1) = w(τ) +Δw(τ). Different algorithms involve different choices for the weight vector update Δw(τ).
