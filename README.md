## Configuration
### USD_CPP_UTILITIES_SCALE_UPPER_BOUND
The value used to detect "bad" scale values. Default: 0.0001.  Any
value does distance to zero is on-or-less than this value is considered
bad. (Small, negative values are also considered bad).


- Make sure there's a GPU performance test
- Add CUDA support, via ephemerals
- Optimize it to be as fast as possible

- Make sure that I can include it into another Rez package
    - Get .h included as a separate folder (so it can be importable)

- Make sure passing just a list / set / container / etc to the function is valid
