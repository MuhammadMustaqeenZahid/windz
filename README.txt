This document explains important parts of the package windz.
This package finds the Weibull distribution parameters to model a wind distribution.
The package also models the same distribution using the Maximum Entropy Principle.
Five methods
(i) Empirical Method (EM)
(ii) Energy Pattern Factor Method (EPFM)
(iii) Method of Moments (MoM)
(iv) Maximum likelihood Method (MLM), and 
(iv) Modified Maximum likelihood Method (MMLM),
can be used to find the shape and scale parameters of the Weibull distribution.

The maximum entropy principle employs Lagrange multipliers to model wind distribution.
*************************************Data Reading****************************************
For both Weibull and MEP fitting, the input data is converted into frequency or probability 
distribution and stored in an Excel file, which is used as an input file.

*****************************************************************************************
The following functions are imported from the package
from windz.MEP import mep, em, epm, mlm, mmlm, mom 
import windz.SE as se
import windz.SEMEP as semep

se and semep are the error calculators for Weibull and MEP, respectively.
mep(N,v, F) function takes three parameters: (i) N, the number of moments, (ii) v, and (F) are the values of wind speeds and probabilities in the Excel file.
W(k,c,v) function is a Weibull distribution calculator; it takes three parameters: shape, scale, and wind speeds.
mom(v, F) takes wind speeds and corresponding probabilities to determine k and c using the method of moments.
em(v, F) takes wind speeds and corresponding probabilities to determine k and c using the Empirical method.
epm(v, F) takes wind speeds and corresponding probabilities to determine k and c using the energy pattern factor method.
mlm(v, F) takes wind speeds and corresponding probabilities to determine k and c using the Maximum likelihood method.
mmlm(v, F) takes wind speeds and corresponding probabilities to determine k and c using the Modified Maximum likelihood method.


