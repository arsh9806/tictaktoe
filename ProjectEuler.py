# triplets = int(input())
# answer = []
# for k in range(triplets):
#     n1n2el = input().split()
#     A = n1n2el[0]
#     B = n1n2el[1]
#     elementNo = int(n1n2el[2])
#     C = A + B
#     while len(C)< elementNo:
#         A = B
#         B = str(C)
#         C = int(A + B)
#         print(C)
#     answer.append(C[elementNo-1])
# for j in answer:
#     print(answer)
#project euler #2 solution
'''case = int(input())
lis = []
for _ in range(case):
    n = int(input())
    a = 1
    b = 2
    c = a + b
    sum1 = 2
    while True:

        if c < n and c % 2 == 0:
            sum1 += c

        a = b
        b = c
        c = a + b
        if c < n:
            continue
        else:
            break
    lis.append(sum1)
for i in lis:
    print(i)'''
#project euler #3 solution
#
# import math
# lis = []
# case = int(input())
# for _ in range(case):
#     number = int(input())
#     B = 2
#     while number>B:
#         if number%B == 0:
#             number //= B
#             B = 2
#         else:
#             B += 1
#     lis.append(B)
# for i in lis:
#     print(i)
#project euler #4 solution
# import timeit
# case = int(input())
# lis = []
# for _ in range(0,case):
#     max = 0
#     i = 999
#     N = int(input())
#     sum1 = 0
#
#     maxi = 0
#     k = 0
#     while i>=100:
#         j = 999
#         while j>=100:
#             k = i*j
#             if str(k) == str(k)[::-1]:
#
#                 print(k)
#             j -= 1
#         i -= 1
#
#     lis.append(maxi)
# stamp1 = timeit.default_timer()
# for i in lis:
#     print(i)

