''' Infinite Iterators

The built-in function iter() can be called with two arguments 
where the first argument must be a callable object (function) and second is the sentinel. 
The iterator calls this function until the returned value is equal to the sentinel'''




int()
inf = iter(int,1)
next(inf)
next(inf)

