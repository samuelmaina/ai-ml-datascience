import numpy as np
import matplotlib.pyplot as plt;


from sklearn.metrics import r2_score

np.random.seed(2)

pageSpeeds= np.random.normal(3.0, 1.0, 100)
purchaseAmount= np.random.normal(50.0, 30.0, 100)/pageSpeeds


plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

#split the data into 80% as testing data and 20% of the testing
#data.

#Data is shuffled in the real world, not going
trainX= pageSpeeds[:80]
testX= pageSpeeds[80:]

trainY= purchaseAmount[:80]
testY= purchaseAmount[80:]


plt.scatter(trainX, trainY);


x=np.array(trainX)
y=np.array(trainY)


#fit an 8 degree polynomial to the data.
p8= np.poly1d(np.polyfit(x, y, 8))


xp= np.linspace(0, 7, 100)
axes= plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(x,y);
plt.plot(xp,p8(xp),c='r')
plt.show()
    



testx=np.array(testX)
testy= np.array(testY)

axes= plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(testx, testy)
plt.plot(xp, p8(xp),c='r')
plt.show()


#measure how well the fitting was done
r2=r2_score(y,p8(x))

print(r2)
