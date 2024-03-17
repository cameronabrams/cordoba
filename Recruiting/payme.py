import matplotlib.pyplot as plt
import numpy as np
import argparse as ap
import pandas as pd

def salary_sched(initial_salary,N,rate):
    I=np.zeros(N)
    I[0]=initial_salary
    for i in range(1,N):
        I[i]=I[i-1]*(1+rate)
    return I

def cumulative_earnings(initial_investment,initial_annual_earnings,N,rate):
    S=salary_sched(initial_annual_earnings,N,rate)
    J=np.zeros(N)
    J[0]=initial_investment+S[0]
    for i in range(1,N):
        J[i]=J[i-1]*(1+rate)+S[i]
    return J

def nograd_earnings(salary,N,rate=0.03):
    return cumulative_earnings(0.0,salary,N,rate)

def phd(base_as_phd,n_phd,base_post_phd,n_post_phd,rate=0.03):
    asphd=cumulative_earnings(0.0,base_as_phd,n_phd,rate)
    postphd=cumulative_earnings(asphd[-1],base_post_phd,n_post_phd,rate)
    postphd+=asphd[-1]
    return np.concatenate([asphd,postphd])
    
if __name__=='__main__':
    parser=ap.ArgumentParser()
    parser.add_argument('--bs-salary',type=float,help='base year-1 BS salary ($)',default=75000)
    parser.add_argument('--phd-stipend',type=float,help='base year-1 PHD stipend ($)',default=30000)
    parser.add_argument('--phd-salary',type=float,help='base year-1 PHD salary ($)',default=100000)
    parser.add_argument('--n',type=int,default=30,help='total years')
    parser.add_argument('--s',type=str,default='money.png',help='output file name')
    parser.add_argument('--n-phd',type=int,default=5,help='phd duration (y)')
    parser.add_argument('--rate',help='annual growth rate',type=float,default=0.03)
    args=parser.parse_args()

    BS=nograd_earnings(args.bs_salary,args.n,args.rate)
    PHD=phd(args.phd_stipend,args.n_phd,args.phd_salary,args.n-args.n_phd,args.rate)

    fig,ax=plt.subplots(1,1,figsize=(6,9))
    plt.rcParams.update({'font.size':14,'lines.linewidth':2,})
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines[['right', 'top']].set_visible(False)
    # change all spines
    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(2)
    # increase tick width
    ax.tick_params(width=2)

    ax.set_xlabel('years',fontsize=14)
    ax.set_ylabel('total cumulative earnings, 10$^3$ \$',fontsize=14)
    ax.set_xlim(0,args.n+1)
    ax.plot(range(1,args.n+1),BS/1e3,label='BS only',color="#07294D",linewidth=2)
    ax.plot(range(1,args.n+1),PHD/1e3,label='BS and PhD',color="#99A903",linewidth=2)
    ax.legend()
    plt.savefig(args.s,bbox_inches='tight')

    # data=pd.DataFrame({'BS':BS,'PHD':PHD})
    # print(data.to_string(float_format="%0f"))