import face_recognition
import sys
import json
import os

def compare_face(file,adminid):
    known_face_encoding = [[-0.03746536,  0.03712549,  0.08025289, -0.10363182, -0.0629023 ,
       -0.09742056, -0.0533254 , -0.09643141,  0.14367202, -0.09961449,
        0.20628758,  0.03531261, -0.15525876, -0.10061918,  0.03649583,
        0.0931713 , -0.20404501, -0.10667019, -0.04585113, -0.09469586,
        0.02058254,  0.02264052,  0.07848746,  0.07726921, -0.13825828,
       -0.25019822, -0.13810171, -0.11326106,  0.08446721, -0.02064594,
        0.05865587,  0.1005493 , -0.1958295 , -0.08644604,  0.03412535,
        0.04752624,  0.0140353 , -0.02071683,  0.20413111,  0.05749357,
       -0.14346264,  0.09009909, -0.00954056,  0.29791468,  0.19453983,
        0.04964454,  0.11304726, -0.08854464,  0.19746293, -0.29618856,
        0.07715229,  0.13001002,  0.09497075,  0.02447591,  0.09246891,
       -0.17410505,  0.13867056,  0.09516717, -0.24750669,  0.20154135,
        0.11939297, -0.09868044,  0.10023863,  0.07538728,  0.19982612,
        0.046467  , -0.10250978, -0.12780455,  0.13058749, -0.12691611,
       -0.00969642,  0.19647405, -0.14725104, -0.16504999, -0.36411586,
        0.03540164,  0.44548061,  0.17010759, -0.1146895 ,  0.02918696,
       -0.14075784,  0.03662509,  0.10272308,  0.06412455, -0.10700801,
       -0.04043651, -0.16070512,  0.0900458 ,  0.23151948,  0.00399549,
       -0.09813125,  0.29184443,  0.05735405,  0.07622643,  0.01012831,
        0.09982387, -0.09056631, -0.04747427, -0.11317498,  0.04991573,
        0.01420304, -0.04955112,  0.02409022,  0.09482649, -0.17868555,
        0.14179979, -0.08089846, -0.03974171, -0.15851033, -0.00862763,
       -0.11785666,  0.05801655,  0.11610338, -0.28504199,  0.20477663,
        0.21355356,  0.07588208,  0.11569575,  0.05385513, -0.02712957,
       -0.04982603, -0.13525017, -0.04407842, -0.0728984 ,  0.01238692,
       -0.00504612,  0.12865418,  0.05302283], [-0.1126736 ,  0.07769954,  0.14384159, -0.13007592, -0.12962745,
       -0.00844061, -0.07332742, -0.12963207,  0.29638442, -0.20185634,
        0.06683289,  0.06465581, -0.15606831,  0.05444936, -0.06577514,
        0.17915659, -0.23357695, -0.20301515, -0.01556633, -0.13815309,
       -0.01460012,  0.04075821,  0.05958659,  0.10344711, -0.15715548,
       -0.29405102, -0.1228472 , -0.01491298,  0.02511392, -0.08230974,
        0.03344018,  0.13268016, -0.18873169,  0.04829371, -0.01815552,
        0.15312481, -0.03096115, -0.1249585 ,  0.16911431,  0.09489729,
       -0.23411682, -0.01296951,  0.09440471,  0.25146157,  0.29891512,
        0.01138407,  0.02828692, -0.03147966,  0.18358369, -0.35026598,
        0.08875795,  0.15087661,  0.10461593,  0.04458129,  0.08487201,
       -0.2176798 ,  0.01557813,  0.09018717, -0.15224038,  0.12454343,
        0.11955944, -0.1467355 ,  0.03285275,  0.01260603,  0.21578149,
        0.21278112, -0.09555174, -0.17011952,  0.26555479, -0.18619044,
       -0.03719156,  0.12730899, -0.11351974, -0.16094771, -0.17105286,
       -0.00319753,  0.46628535,  0.18518528, -0.037776  ,  0.03841892,
       -0.11987801, -0.01393437, -0.06310003,  0.16743498, -0.07393816,
       -0.0627467 , -0.07674176,  0.04717146,  0.27451754,  0.05672777,
       -0.06533151,  0.27061781,  0.0397692 ,  0.00669724, -0.03936054,
        0.01350288, -0.12895925,  0.0501561 , -0.15293211, -0.05400323,
       -0.09721746, -0.02140596, -0.01085106,  0.09753364, -0.19332874,
        0.23269388, -0.04604136, -0.04062532, -0.06619231,  0.03927028,
       -0.11000293,  0.02761496,  0.17193149, -0.26009306,  0.17472403,
        0.17843455,  0.07617638,  0.19217585,  0.04668907,  0.13685222,
        0.10399143, -0.09394654, -0.07216489, -0.05844739, -0.00635387,
       -0.13060102,  0.05233167,  0.11984412], [-0.10567228,  0.07915562,  0.08877265, -0.09583787, -0.10901047,
        0.02755177, -0.0113965 , -0.12409644,  0.21365672, -0.10332462,
        0.28061879,  0.04597727, -0.34586102, -0.03671748, -0.04145012,
        0.08473161, -0.19060858, -0.11551243, -0.06392136, -0.11719736,
       -0.05752272,  0.01621418,  0.03405805,  0.01159358, -0.05617515,
       -0.31250116, -0.04827827, -0.10677505,  0.08718917, -0.13868409,
       -0.00467502,  0.01935967, -0.1828455 , -0.03575002, -0.05255083,
        0.11579536, -0.1512657 , -0.15306827,  0.25997007, -0.08198243,
       -0.10536963, -0.0488768 , -0.06698377,  0.24464032,  0.20608699,
       -0.06384879,  0.03110983, -0.14010936,  0.19540906, -0.21365418,
        0.06780203,  0.2367457 ,  0.14062394,  0.03583594,  0.00898775,
       -0.13470654,  0.0325021 ,  0.12309484, -0.23466022, -0.00106011,
        0.15810949, -0.06149198, -0.05176425, -0.07890674,  0.17169523,
        0.05225831, -0.16546971, -0.15468292,  0.17173949, -0.14388409,
       -0.02688714,  0.07310978, -0.17435053, -0.21929173, -0.24251541,
        0.08358296,  0.31435102,  0.10780039, -0.06172837,  0.02266208,
       -0.12243256, -0.07773126, -0.02878256,  0.05659514, -0.11094899,
       -0.04804657, -0.12867594,  0.12849955,  0.14400575, -0.02025126,
       -0.05001794,  0.18533587, -0.00504069,  0.00702905,  0.00824386,
        0.13159768, -0.11808156,  0.0668896 , -0.10679658,  0.08952976,
        0.10120353, -0.09629786,  0.0183007 ,  0.09482519, -0.12367217,
        0.2251727 , -0.04081124,  0.03839486,  0.02942635, -0.20438217,
       -0.1478464 ,  0.00929884,  0.23892918, -0.27544126,  0.21705718,
        0.11159101,  0.09794552,  0.13272874,  0.07471404,  0.02300809,
       -0.02058194, -0.08301041, -0.28535187, -0.06796059,  0.02346317,
       -0.02621401,  0.08310406,  0.05645993], [-0.09809164,  0.18160714, -0.00810427,  0.02757933, -0.10735264,
        0.05661538,  0.03884231, -0.01679808,  0.23168963, -0.0458906 ,
        0.30594492,  0.04286021, -0.17895608, -0.09721369, -0.08395906,
        0.12997293, -0.20957701, -0.08677538, -0.161671  , -0.09488915,
        0.07772493,  0.07579189, -0.06081212,  0.01715339, -0.22805713,
       -0.24046412,  0.01432238, -0.0794535 ,  0.11215173, -0.20549555,
        0.05148806,  0.0945944 , -0.18261077, -0.03975127,  0.01386934,
       -0.00145953, -0.0523471 , -0.0130728 ,  0.22851126, -0.00444302,
       -0.14595738,  0.06066118,  0.01811482,  0.30233821,  0.25162077,
       -0.02872217, -0.02838095, -0.07345292,  0.14816663, -0.31823474,
       -0.00977723,  0.21440822,  0.0844564 ,  0.09059182,  0.12105939,
       -0.14718124, -0.07051317,  0.12390533, -0.10941464,  0.05707086,
        0.00359604, -0.0976663 , -0.01364659, -0.07608742,  0.08233501,
        0.02611692, -0.079586  , -0.14597167,  0.144922  , -0.14549533,
       -0.02994824,  0.15451723, -0.04357915, -0.21592763, -0.24173695,
        0.05411957,  0.42979434,  0.19563057, -0.19461167,  0.03738844,
       -0.05467833, -0.05729993,  0.09199505,  0.00949666, -0.03873695,
       -0.14076422, -0.10296596,  0.08634289,  0.23321557,  0.00876668,
       -0.02934331,  0.22414801,  0.0012664 , -0.04024687, -0.02057241,
       -0.01731127, -0.0960297 ,  0.03404412, -0.02365436,  0.02107972,
        0.04329345, -0.07351888,  0.00355926,  0.08716468, -0.09814903,
        0.18122946, -0.00520919,  0.05696993, -0.01670784, -0.01995191,
       -0.09534618,  0.10578553,  0.18441394, -0.25873727,  0.32876626,
        0.08323045, -0.06396595,  0.12464517,  0.06878658,  0.05802016,
       -0.01280658, -0.02145462, -0.11459505, -0.11849465,  0.00484494,
       -0.12413657,  0.07497178, -0.05310374], [-0.00051243,  0.08701132, -0.06226364, -0.05261512, -0.08077674,
        0.02527721,  0.0059399 , -0.14216483,  0.02904219, -0.01993081,
        0.22143658,  0.01526419, -0.27456546, -0.09496373,  0.00894523,
        0.03471675, -0.10459014, -0.11500993, -0.26675215, -0.11419149,
       -0.05300334,  0.01196472,  0.02798573,  0.03098548, -0.12556215,
       -0.22187363, -0.05948941, -0.20618935,  0.09916492, -0.17916764,
       -0.04407416, -0.00267043, -0.14905798, -0.06558284, -0.01120078,
       -0.02538414, -0.08517435, -0.04997439,  0.24201649, -0.02208286,
       -0.11008451,  0.14583716,  0.01468649,  0.28972334,  0.25724372,
        0.00318031,  0.10116517, -0.08093581,  0.14873265, -0.2400001 ,
        0.11541292,  0.09579076,  0.15603311,  0.0586448 ,  0.06378933,
       -0.24342746, -0.01916683,  0.13818152, -0.22460894,  0.14438526,
        0.0098662 , -0.12695792, -0.10273359, -0.02989368,  0.1659909 ,
        0.07075053, -0.08459824, -0.17029428,  0.19698757, -0.19016689,
        0.00356471,  0.087124  , -0.09185235, -0.15935205, -0.19902116,
        0.10090926,  0.36528143,  0.13584307, -0.22039473,  0.08041398,
       -0.14670286, -0.08594172,  0.0078599 , -0.00862459, -0.05331235,
       -0.08423281, -0.13522702,  0.043664  ,  0.20250848, -0.10110267,
        0.03994785,  0.21724854,  0.03390542, -0.08351826,  0.08301376,
        0.05327167, -0.19607782,  0.00106234, -0.04046681,  0.02241045,
        0.03855221, -0.21100445,  0.00413722,  0.00519415, -0.16783927,
        0.23810072, -0.03997205, -0.02630986, -0.0294307 , -0.1313584 ,
       -0.0044685 , -0.00039468,  0.23315869, -0.32524279,  0.23468108,
        0.1795879 ,  0.05994981,  0.16155675,  0.01906111,  0.06274381,
        0.01042214,  0.0393453 , -0.25271848, -0.09878332,  0.03960638,
       -0.02105927, -0.01200039,  0.0832946 ], [-1.58522725e-01,  1.83218256e-01,  1.25399828e-01,  7.66650820e-03,
       -1.44560635e-01, -1.07845645e-02, -4.16677743e-02, -3.71088944e-02,
        1.78978369e-01, -2.14561149e-02,  2.61412561e-01, -3.42612751e-02,
       -1.60953477e-01, -5.01086526e-02, -3.07997447e-02,  1.61255896e-01,
       -1.33171842e-01, -8.49718451e-02, -3.74674760e-02, -6.70020655e-02,
        9.53378379e-02,  6.72526881e-02,  5.11669554e-02,  1.31533099e-02,
       -1.15928911e-01, -3.57182264e-01,  1.12565514e-03, -1.32276744e-01,
        1.19097538e-01, -1.35370955e-01, -8.36986080e-02,  7.54816597e-03,
       -1.51440978e-01, -6.71943575e-02,  1.13894027e-02,  4.42649461e-02,
       -3.03510763e-02, -1.20377310e-01,  1.73888952e-01, -7.54352883e-02,
       -1.87271386e-01,  3.60102486e-03,  2.42263973e-02,  2.39396200e-01,
        1.82217464e-01, -7.41451532e-02,  4.68509793e-02, -1.58801436e-01,
        1.43389791e-01, -1.58627361e-01,  1.10172369e-01,  1.37902588e-01,
        4.49548028e-02,  7.93577209e-02,  1.23410039e-01, -1.26848325e-01,
        1.33482525e-02,  1.28682464e-01, -2.16524556e-01,  3.50204557e-02,
        9.51840132e-02,  8.20144564e-02, -5.60473502e-02, -1.09419860e-01,
        1.20385177e-01,  1.18357867e-01, -1.17147543e-01, -1.74571976e-01,
        5.86337373e-02, -1.15932018e-01, -4.83322479e-02,  7.57123157e-02,
       -1.15441561e-01, -1.94829613e-01, -3.03521603e-01,  3.02498583e-02,
        3.49714875e-01,  1.51054606e-01, -2.79363841e-01, -6.89904019e-03,
       -8.13210756e-03, -5.90994209e-02,  1.16274193e-01,  1.34804428e-01,
       -6.30155653e-02,  2.38882862e-02, -1.07490256e-01,  3.11890524e-02,
        9.81269628e-02,  2.76156254e-02, -5.84613793e-02,  2.34406784e-01,
        4.04508188e-02, -2.02208646e-02,  3.35371792e-02,  1.84435472e-01,
       -1.59224123e-01, -9.62631404e-03, -1.37763873e-01, -6.29379600e-02,
        5.92261180e-02, -4.90200110e-02, -8.35228488e-02,  1.31933168e-01,
       -1.80147812e-01,  2.01610148e-01, -2.08224729e-03,  6.48586154e-02,
       -4.49815094e-02, -7.26484433e-02, -1.87506694e-02,  4.22335118e-02,
        1.04820274e-01, -1.89221084e-01,  1.53326124e-01,  1.01801418e-01,
        2.58116368e-02,  1.71575949e-01,  6.09338135e-02,  2.02486385e-02,
        3.18324426e-03, -4.72326763e-02, -1.51096389e-01, -5.02207130e-02,
       -1.95712782e-04, -4.18898612e-02,  2.27442402e-02,  5.64599782e-02], [-0.08478162,  0.06980959, -0.00868447, -0.11696958, -0.08536634,
        0.06024005, -0.01286111, -0.07392724,  0.16652319, -0.07776348,
        0.226907  ,  0.09031598, -0.31223229, -0.05724759,  0.0939795 ,
        0.0315448 , -0.19445942, -0.12445823, -0.06360479, -0.10525957,
       -0.01994105,  0.03469551, -0.03778994,  0.03152243, -0.13219014,
       -0.24694891, -0.06686708, -0.04146481,  0.02747064, -0.09059735,
        0.07466417,  0.04657922, -0.17028064, -0.03064576,  0.07753187,
        0.16473956, -0.10376266, -0.08700803,  0.26076272,  0.0262095 ,
       -0.12148138, -0.0220125 ,  0.07322782,  0.26011547,  0.17268188,
       -0.00746564,  0.01058578, -0.06059321,  0.16771421, -0.30205819,
        0.1310734 ,  0.20229855,  0.13361891,  0.08909329,  0.0225025 ,
       -0.26509508, -0.04978203,  0.17952611, -0.17891869,  0.09937079,
        0.03146577, -0.13603991, -0.07979651, -0.05764761,  0.21794099,
        0.14636038, -0.19422042, -0.18633419,  0.19646579, -0.11768723,
       -0.13962899,  0.11483273, -0.14972967, -0.19568743, -0.24941571,
        0.1429134 ,  0.42525777,  0.11264718, -0.16666   , -0.01578722,
       -0.09021887, -0.07347081, -0.01116241,  0.14669538, -0.05219819,
       -0.06325159, -0.0375569 ,  0.04793857,  0.24459803,  0.03575182,
       -0.11191981,  0.20215032,  0.04434559,  0.08981177,  0.04709392,
        0.04435253, -0.03805794, -0.06571217, -0.20764026, -0.05298742,
        0.01271482, -0.13850848, -0.00717725,  0.16107038, -0.17787641,
        0.21889912,  0.06393985, -0.06510997,  0.0030875 , -0.01896513,
       -0.10861555, -0.0057331 ,  0.19872056, -0.34656361,  0.27892208,
        0.17510778,  0.13303085,  0.18787764,  0.10201351,  0.07336922,
        0.09424656, -0.04801069, -0.16777354, -0.10747477, -0.01318072,
        0.04021424,  0.05301973,  0.0376516 ], [-5.49493954e-02,  3.77254486e-02,  1.55936673e-01,  1.70047767e-02,
       -2.03493461e-02, -1.02373578e-01, -7.07861781e-02, -1.26997560e-01,
        9.46515054e-02, -1.14004262e-01,  2.41973430e-01, -7.90873170e-03,
       -2.37219766e-01, -1.12830894e-02, -3.95141803e-02,  1.31718725e-01,
       -1.57242626e-01, -4.58349101e-02, -9.96758416e-02, -3.49048413e-02,
        1.40673239e-02,  6.42407462e-02,  9.75081474e-02, -1.43951550e-02,
       -1.21758513e-01, -3.07522655e-01, -1.57088041e-01, -6.77957833e-02,
        8.95266309e-02, -3.24235670e-02, -4.96013798e-02, -2.71644872e-02,
       -1.62805930e-01, -8.19611773e-02,  2.25209631e-02,  2.17089225e-02,
       -7.22969696e-02, -1.07230991e-01,  1.62998691e-01,  7.49918669e-02,
       -1.21825106e-01,  2.71637607e-02, -1.31609198e-03,  2.93054163e-01,
        1.58273399e-01,  9.32327658e-02,  6.88809454e-02, -7.79430494e-02,
        2.22342089e-04, -2.32744694e-01,  8.38464648e-02,  8.11590552e-02,
        1.17897004e-01,  4.80746776e-02,  1.57241255e-01, -1.79915980e-01,
        6.80582076e-02,  2.05710366e-01, -1.93448514e-01,  1.37985945e-01,
        2.91685816e-02,  1.38578992e-02,  1.25229418e-01,  5.41878343e-02,
        2.33001962e-01,  6.22740462e-02, -1.17325798e-01, -4.83012088e-02,
        1.00075446e-01, -1.17809460e-01, -3.97976255e-03,  2.88871937e-02,
       -7.23220259e-02, -1.86464027e-01, -2.78431267e-01, -3.59610505e-02,
        3.88192862e-01,  1.37040854e-01, -1.93718851e-01,  2.07273439e-02,
       -1.08443491e-01, -1.00234523e-01,  9.16345045e-02,  4.76215966e-02,
       -8.34830105e-02, -1.17475633e-02, -1.46253586e-01, -2.81207655e-02,
        1.77483186e-01, -6.27243239e-03, -3.73050524e-03,  2.72792220e-01,
       -2.75894199e-02, -9.07927081e-02,  2.79813893e-02, -4.01843665e-03,
       -2.20689029e-01, -1.30841546e-02, -6.98594302e-02, -1.29370436e-01,
        3.47355492e-02, -9.72112641e-02, -5.40933292e-03,  1.07882343e-01,
       -2.32346609e-01,  1.44372717e-01, -1.69684961e-02, -5.31995744e-02,
        2.62112170e-02, -1.43183107e-02, -1.21769406e-01, -1.59831606e-02,
        1.56867743e-01, -2.74480700e-01,  1.56161994e-01,  2.22730801e-01,
        1.92534383e-02,  1.35168344e-01,  6.45205677e-02,  9.47355106e-03,
       -2.57490389e-02,  1.95272863e-02, -1.18104190e-01, -8.12353939e-02,
       -1.00398464e-02, -5.66168837e-02,  1.12452358e-01,  5.46187088e-02]]
    img = face_recognition.load_image_file(file)
    unknown_face_encodings = face_recognition.face_encodings(img)

    face_found = False
    is_admin= False

    if len(unknown_face_encodings) > 0:
        face_found = True
        match_results = face_recognition.compare_faces([known_face_encoding[adminid]], unknown_face_encodings[0])
        if match_results[0]:
            is_admin = True
    result = {
        "face_found_in_image": face_found,
        "is_picture_of_admin": is_admin
    }
    return result