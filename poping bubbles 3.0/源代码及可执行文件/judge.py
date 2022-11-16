# 判断position是否位于area内
def judge_in(position, area):
    x, y = position
    [(x1, x2), (y1, y2)] = area
    if x1<x<x2 and y1<y<y2:
        return True
    else:
        return False

def judge_level(score):
    level = score//200 + 1

    level_up = False
    if (not(score%200)) and score:
        level_up = True
        
    return (level, level_up)