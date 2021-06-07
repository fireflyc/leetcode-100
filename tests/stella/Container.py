import unittest
from leetcode.stella import Container


class ContainerTestCase(unittest.TestCase):
    def test_count_triples(self):
        self.assertEqual(927990, Container.count_triplets(
            [1925, 22798, 653, 63853, 53674, 4621, 58552, 13630, 13421, 44155, 61489, 8073, 470, 24191, 1615, 39639,
             56306, 12254, 7365, 22573, 62860, 8530, 63341, 23739, 31022, 19177, 61415, 62793, 41675, 12061, 65074,
             6722, 38066, 10250, 58830, 61975, 52716, 20702, 15914, 49470, 19074, 27511, 3031, 8666, 1346, 5106, 4797,
             27540, 36095, 48554, 9324, 27668, 41744, 5541, 29151, 24199, 62189, 3791, 26779, 27343, 47722, 21015,
             13368, 19222, 30860, 62276, 52200, 18151, 36580, 45101, 52144, 29239, 26134, 50308, 28292, 16250, 29717,
             61414, 9343, 30306, 41766, 31672, 13345, 120, 45809, 40549, 509, 19566, 50373, 41216, 35730, 10238, 46287,
             30895, 44445, 49813, 15228, 49938, 18355, 64488, 7918, 57915, 2657, 16814, 34478, 38116, 25967, 6686,
             16554, 18572, 49494, 59557, 39020, 2323, 51920, 20028, 22275, 34746, 16321, 60291, 10718, 27186, 18985,
             34067, 37616, 41100, 34824, 26922, 41588, 26438, 51023, 51653, 19153, 24366, 41209, 10293, 45680, 24997,
             38735, 9144, 43794, 23203, 30976, 27204, 31242, 45527, 20856, 42733, 3946, 19672, 48838, 3434, 40707, 1674,
             30902, 58231, 662, 34526, 4355, 56826, 44977, 48624, 43844, 420, 2698, 40689, 65515, 57222, 45854, 47651,
             14856, 49257, 18869, 6911, 30205, 21639, 11026, 27637, 58798, 28525, 29313, 46453, 34351, 8468, 59663,
             29106, 51730, 25485, 52877, 25528, 14428, 12857, 61606, 38438, 3263, 25450, 15337, 5548, 12239, 3734]))
        self.assertEqual(113138322, Container.count_triplets(
            [41816, 11362, 40028, 40141, 46197, 33562, 18640, 57505, 23138, 30034, 41410, 33824, 62683, 62568, 60932,
             61215, 38073, 32125, 46144, 14117, 17424, 2870, 10673, 253, 42901, 9201, 51555, 44597, 63614, 25985, 60384,
             29733, 22249, 6706, 57857, 52087, 21163, 29867, 21308, 1889, 2906, 24163, 13735, 34374, 12306, 13213,
             44083, 48208, 20462, 56360, 16688, 22540, 46693, 2916, 61222, 4740, 30207, 47487, 3110, 53018, 64152,
             30180, 7741, 5339, 6470, 50163, 27132, 60242, 28877, 5055, 27979, 49468, 54351, 2578, 11821, 32113, 8394,
             57087, 61240, 20945, 28497, 36507, 18710, 35459, 13184, 19440, 28952, 39627, 35138, 17104, 15190, 7781,
             51347, 6481, 48030, 16303, 18648, 48239, 43228, 48622, 33769, 56301, 7981, 42283, 7749, 48318, 23521,
             44229, 46103, 43293, 14520, 54512, 15737, 33957, 44213, 15309, 41190, 18797, 11231, 53067, 36249, 21488,
             38366, 1657, 8508, 25924, 63947, 33454, 5010, 50137, 51212, 50777, 37322, 45593, 13989, 48009, 53488,
             49805, 23164, 38733, 41221, 59035, 7078, 54652, 34500, 23502, 29858, 828, 14422, 42779, 43309, 32420,
             62477, 31517, 20574, 55560, 16984, 39603, 46099, 53850, 51469, 25171, 3878, 2509, 47609, 63025, 22489,
             28914, 47565, 43111, 17046, 44012, 19982, 23354, 35357, 47992, 9910, 1440, 41145, 1609, 2946, 14796, 42852,
             4361, 4089, 63707, 27698, 58486, 14190, 28522, 23464, 11595, 21549, 64670, 48975, 25078, 26822, 17284,
             34821, 48210, 45000, 30320, 2748, 60391, 26799, 25578, 203, 9058, 56941, 33681, 48000, 9710, 21630, 55059,
             53782, 16173, 1440, 52852, 11065, 51621, 44804, 11030, 5143, 60794, 39182, 40665, 29983, 9835, 39450,
             16546, 52815, 48019, 1786, 61107, 2380, 5873, 19184, 9883, 15476, 23318, 48201, 26523, 17684, 32264, 25728,
             20366, 59017, 36074, 64050, 50653, 37388, 17199, 45012, 29879, 47276, 26462, 32506, 1355, 48493, 2246,
             44612, 38142, 50850, 18990, 44964, 13572, 34686, 22300, 64123, 63692, 13695, 37095, 21590, 63474, 60589,
             38413, 47191, 44651, 23157, 60054, 58946, 21670, 48981, 595, 53500, 37019, 62410, 23802, 41006, 21168,
             51300, 39367, 64714, 66, 9224, 2857, 8247, 60908, 62167, 31484, 62042, 53633, 51027, 48973, 12298, 35971,
             27779, 62245, 11392, 11131, 43179, 10315, 7212, 33025, 52209, 39652, 49463, 17416, 18675, 28095, 64936,
             47049, 62013, 35249, 36343, 64886, 12451, 51287, 51872, 55360, 49155, 10179, 43327, 60535, 36915, 23654,
             62227, 36804, 26977, 40247, 52699, 14962, 1028, 34674, 61692, 44581, 41347, 41144, 32570, 47901, 16331,
             58442, 17987, 61927, 60718, 5106, 29371, 48761, 29468, 33351, 52876, 46202, 62783, 10779, 60526, 60816,
             41598, 61629, 16560, 57788, 50690, 39956, 5939, 1974, 718, 16420, 49961, 25337, 50819, 41002, 25510, 57681,
             2517, 30494, 54385, 8310, 46562, 21503, 1592, 31046, 34189, 2725, 37088, 22769, 294, 12502, 7262, 35430,
             2825, 60826, 55381, 61951, 20630, 59327, 64507, 50117, 18027, 43967, 39037, 26489, 20060, 3922, 8217, 8778,
             31515, 42067, 50073, 3061, 53985, 2848, 36368, 48768, 41367, 62238, 22590, 38396, 5426, 36686, 53300,
             13212, 17102, 45901, 16638, 16989, 61309, 65440, 10171, 58993, 36223, 2529, 38371, 42044, 2214, 49656,
             53595, 4695, 42493, 29920, 15644, 30059, 10445, 21867, 42939, 31226, 36432, 35615, 53778, 22503, 53278,
             5242, 28031, 23089, 29594, 54624, 33580, 64700, 56456, 7788, 20767, 1489, 48087, 1258, 58060, 12670, 27121,
             4065, 20398, 25527, 3423, 50302, 46619, 23454, 54735, 5073, 3539, 23263, 59103, 49575, 44061, 36879, 52675,
             27015, 2011, 52586, 12484, 25405, 23436, 8084, 22989, 11605, 40371, 42823, 894, 29915, 36310, 57125, 32507,
             5272, 3389, 56499, 51821, 56259, 17186, 42467, 6272, 54170, 21863, 62596, 30892, 2167, 59575, 40994, 18814,
             2411, 24686, 10280, 35932, 9626, 11443, 60350, 41950, 15897, 57599, 40941, 61970, 31648, 58189, 44462,
             2894, 15747, 18453, 11142, 15609, 14813, 57563, 30336, 57443, 9043, 37022, 882, 60968, 369, 25552, 52532,
             65528, 1278, 54007, 33429, 2502, 50929, 7333, 40073, 51008, 44144, 24895, 1732, 28590, 59879, 21818, 16250,
             9032, 33439, 34953, 4787, 26722, 43167, 63311, 28281, 28576, 30876, 14747, 25876, 42288, 26021, 38101,
             54760, 65402, 58001, 24366, 1423, 40082, 31100, 15533, 2641, 21074, 52302, 63184, 6990, 57516, 3192, 46758,
             1756, 27593, 57031, 25762, 60592, 46739, 39595, 10576, 22314, 26941, 38679, 65276, 18593, 33001, 61174,
             22637, 41196, 50209, 41305, 49376, 12824, 62740, 11593, 38252, 19401, 41577, 19078, 28259, 44710, 17633,
             47702, 22732, 8660, 40182, 10863, 28218, 26109, 4991, 46581, 44618, 50973, 35711, 36301, 11090, 13596,
             14958, 34426, 53672, 23394, 57794, 48226, 46953, 21965, 7764, 63097, 56007, 26795, 56571, 58931, 22444,
             32870, 21744, 45557, 59779, 64523, 48744, 20004, 57704, 65052, 22709, 62174, 33524, 63218, 65264, 53276,
             44789, 10093, 322, 39024, 46167, 61311, 33889, 45668, 42425, 13429, 42224, 64338, 7286, 45124, 40259,
             24632, 51992, 687, 58485, 53566, 31503, 7087, 29663, 38289, 16638, 31885, 50838, 60472, 36807, 54214, 5107,
             56122, 60346, 11010, 54230, 55677, 57583, 33891, 39862, 13636, 46408, 26543, 1387, 8799, 25442, 58011,
             37024, 60047, 60914, 5688, 38549, 21923, 33213, 29853, 31453, 6671, 54601, 32130, 42269, 30977, 11863,
             35455, 10455, 55848, 54500, 9413, 4511, 4488, 25771, 62458, 36447, 17401, 15050, 7266, 9245, 53206, 9085,
             56627, 53936, 8965, 36616, 462, 56494, 36587, 49501, 32135, 45247, 61029, 36670, 57324, 22481, 6391, 337,
             14853, 54957, 20414, 14720, 32481, 62056, 33356, 22339, 5079, 37595, 14827, 24084, 24979, 49688, 15180,
             61334, 48653, 31530, 57702, 23538, 25188, 8478, 51023, 26292, 32784, 30865, 43003, 24506, 60021, 28306,
             23541, 26271, 50219, 65080, 56787, 31439, 19094, 29228, 22545, 15960, 12251, 62644, 32722, 7207, 25159,
             25474, 33654, 64227, 64004, 37086, 40507, 44278, 32913, 31894, 20612, 44821, 6022, 20784, 58391, 14901,
             63411, 64498, 37708, 2650, 6126, 13126, 21417, 7412, 52246, 23865, 15317, 2863, 25078, 295, 7634, 39626,
             61272, 13065, 48566, 12956, 97, 58755, 55450, 4376, 11608, 15355, 60838, 25030, 52912, 28561, 24985, 50157,
             40354, 17650, 38195, 46127, 54203, 44379, 41992, 39053, 6032, 61943, 46847, 17882, 45373, 40685, 43178,
             24832, 37563, 43255, 13215, 33293, 7886, 6916, 59707, 8162, 58541, 30788, 29812, 22270, 27277, 24722,
             37026, 21993, 53869, 15306, 16283, 31493, 61281, 1567, 47409, 393, 26532, 50083, 29234, 28146, 16594,
             31135, 14959, 18580, 42814, 39285, 60918, 63495, 34234, 5738, 19654, 33934, 44116, 62009, 10165, 2404,
             57018, 52767, 50184, 30710, 44419, 26966, 12586, 25617, 51579, 52550, 62988, 58174, 44701, 34138, 47443,
             12006, 60495, 46699, 38960, 28445, 41519, 40480, 58907, 37403, 13983, 28926, 15923, 59306, 55281, 36426,
             12870, 2853, 8792, 29046, 44184, 14679, 44860, 56488, 49626, 27887, 42318, 64773, 58026, 22160, 44921,
             10696, 36527, 23365, 28714, 28763, 43465, 55443, 30708, 9606, 49424, 49259, 62511, 25824, 30400, 35428,
             58466, 46151, 1394, 13587, 55960, 38369, 57272, 26961, 13793, 271, 65277, 8937, 42137, 32093, 24913, 35206,
             5130, 63572, 32292]))

    def test_design_underground_system(self):
        self.assertEqual(
            [None, None, None, None, None, None, None, 14.0, 11.0, None, 11.0, None, 12.0],
            Container.design_underground_system(
                ["UndergroundSystem", "checkIn", "checkIn", "checkIn", "checkOut", "checkOut", "checkOut",
                 "getAverageTime", "getAverageTime", "checkIn", "getAverageTime", "checkOut", "getAverageTime"],
                [[], [45, "Leyton", 3], [32, "Paradise", 8], [27, "Leyton", 10], [45, "Waterloo", 15],
                 [27, "Waterloo", 20],
                 [32, "Cambridge", 22], ["Paradise", "Cambridge"], ["Leyton", "Waterloo"],
                 [10, "Leyton", 24],
                 ["Leyton", "Waterloo"], [10, "Waterloo", 38], ["Leyton", "Waterloo"]]
            )
        )

    def test_design_tweeter(self):
        self.assertEqual([None, None, [5], None, None, [6, 5], None, [5]], Container.design_tweeter(
            ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
            [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
        ))

    def test_min_stack(self):
        self.assertEqual([None, None, None, None, -3, None, 0, -2], Container.min_stack(
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []]
        ))
