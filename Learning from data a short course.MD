# Learning from data: a short course
> Yaser S. Abu-Mostafa, Pasadena, California. Malik Magdon-Ismail, Troy, New York. Hsuan-Tien Lin, Taipei, Taiwan. March, 2012.4

## Chapter 1: The Learning Problem

### Notes
- Learning  on data is used in situations where we don't have an analytic solution, but we do have data that we can use to construct an empirical solu­tion
- The hypothesis set and learning algorithm are referred to informally as the learning model.
- How could a limited data reveal enough information to pin down the entire target function?
- Dose the training data set tell us anything outside of it? If the answer is yes, then we have learned something, otherwise, we can conclude the learning is not feasible.
- For training data set D, generally, if there is something certain about target function outside D, no!if there is something likely about target function outside D, yes!

## Chapter 2: Training versus testing

Two much math, need reading book for notes

## Chapter 3： The Linear Model
SGD: That is 'on average' the minimization proceeds in the right direction, but is a bit wiggly.(The expectation is the same as GD).

## Chapter 4: overfitting
Overfitting is the phenomenon where fitting the observed facts (data) well no longer indicates that we will get a decent out-of-sample error, and may actually lead to the opposite effect.
A typical overfitting scenario, in which a complex model uses its additional degrees of freedom to 'learn' the noise.
To overfitting, what matters is how the model complexity matches the quantity and quality of the data we have, not how it matches the target function.
Regularization is a way to combat overfitting, it constrains the learning algorithm to improve out-of-sample error, especally when noise is present.
From the bias-var view of model, by constraining the learning algorithm to select 'simpler' hypotheses from H, we sacrifice a little bias for a significant gain in var.
