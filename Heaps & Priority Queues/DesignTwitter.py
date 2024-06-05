class Twitter:

    def __init__(self):
        """
        for following: key = user, values = list of userId they follow
        for posts: key = user, values = list of posts they made
        time is decremented at each step
        """
        self.following = {}
        self.posts = {} 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        if userId not in self.following.keys():
            self.following[userId] = [userId]
        if userId not in self.posts.keys():
            self.posts[userId] = [(self.time, tweetId)]
        else:
            self.posts[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.time-=1
        """
        we go through each following account which includes self and scrutenize
        we need list of array formatted (-time, tweetId)
        """
        if userId not in self.following.keys() and userId not in self.posts.keys():
            return []
        elif userId not in self.following.keys() and userId in self.posts.keys():
            arr = self.posts[userId]
        else:
            arr = []
            follower_list = self.following[userId]
            for id in follower_list:
                if id in self.posts.keys():
                    arr = arr + self.posts[id]
        heapq.heapify(arr)
        count = 10
        res = []
        while count != 0 and len(arr) != 0:
            _, tweetId = heapq.heappop(arr)
            res.append(tweetId)
            count-=1
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time-=1
        if followerId not in self.following.keys():
            self.following[followerId] = [followerId, followeeId]
        elif followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time-=1
        if followerId in self.following.keys():
            arr = self.following[followerId]
            if followeeId in arr:
                arr.remove(followeeId)
                self.following[followerId] = arr


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)