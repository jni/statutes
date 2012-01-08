from numpy import unique

def get_rejection_sample(rep_samples, n):
    """Get a rejection sample from a sample with replacement."""
    top, bottom = len(rep_samples), 0
    mid = top/2
    u = unique(rep_samples[:mid])
    while len(u) != n:
        if len(u) < n:
            bottom = mid
        else:
            top = mid
        mid = (top+bottom)/2
        u = unique(rep_samples[:mid])
        if mid == top or mid == bottom:
            break
    return u
