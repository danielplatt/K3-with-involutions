from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import itertools
import pexpect
import re

from pexpect import run
from pexpect.exceptions import TIMEOUT

from log import get_logger
import logging

log = get_logger(__name__, with_logfile=True, level=logging.DEBUG)


def get_general_quartic_poly(coeff):
    assert len(coeff)==35
    poly = str(coeff[0])+'*x^4+'+\
           str(coeff[1])+'*x^3*y+'+\
           str(coeff[2])+'*x^3*z+'+\
           str(coeff[3])+'*x^3*w+'+\
           str(coeff[4])+'*x^2*y^2+'+\
           str(coeff[5])+'*x^2*y*z+'+\
           str(coeff[6])+'*x^2*y*w+'+\
           str(coeff[7])+'*x^2*z^2+'+\
           str(coeff[8])+'*x^2*z*w+'+\
           str(coeff[9])+'*x^2*w^2+'+\
           str(coeff[10])+'*x*y^3+'+\
           str(coeff[11])+'*x*y^2*z+'+\
           str(coeff[12])+'*x*y^2*w+'+\
           str(coeff[13])+'*x*y*z^2+'+\
           str(coeff[14])+'*x*y*z*w+'+\
           str(coeff[15])+'*x*y*w^2+'+\
           str(coeff[16])+'*x*z^3+'+\
           str(coeff[17])+'*x*z^2*w+'+\
           str(coeff[18])+'*x*z*w^2+'+\
           str(coeff[19])+'*x*w^3+'+\
           str(coeff[20])+'*y^4+'+\
           str(coeff[21])+'*y^3*z+'+\
           str(coeff[22])+'*y^3*w+'+\
           str(coeff[23])+'*y^2*z^2+'+\
           str(coeff[24])+'*y^2*z*w+'+\
           str(coeff[25])+'*y^2*w^2+'+\
           str(coeff[26])+'*y*z^3+'+\
           str(coeff[27])+'*y*z^2*w+'+\
           str(coeff[28])+'*y*z*w^2+'+\
           str(coeff[29])+'*y*w^3+'+\
           str(coeff[30])+'*z^4+'+\
           str(coeff[31])+'*z^3*w+'+\
           str(coeff[32])+'*z^2*w^2+'+\
           str(coeff[33])+'*z*w^3+'+\
           str(coeff[34])+'*w^4'
    return poly

def get_demo_poly():
    one_indices = set([0,2,4,6,7,8,10,14,15,17,22,23,24,25,27,30,33])
    coeff = [0 for _ in range(35)]
    for k in range(35):
        if k in one_indices:
            coeff[k] = 1
    return get_general_quartic_poly(coeff)

def get_x_y_symmetric_poly(coeff):
    assert len(coeff)==22
    new_coeff = [0 for _ in range(35)]

    new_coeff[0] = coeff[0] #x^4
    new_coeff[20] = coeff[0] #y^4
    new_coeff[1] = coeff[1] #x^3*y
    new_coeff[10] = coeff[1] #x*y^3
    new_coeff[2] = coeff[2] #x^3*z
    new_coeff[21] = coeff[2] #y^3*z
    new_coeff[3] = coeff[3] #x^3*w
    new_coeff[22] = coeff[3]  #y^3*w
    new_coeff[4] = coeff[4] #x^2*y^2
    new_coeff[5] = coeff[5] #x^2*y*z
    new_coeff[11] = coeff[5] #x * y ^ 2 * z
    new_coeff[6] = coeff[6] #x^2*y*w
    new_coeff[12] = coeff[6] #x*y^2*w
    new_coeff[7] = coeff[7] #x^2*z^2
    new_coeff[23] = coeff[7] #y^2*z^2
    new_coeff[8] = coeff[8] #x^2*z*w
    new_coeff[24] = coeff[8] #y^2*z*w
    new_coeff[9] = coeff[9] #x^2*w^2
    new_coeff[25] = coeff[9] #y^2*w^2

    new_coeff[13] = coeff[10]
    new_coeff[14] = coeff[11]
    new_coeff[15] = coeff[12]

    new_coeff[16] = coeff[13] #x*z^3
    new_coeff[26] = coeff[13] #y*z^3
    new_coeff[17] = coeff[14] #x*z^2*w
    new_coeff[27] = coeff[14] #y*z^2*w
    new_coeff[18] = coeff[15] #x*z*w^2
    new_coeff[28] = coeff[15] #y*z*w^2
    new_coeff[19] = coeff[16] #x*w^3
    new_coeff[29] = coeff[16] #y*w^3

    new_coeff[30] = coeff[17] #z^4
    new_coeff[31] = coeff[18] #z^3*w
    new_coeff[32] = coeff[19] #z^2*w^2
    new_coeff[33] = coeff[20] #z*w^3
    new_coeff[34] = coeff[21] #w^4

    return get_general_quartic_poly(new_coeff)

def is_singular_quartic_with_magma_process(poly, c):
    commands = [
        'f:='+poly+';',
        'S := Scheme(P3, f);',
        'IsSingular(S);'
    ]
    for comm in commands:
        c.sendline(comm)
        c.expect(';\r\n')

    c.expect('>')
    result = c.before.splitlines()[0]
    if result == 'true':
        return True
    elif result == 'false':
        return False
    else:
        raise ValueError('Smoothness of this quartic cannot be determined: %s' % (poly,))

def check_all_polys_using_same_magma_process(start_from_id=0):
    path_to_magma_executable = '/Applications/Magma/magma'
    c = pexpect.spawnu(path_to_magma_executable)
    c.expect('>')
    commands = [
        'q1<t>:=PolynomialRing(RationalField());',
        'z4<x,y,z,w>:=PolynomialRing(IntegerRing(),4);',
        'p:=2;',
        'P3 := ProjectiveSpace(GF(p), 3);'
    ]

    for comm in commands:
        c.sendline(comm)
        c.expect(';\r\n')

    coeff_generator = itertools.product([0, 1], repeat=22)
    for id, coeff in enumerate(coeff_generator):
        if id<start_from_id:
            continue
        poly = get_x_y_symmetric_poly(coeff)
        try:
            result = is_singular_quartic_with_magma_process(poly, c)
        except TIMEOUT:
            result = 'timeout'
        except ValueError:
            result = 'error'
        log.info('ID: %s. Result: %s. Coefficients (short form): %s.' % (id, result, coeff,))

if __name__ == '__main__':
    check_all_polys_using_same_magma_process(start_from_id=1)
