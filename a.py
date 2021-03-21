import numpy as np
def find_convex_cover(pvertices,clist):
    '''
    This function finds the optimal radii of m circles centered at the m points
    specified by clist such that the sum of areas of the circles is minimized 
    and that any vertex in pvertices is also contained in at least one of the m
    circles

    Parameters
    ----------
    pvertices : numpy array
        (n-1) long iterable of polygon vertices.
    clist : list
        list of m (x,y) tuples of circle centers.

    Returns
    -------
    a list of m radii
    '''
    assert isinstance(pvertices, np.ndarray)
    #assert pvertices.shape[0] >= 3
    assert pvertices.shape[1] == 2
    assert isinstance(clist, list) and len(clist) > 0
    assert all(isinstance(c, tuple) for c in clist)
    
    a = pvertices[:,None] - clist
    dist = np.square(a[:,:,0]) + np.square(a[:,:,1])
    nearest_center = np.sqrt(np.min(dist,axis=1))
    nn = np.argmin(dist,axis=1)
    rad = [0]*dist.shape[1]
    for i in range(len(nearest_center)):
        if nearest_center[i]>rad[nn[i]]:
            rad[nn[i]] = nearest_center[i]
            
    return rad