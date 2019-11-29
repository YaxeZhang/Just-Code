class Solution():
    def maxScoreWords(self, words, letters, score):
        self.max_score = 0
        words_score = [sum(score[ord(c)-ord('a')] for c in word) for word in words]
        words_counter = [collections.Counter(word) for word in words]
        
        def dfs(i, curr_score, counter):
            if curr_score + sum(words_score[i:]) <= self.max_score:
                return
            self.max_score = max(self.max_score, curr_score)
            for j, wcnt in enumerate(words_counter[i:], i):
                if all(n <= counter.get(c,0) for c,n in wcnt.items()):
                    dfs(j+1, curr_score+words_score[j], {c:n-wcnt.get(c,0) for c,n in counter.items()})
        
        dfs(0, 0, collections.Counter(letters))
        return self.max_score