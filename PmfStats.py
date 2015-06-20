#!/usr/bin/python

def pmf_mean(pmf):
    mean_p = 0.0
    count = len(pmf.Items())
    for val, freq in pmf.Items():
        mean_p += val * freq

    return mean_p

def pmf_var(pmf):
    mean_p = pmf_mean(pmf)
    var_p = 0.0
    for val, freq in pmf.Items():
        var_p += freq * ((val - mean_p)**2)

    return var_p
