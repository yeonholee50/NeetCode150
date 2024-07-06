class Twitter:

    def __init__(self):
        self.followers = {}
        self.posts = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        if userId not in self.followers.keys():
            self.followers[userId] = [userId]
        if userId not in self.posts.keys():
            self.posts[userId] = [(self.time, tweetId)]
        else:
            self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.time-=1
        
        if userId in self.followers.keys():
            follow_list = self.followers[userId]
            time_tweet_list = []
            for ID in follow_list:
                if ID in self.posts.keys():
                    time_tweet_list = time_tweet_list + self.posts[ID]
            heapq.heapify(time_tweet_list)
            length = min(len(time_tweet_list), 10)
            res = []
            for i in range(length):
                res.append(heapq.heappop(time_tweet_list)[-1])
            return res
        else:
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time-=1
        if followerId not in self.followers.keys():
            self.followers[followerId] = [followerId, followeeId]
        elif followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time-=1
        if followerId in self.followers.keys() and followeeId in self.followers[followerId]:
            follow_list = self.followers[followerId]
            follow_list.remove(followeeId)
            self.followers[followerId] = follow_list


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
