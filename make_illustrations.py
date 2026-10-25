import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Ellipse, Polygon, Arc, FancyArrowPatch
for f in fm.findSystemFonts():
    if 'Carlito' in f: fm.fontManager.addfont(f)
plt.rcParams['font.family']='Carlito'
NAVY='#1E3A8A'; SLATE='#334155'; GREY='#94A3B8'

# ---------- Image 1: collar on trunk, cutaway ----------
fig=plt.figure(figsize=(6,4.4),dpi=300); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,6); ax.set_ylim(0,4.4); ax.axis('off')
ax.add_patch(Rectangle((0,0),6,4.4,fc='#F1F5F9',ec='none'))
# trunk
ax.add_patch(Rectangle((2.0,0),2.0,4.4,fc='#A16207',ec='#713F12',lw=1.5))
rng=np.random.default_rng(3)
for x in np.linspace(2.1,3.9,9):
    y0=rng.uniform(0,3.5); ax.plot([x,x+rng.uniform(-.05,.05)],[y0,y0+rng.uniform(.5,.9)],color='#854D0E',lw=1.2,alpha=.8,zorder=2)
# cutaway window
ax.add_patch(FancyBboxPatch((2.15,0.3),1.7,2.25,boxstyle='round,pad=0,rounding_size=0.08',fc='#FDE68A',ec='#713F12',lw=1.2,zorder=3))
for r in np.linspace(.25,2.0,6):
    ax.plot([2.15,3.85],[0.3+r*0.0+0.0,0.3+0.0],alpha=0)  # no-op
for yy in np.linspace(0.45,2.4,8): ax.plot([2.2,3.8],[yy,yy],color='#FCD34D',lw=.8,alpha=.7,zorder=4)
# tunnel + larva
t=np.linspace(0,1,60); tx=2.3+1.4*t; ty=0.75+1.1*t+0.12*np.sin(t*14)
ax.plot(tx,ty,color='#78350F',lw=11,solid_capstyle='round',alpha=.85,zorder=5)
lx,ly=3.0,1.4
seg=[(lx+dx,ly+dy,0.15-0.015*i) for i,(dx,dy) in enumerate([(-0.3,-0.2),(-0.15,-0.1),(0,0),(0.15,0.1),(0.3,0.2)])]
for sx,sy,sr in seg: ax.add_patch(Circle((sx,sy),sr,fc='#FEF3C7',ec='#92400E',lw=1,zorder=6))
ax.add_patch(Circle((lx+0.36,ly+0.24),0.07,fc='#92400E',ec='none',zorder=7))
# sound arcs
for r in [0.4,0.7,1.0,1.3]:
    ax.add_patch(Arc((lx,ly),2*r,2*r,theta1=50,theta2=130,color='#DC2626',lw=2.2,zorder=7))
# collar band
ax.add_patch(Rectangle((1.9,2.75),2.2,0.72,fc='#CBD5E1',ec='#475569',lw=1.5,zorder=10))
ax.add_patch(Rectangle((2.7,2.8),0.6,0.1,fc='#64748B',ec='none',zorder=11))  # tensioner hint
ax.plot([1.9,4.1],[2.9,2.9],color='#64748B',lw=.8,zorder=11)
# Al plate + PZT (inside collar band, at contact)
ax.add_patch(Rectangle((2.55,2.62),0.9,0.15,fc='#E2E8F0',ec='#475569',lw=1.2,zorder=11))   # Al plate
ax.add_patch(Rectangle((2.8,2.52),0.4,0.1,fc='#F59E0B',ec='#92400E',lw=1,zorder=11))       # PZT
# housing + solar
ax.add_patch(FancyBboxPatch((2.45,2.95),1.1,0.5,boxstyle='round,pad=0,rounding_size=0.05',fc='#F8FAFC',ec='#475569',lw=1.5,zorder=10))
ax.text(3.0,3.2,'MCU · AFE\nLoRa',ha='center',va='center',fontsize=9,color=SLATE,zorder=13)
ax.add_patch(Polygon([[2.4,3.55],[3.6,3.55],[3.75,3.95],[2.55,3.95]],fc='#1E40AF',ec='#1E3A8A',lw=1.2,zorder=11))
for k in range(1,3): ax.plot([2.4+0.4*k+0.05*k*0,2.55+0.4*k],[3.55,3.95],color='#93C5FD',lw=.7,zorder=12)
ax.plot([2.47,3.67],[3.75,3.75],color='#93C5FD',lw=.7,zorder=12)
ax.plot([3.0,3.0],[3.45,3.55],color='#475569',lw=2,zorder=11)
# callouts
def call(txt,xy,xt,yt,ha):
    ax.annotate(txt,xy=xy,xytext=(xt,yt),ha=ha,va='center',fontsize=12.5,color=NAVY,fontweight='bold',
                arrowprops=dict(arrowstyle='-|>',color=NAVY,lw=1.3,shrinkA=2,shrinkB=2))
