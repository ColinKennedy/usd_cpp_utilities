#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class Timer(object):
    def __init__(self):
        super(Timer, self).__init__()

        self._start = -1
        self._end = -1

    def get_recorded_delta(self):
        if self._start == -1:
            raise RuntimeError("Start is not set. Cannot continue.")

        if self._end == -1:
            raise RuntimeError("End is not set. Cannot continue.")

        if self._end < self._start:
            raise RuntimeError('End "{self._end}" is less than "{self._start}". This should never happen.'.format(self=self))

        return self._end - self._start

    def __enter__(self):
        self._start = time.time()

        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self._end = time.time()
