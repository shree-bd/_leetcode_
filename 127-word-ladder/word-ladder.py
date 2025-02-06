class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)     #convert list to set for (1) lookup
        if endWord not in wordSet:
            return 0
            
        neigh = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern  = word[:j] + "*" + word[j + 1:]
                neigh[pattern].append(word)

        # BFS 
        visit = set([beginWord])
        dq = deque([(beginWord, 1)])    

        while dq:
            word, steps = dq.popleft()

            if word == endWord:
                return steps
                
            for j in range(len(word)):
                pattern  = word[:j] + "*" + word[j + 1:]
                    
                for neiWord in neigh[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        dq.append((neiWord, steps + 1))
                    
                neigh[pattern] = []

        return 0

        