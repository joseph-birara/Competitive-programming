class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #to save number of visits 
        frequencyTable = defaultdict(int)
        
        # 
        for domains in cpdomains:
            tempDomain = domains.split()
            subDomain = tempDomain[1].split(".")
            if len(subDomain) == 3:
                frequencyTable[subDomain[1]+"."+ subDomain[2]] +=int(tempDomain[0])
                frequencyTable[subDomain[0]+"."+subDomain[1] + "."+subDomain[2]] +=int(tempDomain[0])
                frequencyTable[subDomain[2]] +=int(tempDomain[0])
            elif len(subDomain) ==2:
                frequencyTable[subDomain[0]+"."+subDomain[1]] +=int(tempDomain[0])
                frequencyTable[subDomain[1]] +=int(tempDomain[0])
        result = []
        for domain in  frequencyTable:
            temp =  str(frequencyTable[domain]) + " " + domain
            result.append(temp)
        return result
        