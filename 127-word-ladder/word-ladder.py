class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)     #convert list to set for (1) lookup
        if endWord not in wordSet:
            return 0
            
        neigh = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern  = word[:j] + "*" + word[j + 1:]
                neigh[pattern].append(word)

        visit = set([beginWord])
        dq = deque([beginWord])    
        res = 1
        while dq:
            for i in range(len(dq)):
                word = dq.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern  = word[:j] + "*" + word[j + 1:]
                    for neiWord in neigh[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            dq.append(neiWord)
            res += 1

        return 0

        