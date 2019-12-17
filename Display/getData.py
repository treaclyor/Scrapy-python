import pymysql
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def getdata(old_list, new_list):
    for data in old_list:
        data = data[0]
        new_list.append(data)


if __name__=="__main__":

    try:
        div_price_count = []    #大连各段房价房子数量
        country_price = []
        conn = pymysql.connect(
            host="localhost", user="root", password="taistrive0900",
            database="house", port=3306, charset='utf8'
        )
        cursor = conn.cursor()
        sql1 = "select focus from dalian_salehouse"     #选择大连的关注人数
        sql2 = "select price from dalian_salehouse"     #选择大连的房价
        sql3 = "select per_price from dalian_salehouse" #选择大连每平米的房价
        sql4 = "select style from dalian_salehouse"     #选择大连房子的户型
        dalian_price_max150 = "select count(price) from dalian_salehouse where price >= 0 && price < 150"       #筛选大连房子价格
        dalian_price_max300 = "select count(price) from dalian_salehouse where price >= 150 && price < 300"    #筛选大连房子价格
        dalian_price_max450 = "select count(price) from dalian_salehouse where price >= 300 && price < 450"    #筛选大连房子价格
        dalian_price_max = "select count(price) from dalian_salehouse where price >= 450"                       #筛选大连房子价格

        #获取十大城市的平均每平米房价
        dalian_perprice = "select avg(per_price) from dalian_salehouse"
        beijing_perprice = "select avg(per_price) from beijing_salehouse"
        changsha_perprice = "select avg(per_price) from changsha_salehouse"
        changchun_perprice = "select avg(per_price) from changchun_salehouse"
        chengdu_perprice = "select avg(per_price) from chengdu_salehouse"
        shenzhen_perprice = "select avg(per_price) from shenzhen_salehouse"
        shanghai_perprice = "select avg(per_price) from shanghai_salehouse"
        nanjing_perprice = "select avg(per_price) from nanjing_salehouse"
        shenyang_perprice = "select avg(per_price) from shenyang_salehouse"
        xiamen_perprice = "select avg(per_price) from xiamen_salehouse"

        #十大城市的用户对于房子大小的需求量
        dalian_house_size_MAX60 = "select count(focus) from dalian_salehouse where house_size > 0 && house_size <= 60"
        beijing_house_size_MAX60 = "select count(focus) from beijing_salehouse where house_size > 0 && house_size <= 60"
        changsha_house_size_MAX60 = "select count(focus) from changsha_salehouse where house_size > 0 && house_size <= 60"
        changchun_house_size_MAX60 = "select count(focus) from changchun_salehouse where house_size > 0 && house_size <= 60"
        chengdu_house_size_MAX60 = "select count(focus) from chengdu_salehouse where house_size > 0 && house_size <= 60"
        shenzhen_house_size_MAX60 = "select count(focus) from shenzhen_salehouse where house_size > 0 && house_size <= 60"
        shanghai_house_size_MAX60 = "select count(focus) from shanghai_salehouse where house_size > 0 && house_size <= 60"
        nanjing_house_size_MAX60 = "select count(focus) from nanjing_salehouse where house_size > 0 && house_size <= 60"
        shenyang_house_size_MAX60 = "select count(focus) from shenyang_salehouse where house_size > 0 && house_size <= 60"
        xiamen_house_size_MAX60 = "select count(focus) from xiamen_salehouse where house_size > 0 && house_size <= 60"

        dalian_house_size_MAX120 = "select count(focus) from dalian_salehouse where house_size > 60 && house_size <= 120"
        beijing_house_size_MAX120 = "select count(focus) from beijing_salehouse where house_size > 60 && house_size <= 120"
        changsha_house_size_MAX120 = "select count(focus) from changsha_salehouse where house_size > 60 && house_size <= 120"
        changchun_house_size_MAX120 = "select count(focus) from changchun_salehouse where house_size > 60 && house_size <= 120"
        chengdu_house_size_MAX120 = "select count(focus) from chengdu_salehouse where house_size > 60 && house_size <= 120"
        shenzhen_house_size_MAX120 = "select count(focus) from shenzhen_salehouse where house_size > 60 && house_size <= 120"
        shanghai_house_size_MAX120 = "select count(focus) from shanghai_salehouse where house_size > 60 && house_size <= 120"
        nanjing_house_size_MAX120 = "select count(focus) from nanjing_salehouse where house_size > 60 && house_size <= 120"
        shenyang_house_size_MAX120 = "select count(focus) from shenyang_salehouse where house_size > 60 && house_size <= 120"
        xiamen_house_size_MAX120 = "select count(focus) from xiamen_salehouse where house_size > 60 && house_size <= 120"

        dalian_house_size_MAX180 = "select count(focus) from dalian_salehouse where house_size > 120 && house_size <= 180"
        beijing_house_size_MAX180 = "select count(focus) from beijing_salehouse where house_size > 120 && house_size <= 180"
        changsha_house_size_MAX180 = "select count(focus) from changsha_salehouse where house_size > 120 && house_size <= 180"
        changchun_house_size_MAX180 = "select count(focus) from changchun_salehouse where house_size > 120 && house_size <= 180"
        chengdu_house_size_MAX180 = "select count(focus) from chengdu_salehouse where house_size > 120 && house_size <= 180"
        shenzhen_house_size_MAX180 = "select count(focus) from shenzhen_salehouse where house_size > 120 && house_size <= 180"
        shanghai_house_size_MAX180 = "select count(focus) from shanghai_salehouse where house_size > 120 && house_size <= 180"
        nanjing_house_size_MAX180 = "select count(focus) from nanjing_salehouse where house_size > 120 && house_size <= 180"
        shenyang_house_size_MAX180 = "select count(focus) from shenyang_salehouse where house_size > 120 && house_size <= 180"
        xiamen_house_size_MAX180 = "select count(focus) from xiamen_salehouse where house_size > 120 && house_size <= 180"

        dalian_house_size_MAX240 = "select count(focus) from dalian_salehouse where house_size > 180 && house_size <= 240"
        beijing_house_size_MAX240 = "select count(focus) from beijing_salehouse where house_size > 180 && house_size <= 240"
        changsha_house_size_MAX240 = "select count(focus) from changsha_salehouse where house_size > 180 && house_size <= 240"
        changchun_house_size_MAX240 = "select count(focus) from changchun_salehouse where house_size > 180 && house_size <= 240"
        chengdu_house_size_MAX240 = "select count(focus) from chengdu_salehouse where house_size > 180 && house_size <= 240"
        shenzhen_house_size_MAX240 = "select count(focus) from shenzhen_salehouse where house_size > 180 && house_size <= 240"
        shanghai_house_size_MAX240 = "select count(focus) from shanghai_salehouse where house_size > 180 && house_size <= 240"
        nanjing_house_size_MAX240 = "select count(focus) from nanjing_salehouse where house_size > 180 && house_size <= 240"
        shenyang_house_size_MAX240 = "select count(focus) from shenyang_salehouse where house_size > 180 && house_size <= 240"
        xiamen_house_size_MAX240 = "select count(focus) from xiamen_salehouse where house_size > 180 && house_size <= 240"

        dalian_house_size_MIN240 = "select count(focus) from dalian_salehouse where house_size > 240"
        beijing_house_size_MIN240 = "select count(focus) from beijing_salehouse where house_size > 240"
        changsha_house_size_MIN240 = "select count(focus) from changsha_salehouse where house_size > 240"
        changchun_house_size_MIN240 = "select count(focus) from changchun_salehouse where house_size > 240"
        chengdu_house_size_MIN240 = "select count(focus) from chengdu_salehouse where house_size > 240"
        shenzhen_house_size_MIN240 = "select count(focus) from shenzhen_salehouse where house_size > 240"
        shanghai_house_size_MIN240 = "select count(focus) from shanghai_salehouse where house_size > 240"
        nanjing_house_size_MIN240 = "select count(focus) from nanjing_salehouse where house_size > 240"
        shenyang_house_size_MIN240 = "select count(focus) from shenyang_salehouse where house_size > 240"
        xiamen_house_size_MIN240 = "select count(focus) from xiamen_salehouse where house_size > 240"


        cursor.execute(sql1)
        focus = list(cursor.fetchall())     #关注人数
        cursor.execute(sql2)
        price = list(cursor.fetchall())     #房子总价
        cursor.execute(sql4)
        style = list(cursor.fetchall())     #房子类型

        #获取分段的值
        cursor.execute(dalian_price_max150)
        div_price_count.append(cursor.fetchone())
        cursor.execute(dalian_price_max300)
        div_price_count.append(cursor.fetchone())
        cursor.execute(dalian_price_max450)
        div_price_count.append(cursor.fetchone())
        cursor.execute(dalian_price_max)
        div_price_count.append(cursor.fetchone())

        #获取十大城市平均房价
        cursor.execute(dalian_perprice)    #大连平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(beijing_perprice)           #北京平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(changsha_perprice)       #长沙平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(changchun_perprice)       #长春平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(chengdu_perprice)  # 成都平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(shenzhen_perprice)  # 深圳平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(shanghai_perprice)   #上海平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(nanjing_perprice) #南京平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(shenyang_perprice)   #沈阳平均房价
        country_price.append(cursor.fetchone())
        cursor.execute(xiamen_perprice)  # 厦门平均房价
        country_price.append(cursor.fetchone())

        country_house_size_MAX60 = []
        #获取十大城市用户对房子平米数的关注程度
        cursor.execute(dalian_house_size_MAX60)  # 大连对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(beijing_house_size_MAX60)  # 北京对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(changsha_house_size_MAX60)  # 长沙对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(changchun_house_size_MAX60)  # 长春对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(chengdu_house_size_MAX60)  # 成都对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(shenzhen_house_size_MAX60)  # 深圳对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(shanghai_house_size_MAX60)  # 上海对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(nanjing_house_size_MAX60)  # 南京对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(shenyang_house_size_MAX60)  # 沈阳对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())
        cursor.execute(xiamen_house_size_MAX60)  # 厦门对于小于60平米的关注人数
        country_house_size_MAX60.append(cursor.fetchone())

        country_house_size_MAX120 = []
        # 获取十大城市用户对房子平米数的关注程度
        cursor.execute(dalian_house_size_MAX120)  # 大连对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(beijing_house_size_MAX120)  # 北京对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(changsha_house_size_MAX120)  # 长沙对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(changchun_house_size_MAX120)  # 长春对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(chengdu_house_size_MAX120)  # 成都对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(shenzhen_house_size_MAX120)  # 深圳对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(shanghai_house_size_MAX120)  # 上海对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(nanjing_house_size_MAX120)  # 南京对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(shenyang_house_size_MAX120)  # 沈阳对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())
        cursor.execute(xiamen_house_size_MAX120)  # 厦门对于小于120平米的关注人数
        country_house_size_MAX120.append(cursor.fetchone())

        country_house_size_MAX180 = []
        # 获取十大城市用户对房子平米数的关注程度
        cursor.execute(dalian_house_size_MAX180)  # 大连对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(beijing_house_size_MAX180)  # 北京对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(changsha_house_size_MAX180)  # 长沙对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(changchun_house_size_MAX180)  # 长春对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(chengdu_house_size_MAX180)  # 成都对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(shenzhen_house_size_MAX180)  # 深圳对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(shanghai_house_size_MAX180)  # 上海对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(nanjing_house_size_MAX180)  # 南京对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(shenyang_house_size_MAX180)  # 沈阳对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())
        cursor.execute(xiamen_house_size_MAX180)  # 厦门对于小于180平米的关注人数
        country_house_size_MAX180.append(cursor.fetchone())

        country_house_size_MAX240 = []
        # 获取十大城市用户对房子平米数的关注程度
        cursor.execute(dalian_house_size_MAX240)  # 大连对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(beijing_house_size_MAX240)  # 北京对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(changsha_house_size_MAX240)  # 长沙对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(changchun_house_size_MAX240)  # 长春对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(chengdu_house_size_MAX240)  # 成都对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(shenzhen_house_size_MAX240)  # 深圳对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(shanghai_house_size_MAX240)  # 上海对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(nanjing_house_size_MAX240)  # 南京对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(shenyang_house_size_MAX240)  # 沈阳对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())
        cursor.execute(xiamen_house_size_MAX240)  # 厦门对于小于240平米的关注人数
        country_house_size_MAX240.append(cursor.fetchone())

        country_house_size_MIN240 = []
        # 获取十大城市用户对房子平米数的关注程度
        cursor.execute(dalian_house_size_MIN240)  # 大连对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(beijing_house_size_MIN240)  # 北京对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(changsha_house_size_MIN240)  # 长沙对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(changchun_house_size_MIN240)  # 长春对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(chengdu_house_size_MIN240)  # 成都对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(shenzhen_house_size_MIN240)  # 深圳对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(shanghai_house_size_MIN240)  # 上海对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(nanjing_house_size_MIN240)  # 南京对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(shenyang_house_size_MIN240)  # 沈阳对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())
        cursor.execute(xiamen_house_size_MIN240)  # 厦门对于大于240平米的关注人数
        country_house_size_MIN240.append(cursor.fetchone())



        conn.commit()
        focus_list = []                                 #房屋关注人数
        price_list = []                                 #房屋价格
        style_list = []                                 #房屋类型
        new_div_price_count = []                                                #饼状图房价范围
        price_label = ['0-150万','150-300万','300-450万','450万以上']     #饼状图标签
        percent_priceList = []          #百分比列表
        new_country_house_size_MAX60 = []
        new_country_house_size_MAX120 = []
        new_country_house_size_MAX180 = []
        new_country_house_size_MAX240 = []
        new_country_house_size_MIN240 = []

        #将其转换为列表类型
        getdata(div_price_count,new_div_price_count)
        getdata(focus,focus_list)
        getdata(style,style_list)
        getdata(country_house_size_MAX60,new_country_house_size_MAX60)
        getdata(country_house_size_MAX120, new_country_house_size_MAX120)
        getdata(country_house_size_MAX180, new_country_house_size_MAX180)
        getdata(country_house_size_MAX240, new_country_house_size_MAX240)
        getdata(country_house_size_MIN240, new_country_house_size_MIN240)

        #算百分比
        for price_per in new_div_price_count:
            percent_priceList.append(price_per/sum(new_div_price_count)*100)
        avg_country_price = []
        #平均城市房价
        for i in country_price:
            i = int(i[0])
            avg_country_price.append(i)
        #print(avg_country_price)

        sum_country_label = ['大连', '北京', '长沙', '长春', '成都', '深圳', '上海', '南京', '沈阳', '厦门']
        sum_countryPrice = zip(avg_country_price,sum_country_label)         #采用zip方式进行打包
        sorted_sum_countryPrice = sorted(sum_countryPrice,reverse=True)     #按照降序排列
        sort_sum_contry_label = []      #排序之后的城市房价列表
        sort_country_price = []      #排序之后的城市名字
        for item in sorted_sum_countryPrice:
           sort_country_price.append(item[0])   #排序之后的各大城市平均房价
           sort_sum_contry_label.append(item[1])    #排序之后的各大城市标签

        # 解决中文显示问题
        plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        #查看用户对哪个房型的需求量更高一些
        x1 = np.array(style_list)    #房型列表转换成numpy.array类型
        y1 = np.array(focus_list)    #关注人数列表转换成numpy.array类型
        fig = plt.figure(figsize=(8, 4))   #设置更大画布
        plt.xticks(rotation=-30)    #设置倾斜角度
        #x轴，y轴，柱体宽度，柱体颜色
        plt.bar(x1, y1, width = 0.5,color=['b','r','g','y','c','m','y','k','c','g','r','k','g','y','c','b','r','g','y'])
        plt.xlabel("房型")    #x轴显示标签
        plt.ylabel("关注人数")  #y轴显示标签
        plt.title('大连市用户对房型的需求量')  #标题
        plt.show()

        #查看用户对价格的关注程度
        fig = plt.figure(figsize=(8, 4))
        #每块的值，将某一块分割出来，价格标签，饼状图颜色，保留小数，数值距离圆心半径倍数的距离，显示阴影
        plt.title("大连市用户对于房子价格的关注程度")
        plt.pie(percent_priceList,explode=(0.1,0,0,0),labels=price_label,colors=['r','y','b','g'],autopct='%3.2f%%',pctdistance=0.6,shadow=True)
        #x,y轴刻度一致，保证是一个圆形
        plt.axis('equal')
        plt.show()

        x2 = np.array(sort_sum_contry_label)  # 城市列表转换成numpy.array类型
        y2 = np.array(sort_country_price)  # 每平米房价列表转换成numpy.array类型
        fig = plt.figure(figsize=(8, 4))  # 设置更大画布
        # x轴，y轴，柱体宽度，柱体颜色
        plt.bar(x2, y2, width=0.5,
                color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g'])
        plt.xlabel("城市")  # x轴显示标签
        plt.ylabel("每平米房价")  # y轴显示标签
        plt.title('十大城市的每平米房价')  # 标题
        plt.show()


        #查看全国人对房子大小的关注程度
        fig = plt.figure(figsize=(8, 4))
        plt.title("十大城市用户对于房子大小的需求量")
        plt.plot(sum_country_label,new_country_house_size_MAX60, color = 'r',label='小于等于60㎡')   #一条折线
        plt.plot(sum_country_label, new_country_house_size_MAX120, color='y', label='大于60㎡并且小于120㎡')
        plt.plot(sum_country_label, new_country_house_size_MAX180, color='g', label='大于120㎡并且小于180㎡')
        plt.plot(sum_country_label, new_country_house_size_MAX240, color='b', label='大于180㎡并且小于240㎡')
        plt.plot(sum_country_label, new_country_house_size_MIN240, color='k', label='大于240㎡')
        plt.legend(bbox_to_anchor=(1, 1))    #设置图例和其中的文本显示第二个参数 bbox_to_anchor 被赋予的二元组中，
        # num1 用于控制 legend 的左右移动，值越大越向右边移动，num2 用于控制 legend 的上下移动，值越大，越向上移动。用于微调图例的位置。
        plt.show()      #显示图片

    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()