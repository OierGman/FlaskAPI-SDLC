'''
The following information is the coefficients of each variable in our mathematical analysis
model and allows us to formulate an equation such as the one below where each value is multiplied
by the relevant information passed.

# predict_y = 255565.408464x1 - 308139.564241x2 + 396790.685117x3 + 298342.349600x4  -
# 171475.121333x5 - 215518.349143x6 + 177999.88870660076

# x1 => ROOMS
# x2 => bungalow
# x3 => detached
# x4 => flats
# x5 => semi-detached
# x6 => terraced
'''


Rooms = 255565.408464
bungalow = B = -308139.564241
detached = D = 396790.685117
flat = F = 298342.349600
semidetached = SD = -171475.121333
terraced = T = -215518.349143
Constant = 177999.88870660076

property_type = [B, D, F, SD, T]

# main formula
predict_formula = Rooms - B + D + F - SD - T + Constant

def result_prediction(room, type):
    result = Rooms*room
    for i in property_type:
        if type == i:
            result+=i
    result+=Constant
    return int(round(result,0))

