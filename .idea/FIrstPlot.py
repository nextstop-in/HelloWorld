import matplotlib.pyplot as view


views=[123,245,765,444,321,546,345]
users=[154,353,635,836,765,937,231]
subscribers=[90,80,70,60,50,40,30]
days= range(1,8)

#Here 8 is excluded and no jumps has been mentioned eg : range(1,8,2) means 1,3,5,7 and range(1,8) means
# 1,2,3,4,5,6,7
view.xlabel('No. Of Days')
view.ylabel('Views')

view.plot(days,views, label='Youtube Views',color='r',marker='o',linestyle='-.',linewidth=1.5)# plot(x-axis,y-axis)
view.plot(days,subscribers,label='Subscribers',color='g',marker='o')

view.plot(days,users,label='No. Of Users',marker='o')
view.title('Views On A Daily Basis')
view.legend(loc='upper left')
view.ylim(0,1000)
view.grid(True)
view.show()