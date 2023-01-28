#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l1=[]
l2=[]
q=[]
l3=[]
for j in range(2):
    page=j+1
    url_site=f'https://diabet-shop.com/categories/%D9%86%D8%A7%D9%86-%D8%B4%DB%8C%D8%B1%DB%8C%D9%86%DB%8C-%D9%88-%D8%A8%DB%8C%D8%B3%DA%A9%D9%88%D9%8A%DB%8C%D8%AA?page={page}'
    url_r=requests.get(url_site)
    soup=BeautifulSoup(url_r.text,'html.parser')
    x=soup.find('div',{'class':"row products-category"})
    y=x.find_all('img',{'class':'img-responsive'})
    z=x.find_all('span',{'class':"price-new"})
    r=x.find_all('div',{'class':"image"})
    for i in range(len(y)):
        l1.append(y[i]['title'])
        q.append(r[i].find('a'))
        l3.append("https://diabet-shop.com"+str(q[i]['href']))
        l2.append(z[i].text)
D={"title":l1,
   "price":l2,
   "link":l3}
pan=pd.DataFrame(D)
pan.to_excel(f'F:\python ali nazari\Season_2-2\Season_2\python 2_19/fidiabetshop.xlsx')

