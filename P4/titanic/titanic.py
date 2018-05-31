
# coding: utf-8

# ## 机器学习P4 探索数据集项目——《泰坦尼克号生还探测》

# ### 数据集选择
#     泰坦尼克号数据：包括泰坦尼克号上 2224 名乘客和船员中 891 名的人口学数据和乘客基本信息。数据集来自Kaggle。

# ### 探索问题
# 
#     1.探索不同性别的存活率
#     2.探索不同年龄段的存活率
#     3.探索不同仓位的存活率
#     4.探索不同票价的存活率
#     5.探索不同登船港口的存活率

# ### 数据导入+清洗

# In[143]:


# 引入所需要的类库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic(u'matplotlib inline')


# In[144]:


# 导入数据
titanic_df = pd.read_csv('./titanic-data.csv')
# 了解数据情况
titanic_df.info()


# 分析数据：从以上数据可以看出字段Age、Cabin都有NaN的情况，下一步删除NaN的记录

# In[145]:


# 为了提升效率，删除不相关字段
non_titanic_df = titanic_df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin'], axis = 1)


# In[146]:


# 通用函数,删除data中指定字段的NaN的记录
def clean_data_nan(data, subset):
    return data.dropna(subset = subset)


# In[147]:


# 清除对应字段的NaN记录
titanic_age_survived = clean_data_nan(non_titanic_df, ['Survived','Age'])
titanic_embarked_survived = clean_data_nan(non_titanic_df, ['Survived','Embarked'])

print len(titanic_age_survived)
print len(titanic_embarked_survived)


# In[148]:


non_titanic_df.describe()


# 从以上信息可以看出,平均生还率约38%

# ### 数据分析, 函数实现

# In[149]:


# 通用函数，判断指定因素对存活率的影响
def influence(data,element):
    # 判断**对存活率的影响
    groupby_element = data.groupby(element)
    total_groupby_element = groupby_element.count()
    survived_groupby_element = groupby_element.sum()

    # **的生还人数
    print("生还人数")
    print(survived_groupby_element)
    # **的总人数
    print("总人数")
    print(total_groupby_element)
    # **的生还率
    print("生还率")
    survived_rate_element = survived_groupby_element / total_groupby_element
    print(survived_rate_element)
    # 直方图**的生还率
    survived_rate_element.plot(kind='bar')
    plt.title(element + 'Survival rate')
    plt.xlabel(element)
    plt.ylabel('survived')
    plt.show()


# In[150]:


# 通用分组
def cla(n, lim):
    if n == 0:
        return 'unknown'
    return '[%d, %d)' % (lim * (n // lim), lim * (n // lim) + lim)

# 通用函数, 判断指定因素, 指定区间对存活率的影响
def section_influence(data, element, lim):

    section_group = pd.DataFrame({
        'element_group': [cla(section, lim) for section in data[element]]
    })

    groupby_section = pd.concat([data['Survived'], section_group], axis=1)

    groupby_element = groupby_section.groupby('element_group')
    total_groupby_element = groupby_element.count()
    survived_groupby_element = groupby_element.sum()

    # 分组的生还人数
    print(survived_groupby_element)
    # 分组的总人数
    print(total_groupby_element)
    # 分组的生还率
    survived_rate_element = survived_groupby_element / total_groupby_element
    print(survived_rate_element)
    # 直方图分组的生还率
    survived_rate_element.plot(kind='bar')
    plt.title(element + 'Survival rate')
    plt.xlabel(element)
    plt.ylabel('survived')
    survived_rate_element.plot(kind='pie',subplots=True)
    plt.show()


# In[151]:


# 性别对存活率的影响
influence(non_titanic_df, 'Sex')


# 分析结果：女性的存活率较高约为74%

# In[152]:


# 年龄对存活率的影响
section_influence(titanic_age_survived, 'Age', 20)


# 分析结果：年龄段在20～40岁之间的存活率较高

# In[153]:


# 仓位对存活率的影响
influence(non_titanic_df, 'Pclass')


# 分析结果：客舱级别为1的存活率较高约为63%

# In[154]:


# 票价对存活率的影响
section_influence(titanic_age_survived, 'Fare', 100)


# 分析结果：票价在100～200之间的存活率较高约65%

# In[155]:


# 登船港口对存活率的影响
influence(titanic_embarked_survived, 'Embarked')


# 分析结果：登船港口为C的生还率较高约55%

# ### 结论
#     泰坦尼克号的总人数大概有2200多,乘客有1300多,样本中的900左右数据量虽然不是全部人员的数据,但是就乘客而言样本数量所占比例已然接近70%,根据我们分析的结果显示舱位等级和性别对存活率有较大的影响,由于数据不完整且有缺失,分析结果并不一定正确,这种结果只是代表一个较大概率的可能性. 
#     除了样本所提供的因素,其他因素已知或者未知对于存活率的影响也是无法忽视,其中我认为泰坦尼克号上的800多工作人员对存活率的影响是非常大的,工作人员的行为显然可以很大程度引导乘客,目前这方面数据完全空缺,所以不能保证我们的结果是完全正确的.
