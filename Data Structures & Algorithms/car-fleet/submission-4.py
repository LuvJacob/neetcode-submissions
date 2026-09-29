class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            temp=[]
            times=[]
            for i in range(len(position)):
                temp.append([position[i],speed[i]])
            temp = sorted(temp,key= lambda pair: pair[0], reverse=True)
            for pos, spd in temp:
                time = (target-pos)/spd
                if not times or time> times[-1]:
                    times.append(time)

            return len(times)