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

# initial calculation of coefficients

# Rooms = 255565.408464
# bungalow = B = -308139.564241
# detached = D = 396790.685117
# flat = F = 298342.349600
# semidetached = SD = -171475.121333
# terraced = T = -215518.349143
# Constant = 177999.88870660076
#
# property_type = [B, D, F, SD, T]
#
# # main formula
# predict_formula = Rooms - B + D + F - SD - T + Constant
#
# def result_prediction(room, type):
#     result = Rooms*room
#     for i in property_type:
#         if type == i:
#             result+=i
#     result+=Constant
#     return int(round(result,0))


# updated / refined coefficients that now calculate locational value as a factor
intercept = 7.081e+04
rooms = 8.609e+04

coefficients = {
    "ashford": -8387.7891,
    "aylesford": 5742.2679,
    "bearsted": 2272.7153,
    "birchington": 1.028e+04,
    "broadstairs": 1.981e+04,
    "brogdale": -2.54e+04,
    "canterbury": 2.06e+04,
    "cranbrook": -2.209e+04,
    "dartford": 7.667e+04,
    "deal": -7175.8266,
    "dover": -4.864e+04,
    "edenbridge": 3495.5067,
    "faversham": -1.965e+04,
    "folkestone": 9114.7447,
    "hawkinge": -2.608e+04,
    "hernebay": 2.438e+04,
    "hythe":  2.318e+04,
    "kingshill": -1.294e+04,
    "kingsnorth": -1.464e+04,
    "maidstone": 2.496e+04,
    "margate": 1.853e+04,
    "minster": -2.038e+04,
    "minsterosea": -5.338e+04,
    "newrommeny": -1.389e+05,
    "paddockwood": -7.708e+04,
    "pembury": 2.139e+04,
    "ramsgate": 1.577e+04,
    "royaltonbridgewells": 1.291e+05,
    "sandwich": 2.561e+04,
    "sevenoaks": 1.742e+05,
    "sheerness": -5.633e+04,
    "sittingbourne": -3.004e+04,
    "snodland": 1.396e+04,
    "southborough": 9.787e+04,
    "staplehurst": -2.14e+05,
    "tonbridge": 1.006e+05,
    "westmalling": 2.924e+04,
    "whitfield": -5.469e+04,
    "whitstable": 5.385e+04,
    "b": 4.8e+04,
    "d": 1.102e+05,
    "f": -5.058e+04,
    "sd": -2578.1692,
    "t": -3.424e+04}

# value = intercept + roomCoef * rooms + houseTypeCoef[i]   + locationCoef[i]

# propertyType = [b, d, f, sd, t]
#
# location = [ashfor, aylesford, bearsted, birchington, broadstairs
#     , brogdale, canterbury, cranbrook, dartford, deal, dover, edenbridge, faversham, folkestone, hawkinge, herneBay,
#             hythe, kingsHill, kingsnorth, maidstone, margate, minster, minsterOnSea, newRommeny, paddockWood, pembury,
#             ramsgate, royalTonbridgeWells, sandwich, sevenoaks, sheerness, sittingbourne, snodland, southborough,
#             staplehurst, tonbridge, westMalling, whitfield, whitstable]
#
#
# predictedValue = intercept + (b + d - f - sd - t) + (- ashford + aylesford + bearsted + birchington + broadstairs
#                                                      - brogdale + canterbury - cranbrook + dartford - deal - dover + edenbridge - faversham + folkestone - hawkinge + herneBay +
#                                                      hythe - kingsHill - kingsnorth + maidstone + margate - minster - minsterOnSea - newRommeny - paddockWood + pembury +
#                                                      ramsgate + royalTonbridgeWells + sandwich + sevenoaks - sheerness - sittingbourne + snodland + southborough -
#                                                      staplehurst + tonbridge + westMalling - whitfield + whitstable)
#

def locationPrediction(val, loc):
    value = val
    for j in coefficients:
        if j == loc:
            value += coefficients[j]
    return value

def roomtypePrediction(room, ptype, loc):
    value = intercept
    value += (room * rooms)
    for i in coefficients:
        if i == ptype:
            value += coefficients[i]
    x = locationPrediction(value,loc)
    return int(round(x, 0))