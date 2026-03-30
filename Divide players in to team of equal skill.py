class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        chem=0
        l=0
        r=len(skill)-1
        while l<r:
            if skill[l] + skill[r]!=target:
                return -1
            chem+=skill[l]*skill[r]
            l+=1
            r-=1
        return chem
