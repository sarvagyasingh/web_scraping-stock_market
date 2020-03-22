import requests
import lxml.html as lh
import time
import sys
import timeit
url = 'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

#To handle the Recursion Limit
sys.setrecursionlimit(20000)
#Check the length of the first 12 rows
print([len(T) for T in tr_elements[1:12]])



def chg_check(exp_col):
    for c in range(10,310,6):
        if(float(exp_col[c])>2):
            print((str(exp_col[c-4]))[0:15])


def main_prog():
    #Create empty list
    col=[]
    i=0

    #For each row, store each first element (header) and an empty list
    for f in range(1,52):
        for t in tr_elements[f]:
                i+=1
                name=t.text_content()
                #print ('%d:"%s"'%(i,name))
                col.append(name)

    exp_col = col
    chg_check(exp_col)
    time.sleep(30)
    


main_prog()

elapsed_time = timeit.timeit(main_prog, number = 2)

    
if(elapsed_time>=900):
    print("Time elapsed")
    sys.exit()
else:
    main_prog()