import string
import heapq

def main():
    # Question: You have a list of possible features that your team could be working on next, but resource is limited.
    #   Therefore, you will need to find the most popular features to implement.
    #   Given a list of possible features represented by 1 word strings
    #   AND given a list of feature requests; comments scraped from an online forum discussing your product (words/sentences + punctuation)
    #   AND given the number of feature your team has capcity for
    #   Figure out which features to implement, via popularity

    # Test Case
    teamCapacity = 2
    possibleFeatures = ['audio', 'anello', 'apple', 'aiml', 'screen', 'glass']
    featureRequests = [
        'I just want that audio feature to become a reality bro!',
        'audio stuff! yeah! would be soo cool',
        'anello isn\' half bad either, would be nice.',
        'oh my god, totally agree, anello would be great!',
        'aiml is where it\'s at my boys!',
        'bigger screen would be good too',
        'as big as apple products, I want that 12-14inch stuff!',
        'would be nice if they used fiber glass, i really like those',
        'yeah! or like destroyer glass! they are really nice!',
        'I dig apple stuff, but this would be something if it had anello, aiml, doop glass, etc. I would buy it.'
    ]

    print("The team should implement: {0}".format(implementFeatures(teamCapacity, possibleFeatures, featureRequests)))

def implementFeatures(teamCapacity, possibleFeatures, featureRequests):
    # teamCapacity -> int; number of features the team is capable of implementing
    # possibleFeatures -> [] of str; possible features that could be implemented
    # featureRequests -> [] of str; feature requests from users

    # create a dictionary for O(1) access to each possible feature
    featureDict = {}
    for possibleFeature in possibleFeatures:
        featureDict[possibleFeature] = 0

    for feature in featureRequests:
        words = feature.translate(str.maketrans('', '', string.punctuation)).split(' ')
        for word in words:
            if word in featureDict:
                featureDict[word] += 1
    
    # construct a max heap, ideally done in O(n); however, heapq only supports O(nlogn)
    heap = []
    heaplen = len(featureDict)
    for key, value in featureDict.items():
        heapq.heappush(heap, (-value, key))

    # list out the top features
    topFeatures = []
    for i in range(teamCapacity):
        if i < heaplen:
            topFeatures.append(heapq.heappop(heap)[1])
    
    return topFeatures

def printHeap(heap):
    while heap:
        next_item = heapq.heappop(heap)
        print(next_item)

if __name__ == "__main__":
    main()