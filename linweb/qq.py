a = int(input("其中考(40%)："))
b = int(input("其末考(60%)："))
sum = (a*0.4)+(b*0.6)

if(0<=sum<60):{print("總分",sum,"E")}
elif(sum<=70):{print("總分",sum,"D")}
elif(sum<=80):{print("總分",sum,"C")}
elif(sum<90):{print("總分",sum,"B")}
elif(100>=sum>90):{print("總分",sum,"A")}
else:{print("錯誤囉")}
"""銘傳程式設計作業其中一題"""
"幫同學做沒那麼開心過"