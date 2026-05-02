class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_id_to_list = {}

        for word in strs:
            anagram_id = "".join(sorted(word))
            if anagram_id in anagram_id_to_list:
                anagram_id_to_list[anagram_id].append(word)
            else:
                anagram_id_to_list[anagram_id] = [word]
        
        result_list = []
        for result in anagram_id_to_list.values():
            result_list.append(result)

        return result_list

