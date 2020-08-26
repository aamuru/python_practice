class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        |arr[i] - arr[j]| <= a
        |arr[j] - arr[k]| <= b
        |arr[i] - arr[k]| <= c
        """
        triplets=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if abs(arr[i] - arr[j])<=a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k])<= c:
                        triplets+=1
        return triplets