class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def valid_ip4(var):
            temp = var.split('.')
            n = len(temp)
            if n != 4:
                return False
            for el in temp:
                if not el.isdigit():
                    return False
                if el and ((el[0] == '0' and len(el) >1) or int(el)>255):
                    return False
            return True

        def valid_ip6(var):
            temp = var.split(':')
            n = len(temp)
            if n != 8:
                return False
            for el in temp:
                if len(el)>4 or not el:
                    return False
                for char in el:
                    if not ('A'<= char<='F' or 'a'<=char <='f' or '0' <= char <= '9'):
                        return False
            return True

        if valid_ip6(queryIP):
            return "IPv6"
        if valid_ip4(queryIP):
            return "IPv4"
        
        return "Neither"


        
