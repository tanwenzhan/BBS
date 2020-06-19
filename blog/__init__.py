# from bs4 import BeautifulSoup
# s='''span style="font-size: 16px;"><strong>基于属性的查询，也称为</strong><span style="color: #ff0000;"><strong>属性查询<span style="color: #000000;">。</span></strong></span><br></span></p>
# <p><strong><span style="font-size: 16px;">基于空间位置的查询，也称为<span style="color: #ff0000;">空间查询</span>。</span></strong></p>
# <p>&nbsp;</p><img src="https://img2018.cnblogs.com/blog/1665796/201910/1665796-20191026101437404-1606967348.png" alt="">
# <p><span style="font-size: 16px;"><strong><span style="color: #ff0000;">查询类的基本思路</span>（适用于属性查询以及空间查询）</strong></span></p>
# <p><span style="font-size: 16px;"><strong><img src="https://img2018.cnblogs.com/blog/1665796/201910/1665796-20191026101437404-1606967348.png" alt=""></strong></span></p>
# <p>&nbsp;</p>
# <img src="https://ifdsfdfs.com/blog/" alt="">
# <script></script>
# # <h1></h1>
# # # <script></script>
# # # '''
# # soup=BeautifulSoup(s,'html.parser')
# # ret = soup.find_all()
# # # print(ret)
# # for tag in ret:
# #     # print(tag.name)
# #     if tag.name=='script':
# #         tag.decompose()
# # print(type(str(soup)))
# # print(soup,type(soup))
#
# # print(soup.find_all())
# # ret = soup.find_all('img')
# # for tag in ret:
# #     print(tag.get('src'))
from bs4 import BeautifulSoup
# s='''<p>
# 	&lt;script&gt;alert('火狐')&lt;/script&gt;
# </p>
# <p>
# 	565645
# </p>'''
# soup = BeautifulSoup(s,'html.parser')
# if soup.text
# s='''
# desc
#
#
# 		完美解决textarea输入框提示文字，必须添加默认内容
#
#
# 		<input/>有placeholder标签，可以添加提示文字 ，但是<textarea>没有，一般来说我们是把提示内容写在<textarea>外面，如下图：
#
#
#
# 		当然，这样的布局并不是最想要的效果，
# '''