'''case = int(input())
lis = [580085, 514415, 906609, 119911, 282282, 141141, 853358, 650056, 601106, 592295, 543345, 485584, 436634, 378873, 329923, 408804, 204402, 623326, 525525, 299992, 469964, 886688, 804408, 698896, 631136, 616616, 443344, 428824, 270072, 255552, 828828, 414414, 487784, 180081, 888888, 666666, 444444, 222222, 348843, 770077, 653356, 855558, 807708, 696696, 648846, 531135, 489984, 372273, 324423, 165561, 117711, 577775, 723327, 649946, 272272, 219912, 292292, 840048, 821128, 802208, 630036, 611116, 420024, 401104, 210012, 238832, 227722, 595595, 589985, 560065, 554455, 548845, 513315, 507705, 564465, 174471, 861168, 809908, 470074, 489984, 693396, 672276, 579975, 888888, 861168, 828828, 801108, 696696, 636636, 444444, 279972, 252252, 219912, 476674, 780087, 393393, 262262, 131131, 886688, 443344, 513315, 824428, 412214, 906609, 793397, 747747, 650056, 604406, 588885, 491194, 445544, 302203, 286682, 143341, 551155, 99299, 819918, 729927, 639936, 549945, 459954, 369963, 279972, 189981, 657756, 507705, 407704, 168861, 824428, 819918, 661166, 656656, 493394, 488884, 412214, 407704, 244442, 239932, 828828, 414414, 561165, 855558, 461164, 840048, 654456, 468864, 420024, 234432, 536635, 428824, 214412, 272272, 602206, 301103, 252252, 106601, 618816, 357753, 280082, 93839, 663366, 442244, 221122, 652256, 737737, 853358, 809908, 793397, 749947, 689986, 534435, 474474, 215512, 155551, 821128, 801108, 89198, 523325, 749947, 198891, 828828, 696696, 666666, 636636, 606606, 474474, 444444, 414414, 282282, 252252, 222222, 675576, 345543, 802208, 447744, 401104, 780087, 737737, 616616, 484484, 363363, 242242, 188881, 121121, 99099, 88088, 297792, 585585, 807708, 259952, 510015, 95259, 508805, 397793, 698896, 611116, 442244, 425524, 408804, 290092, 273372, 256652, 239932, 678876, 595595, 219912, 804408, 603306, 402204, 201102, 98889, 579975, 576675, 573375, 570075, 528825, 525525, 522225, 462264, 84048, 371173, 660066, 89598, 747747, 666666, 585585, 414414, 333333, 252252, 171171, 99099, 90909, 83538, 611116, 84048, 678876, 666666, 654456, 642246, 630036, 468864, 456654, 444444, 432234, 420024, 258852, 246642, 234432, 222222, 210012, 366663, 99999, 696696, 464464, 232232, 84448, 639936, 426624, 257752, 213312, 434434, 575575, 654456, 770077, 729927, 660066, 619916, 550055, 509905, 440044, 330033, 292292, 220022, 182281, 110011, 378873, 689986, 675576, 639936, 612216, 468864, 441144, 405504, 297792, 270072, 234432, 565565, 642246, 321123, 276672, 266662, 84348, 239932, 666666, 555555, 444444, 333333, 222222, 111111, 90909, 80808, 571175, 520025, 630036, 612216, 619916, 84148, 489984, 447744, 405504, 82728, 513315, 545545, 477774, 86868, 359953, 89798, 723327, 663366, 519915, 459954, 414414, 399993, 354453, 294492, 105501, 506605, 696696, 464464, 232232, 84448, 297792, 535535, 693396, 652256, 611116, 462264, 421124, 409904, 272272, 231132, 219912, 86768, 85158, 270072, 636636, 424424, 212212, 171171, 154451, 89298, 81918, 654456, 571175, 512215, 367763, 308803, 284482, 225522, 142241, 525525, 661166, 79897, 611116, 168861, 696696, 656656, 616616, 464464, 424424, 272272, 232232, 88088, 84448, 80808, 99599, 92329, 672276, 657756, 603306, 471174, 456654, 402204, 270072, 255552, 201102, 89298, 698896, 515515, 80908, 595595, 585585, 575575, 565565, 555555, 545545, 535535, 525525, 515515, 505505, 219912, 83538, 399993, 266662, 133331, 650056, 485584, 88288, 91719, 82128, 606606, 505505, 404404, 303303, 279972, 202202, 178871, 101101, 639936, 618816, 489984, 468864, 447744, 426624, 405504, 297792, 276672, 255552, 234432, 213312, 579975, 83538, 576675, 78987, 489984, 82128, 573375, 512215, 290092, 666666, 585585, 414414, 333333, 279972, 252252, 198891, 171171, 108801, 99099, 570075, 73937, 636636, 424424, 212212, 401104, 550055, 519915, 86868, 127721, 74447, 653356, 649946, 602206, 485584, 434434, 270072, 266662, 215512, 87978, 648846, 452254, 82228, 520025, 513315, 506605, 452254, 445544, 438834, 391193, 384483, 377773, 81618, 630036, 468864, 432234, 234432, 81918, 650056, 445544, 83538, 604406, 68186, 98489, 137731, 282282, 209902, 90009, 79497, 72927, 438834, 273372, 89598, 416614, 631136, 408804, 76167, 471174, 432234, 374473, 335533, 277772, 238832, 73337, 78287, 71817, 611116, 588885, 81018, 528825, 84348, 623326, 489984, 464464, 416614, 280082, 257752, 232232, 209902, 86768, 616616, 595595, 525525, 434434, 343343, 252252, 161161, 93639, 85358, 77077, 70707, 447744, 258852, 509905, 522225, 215512, 589985, 87078, 456654, 579975, 561165, 477774, 408804, 375573, 306603, 273372, 204402, 189981, 171171, 102201, 67176, 92529, 320023, 462264, 231132, 84048, 63036, 96869, 464464, 424424, 299992, 272272, 259952, 232232, 219912, 88088, 534435, 601106, 256652, 69996, 296692, 89498, 62526, 63036, 282282, 141141, 63336, 65056, 65556, 459954, 426624, 279972, 246642, 213312, 592295, 577775, 564465, 551155, 549945, 536635, 523325, 510015, 508805, 88788, 225522, 98289, 89698, 138831, 95559, 560065, 375573, 85058, 68286, 414414, 99699, 84348, 64746, 554455, 468864, 234432, 63936, 75057, 83638, 252252, 219912, 88788, 65856, 548845, 67976, 82928, 80008, 69496, 580085, 447744, 424424, 401104, 391193, 258852, 235532, 212212, 294492, 98189, 79597, 71217, 87278, 374473, 68086, 468864, 405504, 297792, 234432, 69696, 63936, 239932, 384483, 484484, 464464, 444444, 424424, 404404, 292292, 272272, 252252, 232232, 212212, 88088, 82928, 69296, 68486, 65656, 62826, 297792, 421124, 377773, 72627, 68686, 83738, 513315, 507705, 462264, 456654, 399993, 231132, 225522, 219912, 180081, 174471, 168861, 74347, 270072, 441144, 98589, 80208, 58485, 67276, 61716, 543345, 531135, 402204, 201102, 474474, 86268, 76867, 513315, 440044, 409904, 80008, 69596, 493394, 216612, 64546, 474474, 444444, 414414, 282282, 252252, 222222, 86268, 83538, 80808, 66066, 63336, 60606, 507705, 93939, 488884, 244442, 88888, 66666, 249942, 184481, 525525, 434434, 343343, 289982, 252252, 219912, 198891, 161161, 128821, 77077, 491194, 289982, 83838, 68886, 239932, 432234, 55755, 442244, 221122, 80408, 60306, 489984, 468864, 447744, 426624, 405504, 297792, 276672, 255552, 234432, 213312, 69696, 399993, 266662, 133331, 61016, 276672, 165561, 93939, 444444, 222222, 80808, 60606, 514415, 476674, 461164, 335533, 320023, 297792, 282282, 209902, 156651, 141141, 420024, 210012, 63736, 85158, 489984, 405504, 292292, 70007, 69496, 425524, 92129, 77877, 86868, 69596, 53235, 487784, 470074, 459954, 442244, 414414, 294492, 266662, 238832, 221122, 97079, 74947, 82328, 66766, 99699, 367763, 66866, 85158, 68586, 485584, 88288, 59895, 54945, 49894, 86768, 78387, 56465, 408804, 306603, 204402, 102201, 98289, 445544, 69296, 299992, 73537, 58685, 53835, 469964, 443344, 428824, 402204, 296692, 270072, 255552, 214412, 88088, 69696, 67276, 48884, 414414, 68586, 88688, 444444, 333333, 222222, 111111, 90909, 80808, 70707, 60606, 50505, 87178, 67876, 60706, 72027, 272272, 219912, 69496, 57475, 52725, 86268, 47874, 420024, 401104, 397793, 378873, 359953, 210012, 187781, 168861, 149941, 87978, 238832, 82128, 108801, 83838, 48984, 85358, 53935, 252252, 354453, 96669, 64446, 56265, 51615, 86768, 84448, 82128, 46864, 61116, 57875, 444444, 414414, 282282, 279972, 252252, 249942, 222222, 219912, 66066, 86668, 83538, 57375, 443344, 87478, 80608, 47174, 412214, 55055, 54145, 53235, 52325, 51415, 50505, 82628, 45854, 88788, 72027, 407704, 80908, 412214, 407704, 371173, 366663, 244442, 239932, 198891, 122221, 117711, 89298, 70807, 81718, 77677, 65856, 48384, 162261, 92529, 436634, 81618, 420024, 258852, 234432, 210012, 80808, 63936, 61716, 44844, 428824, 214412, 98789, 79297, 272272, 83538, 252252, 198891, 280082, 140041, 92629, 60006, 49494, 221122, 99199, 80408, 79097, 60306, 273372, 84148, 59595, 43834, 92229, 89198, 46764, 63936, 48384, 62926, 58185, 414414, 393393, 363363, 333333, 303303, 282282, 252252, 222222, 171171, 141141, 111111, 99099, 66066, 277772, 65056, 84348, 68586, 57375, 401104, 44944, 42824, 297792, 259952, 68786, 45154, 70307, 52625, 308803, 56565, 408804, 290092, 273372, 256652, 239932, 221122, 204402, 63536, 105501, 61716, 52125, 84448, 53535, 45954, 41814, 55755, 231132, 84048, 63036, 42024, 330033, 90009, 89598, 60006, 59595, 74847, 67076, 219912, 84048, 42024, 369963, 357753, 345543, 333333, 321123, 258852, 246642, 234432, 222222, 210012, 159951, 147741, 135531, 123321, 111111, 54945, 41514, 232232, 209902, 84448, 63336, 42224, 279972, 257752, 235532, 213312, 48884, 46864, 44844, 42824, 40804, 76167, 225522, 66566, 171171, 66466, 46964, 187781, 79797, 62726, 297792, 279972, 270072, 252252, 234432, 216612, 84348, 69696, 57275, 47674, 43734, 276672, 159951, 39693, 219912, 65856, 266662, 133331, 48484, 372273, 294492, 378873, 91719, 68886, 284482, 84148, 49794, 55055, 48384, 46464, 44544, 42624, 40704, 82728, 38683, 87478, 129921, 86868, 75057, 43434, 83538, 48384, 232232, 84448, 63336, 42224, 297792, 44744, 57375, 52125, 272272, 266662, 231132, 225522, 219912, 86768, 45254, 41514, 37673, 270072, 212212, 99799, 198891, 117711, 99999, 89298, 81918, 71217, 238832, 88688, 81618, 59495, 52925, 50005, 292292, 272272, 252252, 232232, 212212, 88088, 86268, 84448, 82628, 80808, 65156, 63336, 61516, 44044, 42224, 40404, 348843, 270072, 255552, 201102, 162261, 147741, 99099, 89298, 79497, 69696, 66066, 59895, 56265, 46464, 36663, 62626, 49594, 71117, 63536, 55955, 90109, 76467, 80908, 65156, 219912, 168861, 98889, 83538, 88288, 44144, 59995, 82128, 99899, 96369, 67776, 64246, 35653, 297792, 276672, 255552, 234432, 213312, 80608, 69696, 46464, 90909, 83538, 76167, 50605, 82128, 63336, 44544, 290092, 62626, 46364, 93639, 90209, 65856, 62426, 34643, 86868, 85158, 43434, 301103, 270072, 266662, 215512, 184481, 133331, 129921, 87978, 56265, 324423, 95259, 78987, 49494, 61516, 329923, 82228, 41114, 65856, 48384, 59295, 53935, 66466, 234432, 135531, 90909, 81918, 72927, 63936, 60606, 54945, 51615, 45954, 42624, 36963, 33633, 40504, 302203, 95659, 68186, 282282, 209902, 141141, 57575, 44744, 88888, 82328, 273372, 89598, 64746, 204402, 68786, 52325, 35853, 32623, 68586, 180081, 280082, 257752, 232232, 209902, 165561, 140041, 117711, 92829, 86768, 258852, 40704, 149941, 94149, 48184, 215512, 86268, 55755, 53235, 286682, 83838, 48984, 37873, 34743, 31613, 80808, 63336, 48984, 174471, 67176, 51315, 231132, 84048, 63036, 42024, 299992, 292292, 279972, 272272, 259952, 252252, 239932, 232232, 219912, 212212, 88088, 44044, 256652, 94249, 69996, 46664, 225522, 83538, 63036, 65056, 63536, 279972, 246642, 213312, 189981, 156651, 123321, 47874, 44844, 41814, 39693, 36663, 33633, 30603, 88788, 87278, 168861, 89698, 74347, 161161, 52325, 37973, 89698, 83738, 94149, 84348, 74547, 64746, 54945, 234432, 80808, 63936, 42624, 59295, 55755, 252252, 219912, 88788, 65856, 42924, 67976, 38383, 35453, 32523, 82928, 80008, 69496, 42924, 40004, 29492, 92829, 53835, 95659, 87278, 47974, 39593, 234432, 69696, 63936, 48384, 42624, 239932, 198891, 77777, 39893, 282282, 272272, 262262, 252252, 242242, 232232, 222222, 212212, 202202, 88088, 66066, 44044, 52725, 51015, 84348, 82928, 69296, 67876, 99899, 68486, 65656, 62826, 37073, 34243, 31413, 29892, 28482, 95259, 83738, 37373, 270072, 76167, 51615, 67276, 61716, 201102, 98889, 57475, 52525, 220022, 89598, 80008, 69596, 60006, 49594, 40004, 29592, 252252, 222222, 171171, 141141, 111111, 99099, 96369, 93639, 90909, 86268, 83538, 80808, 76167, 73437, 70707, 66066, 63336, 60606, 53235, 50505, 43134, 40404, 33033, 30303, 86768, 84048, 27472, 244442, 122221, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 99799, 73437, 46364, 27872, 83838, 68886, 34443, 239932, 66766, 29792, 59095, 255552, 234432, 219912, 213312, 69696, 46464, 90209, 61016, 27772, 26462, 117711, 222222, 111111, 90909, 80808, 70707, 60606, 50505, 40404, 30303, 27972, 210012, 87978, 68886, 49794, 63736, 55255, 48384, 44544, 40704, 57375, 56865, 86868, 69596, 60706, 43434, 26162, 238832, 221122, 178871, 161161, 133331, 105501, 48384, 27972, 25452, 90109, 82328, 74547, 66766, 58985, 85158, 53535, 39093, 215512, 88288, 63736, 44144, 171171, 74347, 49894, 89298, 81918, 66666, 28782, 57575, 54145, 82228, 69296, 40504, 27572, 227722, 214412, 201102, 89298, 88088, 69696, 68486, 67276, 66066, 48884, 47674, 46464, 45254, 44044, 26862, 25652, 24442, 88688, 51815, 44344, 128821, 67876, 60706, 56165, 219912, 83538, 69496, 44744, 91719, 86268, 47874, 43134, 82128, 46964, 25252, 58985, 57575, 56165, 83538, 60606, 28782, 78987, 52425, 26562, 86768, 84448, 82128, 67976, 65656, 63336, 61016, 46864, 44544, 42224, 25752, 23432, 222222, 219912, 198891, 171171, 168861, 141141, 138831, 111111, 108801, 99099, 66066, 33033, 28182, 87478, 80608, 47174, 40304, 35953, 86868, 69996, 182281, 99199, 82628, 45854, 41314, 80908, 49494, 27572, 57375, 52425, 84448, 65856, 48384, 29792, 188881, 98789, 81618, 59095, 56865, 210012, 81918, 80808, 63936, 62826, 61716, 60606, 45954, 44844, 43734, 42624, 41514, 40404, 27972, 26862, 25752, 24642, 23532, 22422, 83538, 54145, 26962, 90009, 79497, 72927, 60006, 49494, 42924, 30003, 89598, 84148, 64746, 76167, 43834, 82728, 67176, 63936, 48384, 29592, 55255, 53535, 51815, 65056, 45154, 25252, 92229, 84348, 76467, 68586, 44944, 42824, 40704, 29892, 27772, 25652, 23532, 21412, 92629, 68786, 45154, 23632, 204402, 189981, 171171, 154451, 137731, 102201, 63536, 57475, 84448, 42224, 27872, 96669, 92529, 45954, 41814, 89198, 84048, 68186, 63036, 47174, 42024, 26162, 21012, 55555, 84048, 63036, 42024, 21012, 84448, 63336, 42224, 21112, 49894, 48884, 47874, 46864, 45854, 44844, 43834, 42824, 41814, 40804, 29492, 28482, 27472, 26462, 25452, 24442, 23432, 22422, 21412, 20402, 98289, 79797, 59295, 20502, 99699, 66466, 46964, 33233, 89298, 84348, 69696, 64746, 75057, 71117, 47674, 43734, 88788, 65856, 42924, 29792, 53235, 50505, 142241, 97079, 84148, 71217, 49794, 36863, 23932, 69696, 67776, 65856, 63936, 48384, 46464, 44544, 42624, 40704, 27072, 25152, 23232, 21312, 87478, 52525, 36863, 19291, 90909, 83538, 76167, 55755, 48384, 27972, 86668, 44744, 29892, 27072, 180081, 174471, 168861, 133331, 127721, 86768, 45254, 41514, 87978, 54945, 53835, 52725, 51615, 50505, 88688, 80408, 44344, 29992, 21712, 81618, 74847, 28182, 88088, 87178, 86268, 85358, 84448, 83538, 82628, 81718, 80808, 66066, 65156, 64246, 63336, 62426, 61516, 60606, 44044, 43134, 42224, 41314, 40404, 22022, 21112, 20202, 93939, 92129, 79097, 62626, 49594, 31313, 18281, 155551, 80908, 79297, 65156, 51015, 28282, 88288, 83838, 68886, 44144, 29192, 24742, 98589, 82128, 59295, 55755, 86768, 80608, 69696, 63536, 46464, 40304, 29392, 23232, 57575, 52325, 82128, 63336, 44544, 25752, 165561, 93939, 77677, 62626, 46364, 31313, 86868, 85158, 43434, 18981, 17271, 98189, 61516, 59995, 53235, 80808, 65856, 63336, 48384, 99699, 70307, 66466, 33233, 29392, 85158, 66566, 47974, 40504, 26062, 21912, 59895, 56265, 54945, 51315, 88888, 82328, 67076, 44444, 29192, 21812, 102201, 98289, 68786, 59495, 29992, 68586, 53935, 52325, 17871, 16261, 95559, 78387, 72027, 40704, 29892, 23532, 86268, 62726, 47874, 43134, 28282, 143341, 108801, 96869, 83838, 70807, 48984, 39093, 35953, 26062, 22922, 86268, 80808, 63336, 48984, 40404, 56265, 55955, 51615, 88088, 66066, 44044, 28182, 22022, 83538, 77877, 63036, 57375, 20502, 80408, 65056, 63536, 48184, 46664, 29792, 88788, 87278, 73537, 72027, 16761, 15251, 98489, 92529, 89698, 83738, 74947, 80808, 63936, 61716, 44844, 42624, 40404, 27972, 25752, 23532, 21312, 93639, 88788, 70707, 65856, 42924, 18081, 89498, 82928, 80008, 69496, 62926, 60006, 49494, 42924, 40004, 29492, 22922, 20002, 59595, 57275, 52925, 50605, 80208, 69696, 63936, 48384, 42624, 27072, 21312, 141141, 131131, 121121, 111111, 101101, 99099, 88088, 77077, 66066, 55055, 44044, 33033, 22022, 19591, 85058, 84348, 83638, 82928, 69296, 68586, 67876, 29892, 28482, 27072, 15651, 14241, 105501, 76867, 67276, 61716, 52125, 39893, 24742, 15151, 87078, 68586, 64446, 60306, 45954, 41814, 110011, 99599, 90009, 89598, 80008, 79597, 70007, 69596, 60006, 59595, 50005, 49594, 40004, 39593, 30003, 29592, 20002, 19591, 86768, 84048, 69496, 44744, 42024, 27472, 58185, 57375, 56565, 55755, 54945, 85358, 66866, 46364, 27872, 20502, 74347, 66766, 37373, 29792, 21812, 84348, 69696, 61116, 46464, 23232, 21912, 39693, 38383, 37073, 27772, 26462, 25152, 15851, 14541, 13231, 91719, 87978, 72627, 68886, 53535, 49794, 34443, 15351, 48384, 46464, 44544, 42624, 40704, 92329, 86868, 75057, 69596, 60706, 43434, 37973, 26162, 83538, 81018, 60606, 48384, 27972, 25452, 57875, 57375, 52625, 52125, 88288, 63736, 48484, 44144, 23932, 117711, 99999, 89298, 81918, 71217, 66666, 33333, 28782, 18081, 82228, 81618, 69296, 68686, 41114, 40504, 28182, 27572, 26962, 119911, 106601, 99099, 89298, 88088, 79497, 78287, 77077, 69696, 68486, 67276, 66066, 59895, 58685, 57475, 56265, 55055, 48884, 47674, 46464, 45254, 44044, 37873, 36663, 35453, 34243, 33033, 26862, 25652, 24442, 23232, 22022, 15851, 14641, 13431, 12221, 98889, 83538, 69496, 54145, 44744, 15351, 89798, 82128, 68086, 64546, 46964, 25252, 21712, 99099, 90909, 83538, 76167, 60606, 53235, 30303, 28782, 86768, 84448, 82128, 67976, 65656, 63336, 61016, 46864, 44544, 42224, 25752, 23432, 21112, 56465, 53935, 52325, 86868, 85158, 69996, 68286, 60306, 43434, 26562, 95259, 80908, 78987, 73337, 51415, 49494, 27572, 84448, 65856, 48384, 42224, 29792, 23632, 90909, 81918, 80808, 72927, 71817, 70707, 63936, 62826, 61716, 60606, 54945, 53835, 52725, 51615, 50505, 45954, 44844, 43734, 42624, 41514, 40404, 36963, 35853, 34743, 33633, 32523, 31413, 30303, 27972, 26862, 25752, 24642, 23532, 22422, 21312, 20202, 18981, 17871, 16761, 15651, 14541, 13431, 12321, 11211, 99299, 89598, 84148, 79897, 74447, 64746, 15151, 84348, 82728, 67176, 65556, 63936, 48384, 46764, 29592, 27972, 93839, 73937, 65056, 45154, 25252, 44944, 42824, 40704, 29892, 27772, 25652, 23532, 21412, 58485, 55755, 53235, 50505, 88088, 84448, 80808, 63336, 48984, 42224, 27872, 21112, 89198, 84048, 68186, 63036, 47174, 42024, 26162, 21012, 84048, 83538, 63036, 62526, 42024, 41514, 21012, 20502, 49894, 48884, 47874, 46864, 45854, 44844, 43834, 42824, 41814, 40804, 39693, 38683, 37673, 36663, 35653, 34643, 33633, 32623, 31613, 30603, 29492, 28482, 27472, 26462, 25452, 24442, 23432, 22422, 21412, 20402, 19291, 18281, 17271, 16261, 15251, 14241, 13231, 12221, 11211, 10201]
newlis = []
lis.sort(reverse=1)
for _ in range(0,case):
    N = int(input())
    while True:
        if str(N) == str(N)[::-1] and N in lis:
            newlis.append(N)
            break
        else:
            N -= 1
for i in newlis:
    print(i)'''

