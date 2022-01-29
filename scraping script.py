# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:44:06 2022

@author: mianyong
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

#this is cited from:
def extractinfor(url1,catname):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    
    
  
 
    api_url = "https://www.indeed.com/viewjob?viewtype=embedded&jk={job_id}"
    
    list2 = [x*10 for x in range(0, 8)]
    address=[url1+str(x) for x in list2]
    
    import numpy as np
    
    
    
    souplist=[BeautifulSoup(requests.get(address[i], headers=headers).content, "html.parser") for i in range(0,8)]
    
    allall=pd.DataFrame(columns=["title","description","category"])
    soup = BeautifulSoup(requests.get(url1, headers=headers).content, "html.parser")
    for soup in souplist:    
        i=0
        job1=[]
        titles=[]
        dess=[]
        for job in soup.select('a[id^="job_"]'):
            job_id = job["id"].split("_")[-1]
            s = BeautifulSoup(
                requests.get(api_url.format(job_id=job_id), headers=headers).content,
                "html.parser",
            )
            title1=s.title.get_text(strip=True)
            #print(title1)
            titles.append(title1)
        
            des1= s.select_one("#jobDescriptionText").get_text(strip=True, separator="\n")
           # print(des1)
            #print("#" * 80)
            des1=des1.replace("\n", "")
            dess.append(des1)
            
            #print(i)
            
            
            i=i+1
        
        l1=len(dess)
        cat=np.repeat(np.array([catname]), l1)
        all1=pd.DataFrame({"title":titles,"description":dess,"category":cat})
        
        allall=allall.append(all1)
    return allall
    
    
a1=extractinfor("https://www.indeed.com/jobs?q=Bioinformatics&start=","bioinformatics")


teacherurl1="https://www.indeed.com/jobs?q=teacher&jt=fulltime&explvl=entry_level&start="
#da3=extractinfor(teacherurl1,"teacher")
marketing="https://www.indeed.com/jobs?q=marketing&start="
da4=extractinfor(marketing,"marketing")


itt="https://www.indeed.com/jobs?q=it&jt=fulltime&explvl=entry_level&start="


dit=extractinfor(itt,"it")



