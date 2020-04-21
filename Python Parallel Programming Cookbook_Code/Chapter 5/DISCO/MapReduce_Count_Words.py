from disco.core import Job, result_iterator

def map(line, params):
    import string
    for word in line.split():
        strippedWord = word.translate\
                       (string.maketrans("",""), string.punctuation)
        yield strippedWord, 1
        
def reduce(iter, params):
    from disco.util import kvgroup
    for word, counts in kvgroup(sorted(iter)):
        yield word, sum(counts)
        
if __name__ == '__main__':
    job = Job().run(input="There are known knowns.\
                           These are things we know that we know.\
                           There are known unknowns. \
                           That is to say,\
                           there are things that \
                           we know we do not know.\
                           But there are also unknown unknowns.\
                           There are things \
                           we do not know we don't know",
                    map=map,
                    reduce=reduce)

    
    sort_in_numerical_order =\
                            open('SortNumerical.txt', 'w')
    sort_in_alpbabetically_order = \
                                 open('SortAlphabetical.txt', 'w')
    
    wordCount = []
    for word, count in \
        result_iterator(job.wait(show=True)):
        sort_in_alpbabetically_order.write('%s \t %d\n' %
                      (str(word), int(count)) )
        wordCount.append((word,count))

    sortedWordCount =sorted(wordCount, \
                            key=lambda count: count[1],\
                            reverse=True)
    
    for word, count in sortedWordCount:
        sort_in_numerical_order.write('%s \t %d\n'\
                                      % (str(word), int(count)) )
        
    sort_in_alpbabetically_order.close()
    sort_in_numerical_order.close()

    
   
    