#project euler problem 5
'''case = int(input())
lis = []
for _ in range(case):
    N = int(input())
    a = 1
    b = 2
    while b<=N:
        a = (a*b)//gcd(a,b)
        b += 1
    lis.append(a)
for i in lis:
    print(i)'''

#project euler problem 6
'''case = int(input())
lis = []
for _ in range(case):
    n = int(input())
    lis.append(((n*(n+1))//2)**2 - (n*(n+1)*(2*n + 1))//6)
for i in lis:
    print(i)'''
import math
nk = input().split()
BoardLength = int(nk[0])
NumberOfObstacles = int(nk[1])
rk = input().split()
rQueen = int(rk[0])
cQueen = int(rk[1])
rRObstacle = -1
cRObstacle = -1
rBRObstacle = -1
cBRObstacle = -1
rBObstacle = -1
cBObstacle = -1
rBLObstacle = -1
cBLObstacle = -1
rLObstacle = -1
cLObstacle = -1
rTLObstacle = -1
cTLObstacle = -1
rTObstacle = -1
cTObstacle = -1
rTRObstacle = -1
cTRObstacle = -1
TotalSquares = 0
for i in range(NumberOfObstacles):
    rc = input().split()
    rObstacle, cObstacle = int(rc[0]), int(rc[1])
    #right
    if ((cRObstacle > cObstacle) or rRObstacle == -1) and (cQueen < cObstacle) and (rRObstacle == rQueen):
        rRObstacle = rObstacle
        cRObstacle = cObstacle

    #Bottom Right
    if (rQueen - rObstacle == cObstacle - cQueen and cObstacle > cQueen and rObstacle < rQueen) and ((rObstacle > rBRObstacle and cObstacle < cBRObstacle) or rBRObstacle == -1):
        rBRObstacle = rObstacle
        cBRObstacle = rObstacle

    #Bottom
    if (rObstacle > rBObstacle or rBObstacle == -1) and rObstacle < rQueen and cObstacle == cQueen:
        rObstacle = rBObstacle
        cObstacle = cBObstacle

    #BOttom Left
    if (rQueen - rObstacle == cQueen - cObstacle and cObstacle < cQueen and rObstacle < rQueen) and ((rObstacle > rBLObstacle and cObstacle > cBLObstacle) or rBLObstacle == -1):
        rBLObstacle = rObstacle
        cBLObstacle = cObstacle

    #Left
    if (cObstacle > cLObstacle or rLObstacle == -1) and cObstacle<cQueen and rObstacle == rQueen:
        rLObstacle = rObstacle
        cLObstacle = cObstacle

    #top Left
    if (cQueen - cObstacle == rObstacle - rQueen and cObstacle<cQueen and rObstacle > rQueen) and ((rObstacle < rTLObstacle and cObstacle  > cTLObstacle ) or rTLObstacle == -1):
        rTLObstacle = rObstacle
        cTLObstacle = cObstacle

    #Top
    if (rObstacle < rTObstacle or rTObstacle == -1 ) and rObstacle > rQueen and cObstacle == cQueen:
        cTObstacle = cObstacle
        rTObstacle = rObstacle

    #top Right
    if rObstacle - rQueen and cObstacle - cQueen and cObstacle > cQueen and rObstacle > rQueen and ((rObstacle < rTRObstacle and cObstacle < cTRObstacle) or rTRObstacle == -1):
        rTRObstacle = rObstacle
        cTRObstacle = cObstacle

#R B L T
TotalSquares += cRObstacle-cQueen - 1 if cRObstacle != -1 else BoardLength - cQueen
TotalSquares += rQueen - rBObstacle - 1 if rBObstacle != -1 else rQueen - 1
TotalSquares += cQueen - cLObstacle -1 if cLObstacle != -1 else cQueen - 1
TotalSquares += rTObstacle - rQueen - 1 if rTObstacle != -1 else BoardLength - rQueen

#BR BL TL TR
TotalSquares += cBRObstacle - cQueen - 1 if cBRObstacle != -1 else min(BoardLength-cQueen, rQueen - 1)
TotalSquares += cQueen - cBLObstacle - 1 if cBLObstacle != -1 else min(cQueen - 1, rQueen - 1)
TotalSquares += cQueen - cTLObstacle -1 if cTLObstacle != -1 else min(cQueen - 1, BoardLength - rQueen)
TotalSquares += cTRObstacle - cQueen - 1 if cTRObstacle != -1 else min(BoardLength - cQueen, BoardLength - rQueen)
print(TotalSquares)
