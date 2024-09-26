# CSAPI Usage

This document describes the vision for the next revision of this library.

## Time

Timing, scheduling, and timeout utilities.

```python
from csapi import time

# light sleep for a number of seconds
time.lightsleep(seconds)

# Run function(), returning early if it runs for more than the given number of seconds.
time.timeout(seconds, function)

# Returns the current epoch time, or throws exception if not yet synced.
time.time()

# Returns time.time()-<monotonic time>
time.get_offset()
```
