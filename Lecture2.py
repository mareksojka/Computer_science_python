# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:38:02 2017

@author: marek
"""

s = 'azcbobobegghakl'
alphabet='abcdefghijklmnopqrstuvwxyz'
alpha_index=[]
alpha_lenght_list=[]
alpha_index_list=[]
alpha_start_index=0
alpha_lenght=0
for index,letter in enumerate(s):
    alpha_index.append(alphabet.find(s[index]))
    #print(alpha_index)
    if index>0:
        if alpha_index[index]>=alpha_index[index-1]:
            alpha_lenght+=1
            #alpha_lenght_list.append(alpha_lenght)
            #alpha_index_list.append(alpha_start_index)
            #print("alpha_lenght:",alpha_lenght)
        elif alpha_index[index]<alpha_index[index-1]:
            alpha_start_index=index
            alpha_lenght=0
           # print("alpha_lenght:",alpha_lenght)
            #print("alpha_index:",alpha_start_index)
    alpha_lenght_list.append(alpha_lenght)
    alpha_index_list.append(alpha_start_index)
print("alpha_lenght_list",alpha_lenght_list)
print("alpha_index_list",alpha_index_list)
max_lenght_string=max(alpha_lenght_list)
max_lenght_string_index=alpha_index_list[alpha_lenght_list.index(max(alpha_lenght_list))]
#print(max_lenght_string)
#print(max_lenght_string_index)
print("Longest substring in alphabetical order is:",s[max_lenght_string_index:max_lenght_string_index+max_lenght_string+1])