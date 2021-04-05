## usd_cpp_utilities

A simple Rez package with miscellaneous, optimized functions for working
with USD.

The package is relatively simple at the moment and will only add new
items as-needed. The 1.0.0 release can be considered as a "Hello World!"
for a basic C++, USD, Python binding library.

## Configuration
### USD_CPP_UTILITIES_SCALE_UPPER_BOUND
The value used to detect "bad" scale values. Default: 0.0001.  Any scale
value whose distance to zero is on-or-less than this value is considered
bad. (Small, negative values are also considered bad).


## TODO
- Make sure there's a GPU performance test
- Add CUDA support, via ephemerals
- Optimize it to be as fast as possible

- Make sure that I can include it into another Rez package
    - Get .h included as a separate folder (so it can be importable)

- Make sure passing just a list / set / container / etc to the function is valid

Possibly useful links

https://stackoverflow.com/a/15940413/3626104
https://www.boost.org/doc/libs/1_53_0/libs/python/doc/v2/faq.html#custom_string
https://stackoverflow.com/questions/3761391/boostpython-python-list-to-stdvector

- Do the miscellaneous TODO notes
- Add C++ linters
- Make a 1.0.0 release
