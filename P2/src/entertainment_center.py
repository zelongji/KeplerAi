#coding=utf-8
import fresh_tomatoes
import media

# 1、变量采用电影名称拼音命名 2、增加电影年代、类型
beibao = media.Movie("背包去环游GO","背包去环游GO","http://img.paas.onairm.cn/27a61b043d1e4d4a866bbe2e214fca24","http://img.paas.onairm.cn/344a33cd7a83fa3c0a7f354f878a9a7cbase","2013","人文/攻略")
quguo = media.Movie("去过","去过","http://img.paas.onairm.cn/48f64b539c26b7cb39746423158705af","http://img.paas.onairm.cn/7aa27ff0402102d4039993af8f81f9c1base","2017","人文/攻略")
haiduimian = media.Movie("海对面","海对面","http://img.paas.onairm.cn/194fafcace521c904a127a9b6a08418d","http://img.paas.onairm.cn/decab3473e37e39d63e398737b36cb75base","2017","人文/攻略")
duonaohe = media.Movie("多瑙河上的星途游轮","多瑙河上的星途游轮","http://img.paas.onairm.cn/9078540c9fc1557926d05fc2180337b3","http://img.paas.onairm.cn/8ad89c0da115698a75ee8a33ae6346f1basephone","2016","人文/风光")
yadianna = media.Movie("雅典娜的羊","雅典娜的羊","http://img.paas.onairm.cn/70c24f3e79cabc0a76f658df89ff514c","http://img.paas.onairm.cn/c628c62005a83c7df99e5f5416bd2886basephone","2015","人文/风光")
qianqian = media.Movie("茜茜公主的美食地图","茜茜公主的美食地图","http://img.paas.onairm.cn/8872ef2f451889619c4540b15528c9da","http://img.paas.onairm.cn/bd1c3cf1b0fe628f744f32131991ab05basephone","2015","人文/风光")
movies = [beibao,quguo,haiduimian,duonaohe,yadianna,qianqian]
fresh_tomatoes.open_movies_page(movies)
