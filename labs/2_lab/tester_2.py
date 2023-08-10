# -*- coding: utf-8 -*-
import os

TESTS = [
    [
        '0 0',
        '0 0 0 #'],
    [
        '1 0',
        '1 1 0 #'],
    [
        '0 1',
        '1 -1 0 0.00'],
    [
        '1 1',
        '2 0 1 1.00'],
    [
        '-1 -1',
        '-2 0 1 1.00'],
    [
        '1 -1',
        '0 2 -1 -1.00'],
    [
        '1 3',
        '4 -2 3 0.33'],
    [
        '-1 3',
        '2 -4 -3 -0.33'],
    [
        '1 -3',
        '-2 4 -3 -0.33'],
    [
        '99 7',
        '106 92 693 14.14'],
    [
        '99 -7',
        '92 106 -693 -14.14']]


def run(param):
    stream = os.popen('bash ./labs/2_lab/script.bash ' + param)
    return stream.read()


flag = True
for i, test in enumerate(TESTS):
    output = run(test[0])
    if output.strip() != test[1]:
        flag = False

    if flag:
        print('PASSED')
    else:
        print('NOT PASSED')
# okay decompiling tester_3.pyc