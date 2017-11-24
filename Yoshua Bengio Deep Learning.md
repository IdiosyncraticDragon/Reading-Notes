# Deep learning
> author: Ian Goodfellow and Yoshua Bengio and Aaron Courville
> url: http://www.deeplearningbook.org/

## Chapter 10: Sequence modeling: recurrent and recursive nets

主要是些介绍性的内容，比较有价值的是关于back-propagation through time (BPTT)算法的说明。

BPTT的关键在于，通过unroll将rnn展开成计算图，将每个输出的-logy作为loss（在输出是softmax的情况下，这相当于是联合likelihood的negative loss结果），loss之和为总loss，然后逐个对不同时间片上的参数求gradient，每个参数的gradient之和为这个参数的gradient。