call('Solar panel +\nASA housing',(2.55,3.8),1.75,4.05,'right')
call('Al plate + PZT disc\n(rigid contact)',(2.55,2.62),1.8,2.2,'right')
call('Vibration travels\nthrough the wood',(3.5,2.05),4.2,2.4,'left')
call('Larva boring:\nimpulsive clicks',(3.3,1.55),4.2,1.35,'left')
ax.annotate('Tree trunk\n(Ø15–60 cm)',xy=(2.0,0.6),xytext=(1.75,0.6),ha='right',va='center',fontsize=11.5,color=SLATE,
            arrowprops=dict(arrowstyle='-|>',color=SLATE,lw=1.2,shrinkA=2,shrinkB=0))
fig.savefig('../docs/images/collar_principle.png',facecolor='#F1F5F9'); plt.close(fig)

# ---------- Image 2: signal processing panels (synthetic) ----------
fig,axs=plt.subplots(3,1,figsize=(6,3.2),dpi=300,sharex=True)
fig.patch.set_facecolor('white')
n=1500; t=np.linspace(0,3,n); rng=np.random.default_rng(7)
noise=rng.normal(0,1,n)*0.35
wind=0.6*np.sin(2*np.pi*0.8*t)*rng.normal(1,.2,n)
clicks=np.zeros(n)
for c in [0.55,0.95,1.35,1.75,2.15,2.55]:
    i=int(c/3*n); L=40; clicks[i:i+L]+=np.exp(-np.arange(L)/8)*np.sin(np.arange(L)*1.4)*1.0
gust=np.zeros(n); gi=int(0.2/3*n); gust[gi:gi+120]+=rng.normal(0,2.2,120)*np.hanning(120)
raw=noise+wind+clicks+gust
filt=noise*0.3+clicks*2.0+0.12*gust
titles=['1  Raw sensor signal: wind, rain and trunk noise bury the clicks',
        '2  Band-pass filter keeps the larval-click band',
        '3  Burst detector + N-of-M vote: repeated bursts raise the alert']
sig=[raw,filt]
for a,s,tt in zip(axs[:2],sig,titles[:2]):
    a.plot(t,s,color=NAVY if s is raw else '#0F766E',lw=.6); a.set_ylim(-3,3)
    a.set_title(tt,fontsize=10.5,color=NAVY,loc='left',fontweight='bold',pad=2)
a=axs[2]; env=np.abs(filt); sm=np.convolve(env,np.ones(18)/18,'same')
a.plot(t,sm,color='#0F766E',lw=1); a.axhline(0.30,color='#DC2626',ls='--',lw=1)
a.text(2.99,0.33,'threshold',color='#DC2626',fontsize=8.5,ha='right',va='bottom')
for p in [0.55,0.95,1.35,1.75,2.15,2.55]:
    seg=sm[int(p/3*n):int((p+0.2)/3*n)]; k=int(p/3*n)+int(np.argmax(seg))
    a.plot(t[k],sm[k]+0.07,marker='v',color='#DC2626',ms=5)
a.annotate('single gust:\nno repeat, rejected',xy=(0.3,0.12),xytext=(0.03,0.85),fontsize=8.5,color=SLATE,ha='left',va='center',
           arrowprops=dict(arrowstyle='-|>',color=SLATE,lw=.9))
a.text(2.0,1.0,'6 of last 8 windows above threshold: ALERT',fontsize=9.5,color='white',fontweight='bold',ha='center',va='center',
       bbox=dict(boxstyle='round,pad=0.25',fc='#DC2626',ec='none'))
a.set_ylim(0,1.25)
a.set_title(titles[2],fontsize=10.5,color=NAVY,loc='left',fontweight='bold',pad=2)
for a in axs:
    a.set_yticks([]); a.spines[['top','right','left']].set_visible(False); a.spines['bottom'].set_color(GREY)
