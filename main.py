U
    ΔΑγ^  γ                   @   s~  d dl Z d dlZd dlZd dlZd dlZd dlZe d‘ dZee e	dZ
z6dZee
ddZe  ‘ ZejeedZeejZW n   Y nX d	d
 Zdd Zdd Zdd Zdd Ze d‘ ee ed ed ed ed ed ed e	dZee
 edkr$ee
 qnVedkr8ee
 nBedkrLee
 n.edkrje	dZee
e ned e ‘  dS ) ι    NΪclearu{  [0;33;40m

      ββββββ    β  ββ βββββββ  ββββββ    ββ    
   ββββββββββ  ββ βββ   ββ  ββ ββ  ββ ββββββββ 
   ββ  ββ  ββ βββββ    ββββββ  ββ  ββ    ββ  β 
   ββ  ββ  ββ βββββ   βββββββ  ββ  ββ    ββ    
   ββ  ββ  ββ  ββ βββ   ββ  ββ ββ  ββ    ββ    
    β  ββ  ββ  ββ  ββ βββββββ  ββββββ   ββββ  
             CATS GARDEN SCRIPT
[0mz@ [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mToken >> [0;33;40mz;https://cats.garden/api/setting/bindInvitationCode/5CLB683Dϊokhttp/4.4.0©Ϊtokenz
user-agent©Zheadersc                 C   s2  d}t | dd}t ‘ }|j||d}t |j}td t d|‘}t|dkr.g }|D ]}| 	dd	‘}| 
|‘ q\td
t t|  d}	t d|‘}
|
D ] }| 	dd	‘}t|	t| }	q tdt |	 d  t d|‘d  	dd	‘}tdt |  t d|‘d  	dd	‘}tdt |  td d S )Nϊ!https://cats.garden/api/cat/queryr   r   r   z(========================================ϊlevel":[0-9]+r   ϊlevel":Ϊ zE [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mCat Count  >> [0;33;40mzoutput":[0-9]+zoutput":zE [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mCat Income >> [0;33;40mz/szuserGold":[0-9]+z
userGold":zE [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mGold       >> [0;33;40mzuserUSD":[0-9]+.[0-9]+z	userUSD":zE [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mUSD        >> [0;33;40m)ΪstrΪrequestsΪSessionΪgetΪtextΪprintΪreΪfindallΪlenΪreplaceΪappendΪint)r   ΪurlΪheaderΪsessionΪwebΪpageΪstatusZ	cat_levelΪlevelΪtotalZ
cat_incomeZincomeZgoldZusd© r   ϊ	.\cats.pyΪUserInfo   s0    
r!   c                 C   s  zd}t | dd}t ‘ }|j||d}t |j}g }t d|‘}t d|‘}tt|D ]2}	||	  	dd‘}
||	  	d	d‘}| 
|
|g‘ q^|D ]}qtt|D ]Ψ}	tt|D ]Ζ}||	 d
 || d
 krΈ||	 d || d krΈ|	|krΈt ||	 d }t || d }dt | d t | }t | dd}t ‘ }|j||d}t |j}t d|‘}t|d
krΈtd  q¨qΈq¨W q    Y q X q d S )Nr   r   r   r   r   zuserCatIdt":"[a-z0-9-]+r	   r
   zuserCatIdt":"r   ι   z*https://cats.garden/api/cat/synthesisCats/ϊ/ΪSUCCESSzN [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mMerge Status >> [0;33;40mSuccess)r   r   r   r   r   r   r   Ϊranger   r   r   Ϊpostr   )r   r   r   r   r   r   ZcatsZclvlZcIdΪiZcatLVLZcatIDΪcatΪcZcat1Zcat2r   r   r   r    Ϊmerge8   s>    
8
r*   c           	      C   s¬   zdt | }t | dd}t ‘ }|j||d}t |j}t d|‘}t|dkrt d|‘d  dd	‘}t	d
t |d  d t |  n W q    t	d Y q X q d S )Nz https://cats.garden/api/cat/buy/r   r   r   r$   r   zbuyPrice":[0-9]+z
buyPrice":r
   zB [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mBuy Cat >> [0;33;40mz | Price >> [0;33;40mz. [3;31;40m[[0;36;40m*[3;31;40m] REAL ERROR!©
r   r   r   r&   r   r   r   r   r   r   )	r   Ϊcatidr   r   r   r   r   r   Zpricer   r   r    Ϊbuycatc   s    
"r-   c                 C   s~   d}t | dd}t ‘ }|j||d}t |j}t d|‘}t|dkrzt d|‘d  dd	‘}t	d
t |d  d  d S )Nz.https://cats.garden/api/lottery/watchADForMorer   r   r   r$   r   zwatchADTimesLeft":[0-9]+zwatchADTimesLeft":r
   zD [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mMore SPIN >> [0;33;40mz	 + 3 Spinr+   )r   r   r   r   r   r   r   Zadsr   r   r    Ϊmorespinx   s    
r.   c                 C   sv  z`d}t | dd}t ‘ }|j||d}t |j}t d|‘}t|dkr`t d|‘d }| dd	‘}| d
d	‘}| dd	‘}| 	d‘}|d  dd	‘}t |dkr`d}t | dd}t ‘ }|j||d}t |j}t d|‘}t|dkr&|d  dd	‘}	|t
|	 }
tdt |
  nt|  d}t | dd}t ‘ }|j||d}t |j}W q    Y q X q d S )Nz-https://cats.garden/api/lottery/rewardOptionsr   r   r   zlotteryTimesLeft":[0-9]+r   z\["[a-zA-Z0-9",]+\]ϊ[r
   ϊ]ϊ"ϊ,zlotteryTimesLeft":z'https://cats.garden/api/lottery/start/1zindex":[0-9]+zindex":zF [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mSpin Result >> [0;33;40mz/https://cats.garden/api/lottery/watchADForPrize)r   r   r   r&   r   r   r   r   r   Ϊsplitr   r   r.   )r   r   r   r   r   r   r   ΪoptionsZspinΪresultZrewardr   r   r    Ϊlottery   sB    


r6   z6 [3;31;40m[[0;36;40m1[3;31;40m] [1;32;40mSpin Farmz6 [3;31;40m[[0;36;40m2[3;31;40m] [1;32;40mSpin Rollz7 [3;31;40m[[0;36;40m3[3;31;40m] [1;32;40mAuto Mergez9 [3;31;40m[[0;36;40m4[3;31;40m] [1;32;40mAuto Buy Catz NOTE: Auto Buy Cat Need Cat IDz"==================================z= [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mEnter Choice >> Ϊ1Ϊ2Ϊ3Ϊ4z< [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mEnter CatID >> z: [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mInvalid Input)r   ΪosΪsysΪtimer   Ϊ	threadingΪsystemZbannerr   Ϊinputr   r   r   r   r   r   r&   r   r   r   r!   r*   r-   r.   r6   Ϊchoicer,   Ϊexitr   r   r   r    Ϊ<module>   sL   0

+.






