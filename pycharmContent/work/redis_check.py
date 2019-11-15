#!/bin/python3
import svcwatch
if __name__ == '__main__':
    s = svcwatch.StateCheck("/home/admin/logs/state_check.log")
    s.redis_check()
    s.ping_test()
    s.log_clean()

