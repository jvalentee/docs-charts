import matplotlib.pyplot as plt
import numpy as np


def genesisMinted(x, _locktime, _cap, _nativeTokenFactor):

    mintedRewards = 0
    mintedNFTs = 0
    if pow(x, 2) * 2 > _cap:
        mintedNFTs = 0
    else:
        mintedNFTs = pow(x, 2) * 2

    for i in range(0, mintedNFTs):
        mintedRewards += (_locktime*(_cap - i / 2)) / \
            _nativeTokenFactor * 1e18

    return mintedRewards


def rewardsMinted(x, _initialRewards):
    mintedRewards = 0
    for j in range(0, x):
        mintedRewards += weeksRewards(j, _initialRewards)

    return mintedRewards


def weeksRewards(x, _initialRewards):
    if x/7 < 52:
        return (_initialRewards * i/7) / 52
    else:
        return _initialRewards / (pow(2, (i/7 / 52)))


# Define the input values for x (weeks)
x = np.linspace(0, 6*1, 6*1+1, dtype=int)

# Set the values for the function parameters
_cap = 4999
_nativeTokenFactor = 100
# 30 days medium locktime
_locktime = 3600*24*30
# initial rewards
_initialRewards = 1000000

# Evaluate the function for each input value of x
y = []
thisWeeksRewardsArray = []
genesisMintedSumArray = []
rewardsMintedSumArray = []

for i in range(len(x)):
    thisWeeksRewards = weeksRewards(i, _initialRewards)
    thisWeeksRewardsArray.append(thisWeeksRewards)
    genesisMintedSum = genesisMinted(i, _locktime, _cap, _nativeTokenFactor)
    genesisMintedSumArray.append(genesisMintedSum)
    rewardsMintedSum = rewardsMinted(i, _initialRewards)
    rewardsMintedSumArray.append(rewardsMintedSum)

    if genesisMintedSum + rewardsMintedSum == 0:
        y.append(0)
    else:
        y.append(thisWeeksRewards / (genesisMintedSum + rewardsMintedSum))

print("thisWeeksRewardsArray", thisWeeksRewardsArray)
print("genesisMintedSumArray", genesisMintedSumArray)
print("rewardsMintedSumArray", rewardsMintedSumArray)
print("x", x)
print("y", y)

# Generate a plot of the function
plt.plot(x, y)
plt.xlabel('Weeks')
plt.ylabel('APR (%)')
plt.title('leNFT Launch Model')
plt.show()