for a in axs[:2]: a.tick_params(bottom=False)
axs[2].set_xticks([0,1,2,3]); axs[2].set_xticklabels(['0 s','1 s','2 s','3 s'],fontsize=8.5,color=SLATE)
axs[2].set_xlabel('Illustrative synthetic waveform (not measured data)',fontsize=8.5,color=SLATE,labelpad=2)
fig.subplots_adjust(left=0.02,right=0.99,top=0.93,bottom=0.12,hspace=0.55)
fig.savefig('../docs/images/signal_chain.png'); plt.close(fig)

# ---------- Image 3: orchard network (top view) ----------
fig=plt.figure(figsize=(6,3.2),dpi=300); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,6); ax.set_ylim(0,3.2); ax.axis('off')
ax.add_patch(Rectangle((0,0),6,3.2,fc='#ECFDF5',ec='none'))
pts=[(0.5+0.75*i,0.6+0.6*j) for i in range(4) for j in range(4)]
collared={(1,1):'ok',(2,3):'alert',(3,0):'ok'}
flag=None
for idx,(x,y) in enumerate(pts):
    i,j=idx//4,idx%4
    st=collared.get((i,j))
    ax.add_patch(Circle((x,y),0.24,fc='#86EFAC' if st!='alert' else '#FCA5A5',ec='#15803D' if st!='alert' else '#B91C1C',lw=1))
    ax.add_patch(Circle((x,y),0.05,fc='#78350F',ec='none'))
    if st:
        ax.add_patch(Circle((x,y),0.1,fc='none',ec='#475569',lw=2.2))
        if st=='alert': flag=(x,y)
# receiver
ax.add_patch(FancyBboxPatch((4.5,1.0),1.3,1.1,boxstyle='round,pad=0,rounding_size=0.06',fc='white',ec='#475569',lw=1.5))
ax.add_patch(Rectangle((4.62,1.35),1.06,0.65,fc='#DBEAFE',ec='#1E3A8A',lw=1))
ax.text(5.15,1.82,'Dashboard',fontsize=10,ha='center',color=NAVY,fontweight='bold')
ax.add_patch(Circle((4.85,1.58),0.05,fc='#DC2626',ec='none')); ax.text(4.95,1.58,'Tree #07',fontsize=9,va='center',color=SLATE)
ax.add_patch(Circle((4.85,1.43),0.05,fc='#16A34A',ec='none')); ax.text(4.95,1.43,'Others OK',fontsize=9,va='center',color=SLATE)
ax.text(5.15,1.17,'Receiver + laptop',fontsize=9.5,ha='center',color=SLATE)
ax.plot([5.15,5.15],[2.1,2.55],color='#475569',lw=2); ax.add_patch(Circle((5.15,2.6),0.06,fc='#475569'))
for r in [0.2,0.35,0.5]:
    ax.add_patch(Arc((5.15,2.6),2*r,2*r,theta1=20,theta2=160,color='#475569',lw=1.2))
# lora links
for (i,j),st in collared.items():
    x,y=pts[i*4+j]
    col='#DC2626' if st=='alert' else '#2563EB'
    ax.add_patch(FancyArrowPatch((x+0.14,y),(4.5,1.55),arrowstyle='-',connectionstyle='arc3,rad=0.0',color=col,lw=1.6 if st=='alert' else 1,ls='--'))
ax.text(3.75,0.5,'LoRa P2P, 865–867 MHz',fontsize=10.5,color='#1D4ED8',fontweight='bold',ha='center',va='center')
ax.annotate('Infested tree flagged',xy=(flag[0]+0.25,flag[1]+0.05),xytext=(2.45,2.95),fontsize=11,color='#B91C1C',fontweight='bold',ha='left',va='center',
            arrowprops=dict(arrowstyle='-|>',color='#B91C1C',lw=1.3))
ax.text(0.1,3.0,'Orchard (top view)',fontsize=10.5,color='#166534',fontweight='bold',va='center')
ax.add_patch(Circle((0.15,0.14),0.07,fc='none',ec='#475569',lw=2)); ax.text(0.28,0.14,'= ACPDC collar',fontsize=9,va='center',color=SLATE)
fig.savefig('../docs/images/orchard_network.png'); plt.close(fig)
