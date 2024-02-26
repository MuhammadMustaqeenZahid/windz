def W(k,c,v33):
    import numpy as np
    W=((k/c)*np.power((v33/c),k-1)*np.exp(-np.power((v33/c),k)))
    return W