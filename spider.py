# 使用原生爬虫爬取电子书信息， 每一本书的信息都需要爬取，
# 包括书名、作者、内容简介...等。
# 参考地址：http://d81fb43e-d.parkone.cn/
import re
from urllib import request

class Spider():
    url = 'http://d81fb43e-d.parkone.cn/page/'
    url1 = 'http://d81fb43e-d.parkone.cn'
    root_pattern = '<div class="cover">([\s\S]*?)</div>'
    book_pattern = '<a href="([\s\S]*?)" data-toggle="modal" data-target="#bookDetailsModal" data-remote="false">'
    #书名
    book_name = '<h2>([\s\S]*?)</h2>'
    #作者
    author = '<a href="/author/.*"([\s\S]*?)</a>'
    #出版社
    out = '<span>出版社:([\s\S]*?)</span>'
    #出版日期
    date = '<p>出版日期([\s\S]*?)</p>'
    #简介
    simple = '<p class="description">([\s\S]*?)</p>'
    
    def __fetch_content(self,all_url):
        r = request.urlopen(all_url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    def __analysis__(self):
        list_book = []
        j = 1
        while(len(re.findall(Spider.root_pattern,self.__fetch_content(Spider.url+str(j))))>0):
            html = self.__fetch_content(Spider.url+str(j))
            root = re.findall(Spider.root_pattern,html)
            for i in root:
                htmls = re.findall(Spider.book_pattern,i)
                url1 = Spider.url1+str(htmls[0])
                html_all = self.__fetch_content(url1)
                book_name = re.findall(Spider.book_name,html_all)
                author = re.findall(Spider.author,html_all)
                out = re.findall(Spider.out,html_all)
                date = re.findall(Spider.date,html_all)
                simple = re.findall(Spider.simple,html_all)
                sty = {'name':book_name,'author':author,'out':out,'date':date,'easy':simple}
                list_book.append(sty)
            j = j + 1  
            print(list_book)
                  
spider = Spider()
spider.__analysis__()
 
           
            
           
          
    
       
        
           
            

             
    

    
            


           
            
    
   
        

        

        


        
        
    
    
        
       
        
       
        
    

        
        
        
    
            

    
            
        
        

        

       
        
        
            



        
        
       
        
        


