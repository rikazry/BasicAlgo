import numpy as np
import scipy.stats as st
import matplotlib.pylab as plt
"""
Monte Carlo is often applied to:
    * value complex securities
    * simulate the pnl from a trading strategy
    * calculate estimates of var
    * simulate pension fund assets and liabilities over time to examine the variablity of the difference between the 2
    * value portfolios of assets that have non-normal returns distrubution

convergence rate: O( max{ T/m, 1/sqrt(n) } )

pro:
    what if
con:
    cannot provide better conclusion than the assumption
    statistical rather than analytical
"""
"""
CLT:
    sample mean ~ normal(porpulation mean, population variance / n)
    (n >= 30)

standard error of sample mean:
    standard deviation of the distribution of sample means

desirable statistical properties of an estimator:
    unbiasedness
    efficiency ( smaller variance than other unbiased estimators)
    cosistency ( accuracy increases as as sample size increases)
"""

def est_pi(N):
    x, y = st.uniform.rvs(size = (2,N))
    acc = np.power(x,2) + np.power(y,2) <=1
    acc_mean = np.mean(acc)
    est_pi = acc_mean*4
    acc_est_std = np.std(acc, ddof=1)
    est_std = acc_est_std/float(np.sqrt(N))
    acc_thr_var = np.pi/4 - (np.pi/4)**2
    thr_std = np.sqrt(acc_thr_var/N)
    return (est_pi, thr_std, est_std)

def est_gbm(S0, N, mean, std, t = 1):
    """
    dS = mean*S*dt + std*S*dw
    Ito's lemma =>
    d(lnS) = (mean - std^2/2)*dt + std*dw
    """
    dt = float(t)/N
    z = st.norm.rvs(size = N)
    S = np.zeros(N+1)
    S[0] = S0
    for i in range(N):
        S[i+1] = S[i]*np.exp( (mean - std**2/2.)*dt + std*np.sqrt(dt)*z[i] )
    return S

def est_norm_multi_uni(N):
    u = st.uniform.rvs(size=N)
    u_mean = np.mean(u)
    u_thr_var = 1/3. - 1/4.
    th_std = np.sqrt(u_thr_var/N)
    x = (u_mean - .5) / th_std
    return x 

def est_norm_corr(corr):
    z1, z2 = st.norm.rvs(size=2)
    x1, x2 = z1, corr*z1 + np.sqrt(1-corr**2)*z2
    return x1, x

def est_norm_inv():
    u = st.uniform.rvs()
    z = st.norm.ppf(u)
    return z

def est_norm_boxmuller():
    r = 1
    while r >= 1:
        u, v = st.uniform.rvs(loc=-1, scale=2, size=2)
        r = u**2 + v**2
    r = np.sqrt( -2. * np.log(r) / r)
    z1, z2 = u*r, v*r
    return z1, z2
