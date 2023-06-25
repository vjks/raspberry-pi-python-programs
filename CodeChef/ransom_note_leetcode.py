class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_dict = dict()
        mag_dict = dict()
        for char in ransomNote:
            if char not in note_dict:
                note_dict[char] = 1
            else: 
                note_dict[char] = note_dict[char] + 1
        for c in magazine:
            if c not in mag_dict:
                mag_dict[c] = 1
            else:
                mag_dict[c] = mag_dict[c] + 1
        possible = None

        for key in note_dict.keys():
            if key in mag_dict:
                if note_dict[key] <= mag_dict[key]:
                    possible = True
                else:
                    possible = False
                    break
            else:
                possible = False
                break
        return possible