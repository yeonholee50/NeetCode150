class Twitter:

    def __init__(self):
        self.post = {}        
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        if userId not in self.following.keys():
            self.following[userId] = [userId]
        if userId not in self.post.keys():
            self.post[userId] = [(self.time, tweetId)]
        else:
            self.post[userId].append((self.time, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        self.time-=1
        """
        users are guranteed to follow themselves so we can just get a follow list and append to posts
        """
        follows = []
        posts = []
        if userId in self.following.keys():
            follows = self.following[userId]
            for followId in follows:
                if followId in self.post.keys():
                    posts = posts + self.post[followId]
            heapq.heapify(posts)
            counter = 0
            res = []
            while posts and counter < 10:
                res.append(heapq.heappop(posts)[-1])
                counter+=1
            return res

        else:
            return []
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.time-=1
        if followerId not in self.following.keys():
            self.following[followerId] = [followerId, followeeId]
        elif followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time-=1
        if followerId in self.following.keys() and followeeId in self.following[followerId]:
            followers = self.following[followerId]
            followers.remove(followeeId)
            self.following[followerId] = followers
