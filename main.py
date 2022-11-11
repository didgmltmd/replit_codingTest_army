def solution(distance, scope, times):
    needBreak = 0;
    for hwarang in range(1,distance + 1):
      for i in range(0,len(scope)):
        if((hwarang >= scope[i][0] and hwarang <= scope[i][1]) or (hwarang <= scope[i][0] and hwarang >= scope[i][1])):
          partTime = times[i][0] + times[i][1];
          
          if(hwarang > partTime and (hwarang % partTime) != 0):
            checkTime = hwarang % partTime;
          else:
            checkTime = partTime;

          if((checkTime - times[i][0])<0):
            needBreak = 1;
            break;
          
      if(needBreak == 1):
        break;
    print("결과: " , hwarang);        


solution(10,[[3, 4], [5, 8]],[[2, 5], [4, 3]])
solution(12,[[7, 8], [4, 6], [11, 10]],[[2, 2], [2, 4], [3, 3]])

