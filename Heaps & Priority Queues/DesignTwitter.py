class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        """
        we have to follow outselves as well
        We can post tweet using timestamp to keep track of most recent to least recent
        """
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followers.keys():
            self.followers[userId] = [userId]
        if userId not in self.tweets.keys():
            self.tweets[userId] = [(-self.time, tweetId)]
        else:
            self.tweets[userId].append((-self.time, tweetId))

        self.time+=1
    def getNewsFeed(self, userId: int) -> List[int]:
        follower_list = self.followers.get(userId, None)
        if follower_list is None:
            return []
        """
        also account for less than 10 tweets
        """
        tweet_list = []
        for follower in follower_list:
            tweet_list = tweet_list + self.tweets.get(follower, [])
        heapq.heapify(tweet_list)
        res = []
        while tweet_list and len(res) != 10:
            node = heapq.heappop(tweet_list)
            res.append(node[-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers.keys():
            self.followers[followerId] = [followerId, followeeId]
        else:
            if followeeId not in self.followers[followerId]:
                self.followers[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)