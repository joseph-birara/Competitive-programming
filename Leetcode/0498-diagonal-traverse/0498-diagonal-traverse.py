class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         length = len(mat)
#         col_len = len(mat[0])
#         temp_col =0
#         iterator =1
        
#         result_arr = []
        
#         for index in range(length + length-1):
#             if index >=length:
#                 temp = length-1
#             else:
#                 temp = index
            
#             temp_arr = []
#             while temp >-1 and temp_col < col_len:
#                 temp_arr.append(mat[temp][temp_col])
#                 temp -=1
#                 temp_col +=1
                
#             if temp_col >= col_len:
#                 temp_col =iterator
#                 iterator +=1
#             else:
#                 temp_col =0
#             if index %2 ==0:
#                 result_arr.extend(temp_arr)
#             else:
#                 result_arr.extend(reversed(temp_arr))
#         return result_arr
            
                
        d =defaultdict(list)
        length = len(mat)
        col_len = len(mat[0])
        result_arr =[]
        
        
        for index in range(length):
            for index2 in range(col_len):
                d[index+index2].append(mat[index][index2])
                    
        for key,value in d.items():
            if key%2 !=0:
                result_arr.extend(value)
            else:
                result_arr.extend((value[::-1]))
        return result_arr
                    