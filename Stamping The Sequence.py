class Solution(object):
    def movesToStamp(self, stamp, target):
        stamp_len = len(stamp)
        target_len = len(target)
        target = list(target)  
        result = []
        visited = [False] * target_len
        stars = 0 
        
        def can_stamp(pos):
            for i in range(stamp_len):
                if target[pos + i] != '?' and target[pos + i] != stamp[i]:
                    return False
            return True

        def do_stamp(pos):
            count = 0
            for i in range(stamp_len):
                if target[pos + i] != '?':
                    target[pos + i] = '?'
                    count += 1
            return count

        while stars < target_len:
            stamped = False
            for i in range(target_len - stamp_len + 1):
                if not visited[i] and can_stamp(i):
                    stars += do_stamp(i)
                    visited[i] = True
                    result.append(i)
                    stamped = True
                    if stars == target_len:
                        break
            if not stamped:
                return []  

        return result[::-1]  
