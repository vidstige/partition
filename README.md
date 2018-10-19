# partition
Partitions a list according to some discrete ordering, e.g.

    wheel < numpy
    numpy < scikit

Then using an input like this

    scikit
    numpy
    more-stuff
    wheel

it can partition it into three parts

    ['wheel']
    ['numpy']
    ['scikit', 'more-stuff']

Returns a sequence of list, with the minimal number of 
parts needed to satisfy all conditions.
