#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Any class / function which can be used for other testing modules."""

import time


class Timer(object):
    """Record the elapsed time for the duration of this context."""

    def __init__(self):
        """Initialize the base, default variables."""
        super(Timer, self).__init__()

        self._start = -1
        self._end = -1

    def get_recorded_delta(self):
        """Find the seconds which occurred during the execution of this instance's context.

        Raises:
            RuntimeError:
                If for some reason the start / end times are not defined
                or have unexpected values.

        Returns:
            float: Each second that has passed.

        """
        if self._start == -1:
            raise RuntimeError("Start is not set. Cannot continue.")

        if self._end == -1:
            raise RuntimeError("End is not set. Cannot continue.")

        if self._end < self._start:
            raise RuntimeError('End "{self._end}" is less than "{self._start}". This should never happen.'.format(self=self))

        return self._end - self._start

    def __enter__(self):
        """:class:`Timer`: Keep track of the user's current time."""
        self._start = time.time()

        return self

    def __exit__(self, exec_type, exec_value, traceback):
        """Mark the current time as the end of this context's execution."""
        self._end = time.time()
