class Twitter:

    def __init__(self):
        self.follower = {}
        self.posts = {}
        self.time = 0
        """
        follow will be follower id as key and list of followee id including themselves as list as the value
        posts will be user id as key and list of posts under user id as list as the value
        time will be decremented for each function call so that the most negative is least and that translates to most recent
        """

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        if userId not in self.follower.keys():
            self.follower[userId] = [userId]
        if userId not in self.posts.keys():
            self.posts[userId] = [(self.time, tweetId)]
        else:
            self.posts[userId].append((self.time, tweetId))
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.time-=1
        arr = []
        if userId not in self.follower.keys():
            if userId not in self.posts.keys():
                return []
            else:
                arr = self.posts[userId]                    
        else:
            """
            The user does follow someone
            """
            for followId in self.follower[userId]:
                if followId in self.posts.keys():
                    arr = arr + self.posts[followId]
        heapq.heapify(arr)
        res, count = [], 0
        while len(arr) != 0 and count != 10:
            res.append(heapq.heappop(arr)[-1])
            count+=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time-=1
        if followerId in self.follower.keys() and followeeId not in self.follower[followerId]:
            self.follower[followerId].append(followeeId)
        elif followerId not in self.follower.keys():
            self.follower[followerId] = [followerId, followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.time-=1
        if followerId in self.follower.keys() and followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)