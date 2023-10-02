class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        alice_count = bob_count = 0

        for _ in range(1, n - 1):
            if colors[_] == 'A' and colors[_ - 1] == 'A' and colors[_ + 1] == 'A':
                alice_count += 1
            elif colors[_] == 'B' and colors[_ - 1] == 'B' and colors[_ + 1] == 'B':
                bob_count += 1
        
        if alice_count > bob_count:
            return True
        else:
            return False