# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        # use bfs
        # maintain a visited set
        
        que = deque([startUrl])
        visited = set()
        visited.add(startUrl)
        res = []
        hostname = startUrl.split("/")[2]
        while que:
            url = que.popleft()
            res += url,
            for child in htmlParser.getUrls(url):
                if child not in visited and hostname in child:
                    que.append(child)
                    visited.add(child)
                    
            
        return res