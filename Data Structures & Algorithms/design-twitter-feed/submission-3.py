class Twitter:

    def __init__(self):
        self.following = collections.defaultdict(set)
        self.posts = collections.defaultdict(list)
        self.postId = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.postId, tweetId))
        self.postId += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = self.posts[userId].copy()
        for followee in self.following[userId]:
            res.extend(self.posts[followee])
        res.sort(reverse=True)
        return [post_id for (_, post_id) in res[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
