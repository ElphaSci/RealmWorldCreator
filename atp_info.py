import copy

global ATP_INFO
global ATP_CATEGORIES


class ATPNode:
    def __init__(self, number=0, roomType=0, noun='', view=0, pCategory=0, pDescriber='', x=0, y=0, z=0, pPolygon=0,
                 pDoScaler=None, priority=0, pVersion=1, pPlacement=0, pUncommon=0, pMsgFile=0):
        self.attributes = ['number', 'roomType', 'noun', 'view', 'pCategory', 'pDescriber', 'x', 'y', 'z', 'pPolygon',
                           'pDoScaler', 'priority', 'pVersion', 'pPlacement', 'pUncommon', 'pMsgFile']
        for attr in self.attributes:
            if attr == 'pDoScaler' and eval('roomType') != 0 and eval(attr) is None:
                setattr(self, attr, True)
                continue
            setattr(self, attr, eval(attr))
        if number == 0:
            self.number = view - 1000
        elif number > 32768:
            self.number = number - 32768
            self.mirror = True

    def view(self):
        if self.view == 0:
            return self.number + 1000
        return self.view

    def set_room_type(self, roomType):
        if self.pDoScaler is None:
            self.pDoScaler = not roomType in ['TOWN1INT', 'TOWN1', 'HOUSE', 'HOUSE1INT']
        self.roomType = roomType


class Region(dict):
    def __init__(self, name, atp_categories):
        dict.__init__({name: atp_categories})


MidTrees = mySet = [ATPNode(view=1015, noun='BIRCH_CLUMP_N', pDescriber="Birch Clump 1", pDoScaler=True),
                    ATPNode(view=1040, noun='PINE_N', pDescriber="Pine 1A", pDoScaler=True),
                    ATPNode(view=1041, noun='PINE_N', pDescriber="Pine 1B", pDoScaler=True),
                    ATPNode(view=1042, noun='PINE_N', pDescriber="Pine 1C", pDoScaler=True),
                    ATPNode(view=1048, noun='PINE_N', pDescriber="Pine 1", pDoScaler=True),
                    ATPNode(view=1105, noun='PINE_N', pDescriber="Pine 1D", pDoScaler=True),
                    ATPNode(view=1043, noun='PINE_N', pDescriber="Pine 1", pDoScaler=True),
                    ATPNode(view=1044, noun='PINE_N', pDescriber="Pine 2", pDoScaler=False),
                    ATPNode(view=1045, noun='PINE_LARGE_N', pDescriber="Large pine", pDoScaler=False),
                    ATPNode(view=1046, noun='PINE_SHORT_N', pDescriber="Short pine 1", pDoScaler=True),
                    ATPNode(view=1047, noun='PINE_SHORT_N', pDescriber="pine", pDoScaler=True),
                    ATPNode(view=1049, noun='PINE2_N', pDescriber="Avg pine 2", pDoScaler=False),
                    ATPNode(view=1050, noun='PINE_LEAN_N', pDescriber="Leaning pine", pDoScaler=False),
                    ATPNode(view=1051, noun='PINE_DEAD_N', pDescriber="Dead pine", pDoScaler=True),
                    ATPNode(view=1103, noun='BIRCH_CLUMP_N', pDescriber="Birch Clump 3", pDoScaler=True),
                    ATPNode(view=1109, noun='BIRCH_CLUMP_N', pDescriber="Birch Clump 2", pDoScaler=True),
                    ATPNode(view=1120, noun='PINE2_N', pDescriber="Thin Pine", pDoScaler=False),
                    ATPNode(view=1121, noun='CEDAR_CURVED_N', pDescriber="Curved Cedar", pDoScaler=False),
                    ATPNode(view=1122, noun='CEDAR_CURVED_N', pDescriber="Large Tree, Droops", pDoScaler=False),
                    ATPNode(view=1123, noun='BARE_TREE_N', pDescriber="Bare Tree", pDoScaler=True),
                    ATPNode(view=1124, noun='BARE_TREE_N', pDescriber="Full Tree", pDoScaler=True),
                    ATPNode(view=1126, noun='BARE_TREE_N', pDescriber="Tall Tree", pDoScaler=True),
                    ATPNode(view=1125, noun='BARE_TREE_N', pDescriber="Open Tree, Heavy on top", pDoScaler=True),
                    ATPNode(view=1127, noun='PINE2_N', pDescriber="Pine", pDoScaler=True),
                    ATPNode(view=1128, noun='BENT_TREE_N', pDescriber="Bent Tree", pDoScaler=True),
                    ATPNode(view=1131, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=1132, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=1133, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=1134, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=1135, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=1136, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=1137, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=1138, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=1139, noun='BONSAI_N', pDescriber="Bonsai", pDoScaler=True),
                    ATPNode(view=3718, noun='TREE_N', pDescriber="Big Fir", pDoScaler=False),
                    ATPNode(view=3719, noun='TREE_N', pDescriber="Big Fir", pDoScaler=False),
                    ATPNode(view=3951, noun='PINE_SKINNY_N', pDescriber="Skinny Pine", pDoScaler=False),
                    ATPNode(view=3952, noun='PINE_N', pDescriber="Small Pine", pDoScaler=False),
                    ATPNode(view=3953, noun='OAK_N', pDescriber="oak tree", pDoScaler=False)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Mid Trees"
    obj.pPlacement = 'MID1 MID2 MID3 MID4 MID5'
    if obj.pDescriber == '':
        obj.pDescriber = 'Mid'

MidPlant = mySet = [ATPNode(view=1060, noun='BUSH_MED_N', pDescriber="Grn md bush", pDoScaler=True),
                    ATPNode(view=1061, noun='BUSH_N', pDescriber="Low bush", pPolygon=-1, pDoScaler=True),
                    ATPNode(view=1062, noun='BUSH_FLOWER_N', pDescriber="Flower bush", pDoScaler=True),
                    ATPNode(view=1063, noun='BUSH_PINK_N', pDescriber="Pink flowers", pDoScaler=True),
                    ATPNode(view=1064, noun='BUSH_YELLO_N', pDescriber="Yellow flowers", pDoScaler=True),

                    ATPNode(view=1065, noun='BUSH_LEAFY_N', pDescriber="Leafy bushA", pDoScaler=True),
                    ATPNode(view=1066, noun='BUSH_LEAFY_N', pDescriber="Leafy bush", pDoScaler=True),
                    ATPNode(view=1104, noun='BUSH_N', pDescriber="Willow Bush", pDoScaler=True),
                    ATPNode(view=3711, noun='BUSH_SML_N', pDescriber="Grn sm bush", pDoScaler=False),
                    ATPNode(view=3712, noun='BUSH_SML_N', pDescriber="Bush", pDoScaler=False),
                    ATPNode(view=3955, noun='BUSH_SML_N', pDescriber="Low bush", pPolygon=-1, pDoScaler=False),
                    ATPNode(view=3956, noun='BUSH_SML_N', pDescriber="Low bush", pPolygon=-1, pDoScaler=False)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Plants"
    obj.pPlacement = 'MID1 MID2 MID3 MID4 MID5'
    if not obj.pDescriber:
        obj.pDescriber = "Plants"

ForeTrees = mySet = [ATPNode(view=1100, noun='BUSH_LEAFY_N', pDescriber="Bushes", y=325),

                     ATPNode(view=1101, noun='BIRCH_CLUMP_N', pDescriber="Large TreeA"),
                     ATPNode(view=1102, noun='PINE_BIGMAMA_N', pDescriber="Mama pine", y=319),
                     ATPNode(view=1103, noun='BIRCH_CLUMP_N', pDescriber="Birch Clump 3"),
                     ATPNode(view=1106, noun='CEDAR_FORE_N', pDescriber="Cedar", y=317),
                     ATPNode(view=1107, noun='PINE_FORE_N', pDescriber="Pine", y=318),
                     ATPNode(view=1108, noun='BIRCH_CLUMP_N', pDescriber="Tree LeftA"),
                     ATPNode(view=1109, noun='BIRCH_CLUMP_N', pDescriber="Birch Clump 2")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Fore Trees"
    obj.pDoScaler = False
    obj.pPlacement = 'FORE'
    if not obj.pDescriber:
        obj.pDescriber = "Fore"

Rocks = mySet = [ATPNode(view=1200, noun='ROCKS_2_N', pDescriber="2 Rocks", pDoScaler=True),
                 ATPNode(view=1201, noun='ROCK_MED_N', pDescriber="Rock", pDoScaler=True),
                 ATPNode(view=1202, noun='ROCK_BIG_N', pDescriber="Rock-Big", pDoScaler=True),
                 ATPNode(view=1203, noun='ROCK_MED_N', pDescriber="Rock-Med", pDoScaler=True),
                 ATPNode(view=1204, noun='ROCK_SML_N', pDescriber="Rock-Small", pDoScaler=True),
                 ATPNode(view=1250, noun='TOMBSTONE_N', pDescriber="Tomb stone-Plain", pDoScaler=True),
                 ATPNode(view=1251, noun='TOMBSTONE2_N', pDescriber="Tomb stone-Cross", pDoScaler=True),
                 ATPNode(view=1252, noun='TOMBSTONE3_N', pDescriber="Tomb stone-Lg-Cross", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Rocks"
    obj.pDoScaler = True
    if not obj.pDescriber:
        obj.pDescriber = "Rock"

BackTrees = mySet = [ATPNode(view=1140, noun='TREE_BKGD1_N', pDescriber="distant-Tree", pPolygon=-1),
                     ATPNode(view=1141, noun='TREE_BKGD1_N', pDescriber="distant-Tree", pPolygon=-1),
                     ATPNode(view=1142, noun='TREE_BKGD1_N', pDescriber="distant-Tree", pPolygon=-1),
                     ATPNode(view=1145, noun='TREE_BKGD1_N', pDescriber="distant-Tree", pPolygon=-1),
                     ATPNode(view=1146, noun='TREE_BKGD1_N', pDescriber="distant-Tree", pPolygon=-1),
                     ATPNode(view=1149, noun='TREE_BKGD1_N', pDescriber="Full-Tree-L", pPolygon=-1,
                             pPlacement='BACK_FULL'),
                     ATPNode(view=1150, noun='TREE_BKGD1_N', pDescriber="Full-Tree", pPolygon=-1,
                             pPlacement='BACK_FULL'),
                     ATPNode(view=1151, noun='TREE_BKGD1_N', pDescriber="Full-Tree-R", pPolygon=-1,
                             pPlacement='BACK_FULL'),
                     ATPNode(view=1152, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1153, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1154, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1155, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1156, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1157, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1158, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1159, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1160, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1161, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1162, noun='PINE_BKGD_N', pDescriber="Pines-Bkgd", pPolygon=-1),
                     ATPNode(view=1163, noun='TREE_BKGD3_N', pDescriber="Many Pines", pPolygon=-1),
                     ATPNode(view=1164, noun='TREE_BKGD3_N', pDescriber="Many Pines", pPolygon=-1),
                     ATPNode(view=1165, noun='TREE_BKGD3_N', pDescriber="Half-Bkgd", pPolygon=-1),
                     ATPNode(view=1066, noun='TREE_BKGD3_N', pDescriber="Dead tree", pPolygon=-1),
                     ATPNode(view=1067, noun='TREE_BKGD3_N', pDescriber="Dead tree", pPolygon=-1),
                     ATPNode(view=1068, noun='TREE_BKGD3_N', pDescriber="Live tree", pPolygon=-1),
                     ATPNode(view=1069, noun='TREE_BKGD3_N', pDescriber="Live treeA", pPolygon=-1),
                     ATPNode(view=1070, noun='TREE_BKGD3_N', pDescriber="Live treeB", pPolygon=-1),
                     ATPNode(view=1071, noun='TREE_BKGD3_N', pDescriber="Live treeC", pPolygon=-1),
                     ATPNode(view=1168, noun='TREE_BKGD3_N', pDescriber="Half-Bkgd", pPolygon=-1),
                     ATPNode(view=1175, noun='TREE_BKGD2_N', pDescriber="Far Forest-Mid", pPolygon=-1),
                     ATPNode(view=1176, noun='TREE_BKGD2_N', pDescriber="Far Forest-Lft", pPolygon=-1),
                     ATPNode(view=1177, noun='TREE_BKGD2_N', pDescriber="Far Forest-Rt", pPolygon=-1),
                     ATPNode(view=3715, noun='TREE_TRUNK_N', pDescriber="Tree-trunk"),
                     ATPNode(view=3742, noun='TREE_BKGD3_N', pDescriber="Half-Bkgd", pPolygon=-1),
                     ATPNode(view=3743, noun='TREE_BKGD1_N', pDescriber="Full-Tree-M", pPolygon=-1,
                             pPlacement='BACK_FULL')]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Bkgd"
    obj.pDoScaler = False

    if obj.pPlacement == 0:
        obj.pPlacement = 'BACK'

        if not obj.pDescriber:
            obj.pDescriber = "Bkgd"

Sky = mySet = [ATPNode(view=1093, noun='SKY_N', pDescriber="Sky-a", pDoScaler=False, pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1094, noun='SKY_N', pDescriber="Sky-b", pDoScaler=False, pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1096, noun='SKY_N', pDescriber="Sky-c", pDoScaler=False, pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1240, noun='CLOUD1_N', pDescriber="Cloud", pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1241, noun='CLOUD2_N', pDescriber="Cloud", pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1242, noun='CLOUDS_N', pDescriber="Cloud", pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1243, noun='CLOUD1_N', pDescriber="Cloud", pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1244, noun='CLOUD2_N', pDescriber="Cloud", pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1245, noun='CLOUDS_N', pDescriber="Cloud", pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1246, noun='CLOUD1_N', pDescriber="Cloud", pPolygon=-1, pPlacement='SKY'),
               ATPNode(view=1751, noun='MIST_N', pDescriber="Mist", pPolygon=-1, pDoScaler=False),
               ATPNode(view=1752, noun='MIST_N', pDescriber="Mist", pPolygon=-1, pDoScaler=False),
               ATPNode(view=1753, noun='MIST_N', pDescriber="Mist", pPolygon=-1, pDoScaler=False),
               ATPNode(view=1754, noun='MIST_N', pDescriber="Mist", pPolygon=-1, pDoScaler=False),
               ATPNode(view=1755, noun='MIST_N', pDescriber="Mist", pPolygon=-1, pDoScaler=False),
               ATPNode(view=1756, noun='MIST_N', pDescriber="Mist", pPolygon=-1, pDoScaler=False)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Sky"
    if not obj.pDescriber:
        obj.pDescriber = "Sky"

Ground = mySet = [ATPNode(view=1110, noun='GRASS2_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1111, noun='GRASS2_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1112, noun='GRASS1_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1113, noun='GRASS2_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1114, noun='GRASS1_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1115, noun='GRASS2_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1180, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1181, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1182, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1183, noun='GRASS1_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1184, noun='GRASS2_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1185, noun='GRASS2_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1186, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),

                  ATPNode(view=1187, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1188, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1222, noun='GRASS1_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=1223, noun='GRASS1_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),

                  ATPNode(view=1224, noun='GRASS1_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                  ATPNode(view=3716, noun='GRASS1_N', pDescriber="grass", pDoScaler=False, pPolygon=-1)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Ground"
    obj.pPlacement = 'GROUND'

    if not obj.pDescriber:
        obj.pDescriber = "Ground"

MiscForest = mySet = [ATPNode(view=1080, noun='POINTSIGN_N', pDescriber="PointSign-E/W", pDoScaler=False),
                      ATPNode(view=1081, noun='POINTSIGN_N', pDescriber="PointSign-N", pDoScaler=False),
                      ATPNode(view=1082, noun='POINTSIGN_N', pDescriber="PointSign-S", pDoScaler=False),
                      ATPNode(view=1085, noun='CART_N', pDescriber="Cart-front", pDoScaler=True),
                      ATPNode(view=1086, noun='CART_N', pDescriber="Cart-back", pDoScaler=True),
                      ATPNode(view=1189, noun='TOWN_GATE_N', pDescriber="stone-gate-side", pDoScaler=False),
                      ATPNode(view=1190, noun='TOWN_WALL_N', pDescriber="stone-wall-side", pDoScaler=False),
                      ATPNode(view=1191, noun='TOWN_GATE_N', pDescriber="stone-gate-side", pDoScaler=False),

                      ATPNode(view=1192, noun='TOWN_GATE_N', pDescriber="stone-gate-side", pDoScaler=False),
                      ATPNode(view=1193, noun='TOWN_GATE_N', pDescriber="stone-gate-side", pDoScaler=False),
                      ATPNode(view=1194, noun='TOWN_DIST_N', pDescriber="Town-dist-view1", pDoScaler=False,
                              pPolygon=-1),
                      ATPNode(view=1195, noun='TOWN_DIST_N', pDescriber="Town-dist-view2", pDoScaler=False,
                              pPolygon=-1),
                      ATPNode(view=1196, noun='TOWN_WALL_N', pDescriber="Stone-wall-far", pDoScaler=False, pPolygon=-1),
                      ATPNode(view=1197, noun='TOWN_DIST_N', pDescriber="Roof tops", pDoScaler=False, pPolygon=-1),
                      ATPNode(view=1198, noun='TOWN_DIST_N', pDescriber="Roof tops-2", pDoScaler=False, pPolygon=-1),

                      ATPNode(view=1199, noun='TOWN_DIST_N', pDescriber="Roof tops-2", pDoScaler=False, pPolygon=-1),
                      ATPNode(view=1208, noun='RIVER_LOG_N', pDescriber="Plank-EW", pPolygon=-1, pDoScaler=True),
                      ATPNode(view=1209, noun='RIVER_LOG_N', pDescriber="Plank-NS", pPolygon=-1, pDoScaler=True),
                      ATPNode(view=3536, noun='TOWN_WALL_N', pDescriber="stone-wall-back"),
                      ATPNode(view=3539, noun='TOWN_GATE_N', pDescriber="stone-gate-far", pPolygon=-1)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Misc"
    if obj.pPlacement == 0:
        obj.pPlacement = 'SPECIAL'
        if not obj.pDescriber:
            obj.pDescriber = "Misc"

Mountains = mySet = [ATPNode(view=1169, noun='MTNBKGD1_N', pDescriber="Mtn-full-1"),
                     ATPNode(view=1170, noun='MTNBKGD1_N', pDescriber="Mtn-full-2"),
                     ATPNode(view=1171, noun='MTNBKGD1_N', pDescriber="Mtn"),
                     ATPNode(view=1172, noun='MTNBKGD1_N', pDescriber="Mtn-half"),
                     ATPNode(view=1173, noun='HILLS_N', pDescriber="Hill-1"),
                     ATPNode(view=1174, noun='HILLS_N', pDescriber="Hill-2"),
                     ATPNode(view=2250, noun='MTNBKGD1_N', pDescriber="M-trees-1"),
                     ATPNode(view=2251, noun='MTNBKGD1_N', pDescriber="M-trees-2"),
                     ATPNode(view=2260, noun='MTNBKGD1_N', pDescriber="S-trees-1"),
                     ATPNode(view=2261, noun='MTNBKGD1_N', pDescriber="S-trees-2"),
                     ATPNode(view=2262, noun='MTNBKGD1_N', pDescriber="S-trees-3"),
                     ATPNode(view=2270, noun='MTNBKGD1_N', pDescriber="Trees-1"),
                     ATPNode(view=2271, noun='MTNBKGD1_N', pDescriber="Trees-2"),
                     ATPNode(view=2272, noun='MTNBKGD1_N', pDescriber="Trees-3"),
                     ATPNode(view=2273, noun='MTNBKGD1_N', pDescriber="Trees-4"),
                     ATPNode(view=2274, noun='MTNBKGD1_N', pDescriber="Trees-4"),
                     ATPNode(view=2275, noun='MTNBKGD1_N', pDescriber="Trees-4"),
                     ATPNode(view=2280, noun='MTNBKGD1_N', pDescriber="Far-trees-1"),
                     ATPNode(view=2281, noun='MTNBKGD1_N', pDescriber="Far-trees-2"),
                     ATPNode(view=2282, noun='MTNBKGD1_N', pDescriber="Far-trees-3"),
                     ATPNode(view=2283, noun='MTNBKGD1_N', pDescriber="Far-trees-4"),
                     ATPNode(view=2300, noun='HILLS_N', pDescriber="Hill-3"),
                     ATPNode(view=2301, noun='HILLS_N', pDescriber="Hill-4"),
                     ATPNode(view=2302, noun='MTNBKGD1_N', pDescriber="Far-Mtn-1"),
                     ATPNode(view=2303, noun='MTNBKGD1_N', pDescriber="Far-Mtn-2"),
                     ATPNode(view=2304, noun='MTNBKGD1_N', pDescriber="Far-Mtn-3"),
                     ATPNode(view=2305, noun='MTNBKGD1_N', pDescriber="Far-Mtn-4"),
                     ATPNode(view=2306, noun='MTNBKGD1_N', pDescriber="Far-Mtn-5"),
                     ATPNode(view=2307, noun='MTNBKGD1_N', pDescriber="Far-Mtn-6"),
                     ATPNode(view=2308, noun='MTNBKGD1_N', pDescriber="Far-Mtn-7")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Mountains"
    obj.pDoScaler = False
    obj.pPolygon = -1

if obj.pPlacement == 0:
    obj.pPlacement = 'BACK'

    if not obj.pDescriber:
        obj.pDescriber = "Mountains"

River = mySet = [ATPNode(view=1205, noun='RIVER_N', pDescriber="NS-distant", pDoScaler=False),
                 ATPNode(view=1206, noun='RIVER_N', pDescriber="WN-curve", pDoScaler=False),
                 ATPNode(view=1207, noun='RIVER_N', pDescriber="Tee", pDoScaler=False),
                 ATPNode(view=1210, noun='RIVER_N', pDescriber="across1", pDoScaler=True),
                 ATPNode(view=1211, noun='RIVER_N', pDescriber="across2", pDoScaler=True),
                 ATPNode(view=1212, noun='RIVER_N', pDescriber="across3", pDoScaler=True),
                 ATPNode(view=1213, noun='RIVER_N', pDescriber="across4", pDoScaler=True),
                 ATPNode(view=1214, noun='RIVER_N', pDescriber="diag1", pDoScaler=True),
                 ATPNode(view=1215, noun='RIVER_N', pDescriber="diag2", pDoScaler=True),
                 ATPNode(view=1216, noun='RIVER_N', pDescriber="diag3", pDoScaler=True),
                 ATPNode(view=1217, noun='RIVER_N', pDescriber="up1", pDoScaler=False),
                 ATPNode(view=1218, noun='RIVER_N', pDescriber="up2", pDoScaler=True),
                 ATPNode(view=1219, noun='RIVER_N', pDescriber="up3", pDoScaler=False),
                 ATPNode(view=1220, noun='RIVER_N', pDescriber="up4", pDoScaler=True),
                 ATPNode(view=1221, noun='RIVER_N', pDescriber="SE-curve", pDoScaler=True),
                 ATPNode(view=1236, noun='RIVER_N', pDescriber="NS-distant", pDoScaler=False),
                 ATPNode(view=1237, noun='RIVER_N', pDescriber="NS-island", pDoScaler=False),
                 ATPNode(view=1238, noun='RIVER_N', pDescriber="NS-distant", pDoScaler=False),
                 ATPNode(view=1239, noun='RIVER_N', pDescriber="NS-mid", pDoScaler=False),
                 ATPNode(view=1247, noun='RIVER_N', pDescriber="NE-curve", pDoScaler=True),
                 ATPNode(view=1248, noun='SKY_COMBAT_N', pDescriber="horz-polygon", pDoScaler=False),
                 ATPNode(view=1249, noun='SKY_COMBAT_N', pDescriber="vert-polygon", pDoScaler=False)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: River"
    obj.pPlacement = 'GROUND'

    if not obj.pDescriber:
        obj.pDescriber = "River"

Lake = mySet = [ATPNode(view=1930, noun='LAKE_N', pDescriber="Spring", pDoScaler=True, pPolygon=-1),
                ATPNode(view=1932, noun='LAKE_N', pDescriber="Side-1", pDoScaler=False),
                ATPNode(view=1933, noun='LAKE_N', pDescriber="Side-2", pDoScaler=False),
                ATPNode(view=1934, noun='LAKE_N', pDescriber="Back-1", pDoScaler=False),
                ATPNode(view=1935, noun='LAKE_N', pDescriber="Back-2", pDoScaler=False),
                ATPNode(view=1936, noun='LAKE_N', pDescriber="Back-3", pDoScaler=False),
                ATPNode(view=1937, noun='LAKE_N', pDescriber="Side-3", pDoScaler=False),
                ATPNode(view=1938, noun='LAKE_N', pDescriber="Back-4", pDoScaler=False),
                ATPNode(view=1939, noun='LAKE_N', pDescriber="Side-4", pDoScaler=False),
                ATPNode(view=1940, noun='LAKE_N', pDescriber="Side-5", pDoScaler=False),
                ATPNode(view=1941, noun='LAKE_N', pDescriber="Side-6", pDoScaler=False),
                ATPNode(view=1942, noun='LAKE_N', pDescriber="Side-7", pDoScaler=False),
                ATPNode(view=1943, noun='LAKE_N', pDescriber="Side-8", pDoScaler=False),
                ATPNode(view=1944, noun='LAKE_N', pDescriber="Side-9", pDoScaler=False),
                ATPNode(view=1945, noun='LAKE_N', pDescriber="Side-10", pDoScaler=False),
                ATPNode(view=1946, noun='LAKE_N', pDescriber="Side-11", pDoScaler=False),
                ATPNode(view=1947, noun='LAKE_N', pDescriber="Front-1", pDoScaler=False),
                ATPNode(view=1948, noun='LAKE_N', pDescriber="Front-2", pDoScaler=False),
                ATPNode(view=1949, noun='LAKE_N', pDescriber="Front-3", pDoScaler=False),
                ATPNode(view=1950, noun='LAKE_N', pDescriber="Front-4", pDoScaler=False),
                ATPNode(view=1951, noun='LAKE_N', pDescriber="Large", pDoScaler=False),
                ATPNode(view=1952, noun='LAKE_N', pDescriber="Medium", pDoScaler=False),
                ATPNode(view=1953, noun='LAKE_N', pDescriber="Small", pDoScaler=False),
                ATPNode(view=1954, noun='LAKE_N', pDescriber="Large-curve", pDoScaler=False),
                ATPNode(view=1955, noun='LAKE_N', pDescriber="Small-curve", pDoScaler=False),
                ATPNode(view=1957, noun='WAVE_N', pDescriber="Wave-1", pDoScaler=False),
                ATPNode(view=1958, noun='WAVE_N', pDescriber="Wave-2", pDoScaler=False),
                ATPNode(view=1959, noun='WAVE_N', pDescriber="Wave-3", pDoScaler=False),
                ATPNode(view=1960, noun='WAVE_N', pDescriber="Wave-4", pDoScaler=False)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Lake"
    obj.pPlacement = 'GROUND'

    if not obj.pDescriber:
        obj.pDescriber = "Lake"

Road = mySet = [ATPNode(view=1225, noun='PATH1_N', pDescriber="Cap-small", pDoScaler=True),
                ATPNode(view=1226, noun='PATH1_N', pDescriber="Cap-big", pDoScaler=True),
                ATPNode(view=1227, noun='PATH1_N', pDescriber="Curve-SW", pDoScaler=True),
                ATPNode(view=1228, noun='PATH1_N', pDescriber="Curve-NW", pDoScaler=True),
                ATPNode(view=1229, noun='PATH_N', pDescriber="E-W 1", pDoScaler=True),
                ATPNode(view=1230, noun='PATH_N', pDescriber="E-W 2", pDoScaler=True),
                ATPNode(view=1231, noun='PATH_DIST_N', pDescriber="E-W dist", pDoScaler=True),
                ATPNode(view=1232, noun='PATH_DIST_N', pDescriber="N-S dist", pDoScaler=True),
                ATPNode(view=1233, noun='PATH_N', pDescriber="N-S close", pDoScaler=True),
                ATPNode(view=1234, noun='PATH_DIST_N', pDescriber="N-S dist2", pDoScaler=False),
                ATPNode(view=1235, noun='PATH_DIST_N', pDescriber="Curve-NW-dist", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Forest: Road"
    obj.pPolygon = -1
    obj.pPlacement = 'GROUND'

if not obj.pDescriber:
    obj.pDescriber = "Road"

Polygons = mySet = [ATPNode(view=1001, noun='0', pDescriber="sq-polygon"),
                    ATPNode(view=1002, noun='0', pDescriber="sq-polygon"),
                    ATPNode(view=1003, noun='0', pDescriber="sq-polygon"),
                    ATPNode(view=1004, noun='0', pDescriber="horz-polygon"),
                    ATPNode(view=1005, noun='0', pDescriber="horz-polygon"),
                    ATPNode(view=1006, noun='0', pDescriber="horz-polygon"),
                    ATPNode(view=1007, noun='0', pDescriber="horz-polygon"),
                    ATPNode(view=1008, noun='0', pDescriber="vert-polygon"),
                    ATPNode(view=1009, noun='0', pDescriber="vert-polygon"),
                    ATPNode(view=1010, noun='0', pDescriber="vert-polygon"),
                    ATPNode(view=1011, noun='0', pDescriber="vert-polygon"),
                    ATPNode(view=1012, noun='0', pDescriber="vert-polygon"),
                    ATPNode(view=1013, noun='0', pDescriber="big mamma"),
                    ATPNode(view=1014, noun='0', pDescriber="wall tall"),
                    ATPNode(view=1016, noun='0', pDescriber="wall short"),
                    ATPNode(view=8900, noun='0', pDescriber="X-tra-long-tall"),
                    ATPNode(view=8901, noun='0', pDescriber="Long-tall"),
                    ATPNode(view=8902, noun='0', pDescriber="X-tra-long-short"),
                    ATPNode(view=8903, noun='0', pDescriber="Long-short"),
                    ATPNode(view=8904, noun='0', pDescriber="Sharp Angle"),
                    ATPNode(view=8905, noun='0', pDescriber="Angle"),
                    ATPNode(view=8906, noun='0', pDescriber="Medium-tall"),
                    ATPNode(view=8907, noun='0', pDescriber="Medium-short"),
                    ATPNode(view=8908, noun='0', pDescriber="Narrow-tall"),
                    ATPNode(view=8909, noun='0', pDescriber="Narrow-short")]

for i, obj in enumerate(mySet):
    obj.pCategory = "Polygons"
    obj.pDoScaler = False

if obj.pPlacement == 0:
    obj.pPlacement = 'SPECIAL'

    if not obj.pDescriber:
        obj.pDescriber = "All"

Transitions = mySet = [ATPNode(view=1020, noun='GROUND_N', pDescriber="Ground-1"),
                       ATPNode(view=1021, noun='GROUND_N', pDescriber="Ground-2"),
                       ATPNode(view=1022, noun='GROUND_N', pDescriber="Ground-3"),
                       ATPNode(view=1023, noun='GROUND_N', pDescriber="Ground-4"),
                       ATPNode(view=1024, noun='GROUND_N', pDescriber="Ground-5"),
                       ATPNode(view=1025, noun='GROUND_N', pDescriber="Ground-6"),
                       ATPNode(view=1026, noun='GROUND_N', pDescriber="Ground-7"),
                       ATPNode(view=1027, noun='GROUND_N', pDescriber="Ground-8"),
                       ATPNode(view=1028, noun='GROUND_N', pDescriber="Ground-9")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Transitions"
    obj.pDoScaler = True
    obj.pPolygon = -1
    obj.pPlacement = 'GROUND'

if not obj.pDescriber:
    obj.pDescriber = "Transitions"

BeachStuff = mySet = [ATPNode(view=1500, noun='0', pDescriber="Flotsam"),
                      ATPNode(view=1501, noun='0', pDescriber="Jetsam")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 103
    obj.pCategory = "Beach"
    obj.pPolygon = -1

DesertBushes = mySet = [ATPNode(view=2500, noun='BUSH1_DES_N', pDescriber="Bush"),
                        ATPNode(view=2501, noun='BUSH1_DES_N', pDescriber="Bush"),
                        ATPNode(view=2502, noun='BUSH1_DES_N', pDescriber="Bush"),
                        ATPNode(view=2503, noun='BUSH2_DES_N', pDescriber="Bush"),
                        ATPNode(view=2504, noun='BUSH2_DES_N', pDescriber="Bush"),
                        ATPNode(view=2505, noun='BUSH2_DES_N', pDescriber="Bush"),
                        ATPNode(view=2506, noun='OCATILLA_N', pDescriber="Ocatilla"),
                        ATPNode(view=2507, noun='OCATILLA_N', pDescriber="Ocatilla"),
                        ATPNode(view=2508, noun='CENT_PLANT_N', pDescriber="Century Plant")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 106
    obj.pCategory = "Desert: Bushes"
    obj.pDoScaler = True

DesertGrasses = mySet = [ATPNode(view=2520, noun='GRASS_DES_N', pDescriber="Grass"),
                         ATPNode(view=2521, noun='GRASS_DES_N', pDescriber="Grass"),
                         ATPNode(view=2522, noun='GRASS_DES_N', pDescriber="Grass"),
                         ATPNode(view=2523, noun='GRASS_DES_N', pDescriber="Grass")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 106
    obj.pCategory = "Desert: Grass"
    obj.pDoScaler = True
    obj.pPolygon = -1

DesertSagebrush = mySet = [ATPNode(view=2530, noun='SAGE_SM_N', pDescriber="Sagebrush"),
                           ATPNode(view=2531, noun='SAGE_SM_N', pDescriber="Sagebrush"),
                           ATPNode(view=2532, noun='SAGE_SM_N', pDescriber="Sagebrush"),
                           ATPNode(view=2533, noun='SAGE_SM_N', pDescriber="Sagebrush"),
                           ATPNode(view=2534, noun='SAGE_SM_N', pDescriber="Sagebrush"),
                           ATPNode(view=2535, noun='SAGE_LG_N', pDescriber="Sagebrush"),
                           ATPNode(view=2536, noun='SAGE_LG_N', pDescriber="Sagebrush"),
                           ATPNode(view=2537, noun='SAGE_LG_N', pDescriber="Sagebrush"),
                           ATPNode(view=2538, noun='SAGE_LG_N', pDescriber="Sagebrush")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 106
    obj.pCategory = "Desert: Sagebrush"
    obj.pDoScaler = True

DesertPlants = mySet = [ATPNode(view=2540, noun='CACT_TALL_N', pDescriber="Plant"),
                        ATPNode(view=2541, noun='CACT_TALL_N', pDescriber="Plant"),
                        ATPNode(view=2542, noun='CACT_SML_N', pDescriber="Cactus"),
                        ATPNode(view=2543, noun='CACT_FL_N', pDescriber="Cactus Flower"),
                        ATPNode(view=2544, noun='CACT_FL_N', pDescriber="Cactus"),
                        ATPNode(view=2545, noun='CACT_SEG_N', pDescriber="Cactus")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 106
    obj.pCategory = "Desert: Plants"
    obj.pDoScaler = True

DesertTrees = mySet = [ATPNode(view=2510, noun='0', pDescriber="Palm Top"),
                       ATPNode(view=2511, noun='0', pDescriber="Palm Top"),
                       ATPNode(view=2512, noun='0', pDescriber="Palm Top"),
                       ATPNode(view=2513, noun='0', pDescriber="Palm Top"),
                       ATPNode(view=2514, noun='0', pDescriber="Palm Top"),
                       ATPNode(view=2515, noun='0', pDescriber="Palm Top"),
                       ATPNode(view=2516, noun='0', pDescriber="Palm Trunk"),
                       ATPNode(view=2517, noun='0', pDescriber="Palm Trunk"),
                       ATPNode(view=2518, noun='0', pDescriber="Palm Trunk"),
                       ATPNode(view=2519, noun='0', pDescriber="Palm Trunk")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 106
    obj.pCategory = "Desert: Trees"
    obj.pDoScaler = True

DesertDunes = mySet = [ATPNode(view=2570, noun='DUNE_N', pDescriber="Dune"),
                       ATPNode(view=2571, noun='DUNE_N', pDescriber="Dune"),
                       ATPNode(view=2572, noun='DUNE_N', pDescriber="Dune"),
                       ATPNode(view=2573, noun='DUNE_N', pDescriber="Dune"),
                       ATPNode(view=2574, noun='DUNE_N', pDescriber="Dune"),
                       ATPNode(view=2600, noun='HORIZON_DES_N', pDescriber="horizon hills"),
                       ATPNode(view=2601, noun='HORIZON_DES_N', pDescriber="horizon hills"),
                       ATPNode(view=2602, noun='HORIZON_DES_N', pDescriber="horizon hills")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 106
    obj.pCategory = "Desert: Dunes"
    obj.pDoScaler = False
    obj.pPolygon = -1

DesertDirt = mySet = [ATPNode(view=2585, noun='DIRT_CRACK_N', pDescriber="Cracked Dirt"),
                      ATPNode(view=2586, noun='DIRT_CRACK_N', pDescriber="Cracked Dirt"),
                      ATPNode(view=2587, noun='DIRT_CRACK_N', pDescriber="Cracked Dirt"),
                      ATPNode(view=2588, noun='DIRT_CRACK_N', pDescriber="Cracked Dirt"),
                      ATPNode(view=2590, noun='ALKALI_N', pDescriber="Alkai"),
                      ATPNode(view=2591, noun='ALKALI_N', pDescriber="Alkai"),
                      ATPNode(view=2592, noun='ALKALI_N', pDescriber="Alkai"),
                      ATPNode(view=2593, noun='ALKALI_N', pDescriber="Alkai"),
                      ATPNode(view=2594, noun='ALKALI_N', pDescriber="Alkai"),
                      ATPNode(view=2595, noun='DIRT_DES_N', pDescriber="Dirt"),
                      ATPNode(view=2596, noun='DIRT_DES_N', pDescriber="Dirt"),
                      ATPNode(view=2597, noun='DIRT_DES_N', pDescriber="Dirt"),
                      ATPNode(view=2598, noun='SHADE_N', pDescriber="Rock Shadow")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 106
    obj.pCategory = "Desert: Dirt"
    obj.pDoScaler = True
    obj.pPolygon = -1

DesertRiver = mySet = [ATPNode(view=2605, noun='DIRT_DES_N', pDescriber="NS river distant"),
                       ATPNode(view=2606, noun='0', pDescriber="NS river middle"),
                       ATPNode(view=2607, noun='0', pDescriber="river tee"),
                       ATPNode(view=2608, noun='0', pDescriber="EW bridge"),
                       ATPNode(view=2609, noun='0', pDescriber="NS bridge"),
                       ATPNode(view=2610, noun='0', pDescriber="EW river"),
                       ATPNode(view=2611, noun='0', pDescriber="EW river"),
                       ATPNode(view=2612, noun='0', pDescriber="EW river"),
                       ATPNode(view=2613, noun='0', pDescriber="short EW river"),
                       ATPNode(view=2614, noun='0', pDescriber="NW river curve"),
                       ATPNode(view=2615, noun='0', pDescriber="NW river curve (rock and bush)"),
                       ATPNode(view=2616, noun='0', pDescriber="SE river curve"),
                       ATPNode(view=2617, noun='0', pDescriber="NS river distant"),
                       ATPNode(view=2618, noun='0', pDescriber="NS river island"),
                       ATPNode(view=2619, noun='0', pDescriber="SE river curve"),
                       ATPNode(view=2620, noun='0', pDescriber="NS river wide"),
                       ATPNode(view=2621, noun='0', pDescriber="NNW river short")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 106
    obj.pCategory = "Desert: River"
    obj.pDoScaler = True
    obj.pPolygon = -1

DungeonWalls = mySet = [ATPNode(view=2750, noun='WALL_DUN_N', pDescriber="Wall-1"),
                        ATPNode(view=2751, noun='WALL_DUN_N', pDescriber="Wall-2"),
                        ATPNode(view=2752, noun='WALL_DUN_N', pDescriber="Wall-3"),
                        ATPNode(view=2753, noun='WALL_DUN_N', pDescriber="Wall-4"),
                        ATPNode(view=2754, noun='WALL_DUN_N', pDescriber="Wall-5"),
                        ATPNode(view=2755, noun='WALL_DUN_N', pDescriber="Wall-6"),
                        ATPNode(view=2756, noun='WALL_DUN_N', pDescriber="Wall-7"),
                        ATPNode(view=2757, noun='WALL_DUN_N', pDescriber="Wall-8"),
                        ATPNode(view=2758, noun='WALL_DUN_N', pDescriber="Wall-9"),
                        ATPNode(view=2759, noun='WALL_DUN_N', pDescriber="Wall-10")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Walls"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

DungeonStalc = mySet = [ATPNode(view=2770, noun='STALACTITE_N', pDescriber="Stalactite_1"),
                        ATPNode(view=2771, noun='STALACTITE_N', pDescriber="Stalactite_2"),
                        ATPNode(view=2772, noun='STALACTITE_N', pDescriber="Stalactite_3"),
                        ATPNode(view=2773, noun='STALACTITE_N', pDescriber="Stalactite_4"),
                        ATPNode(view=2774, noun='STALACTITE_N', pDescriber="Stalactite_5")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Stalactites"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

DungeonStalg = mySet = [ATPNode(view=2780, noun='STALAGMITE_N', pDescriber="Stalagmite_1"),
                        ATPNode(view=2781, noun='STALAGMITE_N', pDescriber="Stalagmite_2"),
                        ATPNode(view=2782, noun='STALAGMITE_N', pDescriber="Stalagmite_3"),
                        ATPNode(view=2783, noun='STALAGMITE_N', pDescriber="Stalagmite_4"),
                        ATPNode(view=2784, noun='STALAGMITE_N', pDescriber="Stalagmite_5"),
                        ATPNode(view=2800, noun='STALAGMITE_N', pDescriber="Crystal_0"),
                        ATPNode(view=2801, noun='STALAGMITE_N', pDescriber="Crystal_1"),
                        ATPNode(view=2802, noun='STALAGMITE_N', pDescriber="Crystal_2"),
                        ATPNode(view=2803, noun='STALAGMITE_N', pDescriber="Crystal_3"),
                        ATPNode(view=2804, noun='STALAGMITE_N', pDescriber="Crystal_4"),
                        ATPNode(view=2805, noun='STALAGMITE_N', pDescriber="Crystal_5"),
                        ATPNode(view=2806, noun='STALAGMITE_N', pDescriber="Crystal_6")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Stalagmites"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

DungeonWebs = mySet = [ATPNode(view=2790, noun='WEB1_DUN_N', pDescriber="Web_1"),
                       ATPNode(view=2791, noun='WEB2_DUN_N', pDescriber="Web_2"),
                       ATPNode(view=2792, noun='WEB1_DUN_N', pDescriber="Web_3"),
                       ATPNode(view=2793, noun='WEB1_DUN_N', pDescriber="Web_4"),
                       ATPNode(view=2794, noun='WEB1_DUN_N', pDescriber="Web_5"),
                       ATPNode(view=2795, noun='WEB1_DUN_N', pDescriber="Web_6"),
                       ATPNode(view=2796, noun='WEB2_DUN_N', pDescriber="Web_7"),
                       ATPNode(view=2797, noun='WEB2_DUN_N', pDescriber="Web_8"),
                       ATPNode(view=2798, noun='WEB2_DUN_N', pDescriber="Web_9"),
                       ATPNode(view=2799, noun='WEB2_DUN_N', pDescriber="Web_10")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Webs"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

DungeonMush = mySet = [ATPNode(view=2810, noun='MUSHRM_DUN_N', pDescriber="Mushroom_1"),
                       ATPNode(view=2811, noun='MUSHRM_DUN_N', pDescriber="Mushroom_2"),
                       ATPNode(view=2812, noun='MUSHRMS_DUN_N', pDescriber="Mushroom_3"),
                       ATPNode(view=2813, noun='MUSHRM_DUN_N', pDescriber="Mushroom_4"),
                       ATPNode(view=2814, noun='MUSHRM_DUN_N', pDescriber="Mushroom_5"),
                       ATPNode(view=2815, noun='MUSHRM_DUN_N', pDescriber="Mushroom_6"),
                       ATPNode(view=2816, noun='MUSHRM_DUN_N', pDescriber="Mushroom_7")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Mushrooms"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

DungeonMoss = mySet = [ATPNode(view=2820, noun='MOSS1_DUN_N', pDescriber="Moss_1"),
                       ATPNode(view=2821, noun='MOSS2_DUN_N', pDescriber="Moss_2"),
                       ATPNode(view=2822, noun='MOSS1_DUN_N', pDescriber="Moss_3"),
                       ATPNode(view=2823, noun='MOSS1_DUN_N', pDescriber="Moss_4"),
                       ATPNode(view=2824, noun='MOSS2_DUN_N', pDescriber="Moss_5"),
                       ATPNode(view=2825, noun='MOSS2_DUN_N', pDescriber="Moss_6")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Moss"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

DungeonMisc = mySet = [ATPNode(view=2900, noun='BONES_N', pDescriber="Bones"),
                       ATPNode(view=2901, noun='SKULL_DUN_N', pDescriber="Skull"),
                       ATPNode(view=2980, noun='SKULL_DUN_N', pDescriber="Skull"),
                       ATPNode(view=2981, noun='SKULL_DUN_N', pDescriber="Skull"),
                       ATPNode(view=2982, noun='SKULL_DUN_N', pDescriber="Skull"),
                       ATPNode(view=2983, noun='SKULL_DUN_N', pDescriber="Skull"),
                       ATPNode(view=2992, noun='SKULL_DUN_N', pDescriber="Skull"),
                       ATPNode(view=2993, noun='SKULL_DUN_N', pDescriber="Skull"),
                       ATPNode(view=2994, noun='SKULL_DUN_N', pDescriber="Skull"),
                       ATPNode(view=2999, noun='SKULL_DUN_N', pDescriber="Skull")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Misc"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

DungeonPassages = mySet = [ATPNode(view=2830, noun='COLUMN_DUN_N', pDescriber="Arch_Left"),
                           ATPNode(view=2831, noun='COLUMN_DUN_N', pDescriber="Arch_Right"),
                           ATPNode(view=2832, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2833, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2835, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2836, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2837, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2838, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2840, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2841, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2842, noun='ARCH_DUN_N', pDescriber="Archway_Back"),
                           ATPNode(view=2850, noun='COLUMN_DUN_N', pDescriber="Cave_Side_1"),
                           ATPNode(view=2851, noun='COLUMN_DUN_N', pDescriber="Cave_Side_2"),
                           ATPNode(view=2852, noun='ARCH_DUN_N', pDescriber="Cave_Side_3"),
                           ATPNode(view=2853, noun='ARCH_DUN_N', pDescriber="Archway_Side")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Passages"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Passage"

DungeonRocks = mySet = [ATPNode(view=2870, noun='FLOOR_DUN_N', pDescriber="Floor_Left"),
                        ATPNode(view=2871, noun='FLOOR_DUN_N', pDescriber="Floor_Right"),
                        ATPNode(view=2872, noun='ROCK_EDGE_DUN_N', pDescriber="Front_Edge_1"),
                        ATPNode(view=2873, noun='ROCK_EDGE_DUN_N', pDescriber="Front_Edge_2"),
                        ATPNode(view=2874, noun='ROCK_EDGE_DUN_N', pDescriber="Front_Edge_2"),
                        ATPNode(view=2875, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_6"),
                        ATPNode(view=2876, noun='ROCK_DUN_N', pDescriber="Rock_7"),
                        ATPNode(view=2877, noun='ROCK_DUN_N', pDescriber="Rock_8"),
                        ATPNode(view=2878, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_9"),
                        ATPNode(view=2879, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2880, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2881, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2882, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2883, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2884, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2892, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2893, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2894, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2899, noun='ROCK_EDGE_DUN_N', pDescriber="Rock_10"),
                        ATPNode(view=2891, noun='FLOOR_DUN_N', pDescriber="Floor")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 203
    obj.pCategory = "Dungeon: Rocks"
    obj.pPolygon = -1

    if not obj.pDescriber:
        obj.pDescriber = "Rock"

Town1Walls = mySet = [ATPNode(view=3501, noun='WALL_T1_N', pDescriber="Lt-Wall"),
                      ATPNode(view=3502, noun='WALL_T1_N', pDescriber="Lt-Wall-middle"),
                      ATPNode(view=3503, noun='WALL_T1_N', pDescriber="Lt-Wall-Gable"),
                      ATPNode(view=3504, noun='WALL_T1_N', pDescriber="Lt-Wall-Roof"),
                      ATPNode(view=3505, noun='WALL_T1_N', pDescriber="Lt-Wall-dbl"),
                      ATPNode(view=3506, noun='WALL_T1_N', pDescriber="Lt-Wall-Mid-dbl"),
                      ATPNode(view=3507, noun='WALL_T1_N', pDescriber="Lt-Wall-Gable-dbl"),
                      ATPNode(view=3508, noun='WALL_T1_N', pDescriber="Lt-Wall-Roof-dbl"),
                      ATPNode(view=3509, noun='WALL_T1_N', pDescriber="Lt-Wall-low"),
                      ATPNode(view=3510, noun='WALL_T1_N', pDescriber="Lt-Wall-Mid-low"),
                      ATPNode(view=3511, noun='WALL_T1_N', pDescriber="Lt-Wall-Gable-low"),
                      ATPNode(view=3512, noun='WALL_T1_N', pDescriber="Lt-Wall-Side-low"),
                      ATPNode(view=3513, noun='WALL_T1_N', pDescriber="Dk-Wall"),
                      ATPNode(view=3514, noun='WALL_T1_N', pDescriber="Dk-Wall-Mid"),
                      ATPNode(view=3515, noun='WALL_T1_N', pDescriber="Dk-Wall-Gable"),
                      ATPNode(view=3516, noun='WALL_T1_N', pDescriber="Dk-Wall-Roof"),
                      ATPNode(view=3517, noun='WALL_T1_N', pDescriber="Dk-Wall-dbl"),
                      ATPNode(view=3518, noun='WALL_T1_N', pDescriber="Dk-Wall-Mid-dbl"),
                      ATPNode(view=3519, noun='WALL_T1_N', pDescriber="Dk-Wall-Gable-dbl"),
                      ATPNode(view=3520, noun='WALL_T1_N', pDescriber="Dk-Wall-Roof-dbl"),
                      ATPNode(view=3521, noun='WALL_T1_N', pDescriber="Dk-Wall-low"),
                      ATPNode(view=3522, noun='WALL_T1_N', pDescriber="Dk-Wall-Mid-low"),
                      ATPNode(view=3523, noun='WALL_T1_N', pDescriber="Dk-Wall-Gable-low"),
                      ATPNode(view=3524, noun='WALL_T1_N', pDescriber="Dk-Wall-Side-low"),
                      ATPNode(view=3525, noun='WALL_T1_N', pDescriber="Med-Wall"),
                      ATPNode(view=3526, noun='WALL_T1_N', pDescriber="Med-Wall-Mid"),
                      ATPNode(view=3527, noun='WALL_T1_N', pDescriber="Med-Wall-Gable"),
                      ATPNode(view=3528, noun='WALL_T1_N', pDescriber="Med-Wall-dbl"),
                      ATPNode(view=3529, noun='WALL_T1_N', pDescriber="Med-Wall-Mid-dbl"),
                      ATPNode(view=3530, noun='WALL_T1_N', pDescriber="Med-Wall-Gable-dbl"),
                      ATPNode(view=3531, noun='WALL_T1_N', pDescriber="Med-Wall-low"),
                      ATPNode(view=3532, noun='WALL_T1_N', pDescriber="Med-Wall-Mid-low"),
                      ATPNode(view=3533, noun='WALL_T1_N', pDescriber="Med-Wall-Gable-low")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Walls"

    if not obj.pDescriber:
        obj.pDescriber = "Wall"

RuinWalls = mySet = [ATPNode(view=3827, noun='RUIN_WALL_N', pDescriber="wall dk corner"),
                     ATPNode(view=3828, noun='RUIN_BRICKS_N', pDescriber="bricks"),
                     ATPNode(view=3829, noun='RUIN_BRICKS_N', pDescriber="bricks"),
                     ATPNode(view=3830, noun='RUIN_CRACK_N', pDescriber="wall crack"),
                     ATPNode(view=3831, noun='RUIN_CRACK_N', pDescriber="wall crack"),
                     ATPNode(view=3832, noun='RUIN_CRACK_N', pDescriber="wall crack"),
                     ATPNode(view=3833, noun='RUIN_CRACK_N', pDescriber="wall crack"),
                     ATPNode(view=3834, noun='RUIN_CRACK_N', pDescriber="wall crack"),
                     ATPNode(view=3835, noun='RUIN_BRICKS_N', pDescriber="brick pile"),
                     ATPNode(view=3836, noun='RUIN_BRICKS_N', pDescriber="brick pile"),
                     ATPNode(view=3837, noun='RUIN_BRICKS_N', pDescriber="bricks"),
                     ATPNode(view=3838, noun='RUIN_BRICKS_N', pDescriber="bricks"),
                     ATPNode(view=3839, noun='RUIN_BRICKS_N', pDescriber="bricks"),
                     ATPNode(view=3840, noun='RUIN_RUBBLE_N', pDescriber="lt rubble"),
                     ATPNode(view=3841, noun='RUIN_RUBBLE_N', pDescriber="lt rubble"),
                     ATPNode(view=3842, noun='RUIN_WALL_N', pDescriber="lt bottom"),
                     ATPNode(view=3843, noun='RUIN_WALL_N', pDescriber="lt bottom middle"),
                     ATPNode(view=3844, noun='RUIN_WALL_N', pDescriber="lt left top"),
                     ATPNode(view=3845, noun='RUIN_WALL_N', pDescriber="lt center top"),
                     ATPNode(view=3846, noun='RUIN_WALL_N', pDescriber="lt right top"),
                     ATPNode(view=3847, noun='RUIN_WALL_N', pDescriber="lt hole"),
                     ATPNode(view=3848, noun='RUIN_WALL_N', pDescriber="lt hole"),
                     ATPNode(view=3849, noun='RUIN_WALL_N', pDescriber="back corner 1"),
                     ATPNode(view=3850, noun='RUIN_RUBBLE_N', pDescriber="dk rubble"),
                     ATPNode(view=3851, noun='RUIN_RUBBLE_N', pDescriber="dk rubble"),
                     ATPNode(view=3852, noun='RUIN_WALL_N', pDescriber="dk bottom"),
                     ATPNode(view=3853, noun='RUIN_WALL_N', pDescriber="dk bottom middle"),
                     ATPNode(view=3854, noun='RUIN_WALL_N', pDescriber="dk left top"),
                     ATPNode(view=3855, noun='RUIN_WALL_N', pDescriber="dk center top"),
                     ATPNode(view=3856, noun='RUIN_WALL_N', pDescriber="dk right top"),
                     ATPNode(view=3857, noun='RUIN_WALL_N', pDescriber="dk hole"),
                     ATPNode(view=3858, noun='RUIN_WALL_N', pDescriber="dk hole"),
                     ATPNode(view=3859, noun='RUIN_WALL_N', pDescriber="back corner 2"),
                     ATPNode(view=3860, noun='RUIN_RUBBLE_N', pDescriber="md rubble"),
                     ATPNode(view=3861, noun='RUIN_RUBBLE_N', pDescriber="md rubble"),
                     ATPNode(view=3862, noun='RUIN_WALL_N', pDescriber="md bottom"),
                     ATPNode(view=3863, noun='RUIN_WALL_N', pDescriber="md bottom middle"),
                     ATPNode(view=3864, noun='RUIN_WALL_N', pDescriber="md left top"),
                     ATPNode(view=3865, noun='RUIN_WALL_N', pDescriber="md center top"),
                     ATPNode(view=3866, noun='RUIN_WALL_N', pDescriber="md right top"),
                     ATPNode(view=3867, noun='RUIN_WALL_N', pDescriber="md hole"),
                     ATPNode(view=3868, noun='RUIN_WALL_N', pDescriber="md hole"),
                     ATPNode(view=3869, noun='RUIN_WALL_N', pDescriber="back corner 3")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 201
    obj.pCategory = "Town Ruins: Walls"

    if not obj.pDescriber:
        obj.pDescriber = "Wall"

RuinRoof = mySet = [ATPNode(view=3870, noun='RUIN_ROOF_N', pDescriber="tile rubble"),
                    ATPNode(view=3871, noun='RUIN_ROOF_N', pDescriber="tile side long"),
                    ATPNode(view=3872, noun='RUIN_ROOF_N', pDescriber="tile side short"),
                    ATPNode(view=3873, noun='RUIN_ROOF_N', pDescriber="tile front long"),
                    ATPNode(view=3874, noun='RUIN_ROOF_N', pDescriber="tile front short"),
                    ATPNode(view=3875, noun='RUIN_ROOF_N', pDescriber="tile gable"),
                    ATPNode(view=3876, noun='RUIN_ROOF_N', pDescriber="straw rubble"),
                    ATPNode(view=3877, noun='RUIN_ROOF_N', pDescriber="straw side long"),
                    ATPNode(view=3878, noun='RUIN_ROOF_N', pDescriber="straw side short"),
                    ATPNode(view=3879, noun='RUIN_ROOF_N', pDescriber="straw front long"),
                    ATPNode(view=3880, noun='RUIN_ROOF_N', pDescriber="straw front short"),
                    ATPNode(view=3881, noun='RUIN_ROOF_N', pDescriber="straw gable"),
                    ATPNode(view=3882, noun='RUIN_ROOF_N', pDescriber="slate rubble"),
                    ATPNode(view=3883, noun='RUIN_ROOF_N', pDescriber="slate side long"),
                    ATPNode(view=3884, noun='RUIN_ROOF_N', pDescriber="slate side short"),
                    ATPNode(view=3885, noun='RUIN_ROOF_N', pDescriber="slate front long"),
                    ATPNode(view=3886, noun='RUIN_ROOF_N', pDescriber="slate front short"),
                    ATPNode(view=3887, noun='RUIN_ROOF_N', pDescriber="slate gable")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 201
    obj.pCategory = "Town Ruins: Roof"

    if not obj.pDescriber:
        obj.pDescriber = "Roof"

RuinWindows = mySet = [ATPNode(view=3890, noun='RUIN_WINDOW_N', pDescriber="arch rubble"),
                       ATPNode(view=3891, noun='RUIN_WINDOW_N', pDescriber="arch open"),
                       ATPNode(view=3892, noun='RUIN_WINDOW_N', pDescriber="arch shutter"),
                       ATPNode(view=3893, noun='RUIN_WINDOW_N', pDescriber="arch stone frame"),
                       ATPNode(view=3894, noun='RUIN_WINDOW_N', pDescriber="arch wood frame"),
                       ATPNode(view=3895, noun='RUIN_WINDOW_N', pDescriber="arch mullions"),
                       ATPNode(view=3896, noun='RUIN_WINDOW_N', pDescriber="arch diamond mullions"),
                       ATPNode(view=3897, noun='RUIN_WINDOW_N', pDescriber="square rubble"),
                       ATPNode(view=3898, noun='RUIN_WINDOW_N', pDescriber="square open"),
                       ATPNode(view=3899, noun='RUIN_WINDOW_N', pDescriber="square wood frame"),
                       ATPNode(view=3900, noun='RUIN_WINDOW_N', pDescriber="square mullions"),
                       ATPNode(view=3901, noun='RUIN_WINDOW_N', pDescriber="tile diamond mullions"),
                       ATPNode(view=3902, noun='RUIN_WINDOW_N', pDescriber="rw lt wood rect"),
                       ATPNode(view=3903, noun='RUIN_WINDOW_N', pDescriber="rw med wood rect"),
                       ATPNode(view=3904, noun='RUIN_WINDOW_N', pDescriber="rw dk mullion"),
                       ATPNode(view=3905, noun='RUIN_WINDOW_N', pDescriber="rw lt mullion"),
                       ATPNode(view=3906, noun='RUIN_WINDOW_N', pDescriber="rw med mullion"),
                       ATPNode(view=3907, noun='RUIN_WINDOW_N', pDescriber="rw dk diamond"),
                       ATPNode(view=3908, noun='RUIN_WINDOW_N', pDescriber="rw lt diamond"),
                       ATPNode(view=3909, noun='RUIN_WINDOW_N', pDescriber="rw med diamond")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 201
    obj.pCategory = "Town Ruins: Windows"

    if not obj.pDescriber:
        obj.pDescriber = "Window"

RuinTrim = mySet = [ATPNode(view=3910, noun='RUIN_EAVES_N', pDescriber="eaves rubble"),
                    ATPNode(view=3911, noun='RUIN_EAVES_N', pDescriber="dk eaves long"),
                    ATPNode(view=3912, noun='RUIN_EAVES_N', pDescriber="dk eaves short"),
                    ATPNode(view=3913, noun='RUIN_EAVES_N', pDescriber="lt eaves long"),
                    ATPNode(view=3914, noun='RUIN_EAVES_N', pDescriber="lt eaves short"),
                    ATPNode(view=3915, noun='RUIN_EAVES_N', pDescriber="dk eaves"),
                    ATPNode(view=3916, noun='RUIN_EAVES_N', pDescriber="dk eaves"),
                    ATPNode(view=3917, noun='RUIN_EAVES_N', pDescriber="lt eaves"),
                    ATPNode(view=3918, noun='RUIN_EAVES_N', pDescriber="lt eaves"),
                    ATPNode(view=3919, noun='RUIN_EAVES_N', pDescriber="md eaves", pDoScaler=True),
                    ATPNode(view=3920, noun='RUIN_BEAM_N', pDescriber="beam rubble"),
                    ATPNode(view=3921, noun='RUIN_BEAM_N', pDescriber="dk beam", pDoScaler=True),
                    ATPNode(view=3922, noun='RUIN_BEAM_N', pDescriber="dk beam"),
                    ATPNode(view=3923, noun='RUIN_BEAM_N', pDescriber="dk beam"),
                    ATPNode(view=3924, noun='RUIN_BEAM_N', pDescriber="lt beam"),
                    ATPNode(view=3925, noun='RUIN_BEAM_N', pDescriber="lt beam"),
                    ATPNode(view=3926, noun='RUIN_BEAM_N', pDescriber="lt beam"),
                    ATPNode(view=3927, noun='RUIN_BEAM_N', pDescriber="md beam"),
                    ATPNode(view=3928, noun='RUIN_BEAM_N', pDescriber="md beam"),
                    ATPNode(view=3929, noun='RUIN_BEAM_N', pDescriber="md beam"),
                    ATPNode(view=3930, noun='RUIN_TWN_WL_N', pDescriber="wall rubble"),
                    ATPNode(view=3931, noun='RUIN_TWN_WL_N', pDescriber="wall back"),
                    ATPNode(view=3932, noun='RUIN_TWN_WL_N', pDescriber="dk wall side"),
                    ATPNode(view=3933, noun='RUIN_TWN_WL_N', pDescriber="lt wall side")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 201
    obj.pCategory = "Town Ruins: Trim"

    if not obj.pDescriber:
        obj.pDescriber = "Trim"

TownRuins = mySet = [ATPNode(view=3934, noun='RUIN_SCORCH_N', pDescriber="scortch 1", pPolygon=-1),
                     ATPNode(view=3935, noun='RUIN_SCORCH_N', pDescriber="scortch 2", pPolygon=-1),
                     ATPNode(view=3936, noun='RUIN_SCORCH_N', pDescriber="scortch 3", pPolygon=-1),
                     ATPNode(view=3950, noun='RUIN_SCORCH_N', pDescriber="scortch center", pPolygon=-1),
                     ATPNode(view=3937, noun='RUIN_TREE_N', pDescriber="burnt tree 6"),
                     ATPNode(view=3938, noun='RUIN_TREE_N', pDescriber="burnt tree 7"),
                     ATPNode(view=3939, noun='RUIN_TREE_N', pDescriber="burnt tree 8"),
                     ATPNode(view=3940, noun='RUIN_TREE_N', pDescriber="burnt tree 1"),
                     ATPNode(view=3941, noun='RUIN_TREE2_N', pDescriber="burnt tree 2"),
                     ATPNode(view=3942, noun='RUIN_TREE2_N', pDescriber="burnt tree 3"),
                     ATPNode(view=3943, noun='RUIN_TREE2_N', pDescriber="burnt tree 4"),
                     ATPNode(view=3944, noun='RUIN_TREE2_N', pDescriber="burnt tree 5"),
                     ATPNode(view=3945, noun='RUIN_BUSH_N', pDescriber="burnt bush 1"),
                     ATPNode(view=3946, noun='RUIN_BUSH_N', pDescriber="burnt bush 2"),
                     ATPNode(view=3947, noun='RUIN_BUSH2_N', pDescriber="burnt bush 3"),
                     ATPNode(view=3948, noun='0', pDescriber="ruin table", pDoScaler=True),
                     ATPNode(view=3949, noun='0', pDescriber="ruin chair", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 201
    obj.pCategory = "Town Ruins: Plants"

    if not obj.pDescriber:
        obj.pDescriber = "Ruins"

Town1Corners = mySet = [ATPNode(view=3751, noun='WALL_T1_N', pDescriber="lt stone 1"),
                        ATPNode(view=3752, noun='WALL_T1_N', pDescriber="lt stone 2"),
                        ATPNode(view=3753, noun='WALL_T1_N', pDescriber="lt stone 3"),
                        ATPNode(view=3754, noun='WALL_T1_N', pDescriber="lt stone 4"),
                        ATPNode(view=3755, noun='WALL_T1_N', pDescriber="dk stone 1"),
                        ATPNode(view=3756, noun='WALL_T1_N', pDescriber="dk stone 2"),
                        ATPNode(view=3757, noun='WALL_T1_N', pDescriber="dk stone 3"),
                        ATPNode(view=3758, noun='WALL_T1_N', pDescriber="dk stone 4"),
                        ATPNode(view=3759, noun='WALL_T1_N', pDescriber="md stone 1"),
                        ATPNode(view=3760, noun='WALL_T1_N', pDescriber="md stone 2"),
                        ATPNode(view=3761, noun='WALL_T1_N', pDescriber="md stone 3"),
                        ATPNode(view=3762, noun='WALL_T1_N', pDescriber="md stone 4"),
                        ATPNode(view=3763, noun='WALL_T1_N', pDescriber="md stone arch")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Corners"

    if not obj.pDescriber:
        obj.pDescriber = "Wall"

Town1Roofs = mySet = [ATPNode(view=3601, noun='ROOFTILE_T1_N', pDescriber="tile-long"),
                      ATPNode(view=3602, noun='ROOFTILE_T1_N', pDescriber="tile-short"),
                      ATPNode(view=3603, noun='ROOFTILE_T1_N', pDescriber="tile-gable"),
                      ATPNode(view=3604, noun='ROOFTILE_T1_N', pDescriber="tile-front-long"),
                      ATPNode(view=3605, noun='ROOFTILE_T1_N', pDescriber="tile-front-short"),
                      ATPNode(view=3606, noun='ROOFTILE_T1_N', pDescriber="tile-front-gable"),
                      ATPNode(view=3607, noun='ROOFSTRAW_T1_N', pDescriber="straw-long"),
                      ATPNode(view=3608, noun='ROOFSTRAW_T1_N', pDescriber="straw-short"),
                      ATPNode(view=3609, noun='ROOFSTRAW_T1_N', pDescriber="straw-gable"),
                      ATPNode(view=3610, noun='ROOFSTRAW_T1_N', pDescriber="straw-front-long"),
                      ATPNode(view=3611, noun='ROOFSTRAW_T1_N', pDescriber="straw-front-short"),
                      ATPNode(view=3612, noun='ROOFSTRAW_T1_N', pDescriber="straw-front-gable"),
                      ATPNode(view=3613, noun='ROOFSLATE_T1_N', pDescriber="slate-long"),
                      ATPNode(view=3614, noun='ROOFSLATE_T1_N', pDescriber="slate-short"),
                      ATPNode(view=3615, noun='ROOFSLATE_T1_N', pDescriber="slate-gable"),
                      ATPNode(view=3616, noun='ROOFSLATE_T1_N', pDescriber="slate-front-long"),
                      ATPNode(view=3617, noun='ROOFSLATE_T1_N', pDescriber="slate-front-short"),
                      ATPNode(view=3618, noun='ROOFSLATE_T1_N', pDescriber="slate-front-gable")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Roofs"
    obj.pPolygon = -1

if not obj.pDescriber:
    obj.pDescriber = "Roof"

Town1Windows = mySet = [ATPNode(view=3541, noun='WINARCH_T1_N', pDescriber="Dk-arch-open"),
                        ATPNode(view=3542, noun='WINARCH_T1_N', pDescriber="Lt-arch-open"),
                        ATPNode(view=3543, noun='WINARCH_T1_N', pDescriber="Med-arch-open"),
                        ATPNode(view=3544, noun='WINSHUTR_T1_N', pDescriber="Dk shutter"),
                        ATPNode(view=3545, noun='WINSHUTR_T1_N', pDescriber="Lt shutter"),
                        ATPNode(view=3546, noun='WINSHUTR_T1_N', pDescriber="Med shutter"),
                        ATPNode(view=3547, noun='WINSTNFR_T1_N', pDescriber="Stone frame-a"),
                        ATPNode(view=3548, noun='WINSTNFR_T1_N', pDescriber="Stone frame-b"),
                        ATPNode(view=3549, noun='WINSTNFR_T1_N', pDescriber="Stone frame-c"),
                        ATPNode(view=3553, noun='WINMULL_T1_N', pDescriber="Mullion arch-a"),
                        ATPNode(view=3554, noun='WINMULL_T1_N', pDescriber="Mullion arch-b"),
                        ATPNode(view=3555, noun='WINMULL_T1_N', pDescriber="Mullion arch-c"),
                        ATPNode(view=3556, noun='WINDIAMAR_T1_N', pDescriber="Diamond arch-a"),
                        ATPNode(view=3557, noun='WINDIAMAR_T1_N', pDescriber="Diamond arch-b"),
                        ATPNode(view=3558, noun='WINDIAMAR_T1_N', pDescriber="Diamond arch-c"),
                        ATPNode(view=3580, noun='WINRECT_T1_N', pDescriber="Dk-rect-open"),
                        ATPNode(view=3581, noun='WINRECT_T1_N', pDescriber="Lt-rect-open"),
                        ATPNode(view=3582, noun='WINRECT_T1_N', pDescriber="Med-rect-open"),
                        ATPNode(view=3585, noun='WINSTNFR_T1_N', pDescriber="Stone frame"),
                        ATPNode(view=3586, noun='WINWOODFR_T1_N', pDescriber="Wood frame-a"),
                        ATPNode(view=3587, noun='WINWOODFR_T1_N', pDescriber="Wood frame-b"),
                        ATPNode(view=3588, noun='WINWOODFR_T1_N', pDescriber="Wood frame-c"),
                        ATPNode(view=3592, noun='WINMULL_T1_N', pDescriber="Mullion-a"),
                        ATPNode(view=3593, noun='WINMULL_T1_N', pDescriber="Mullion-b"),
                        ATPNode(view=3594, noun='WINMULL_T1_N', pDescriber="Mullion-c"),
                        ATPNode(view=3595, noun='WINDIAM_T1_N', pDescriber="Diamond-a"),
                        ATPNode(view=3596, noun='WINDIAM_T1_N', pDescriber="Diamond-b"),
                        ATPNode(view=3597, noun='WINDIAM_T1_N', pDescriber="Diamond-c"),
                        ATPNode(view=3720, noun='0', pDescriber="lt stone gatekeep"),
                        ATPNode(view=3721, noun='0', pDescriber="lt wood gatekeep"),
                        ATPNode(view=3722, noun='0', pDescriber="med stone arch gatekeep"),
                        ATPNode(view=3723, noun='0', pDescriber="med stone square gatekeep"),
                        ATPNode(view=3724, noun='0', pDescriber="med wood gatekeep")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.set_room_type('TOWN1')
    obj.pCategory = "Town Ext: Windows"
    obj.pPolygon = -1

if not obj.pDescriber:
    obj.pDescriber = "Window"

Town1Signs1 = mySet = [ATPNode(view=3691, noun='SIGNCLOTH_T1_N', pDescriber="clothes sign"),
                       ATPNode(view=3694, noun='SIGNPOTION_T1_N', pDescriber="potion"),
                       ATPNode(view=3695, noun='SIGNARMSWD_T1_N', pDescriber="armor-sword-shield"),
                       ATPNode(view=3696, noun='SIGNARMOR_T1_N', pDescriber="armor"),
                       ATPNode(view=3697, noun='SIGNFOOD_T1_N', pDescriber="food"),
                       ATPNode(view=3698, noun='SIGNPOTNS_T1_N', pDescriber="potions"),
                       ATPNode(view=3699, noun='SIGNTAV1_T1_N', pDescriber="beer-mug"),
                       ATPNode(view=3700, noun='SIGNTAV2_T1_N', pDescriber="tavern"),
                       ATPNode(view=3701, noun='SIGNACAD1_T1_N', pDescriber="academy-a"),
                       ATPNode(view=3703, noun='SIGNTEMPL1_T1_N', pDescriber="temple"),
                       ATPNode(view=3704, noun='SIGNTEMPL2_T1_N', pDescriber="temple-swirl"),
                       ATPNode(view=3708, noun='SIGNWOOD_T1_N', pDescriber="sign-fm-dk-wood"),
                       ATPNode(view=3709, noun='SIGNWOOD_T1_N', pDescriber="sign-fm-lt-wood"),
                       ATPNode(view=3710, noun='SIGNMETAL_T1_N', pDescriber="sign-fm-metal"),
                       ATPNode(view=3710, noun='SIGNMETAL_T1_N', pDescriber="sign-fm-metal")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Signs 1"
    obj.pPolygon = -1

if not obj.pDescriber:
    obj.pDescriber = "Sign"

Town1Signs2 = mySet = [ATPNode(view=3702, noun='SIGN_CHAPEL_N', pDescriber="chapel"),
                       ATPNode(view=3770, noun='SIGN_N', pDescriber="dk shield 1"),
                       ATPNode(view=3771, noun='SIGN_N', pDescriber="dk shield 1"),
                       ATPNode(view=3791, noun='SIGN_N', pDescriber="dk shield 1"),
                       ATPNode(view=3792, noun='SIGN_N', pDescriber="lt shield 1"),
                       ATPNode(view=3793, noun='SIGN_N', pDescriber="dk shield 2"),
                       ATPNode(view=3794, noun='SIGN_N', pDescriber="lt shield 2"),
                       ATPNode(view=3795, noun='SIGN_LION_N', pDescriber="lion"),
                       ATPNode(view=3796, noun='SIGN_DRAGON_N', pDescriber="dragon"),
                       ATPNode(view=3797, noun='SIGN_SWAN_N', pDescriber="swan"),
                       ATPNode(view=3798, noun='SIGN_MERMAID_N', pDescriber="mermaid"),
                       ATPNode(view=3799, noun='SIGN_CLOTHES_N', pDescriber="boots&belt"),
                       ATPNode(view=3800, noun='SIGN_TEMPLE_N', pDescriber="heal hand"),
                       ATPNode(view=3801, noun='SIGN_ARMOR_N', pDescriber="mace&axe"),
                       ATPNode(view=3802, noun='SIGN_BOOK_N', pDescriber="book"),
                       ATPNode(view=3803, noun='SIGN_ARMOR_N', pDescriber="helmet"),
                       ATPNode(view=3804, noun='SIGN_TAVERN_N', pDescriber="pig"),
                       ATPNode(view=3805, noun='SIGN_TAVERN_N', pDescriber="cornacopia"),
                       ATPNode(view=3806, noun='SIGN_LADY_N', pDescriber="lady"),
                       ATPNode(view=3807, noun='SIGN_N', pDescriber="tri banner"),
                       ATPNode(view=3808, noun='SIGN_N', pDescriber="squ banner"),
                       ATPNode(view=3809, noun='SIGN_TEMPLE_N', pDescriber="healer")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 201
    obj.pCategory = "Town Ext: Signs 2"
    obj.pPolygon = -1

if not obj.pDescriber:
    obj.pDescriber = "Sign"

Town1Shops = mySet = [ATPNode(view=1085, noun='CART_N', pDescriber="Cart", pDoScaler=True),
                      # elpha - added pDoScaler=True
                      ATPNode(view=1086, noun='CART_STUFF_N', pDescriber="Food on Cart"),
                      ATPNode(view=3101, noun='COUNTER_T1_N', pDescriber="Counter-long-Dk"),
                      ATPNode(view=3102, noun='COUNTER_T1_N', pDescriber="Counter-long-Lt"),
                      ATPNode(view=3103, noun='COUNTER_T1_N', pDescriber="Counter-long-Med"),
                      ATPNode(view=3104, noun='COUNTER_T1_N', pDescriber="Counter-short-Dk"),
                      ATPNode(view=3105, noun='COUNTER_T1_N', pDescriber="Counter-short-Lt"),
                      ATPNode(view=3106, noun='COUNTER_T1_N', pDescriber="Counter-short-Med"),
                      ATPNode(view=3158, noun='MUSIC_CART_N', pDescriber="Music Cart", pDoScaler=True),
                      ATPNode(view=3159, noun='FLOWER_CART_N', pDescriber="Flower Cart", pDoScaler=True),
                      ATPNode(view=3160, noun='SHELF_N', pDescriber="Store Shelf"),
                      ATPNode(view=3241, noun='BARREL_T1_N', pDescriber="Barrel"),
                      ATPNode(view=3244, noun='SACK_N', pDescriber="Flour Bag")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Shops"

    if not obj.pDescriber:
        obj.pDescriber = "Shop Display"

Town1Misc = mySet = [ATPNode(view=3534, noun='WALL_T1_N', pDescriber="Dk-Wall-side"),
                     ATPNode(view=3535, noun='WALL_T1_N', pDescriber="Lt-Wall-side"),
                     ATPNode(view=3598, noun='TABLESQR_T1_N', pDescriber="Square table"),
                     ATPNode(view=3599, noun='TABLERND_T1_N', pDescriber="Round table"),
                     ATPNode(view=3600, noun='TABLERCT_T1_N', pDescriber="Rect table"),
                     ATPNode(view=3728, noun='GARGOYLE_T1_N', pDescriber="gargoyle"),
                     ATPNode(view=3729, noun='WALLFOUNT_T1_N', pDescriber="wall fountain"),
                     ATPNode(view=3730, noun='WALLFOUNT_T1_N', pDescriber="wall fountain face"),
                     ATPNode(view=3731, noun='CRACK_N', pDescriber="crack_1", pDoScaler=False, pPolygon=-1),
                     ATPNode(view=3732, noun='CRACK_N', pDescriber="crack_2", pDoScaler=False, pPolygon=-1),
                     ATPNode(view=3733, noun='CRACK_N', pDescriber="crack_3", pDoScaler=False, pPolygon=-1),
                     ATPNode(view=3734, noun='CRACK_N', pDescriber="crack_4", pDoScaler=False, pPolygon=-1),
                     ATPNode(view=3735, noun='CRACK_N', pDescriber="crack_5", pDoScaler=False, pPolygon=-1),
                     ATPNode(view=3736, noun='CRACK_N', pDescriber="crack_6", pDoScaler=False, pPolygon=-1),
                     ATPNode(view=3737, noun='LAMP_T1_N', pDescriber="Dk-Wall-lamp")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Misc"

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

Town1Bkgd1 = mySet = [ATPNode(view=1195, noun='TOWN_DIST_N', pDescriber="Town-dist-view2", pPolygon=-1),
                      ATPNode(view=1197, noun='TOWN_DIST_N', pDescriber="Roof tops", pPolygon=-1),
                      ATPNode(view=1198, noun='TOWN_DIST_N', pDescriber="Roof tops-2", pPolygon=-1),
                      ATPNode(view=3536, noun='TOWN_WALL_N', pDescriber="stone-wall-back"),
                      ATPNode(view=3537, noun='TOWN_WALL_N', pDescriber="stone-wall-back"),
                      ATPNode(view=3538, noun='TOWN_WALL_N', pDescriber="stone-wall-back"),
                      ATPNode(view=3539, noun='TOWN_GATE_N', pDescriber="stone-gate-far", pPolygon=-1)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Town Ext: Bkgd1"

    if not obj.pDescriber:
        obj.pDescriber = "Bkgd"

Town1Bkgd2 = mySet = [ATPNode(view=3745, noun='BACKFENC_T1_N', pDescriber="low wood fence"),
                      ATPNode(view=3746, noun='BACKSTNWL_T1_N', pDescriber="low stone wall-a"),
                      ATPNode(view=3747, noun='BACKSTNWL_T1_N', pDescriber="low stone wall-b"),
                      ATPNode(view=3748, noun='BACKSTNWL_T1_N', pDescriber="low stone wall-c"),
                      ATPNode(view=3749, noun='BACKSTNWL_T1_N', pDescriber="long stone wall")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Bkgd2"

    if not obj.pDescriber:
        obj.pDescriber = "Bkgd"

Town1Trees = mySet = [
    ATPNode(view=1149, noun='BACKTREE_T1_N', pDescriber="Full-Tree-L", pPlacement='BACK_FULL', pPolygon=-1),
    ATPNode(view=1150, noun='BACKTREE_T1_N', pDescriber="Full-Tree", pPlacement='BACK_FULL', pPolygon=-1),
    ATPNode(view=1151, noun='BACKTREE_T1_N', pDescriber="Full-Tree-R", pPlacement='BACK_FULL', pPolygon=-1),
    ATPNode(view=1152, noun='HOUSEPINE1_N', pDescriber="Pines-Bkgd", pPolygon=-1),
    ATPNode(view=1153, noun='HOUSEPINE1_N', pDescriber="Pines-Bkgd", pPolygon=-1),
    ATPNode(view=1154, noun='HOUSEPINE2_N', pDescriber="Pines-Bkgd", pPolygon=-1),
    ATPNode(view=1164, noun='BACKTREE_T1_N', pDescriber="Many Pines", pDoScaler=False, pPolygon=-1),
    ATPNode(view=3713, noun='BOUGH_N', pDescriber="tree bough"),
    ATPNode(view=3714, noun='BOUGH_N', pDescriber="tree bough"),
    ATPNode(view=3715, noun='TRUNK_T1_N', pDescriber="tree trunk", pPolygon=-1),
    ATPNode(view=3741, noun='WALLFOUNT_T1_N', pDescriber="wall fountain"),
    ATPNode(view=3742, noun='BACKTREE_T1_N', pDescriber="Half-Bkgd", pPolygon=-1),
    ATPNode(view=3743, noun='BACKTREE_T1_N', pDescriber="Full-Tree-M", pPlacement='BACK_FULL', pPolygon=-1),
    ATPNode(view=3953, noun='HOUSEOAK_N', pDescriber="oak tree")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Trees"

    if not obj.pDescriber:
        obj.pDescriber = "Tree"

Town1Plants = mySet = [ATPNode(view=1112, noun='GRASS1_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                       ATPNode(view=1113, noun='GRASS2_N', pDescriber="grass", pDoScaler=True, pPolygon=-1),
                       ATPNode(view=1060, noun='BUSH_N', pDescriber="Bush", pDoScaler=True),
                       # elpha - added pDoScaler=True
                       ATPNode(view=1063, noun='BUSH_PINK_N', pDescriber="Pink flowers", pDoScaler=True),
                       ATPNode(view=1064, noun='BUSH_YELLO_N', pDescriber="Yellow flowers", pDoScaler=True),
                       ATPNode(view=1111, noun='GRASS2_N', pDescriber="grass", pDoScaler=True),
                       # elpha - pDoScaler=True added
                       ATPNode(view=3711, noun='BUSH_SML_N', pDescriber="Grn sm bush"),
                       ATPNode(view=3712, noun='BUSH_SML_N', pDescriber="Bush"),
                       ATPNode(view=3716, noun='GRASS1_N', pDescriber="grass"),
                       ATPNode(view=3717, noun='GRASS1_N', pDescriber="grass-b", pPolygon=-1),
                       ATPNode(view=3954, noun='BUSH_BIG_N', pDescriber="lg bush"),
                       ATPNode(view=3955, noun='BUSH_LEAFY_N', pDescriber="low bush"),
                       ATPNode(view=3956, noun='BUSH_SML_N', pDescriber="sm bush"),
                       ATPNode(view=3957, noun='GRASS2_N', pDescriber="grass-a", pPolygon=-1),
                       ATPNode(view=3958, noun='GRASS2_N', pDescriber="grass-b", pPolygon=-1),
                       ATPNode(view=3974, noun='BUSH_SML_N', pDescriber="sm bush")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Town Ext: Plants"

    if not obj.pDescriber:
        obj.pDescriber = "Plant"

Town1RightEaves = mySet = [ATPNode(view=3626, noun='EAVES_T1_N', pDescriber="REaves-long"),
                           ATPNode(view=3627, noun='EAVES_T1_N', pDescriber="REaves-short"),
                           ATPNode(view=3628, noun='EAVES_T1_N', pDescriber="REaves-center"),
                           ATPNode(view=3629, noun='EAVES_T1_N', pDescriber="REaves-left"),
                           ATPNode(view=3630, noun='EAVES_T1_N', pDescriber="REaves-gable")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: RightEaves"
    obj.pPolygon = -1

if not obj.pDescriber:
    obj.pDescriber = "Eave"

Town1LeftEaves = mySet = [ATPNode(view=3621, noun='EAVES_T1_N', pDescriber="LEaves-long"),
                          ATPNode(view=3622, noun='EAVES_T1_N', pDescriber="LEaves-short"),
                          ATPNode(view=3623, noun='EAVES_T1_N', pDescriber="LEaves-center"),
                          ATPNode(view=3624, noun='EAVES_T1_N', pDescriber="LEaves-right"),
                          ATPNode(view=3625, noun='EAVES_T1_N', pDescriber="LEaves-gable")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: LeftEaves"
    obj.pPolygon = -1

if not obj.pDescriber:
    obj.pDescriber = "Misc"

Town1MiddleEaves = mySet = [ATPNode(view=3631, noun='EAVES_T1_N', pDescriber="MEaves-long"),
                            ATPNode(view=3632, noun='EAVES_T1_N', pDescriber="MEaves-short"),
                            ATPNode(view=3633, noun='EAVES_T1_N', pDescriber="MEaves-center"),
                            ATPNode(view=3634, noun='EAVES_T1_N', pDescriber="MEaves-right"),
                            ATPNode(view=3635, noun='EAVES_T1_N', pDescriber="MEaves-gable")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: MiddleEaves"
    obj.pPolygon = -1

if not obj.pDescriber:
    obj.pDescriber = "Eave"

Town1Beams = mySet = [ATPNode(view=3641, noun='BEAMS_T1_N', pDescriber="Dk-up-vert"),
                      ATPNode(view=3642, noun='BEAMS_T1_N', pDescriber="Dk-mid-vert"),
                      ATPNode(view=3643, noun='BEAMS_T1_N', pDescriber="Dk-low-vert"),
                      ATPNode(view=3644, noun='BEAMS_T1_N', pDescriber="Dk-gable-left"),
                      ATPNode(view=3645, noun='BEAMS_T1_N', pDescriber="Dk-gable-right"),
                      ATPNode(view=3646, noun='BEAMS_T1_N', pDescriber="Dk-gable-side"),
                      ATPNode(view=3647, noun='BEAMS_T1_N', pDescriber="Dk-roof-vert"),
                      ATPNode(view=3648, noun='BEAMS_T1_N', pDescriber="Dk-left-hor"),
                      ATPNode(view=3649, noun='BEAMS_T1_N', pDescriber="Dk-right-hor"),
                      ATPNode(view=3650, noun='BEAMS_T1_N', pDescriber="Dk-mid-hor"),
                      ATPNode(view=3651, noun='BEAMS_T1_N', pDescriber="Dk-UL-diag"),
                      ATPNode(view=3652, noun='BEAMS_T1_N', pDescriber="Dk-UL-LR-diag"),
                      ATPNode(view=3653, noun='BEAMS_T1_N', pDescriber="Dk-LR-diag"),
                      ATPNode(view=3654, noun='BEAMS_T1_N', pDescriber="Dk-UR-diag"),
                      ATPNode(view=3655, noun='BEAMS_T1_N', pDescriber="Dk-UR-LL-diag"),
                      ATPNode(view=3656, noun='BEAMS_T1_N', pDescriber="Dk-LL-diag"),
                      ATPNode(view=3661, noun='BEAMS_T1_N', pDescriber="Lt-up-vert"),
                      ATPNode(view=3662, noun='BEAMS_T1_N', pDescriber="Lt-mid-vert"),
                      ATPNode(view=3663, noun='BEAMS_T1_N', pDescriber="Lt-low-vert"),
                      ATPNode(view=3664, noun='BEAMS_T1_N', pDescriber="Lt-gable-left"),
                      ATPNode(view=3665, noun='BEAMS_T1_N', pDescriber="Lt-gable-right"),
                      ATPNode(view=3666, noun='BEAMS_T1_N', pDescriber="Lt-gable-side"),
                      ATPNode(view=3667, noun='BEAMS_T1_N', pDescriber="Lt-roof-vert"),
                      ATPNode(view=3668, noun='BEAMS_T1_N', pDescriber="Lt-left-hor"),
                      ATPNode(view=3669, noun='BEAMS_T1_N', pDescriber="Lt-mid-hor"),
                      ATPNode(view=3670, noun='BEAMS_T1_N', pDescriber="Lt-right-hor"),
                      ATPNode(view=3671, noun='BEAMS_T1_N', pDescriber="Lt-UL-diag"),
                      ATPNode(view=3672, noun='BEAMS_T1_N', pDescriber="Lt-UL-LR-diag"),
                      ATPNode(view=3673, noun='BEAMS_T1_N', pDescriber="Lt-LR-diag"),
                      ATPNode(view=3674, noun='BEAMS_T1_N', pDescriber="Lt-UR-diag"),
                      ATPNode(view=3675, noun='BEAMS_T1_N', pDescriber="Lt-UR-LL-diag"),
                      ATPNode(view=3676, noun='BEAMS_T1_N', pDescriber="Lt-LL-diag")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Ext: Beams"

    if not obj.pDescriber:
        obj.pDescriber = "Beam"

Town1IntWalls = mySet = [ATPNode(view=3001, noun='WALL_T1_N', pDescriber="Lt-Wall"),
                         ATPNode(view=3002, noun='WALL_T1_N', pDescriber="Lt-Wall-Mid"),
                         ATPNode(view=3003, noun='WALL_T1_N', pDescriber="Lt-Wall-Gable"),
                         ATPNode(view=3004, noun='WALL_T1_N', pDescriber="Lt-Wall-Roof"),
                         ATPNode(view=3005, noun='WALL_T1_N', pDescriber="Lt-Wall-dbl"),
                         ATPNode(view=3006, noun='WALL_T1_N', pDescriber="Lt-Wall-Mid-dbl"),
                         ATPNode(view=3007, noun='WALL_T1_N', pDescriber="Lt-Wall-Gable-dbl"),
                         ATPNode(view=3008, noun='WALL_T1_N', pDescriber="Lt-Wall-Roof-dbl"),
                         ATPNode(view=3009, noun='WALL_T1_N', pDescriber="Lt-Wall-low"),
                         ATPNode(view=3010, noun='WALL_T1_N', pDescriber="Lt-Wall-Mid-low"),
                         ATPNode(view=3011, noun='WALL_T1_N', pDescriber="Lt-Wall-Gable-low"),
                         ATPNode(view=3012, noun='WALL_T1_N', pDescriber="Lt-Wall-Side-low"),
                         ATPNode(view=3013, noun='WALL_T1_N', pDescriber="Dk-Wall"),
                         ATPNode(view=3014, noun='WALL_T1_N', pDescriber="Dk-Wall-Mid"),
                         ATPNode(view=3015, noun='WALL_T1_N', pDescriber="Dk-Wall-Gable"),
                         ATPNode(view=3016, noun='WALL_T1_N', pDescriber="Dk-Wall-Roof"),
                         ATPNode(view=3017, noun='WALL_T1_N', pDescriber="Dk-Wall-dbl"),
                         ATPNode(view=3018, noun='WALL_T1_N', pDescriber="Dk-Wall-Mid-dbl"),
                         ATPNode(view=3019, noun='WALL_T1_N', pDescriber="Dk-Wall-Gable-dbl"),
                         ATPNode(view=3020, noun='WALL_T1_N', pDescriber="Dk-Wall-Roof-dbl"),
                         ATPNode(view=3021, noun='WALL_T1_N', pDescriber="Dk-Wall-low"),
                         ATPNode(view=3022, noun='WALL_T1_N', pDescriber="Dk-Wall-Mid-low"),
                         ATPNode(view=3023, noun='WALL_T1_N', pDescriber="Dk-Wall-Gable-low"),
                         ATPNode(view=3024, noun='WALL_T1_N', pDescriber="Dk-Wall-Side-low"),
                         ATPNode(view=3025, noun='WALL_T1_N', pDescriber="Med-Wall"),
                         ATPNode(view=3026, noun='WALL_T1_N', pDescriber="Med-Wall-Mid"),
                         ATPNode(view=3027, noun='WALL_T1_N', pDescriber="Med-Wall-Gable"),
                         ATPNode(view=3028, noun='WALL_T1_N', pDescriber="Med-Wall-dbl"),
                         ATPNode(view=3029, noun='WALL_T1_N', pDescriber="Med-Wall-Mid-dbl"),
                         ATPNode(view=3030, noun='WALL_T1_N', pDescriber="Med-Wall-Gable-dbl"),
                         ATPNode(view=3031, noun='WALL_T1_N', pDescriber="Med-Wall-low"),
                         ATPNode(view=3032, noun='WALL_T1_N', pDescriber="Med-Wall-Mid-low"),
                         ATPNode(view=3033, noun='WALL_T1_N', pDescriber="Med-Wall-Gable-low")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Int: Walls"

    if not obj.pDescriber:
        obj.pDescriber = "Wall"

Town1IntWindows = mySet = [ATPNode(view=3041, noun='WINARCH_T1_N', pDescriber="Dk-arch-open"),
                           ATPNode(view=3042, noun='WINARCH_T1_N', pDescriber="Lt-arch-open"),
                           ATPNode(view=3043, noun='WINARCH_T1_N', pDescriber="Med-arch-open"),
                           ATPNode(view=3047, noun='WINSTNFR_T1_N', pDescriber="Stone frame-a"),
                           ATPNode(view=3048, noun='WINSTNFR_T1_N', pDescriber="Stone frame-b"),
                           ATPNode(view=3049, noun='WINSTNFR_T1_N', pDescriber="Stone frame-c"),
                           ATPNode(view=3050, noun='WINWOODFR_T1_N', pDescriber="Wood frame-a"),
                           ATPNode(view=3051, noun='WINWOODFR_T1_N', pDescriber="Wood frame-b"),
                           ATPNode(view=3052, noun='WINWOODFR_T1_N', pDescriber="Wood frame-c"),
                           ATPNode(view=3080, noun='WINRECT_T1_N', pDescriber="Dk-rect-open"),
                           ATPNode(view=3081, noun='WINRECT_T1_N', pDescriber="Lt-rect-open"),
                           ATPNode(view=3082, noun='WINRECT_T1_N', pDescriber="Med-rect-open"),
                           ATPNode(view=3085, noun='WINSTNFR_T1_N', pDescriber="Stone frame-d"),
                           ATPNode(view=3086, noun='WINWOODFR_T1_N', pDescriber="Wood frame2-a"),
                           ATPNode(view=3087, noun='WINWOODFR_T1_N', pDescriber="Wood frame2-b"),
                           ATPNode(view=3088, noun='WINWOODFR_T1_N', pDescriber="Wood frame2-c"),
                           ATPNode(view=3544, noun='WINSHUTR_T1_N', pDescriber="Dk-shutter"),
                           ATPNode(view=3545, noun='WINSHUTR_T1_N', pDescriber="Lt-shutter"),
                           ATPNode(view=3546, noun='WINSHUTR_T1_N', pDescriber="Med-shutter"),
                           ATPNode(view=3553, noun='WINMULL_T1_N', pDescriber="glass+mullions-a"),
                           ATPNode(view=3554, noun='WINMULL_T1_N', pDescriber="glass+mullions-b"),
                           ATPNode(view=3555, noun='WINMULL_T1_N', pDescriber="glass+mullions-c"),
                           ATPNode(view=3556, noun='WINDIAMAR_T1_N', pDescriber="glass+diamond-a"),
                           ATPNode(view=3557, noun='WINDIAMAR_T1_N', pDescriber="glass+diamond-b"),
                           ATPNode(view=3558, noun='WINDIAMAR_T1_N', pDescriber="glass+diamond-c"),
                           ATPNode(view=3592, noun='WINMULL_T1_N', pDescriber="Mullion-a"),
                           ATPNode(view=3593, noun='WINMULL_T1_N', pDescriber="Mullion-b"),
                           ATPNode(view=3594, noun='WINMULL_T1_N', pDescriber="Mullion-c"),
                           ATPNode(view=3595, noun='WINDIAM_T1_N', pDescriber="Diamond-a"),
                           ATPNode(view=3596, noun='WINDIAM_T1_N', pDescriber="Diamond-b"),
                           ATPNode(view=3597, noun='WINDIAM_T1_N', pDescriber="Diamond-c")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Int: Windows"
    obj.pPolygon = -1

if not obj.pDescriber:
    obj.pDescriber = "Window"

Town1IntShelf = mySet = [ATPNode(view=3101, noun='COUNTER_T1_N', pDescriber="Counter-long-Dk"),
                         ATPNode(view=3102, noun='COUNTER_T1_N', pDescriber="Counter-long-Lt"),
                         ATPNode(view=3103, noun='COUNTER_T1_N', pDescriber="Counter-long-Med"),
                         ATPNode(view=3104, noun='COUNTER_T1_N', pDescriber="Counter-short-Dk"),
                         ATPNode(view=3105, noun='COUNTER_T1_N', pDescriber="Counter-short-Lt"),
                         ATPNode(view=3106, noun='COUNTER_T1_N', pDescriber="Counter-short-Med"),
                         ATPNode(view=3107, noun='SHELF_T1_N', pDescriber="low-Shelf-Dk"),
                         ATPNode(view=3108, noun='SHELF_T1_N', pDescriber="low-Shelf-Lt"),
                         ATPNode(view=3109, noun='SHELF_T1_N', pDescriber="low-Shelf-Med"),
                         ATPNode(view=3110, noun='SHELF_T1_N', pDescriber="Shelf-Dk"),
                         ATPNode(view=3111, noun='SHELF_T1_N', pDescriber="Shelf-Lt"),
                         ATPNode(view=3112, noun='SHELF_T1_N', pDescriber="Shelf-Med")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Int: Shelves"

    if not obj.pDescriber:
        obj.pDescriber = "Shelf"

GodStuff = mySet = [ATPNode(view=3259, noun='DESPO_STAT_N', pDescriber="Despothes"),
                    ATPNode(view=3251, noun='0', pDescriber="Hanging Lamp"),
                    ATPNode(view=3252, noun='PLATFORM_N', pDescriber="Despothes Platform"),
                    ATPNode(view=3254, noun='0', pDescriber="Despothes Scepter"),
                    ATPNode(view=3255, noun='0', pDescriber="Despothes Stand"),
                    ATPNode(view=3269, noun='DUACH_STAT_N', pDescriber="Duach"),
                    ATPNode(view=3260, noun='PLATFORM_N', pDescriber="Duach Stand 4 Hand"),
                    ATPNode(view=3261, noun='DUACH_HAND_N', pDescriber="Duach Hand"),
                    ATPNode(view=3262, noun='DUACH_STAND_N', pDescriber="Duach Platform"),
                    ATPNode(view=3279, noun='ELPH_STAT_TMP_N', pDescriber="Elphame"),
                    ATPNode(view=3270, noun='TRIPOD_TMP_N', pDescriber="Elphame Tripod"),
                    ATPNode(view=3271, noun='SCALES_TMP_N', pDescriber="Elphame Scales"),
                    ATPNode(view=3272, noun='PLATFORM_N', pDescriber="Elphame Platform"),
                    ATPNode(view=3273, noun='CRACKS_TMP_N', pDescriber="Pedestal Cracks"),
                    ATPNode(view=3289, noun='ENID_TMP_N', pDescriber="Enid"),
                    ATPNode(view=3280, noun='FLOW_SWAG_TMP_N', pDescriber="Flower Swag"),
                    ATPNode(view=3281, noun='LEAF_SWAG_TMP_N', pDescriber="Leaf Swag"),
                    ATPNode(view=3282, noun='FLOW_COL_TMP_N', pDescriber="Flower Column"),
                    ATPNode(view=3283, noun='LEAF_COL_TMP_N', pDescriber="Leaf Column"),
                    ATPNode(view=3284, noun='PLATFORM_N', pDescriber="Enid Platform"),
                    ATPNode(view=3299, noun='FINV_STAT_TMP_N', pDescriber="Finvarra"),
                    ATPNode(view=3290, noun='WAR_STAND_TMP_N', pDescriber="War Hammer Stand"),
                    ATPNode(view=3291, noun='WAR_HAM_TMP_N', pDescriber="War Hammer"),
                    ATPNode(view=3309, noun='MABO_STAT_TMP_N', pDescriber="Mabon"),
                    ATPNode(view=3300, noun='0', pDescriber="Book Stand"),
                    ATPNode(view=3301, noun='0', pDescriber="Book"), ATPNode(view=3302, noun='0', pDescriber="Table"),
                    ATPNode(view=3303, noun='0', pDescriber="Papers 4 Table"),
                    ATPNode(view=3304, noun='STICK_STN_TMP_N', pDescriber="Stand 4 Stick"),
                    ATPNode(view=3305, noun='STICK_TMP_N', pDescriber="Stick"),
                    ATPNode(view=3306, noun='STICK_STN_TMP_N', pDescriber="Stick Stand Back")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 202
    obj.pCategory = "Temple: Gods"
    obj.pDoScaler = True

    if not obj.pDescriber:
        obj.pDescriber = "Temple Object"

TempleColumns = mySet = [ATPNode(view=3310, noun='COLUMN_TMP_N', pDescriber="column 1"),
                         ATPNode(view=3311, noun='COLUMN_TMP_N', pDescriber="column 2"),
                         ATPNode(view=3312, noun='CAPITOL_TMP_N', pDescriber="capitol 1"),
                         ATPNode(view=3313, noun='CAPITOL_TMP_N', pDescriber="capitol 2"),
                         ATPNode(view=3314, noun='CAPITOL_TMP_N', pDescriber="capitol 3"),
                         ATPNode(view=3315, noun='BASE_TMP_N', pDescriber="base 1"),
                         ATPNode(view=3316, noun='BASE_TMP_N', pDescriber="base 2"),
                         ATPNode(view=3317, noun='BASE_TMP_N', pDescriber="base 3"),
                         ATPNode(view=3318, noun='COL_CRK_TMP_N', pDescriber="column crack 1"),
                         ATPNode(view=3319, noun='COL_CRK_TMP_N', pDescriber="column crack 2"),
                         ATPNode(view=3320, noun='COL_CRK_TMP_N', pDescriber="column crack 3"),
                         ATPNode(view=3321, noun='COL_CRK_TMP_N', pDescriber="column crack 4"),
                         ATPNode(view=3322, noun='VINE_COL_TMP_N', pDescriber="column vine 1"),
                         ATPNode(view=3323, noun='VINE_COL_TMP_N', pDescriber="column vine 2"),
                         ATPNode(view=3324, noun='VINE_COL_TMP_N', pDescriber="column vine 3"),
                         ATPNode(view=3325, noun='VINE_COL_TMP_N', pDescriber="column vine 4")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 202
    obj.pCategory = "Temple: Columns"
    obj.pPolygon = -1
    obj.pDoScaler = False

if not obj.pDescriber:
    obj.pDescriber = "Column"

TempleArches = mySet = [ATPNode(view=3326, noun='VINE_ARCH_TMP_N', pDescriber="arch vine 3"),
                        ATPNode(view=3327, noun='VINE_ARCH_TMP_N', pDescriber="arch vine 4"),
                        ATPNode(view=3328, noun='0', pDescriber="holes n divots"),
                        ATPNode(view=3329, noun='0', pDescriber="holes n divots"),
                        ATPNode(view=3330, noun='ARCH_TMP_N', pDescriber="arch 1"),
                        ATPNode(view=3331, noun='ARCH_TMP_N', pDescriber="arch 2"),
                        ATPNode(view=3332, noun='ARCH_TMP_N', pDescriber="arch 3"),
                        ATPNode(view=3333, noun='VINE_ARCH_TMP_N', pDescriber="arch vine 1"),
                        ATPNode(view=3334, noun='VINE_ARCH_TMP_N', pDescriber="arch vine 2"),
                        ATPNode(view=3344, noun='ARCH2_TMP_N', pDescriber="inside arch thin"),
                        ATPNode(view=3345, noun='ARCH2_TMP_N', pDescriber="inside arch thick"),
                        ATPNode(view=3346, noun='ARCH_CAP_TMP_N', pDescriber="arch capstone"),
                        ATPNode(view=3347, noun='ARCH_CAP_TMP_N', pDescriber="capstone inside thin"),
                        ATPNode(view=3348, noun='ARCH_CAP_TMP_N', pDescriber="capstone inside thick")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 202
    obj.pCategory = "Temple: Arches"
    obj.pPolygon = -1
    obj.pDoScaler = False

if not obj.pDescriber:
    obj.pDescriber = "Arch"

TempleWalls = mySet = [ATPNode(view=3335, noun='WALL1_TMP_N', pDescriber="sd wall dk"),
                       ATPNode(view=3336, noun='WALL1_TMP_N', pDescriber="sd wall lt"),
                       ATPNode(view=3337, noun='WALL3_TMP_N', pDescriber="bk wall"),
                       ATPNode(view=3338, noun='WALL1_TMP_N', pDescriber="sd wall dk stone"),
                       ATPNode(view=3339, noun='WALL1_TMP_N', pDescriber="sd wall lt stone"),
                       ATPNode(view=3340, noun='WALL3_TMP_N', pDescriber="bk wall stone"),
                       ATPNode(view=3341, noun='WALL1_TMP_N', pDescriber="sd wall dk detail"),
                       ATPNode(view=3342, noun='WALL1_TMP_N', pDescriber="sd wall lt detail"),
                       ATPNode(view=3343, noun='WALL2_TMP_N', pDescriber="bk wall detail"),
                       ATPNode(view=3362, noun='WALL3_TMP_N', pDescriber="dk wall end"),
                       ATPNode(view=3363, noun='WALL3_TMP_N', pDescriber="lt wall end"),
                       ATPNode(view=3364, noun='WALL2_TMP_N', pDescriber="dk wall end detail"),
                       ATPNode(view=3365, noun='WALL2_TMP_N', pDescriber="lt wall end detail"),
                       ATPNode(view=3366, noun='WALL2_TMP_N', pDescriber="lt wall end detail"),
                       ATPNode(view=3367, noun='WALL2_TMP_N', pDescriber="lt wall end detail"),
                       ATPNode(view=3380, noun='0', pDescriber="outside fence end piece"),
                       ATPNode(view=3381, noun='0', pDescriber="outside stone fence doorway"),
                       ATPNode(view=3382, noun='0', pDescriber="outside fence wall (stone)"),
                       ATPNode(view=3383, noun='0', pDescriber="lintel light"),
                       ATPNode(view=3384, noun='0', pDescriber="lintel dark"),
                       ATPNode(view=3385, noun='0', pDescriber="lintel med"),
                       ATPNode(view=3386, noun='0', pDescriber="lintel patch lt"),
                       ATPNode(view=3387, noun='0', pDescriber="lintel patch dk"),
                       ATPNode(view=3388, noun='0', pDescriber="lintel patch med"),
                       ATPNode(view=3389, noun='0', pDescriber="wall recess"),
                       ATPNode(view=3390, noun='WALL2_TMP_N', pDescriber="wall detail med"),
                       ATPNode(view=3391, noun='WALL2_TMP_N', pDescriber="wall detail lt"),
                       ATPNode(view=3392, noun='WALL2_TMP_N', pDescriber="wall detail dk"),
                       ATPNode(view=3393, noun='WALL2_TMP_N', pDescriber="detail lt patch"),
                       ATPNode(view=3394, noun='WALL2_TMP_N', pDescriber="detail dk patch"),
                       ATPNode(view=3395, noun='WALL2_TMP_N', pDescriber="detail patch med")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 202
    obj.pCategory = "Temple: Walls"
    obj.pPolygon = -1
    obj.pDoScaler = False

if not obj.pDescriber:
    obj.pDescriber = "Lintel"

TempleWindows = mySet = [ATPNode(view=3350, noun='WINDOW1_INT_N', pDescriber="window sides dk"),
                         ATPNode(view=3351, noun='WINDOW2_INT_N', pDescriber="window bottom dk"),
                         ATPNode(view=3352, noun='WINDOW2_INT_N', pDescriber="window top 1 dk"),
                         ATPNode(view=3353, noun='WINDOW2_INT_N', pDescriber="window top 2 dk"),
                         ATPNode(view=3354, noun='WINDOW1_INT_N', pDescriber="window side lt"),
                         ATPNode(view=3355, noun='WINDOW2_INT_N', pDescriber="window bottom lt"),
                         ATPNode(view=3356, noun='WINDOW2_INT_N', pDescriber="window top 1 lt"),
                         ATPNode(view=3357, noun='WINDOW2_INT_N', pDescriber="window top 2 lt"),
                         ATPNode(view=3358, noun='WINDOW1_INT_N', pDescriber="window sides bk"),
                         ATPNode(view=3359, noun='WINDOW2_INT_N', pDescriber="window bottom bk"),
                         ATPNode(view=3360, noun='WINDOW2_INT_N', pDescriber="window top 1 bk"),
                         ATPNode(view=3361, noun='WINDOW2_INT_N', pDescriber="window top 2 bk")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 202
    obj.pCategory = "Temple: Walls"
    obj.pPolygon = -1
    obj.pDoScaler = False

if not obj.pDescriber:
    obj.pDescriber = "Wall"

Town1IntMisc = mySet = [ATPNode(view=3116, noun='COATHOOK_T1_N', pDescriber="Coat hook", pPolygon=-1),
                        ATPNode(view=3117, noun='COATRACK_T1_N', pDescriber="Coat rack", pPolygon=-1),
                        ATPNode(view=3161, noun='HOUSECANDLE_N', pDescriber="Wall-lamp-Lt", pPolygon=-1),
                        ATPNode(view=3162, noun='HOUSECANDLE_N', pDescriber="Wall-lamp-Dk", pPolygon=-1),
                        ATPNode(view=3163, noun='HOUSECANDLE_N', pDescriber="Wall-candle", pPolygon=-1),
                        ATPNode(view=3164, noun='HOUSECANDLE_N', pDescriber="Dk-candle", pPolygon=-1),
                        ATPNode(view=3165, noun='HOUSECANDLE_N', pDescriber="Lt-candle", pPolygon=-1),
                        ATPNode(view=3166, noun='HOUSECANDLE_N', pDescriber="Med-candle", pPolygon=-1),
                        ATPNode(view=3221, noun='FIREPLAC_T1_N', pDescriber="Fireplace"),
                        ATPNode(view=3370, noun='0', pDescriber="temple transition", pPolygon=-1, pDoScaler=False),
                        ATPNode(view=3598, noun='TABLESQR_T1_N', pDescriber="Square Table"),
                        ATPNode(view=3599, noun='TABLERND_T1_N', pDescriber="Round Table"),
                        ATPNode(view=3600, noun='TABLERCT_T1_N', pDescriber="Rect Table")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Int: Misc"

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

Town1IntShops = mySet = [ATPNode(view=3118, noun='SHOPCLOTH_T1_N', pDescriber="Clothes", pPolygon=-1),
                         ATPNode(view=3119, noun='SHOPARM_T1_N', pDescriber="Armor-a", pPolygon=-1),
                         ATPNode(view=3120, noun='SHOPARM_T1_N', pDescriber="Armor/Weapons", pPolygon=-1),
                         ATPNode(view=3121, noun='SHOPARM_T1_N', pDescriber="Armor-c", pPolygon=-1),
                         ATPNode(view=3122, noun='SHOPFOOD_T1_N', pDescriber="Food-a", pPolygon=-1),
                         ATPNode(view=3123, noun='SHOPFOOD_T1_N', pDescriber="Food-b", pPolygon=-1),
                         ATPNode(view=3124, noun='SHOPFOOD_T1_N', pDescriber="Food-c", pPolygon=-1),
                         ATPNode(view=3125, noun='SHOPPOTN_T1_N', pDescriber="Potion-a", pPolygon=-1),
                         ATPNode(view=3126, noun='SHOPPOTN_T1_N', pDescriber="Potion-b", pPolygon=-1),
                         ATPNode(view=3127, noun='SHOPMUGS_T1_N', pDescriber="Mugs", pPolygon=-1),
                         ATPNode(view=3128, noun='SHOPBOTL_T1_N', pDescriber="Bottles", pPolygon=-1),
                         ATPNode(view=3129, noun='SHOPBOOK_T1_N', pDescriber="Books-a", pPolygon=-1),
                         ATPNode(view=3130, noun='SHOPBOOK_T1_N', pDescriber="Books-b", pPolygon=-1),
                         ATPNode(view=3131, noun='SHOPBOOK_T1_N', pDescriber="Books-c", pPolygon=-1),
                         ATPNode(view=3132, noun='SHOPCHEM_T1_N', pDescriber="Chem-a", pPolygon=-1),
                         ATPNode(view=3133, noun='SHOPCHEM_T1_N', pDescriber="Chem-b", pPolygon=-1),
                         ATPNode(view=3134, noun='SHOPCHEM_T1_N', pDescriber="Chem-c", pPolygon=-1),
                         ATPNode(view=3135, noun='SHOPBOOK_T1_N', pDescriber="Books-d", pPolygon=-1),
                         ATPNode(view=3136, noun='SHOPCLOTH_T1_N', pDescriber="Side-Clothes", pPolygon=-1),
                         ATPNode(view=3137, noun='SHOPARM_T1_N', pDescriber="Side-Armor-a", pPolygon=-1),
                         ATPNode(view=3138, noun='SHOPARM_T1_N', pDescriber="Side-Armor-b", pPolygon=-1),
                         ATPNode(view=3139, noun='SHOPARM_T1_N', pDescriber="Side-Armor-c", pPolygon=-1),
                         ATPNode(view=3140, noun='SHOPFOOD_T1_N', pDescriber="Side-Food-a", pPolygon=-1),
                         ATPNode(view=3141, noun='SHOPFOOD_T1_N', pDescriber="Side-Food-b", pPolygon=-1),
                         ATPNode(view=3142, noun='SHOPPOTN_T1_N', pDescriber="Side-Potion-c", pPolygon=-1),
                         ATPNode(view=3143, noun='SHOPPOTN_T1_N', pDescriber="Side-Potion-a", pPolygon=-1),
                         ATPNode(view=3144, noun='SHOPPOTN_T1_N', pDescriber="Side-Potion-b", pPolygon=-1),
                         ATPNode(view=3145, noun='SHOPMUGS_T1_N', pDescriber="Side-Mugs", pPolygon=-1),
                         ATPNode(view=3146, noun='SHOPBOTL_T1_N', pDescriber="Side-Bottles", pPolygon=-1),
                         ATPNode(view=3147, noun='SHOPBOOK_T1_N', pDescriber="Side-Books-a", pPolygon=-1),
                         ATPNode(view=3148, noun='SHOPBOOK_T1_N', pDescriber="Side-Books-b", pPolygon=-1),
                         ATPNode(view=3149, noun='SHOPBOOK_T1_N', pDescriber="Side-Books-c", pPolygon=-1),
                         ATPNode(view=3150, noun='SHOPCHEM_T1_N', pDescriber="Side-Chem-a", pPolygon=-1),
                         ATPNode(view=3151, noun='SHOPCHEM_T1_N', pDescriber="Side-Chem-b", pPolygon=-1),
                         ATPNode(view=3152, noun='SHOPCHEM_T1_N', pDescriber="Side-Chem-c", pPolygon=-1),
                         ATPNode(view=3153, noun='SHOPBOOK_T1_N', pDescriber="Side-Books-d", pPolygon=-1),
                         ATPNode(view=3158, noun='MUSIC_CART_N', pDescriber="Music Cart"),
                         ATPNode(view=3159, noun='FLOWER_CART_N', pDescriber="Flower Cart"),
                         ATPNode(view=3160, noun='SHELF_N', pDescriber="Store Shelf", pPolygon=-1),
                         ATPNode(view=3241, noun='BARREL_T1_N', pDescriber="Barrel"),
                         ATPNode(view=3242, noun='BASKET_T1_N', pDescriber="Basket"),
                         ATPNode(view=3243, noun='BASKET_T1_N', pDescriber="Basket-lid"),
                         ATPNode(view=3244, noun='SACK_N', pDescriber="Flour Bag")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Town Int: Shops"

    if not obj.pDescriber:
        obj.pDescriber = "Item"

House1Misc = mySet = [ATPNode(view=3598, noun='TABLESQR_T1_N', pDescriber="Square table"),
                      ATPNode(view=3599, noun='TABLERND_T1_N', pDescriber="Round table"),
                      ATPNode(view=3600, noun='TABLERCT_T1_N', pDescriber="Rect table"),
                      ATPNode(view=3737, noun='HOUSELAMP_N', pDescriber="Dk-wall lamp", pPolygon=-1),
                      ATPNode(view=3745, noun='BACKFENC_T1_N', pDescriber="wood fence"),
                      ATPNode(view=3746, noun='BACKSTNWL_T1_N', pDescriber="stone wall-a"),
                      ATPNode(view=3747, noun='BACKSTNWL_T1_N', pDescriber="stone wall-b"),
                      ATPNode(view=3748, noun='BACKSTNWL_T1_N', pDescriber="stone wall-c"),
                      ATPNode(view=3991, noun='HOUSEBRKWALK_N', pDescriber="brick walk-a", pPolygon=-1),
                      ATPNode(view=3992, noun='HOUSEBRKWALK_N', pDescriber="brick walk-b", pPolygon=-1),
                      ATPNode(view=3993, noun='HOUSEBRKWALK_N', pDescriber="brick walk-c", pPolygon=-1),
                      ATPNode(view=3994, noun='HOUSEDRTWALK_N', pDescriber="dirt walk-a", pPolygon=-1),
                      ATPNode(view=3995, noun='HOUSEDRTWALK_N', pDescriber="dirt walk-b", pPolygon=-1),
                      ATPNode(view=3996, noun='HOUSEDRTWALK_N', pDescriber="dirt walk-c", pPolygon=-1),
                      ATPNode(view=3997, noun='HOUSESTNWALK_N', pDescriber="stone walk-a", pPolygon=-1),
                      ATPNode(view=3998, noun='HOUSESTNWALK_N', pDescriber="stone walk-b", pPolygon=-1),
                      ATPNode(view=3999, noun='HOUSESTNWALK_N', pDescriber="stone walk-c", pPolygon=-1),
                      ATPNode(view=1104, noun='BUSH_N', pDescriber="Willow Bush", pDoScaler=True),
                      ATPNode(view=1164, noun='TREE_BKGD3_N', pDescriber="Many Pines", pDoScaler=False, pPolygon=-1),
                      ATPNode(view=1180, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                      ATPNode(view=1181, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                      ATPNode(view=1182, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                      ATPNode(view=1186, noun='DIRT1_N', pDescriber="dirt", pDoScaler=True, pPolygon=-1),
                      ATPNode(view=1184, noun='GRASS2_N', pDescriber="grass", pDoScaler=True, pPolygon=-1)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "House Ext: Misc"

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

House1IntMisc = mySet = [ATPNode(view=3110, noun='SHELF_T1_N', pDescriber="Dark shelf"),
                         ATPNode(view=3111, noun='SHELF_T1_N', pDescriber="Light shelf"),
                         ATPNode(view=3112, noun='SHELF_T1_N', pDescriber="Medium shelf"),
                         ATPNode(view=3116, noun='COATHOOK_T1_N', pDescriber="Coat hook", pPolygon=-1),
                         ATPNode(view=3117, noun='COATRACK_T1_N', pDescriber="Coat rack"),
                         ATPNode(view=3118, noun='SHOPCLOTH_T1_N', pDescriber="Clothes"),
                         ATPNode(view=3122, noun='SHOPFOOD_T1_N', pDescriber="Food", pPolygon=-1),
                         ATPNode(view=3123, noun='SHOPFOOD_T1_N', pDescriber="Food2", pPolygon=-1),
                         ATPNode(view=3124, noun='SHOPPOTN_T1_N', pDescriber="Potions", pPolygon=-1),
                         ATPNode(view=3125, noun='SHOPPOTN_T1_N', pDescriber="Potions2", pPolygon=-1),
                         ATPNode(view=3126, noun='SHOPMUGS_T1_N', pDescriber="mugs", pPolygon=-1),
                         ATPNode(view=3127, noun='SHOPMUGS_T1_N', pDescriber="mugs2", pPolygon=-1),
                         ATPNode(view=3130, noun='SHOPBOOK_T1_N', pDescriber="books", pPolygon=-1),
                         ATPNode(view=3131, noun='SHOPBOOK_T1_N', pDescriber="books2", pPolygon=-1),
                         ATPNode(view=3136, noun='SHOPCLOTH_T1_N', pDescriber="Side-Clothes", pPolygon=-1),
                         ATPNode(view=3140, noun='SHOPFOOD_T1_N', pDescriber="Side-Food", pPolygon=-1),
                         ATPNode(view=3141, noun='SHOPFOOD_T1_N', pDescriber="Side-Food2", pPolygon=-1),
                         ATPNode(view=3142, noun='SHOPPOTN_T1_N', pDescriber="Side-Potions", pPolygon=-1),
                         ATPNode(view=3143, noun='SHOPPOTN_T1_N', pDescriber="Side-Potions2", pPolygon=-1),
                         ATPNode(view=3144, noun='SHOPMUGS_T1_N', pDescriber="Side-mugs", pPolygon=-1),
                         ATPNode(view=3145, noun='SHOPMUGS_T1_N', pDescriber="Side-mugs2", pPolygon=-1),
                         ATPNode(view=3147, noun='SHOPBOOK_T1_N', pDescriber="Side-books", pPolygon=-1),
                         ATPNode(view=3148, noun='SHOPBOOK_T1_N', pDescriber="Side-books2", pPolygon=-1),
                         ATPNode(view=3161, noun='HOUSELAMP_N', pDescriber="Dk-lamp", pPolygon=-1),
                         ATPNode(view=3162, noun='HOUSELAMP_N', pDescriber="Lt-lamp", pPolygon=-1),
                         ATPNode(view=3163, noun='HOUSELAMP_N', pDescriber="Med-lamp", pPolygon=-1),
                         ATPNode(view=3164, noun='HOUSECANDLE_N', pDescriber="Dk-candle", pPolygon=-1),
                         ATPNode(view=3165, noun='HOUSECANDLE_N', pDescriber="Lt-candle", pPolygon=-1),
                         ATPNode(view=3166, noun='HOUSECANDLE_N', pDescriber="Med-candle", pPolygon=-1),
                         ATPNode(view=3221, noun='HOUSEFIREPLC_N', pDescriber="Fireplace"),
                         ATPNode(view=3421, noun='HOUSEBLANKET_N', pDescriber="Blanket side", pPolygon=-1),
                         ATPNode(view=3422, noun='HOUSEBLANKET_N', pDescriber="Blanket angle", pPolygon=-1),
                         ATPNode(view=3425, noun='HOUSEMATTRES_N', pDescriber="Mattress side"),
                         ATPNode(view=3426, noun='HOUSEMATTRES_N', pDescriber="Mattress angle"),
                         ATPNode(view=3427, noun='HOUSEPILLOW_N', pDescriber="Pillow side"),
                         ATPNode(view=3428, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3437, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3438, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3439, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3461, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3462, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3463, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3464, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3465, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3466, noun='HOUSEPILLOW_N', pDescriber="Pillow angle"),
                         ATPNode(view=3467, noun='HOUSECANDHLD_N', pDescriber="Candle holder", pPolygon=-1),
                         ATPNode(view=3598, noun='TABLESQR_T1_N', pDescriber="Square Table"),
                         ATPNode(view=3599, noun='TABLERND_T1_N', pDescriber="Round Table"),
                         ATPNode(view=3600, noun='TABLERCT_T1_N', pDescriber="Rect Table")]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "House Int: Misc"

    if not obj.pDescriber:
        obj.pDescriber = "Misc"

SwampPlants = mySet = [ATPNode(view=6520, noun='PINE_SHORT_N', pDescriber="Flower moss 1", pDoScaler=True),
                       ATPNode(view=6521, noun='PINE_SHORT_N', pDescriber="Flower moss 2", pDoScaler=True),
                       ATPNode(view=6522, noun='PINE_SHORT_N', pDescriber="Red flowers", pDoScaler=True),
                       ATPNode(view=6525, noun='PINE_SHORT_N', pDescriber="Plale flowers", pDoScaler=True),
                       ATPNode(view=6543, noun='PINE_SHORT_N', pDescriber="Grass bank", pDoScaler=True),
                       ATPNode(view=6563, noun='PINE_SHORT_N', pDescriber="Grass 1", pDoScaler=True),
                       ATPNode(view=6566, noun='PINE_SHORT_N', pDescriber="Bush & mush 1", pDoScaler=True),
                       ATPNode(view=6571, noun='PINE_SHORT_N', pDescriber="Fern 2", pDoScaler=True),
                       ATPNode(view=6572, noun='PINE_SHORT_N', pDescriber="Fern 3", pDoScaler=True),
                       ATPNode(view=6573, noun='PINE_SHORT_N', pDescriber="Fern 4", pDoScaler=True),
                       ATPNode(view=6574, noun='PINE_SHORT_N', pDescriber="Fern 5", pDoScaler=True),
                       ATPNode(view=6583, noun='PINE_SHORT_N', pDescriber="Spruce bush 1", pDoScaler=True),
                       ATPNode(view=6584, noun='PINE_SHORT_N', pDescriber="Spruce bush 2", pDoScaler=True),
                       ATPNode(view=6586, noun='PINE_SHORT_N', pDescriber="Spruce clump", pDoScaler=True),
                       ATPNode(view=6589, noun='PINE_SHORT_N', pDescriber="Bush clump", pDoScaler=True),
                       ATPNode(view=6596, noun='PINE_SHORT_N', pDescriber="Bush 1", pDoScaler=True),
                       ATPNode(view=6597, noun='PINE_SHORT_N', pDescriber="Bush & mush 2", pDoScaler=True),
                       ATPNode(view=6598, noun='PINE_SHORT_N', pDescriber="Bush 2", pDoScaler=True),
                       ATPNode(view=6621, noun='PINE_SHORT_N', pDescriber="Grass 1", pDoScaler=True),
                       ATPNode(view=6622, noun='PINE_SHORT_N', pDescriber="Grass & mush", pDoScaler=True),
                       ATPNode(view=6627, noun='PINE_SHORT_N', pDescriber="Ivy", pDoScaler=True),
                       ATPNode(view=6694, noun='PINE_SHORT_N', pDescriber="Back bush", pDoScaler=True),
                       ATPNode(view=6713, noun='PINE_SHORT_N', pDescriber="Bush clump 2", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Swamp: Plants"

    if not obj.pDescriber:
        obj.pDescriber = "Plant"

SwampRocks = mySet = [ATPNode(view=6510, noun='PINE_SHORT_N', pDescriber="Chicken Rock", pDoScaler=True),
                      ATPNode(view=6512, noun='PINE_SHORT_N', pDescriber="Huge Rock 1", pDoScaler=True),
                      ATPNode(view=6513, noun='PINE_SHORT_N', pDescriber="Huge Rock 2", pDoScaler=True),
                      ATPNode(view=6514, noun='PINE_SHORT_N', pDescriber="Big Rock", pDoScaler=True),
                      ATPNode(view=6515, noun='PINE_SHORT_N', pDescriber="Flower Rock", pDoScaler=True),
                      ATPNode(view=6528, noun='PINE_SHORT_N', pDescriber="Flower Rock 2", pDoScaler=True),
                      ATPNode(view=6561, noun='PINE_SHORT_N', pDescriber="Huge Rock 3", pDoScaler=True),
                      ATPNode(view=6562, noun='PINE_SHORT_N', pDescriber="Huge Rock 4", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Swamp: Rocks"

    if not obj.pDescriber:
        obj.pDescriber = "Rock"

SwampStumps = mySet = [ATPNode(view=6540, noun='PINE_SHORT_N', pDescriber="Hollow log", pDoScaler=True),
                       ATPNode(view=6541, noun='PINE_SHORT_N', pDescriber="Log 1", pDoScaler=True),
                       ATPNode(view=6542, noun='PINE_SHORT_N', pDescriber="Big log 1", pDoScaler=True),
                       ATPNode(view=6550, noun='PINE_SHORT_N', pDescriber="Stump 1", pDoScaler=True),
                       ATPNode(view=6551, noun='PINE_SHORT_N', pDescriber="Big Stump 1", pDoScaler=True),
                       ATPNode(view=6552, noun='PINE_SHORT_N', pDescriber="Stump 2", pDoScaler=True),
                       ATPNode(view=6553, noun='PINE_SHORT_N', pDescriber="Big Stump 2", pDoScaler=True),
                       ATPNode(view=6554, noun='PINE_SHORT_N', pDescriber="Stump 3", pDoScaler=True),
                       ATPNode(view=6555, noun='PINE_SHORT_N', pDescriber="Sm stump 1", pDoScaler=True),
                       ATPNode(view=6556, noun='PINE_SHORT_N', pDescriber="Sm stump 2", pDoScaler=True),
                       ATPNode(view=6557, noun='PINE_SHORT_N', pDescriber="Stump 4", pDoScaler=True),
                       ATPNode(view=6559, noun='PINE_SHORT_N', pDescriber="Mossy stump 1", pDoScaler=True),
                       ATPNode(view=6628, noun='PINE_SHORT_N', pDescriber="Mossy stump 2", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Swamp: Stumps"

    if not obj.pDescriber:
        obj.pDescriber = "Stump"

SwampMidTrees = mySet = [ATPNode(view=6651, noun='PINE_SHORT_N', pDescriber="Mid tree 1", pDoScaler=True),
                         ATPNode(view=6652, noun='PINE_SHORT_N', pDescriber="Mid tree 2", pDoScaler=True),
                         ATPNode(view=6653, noun='PINE_SHORT_N', pDescriber="Mid tree 3", pDoScaler=True),
                         ATPNode(view=6654, noun='PINE_SHORT_N', pDescriber="Mid tree 4", pDoScaler=True),
                         ATPNode(view=6658, noun='PINE_SHORT_N', pDescriber="Mid tree 5", pDoScaler=True),
                         ATPNode(view=6659, noun='PINE_SHORT_N', pDescriber="Mid tree 6", pDoScaler=True),
                         ATPNode(view=6662, noun='PINE_SHORT_N', pDescriber="Mid tree 7", pDoScaler=True),
                         ATPNode(view=6664, noun='PINE_SHORT_N', pDescriber="Mid tree 8", pDoScaler=True),
                         ATPNode(view=6665, noun='PINE_SHORT_N', pDescriber="Mid tree 9", pDoScaler=True),
                         ATPNode(view=6666, noun='PINE_SHORT_N', pDescriber="Mid tree 10", pDoScaler=True),
                         ATPNode(view=6667, noun='PINE_SHORT_N', pDescriber="Mid tree 11", pDoScaler=True),
                         ATPNode(view=6668, noun='PINE_SHORT_N', pDescriber="Mid tree 12", pDoScaler=True),
                         ATPNode(view=6669, noun='PINE_SHORT_N', pDescriber="Mid tree 13", pDoScaler=True),
                         ATPNode(view=6670, noun='PINE_SHORT_N', pDescriber="Mid tree 14", pDoScaler=True),
                         ATPNode(view=6670, noun='PINE_SHORT_N', pDescriber="Mid tree 15", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Swamp: MidTrees"

    if not obj.pDescriber:
        obj.pDescriber = "Tree"

SwampBack = mySet = [ATPNode(view=1140, noun='0', pDescriber="distant-Tree", pPolygon=-1, pDoScaler=False),
                     ATPNode(view=6580, noun='0', pDescriber="Back spruce 1", pDoScaler=True),
                     ATPNode(view=6581, noun='0', pDescriber="Back spruce 2", pDoScaler=True),
                     ATPNode(view=6582, noun='0', pDescriber="Back spruce 3", pDoScaler=True),
                     ATPNode(view=6629, noun='0', pDescriber="Swamp back", pDoScaler=True),
                     ATPNode(view=6661, noun='0', pDescriber="Back trees", pDoScaler=True),
                     ATPNode(view=6673, noun='0', pDescriber="Back tree 1", pDoScaler=True),
                     ATPNode(view=6691, noun='PINE_SHORT_N', pDescriber="Back tree 2", pDoScaler=True),
                     ATPNode(view=6692, noun='PINE_SHORT_N', pDescriber="Back tree 3", pDoScaler=True),
                     ATPNode(view=6693, noun='PINE_SHORT_N', pDescriber="Back tree 4", pDoScaler=True),
                     ATPNode(view=6695, noun='PINE_SHORT_N', pDescriber="Back tree 5", pDoScaler=True),
                     ATPNode(view=6711, noun='PINE_SHORT_N', pDescriber="Back tree 6", pDoScaler=True),
                     ATPNode(view=6711, noun='PINE_SHORT_N', pDescriber="Back tree 7", pDoScaler=True),
                     ATPNode(view=6714, noun='PINE_SHORT_N', pDescriber="Background", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Swamp: Back"

    if not obj.pDescriber:
        obj.pDescriber = "Tree"

SwampForeTrees = mySet = [ATPNode(view=6641, noun='PINE_SHORT_N', pDescriber="Fore tree 1", pDoScaler=True),
                          ATPNode(view=6642, noun='PINE_SHORT_N', pDescriber="Fore tree 2", pDoScaler=True),
                          ATPNode(view=6643, noun='PINE_SHORT_N', pDescriber="Fore tree 3", pDoScaler=True),
                          ATPNode(view=6645, noun='PINE_SHORT_N', pDescriber="Fore tree 4", pDoScaler=True),
                          ATPNode(view=6647, noun='PINE_SHORT_N', pDescriber="Fore tree 5", pDoScaler=True),
                          ATPNode(view=6648, noun='PINE_SHORT_N', pDescriber="Fore tree 6", pDoScaler=True),
                          ATPNode(view=6650, noun='PINE_SHORT_N', pDescriber="Fore tree 7", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Swamp: ForeTrees"

    if not obj.pDescriber:
        obj.pDescriber = "Tree"

SwampMiscTrees = mySet = [ATPNode(view=6558, noun='PINE_SHORT_N', pDescriber="Dead tree 1", pDoScaler=True),
                          ATPNode(view=6590, noun='PINE_SHORT_N', pDescriber="Tree 1", pDoScaler=True),
                          ATPNode(view=6593, noun='PINE_SHORT_N', pDescriber="Tree 2", pDoScaler=True),
                          ATPNode(view=6594, noun='PINE_SHORT_N', pDescriber="Tree clump 1", pDoScaler=True),
                          ATPNode(view=6595, noun='PINE_SHORT_N', pDescriber="Tree 3", pDoScaler=True),
                          ATPNode(view=6649, noun='PINE_SHORT_N', pDescriber="Tree right", pDoScaler=True),
                          ATPNode(view=6663, noun='PINE_SHORT_N', pDescriber="Dead tree 2", pDoScaler=True),
                          ATPNode(view=6664, noun='PINE_SHORT_N', pDescriber="Suess willow", pDoScaler=True),
                          ATPNode(view=6665, noun='PINE_SHORT_N', pDescriber="Suess & mush", pDoScaler=True),
                          ATPNode(view=6671, noun='PINE_SHORT_N', pDescriber="Tree clump 2", pDoScaler=True)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 101
    obj.pCategory = "Swamp: MiscTrees"

    if not obj.pDescriber:
        obj.pDescriber = "Tree"

GuildExt = mySet = [ATPNode(view=3820, noun='BUSH_SML_N', pDescriber="Shrub", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3821, noun='TREE_N', pDescriber="Tree", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3822, noun='WALL_T1_N', pDescriber="Wall-Ext", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3823, noun='HOUSEBRKWALK_N', pDescriber="Walkway", pDoScaler=True, pPolygon=-1)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Guild Exterior"

if obj.pDescriber == 0:
    obj.pDescriber = "Guild"

GuildInt = mySet = [ATPNode(view=3705, noun='0', pDescriber="Rack-swords", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3706, noun='SHELF_N', pDescriber="Shelf-scrolls", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3707, noun='BARREL_T1_N', pDescriber="Barrel-water", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3725, noun='TABLERCT_T1_N', pDescriber="Table-guild", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3726, noun='0', pDescriber="Podium", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3727, noun='0', pDescriber="Desk", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3738, noun='WALL_T1_N', pDescriber="Wall-Int-side", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3739, noun='0', pDescriber="Rug", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3810, noun='0', pDescriber="Amber banner", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3811, noun='0', pDescriber="Purple banner", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3812, noun='0', pDescriber="Green banner", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3813, noun='0', pDescriber="Double banner", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3814, noun='0', pDescriber="Hut pic", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3815, noun='0', pDescriber="Bard pic", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3816, noun='0', pDescriber="Guy pic", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3817, noun='0', pDescriber="Girl pic", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3818, noun='WINDOW1_INT_N', pDescriber="Window-Int-1", pDoScaler=True, pPolygon=-1),
                    ATPNode(view=3819, noun='WINDOW2_INT_N', pDescriber="Window-Int-2", pDoScaler=True, pPolygon=-1)]

for i, obj in enumerate(mySet):
    obj.pMsgFile = 102
    obj.pCategory = "Guild Interior"

    if not obj.pDescriber:
        obj.pDescriber = "Guild"

ForestRegion = [Town1Trees, MidTrees, MidPlant, ForeTrees, BackTrees, MiscForest, Sky, Mountains, Ground, River,
                Lake, Road, Polygons, Transitions, Rocks]
for i, atpSet in enumerate(ForestRegion):
    ForestRegion[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('FOREST')

BeachRegion = [BeachStuff, Polygons, Transitions]
for i, atpSet in enumerate(BeachRegion):
    BeachRegion[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('BEACH')

DesertRegion = [DesertBushes, DesertGrasses, DesertSagebrush, DesertPlants, DesertTrees, DesertDunes,
                DesertDirt, DesertRiver, TownRuins, Polygons, Transitions, MiscForest, MidPlant, Rocks, Road,
                Ground]
for i, atpSet in enumerate(DesertRegion):
    DesertRegion[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('DESERT')

# DarkForestRegion = []
# for i, atpSet in enumerate(mySet):
#     for obj in atpSet:
#         obj.pMsgFile = 104
#     obj.set_room_type('FOREST')

DungeonRegion = [DungeonWalls, DungeonStalc, DungeonStalg, DungeonWebs, DungeonMush, DungeonMoss, DungeonMisc,
                 DungeonPassages, DungeonRocks, Polygons, Transitions]
for i, atpSet in enumerate(DungeonRegion):
    DungeonRegion[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('DUNGEON')

Town1Region = [Town1Walls, Town1Roofs, Town1Windows, Town1Shops, Town1Signs1, Town1Signs2, Town1Misc,
               Town1Beams, Town1Bkgd1, Town1Bkgd2, Town1RightEaves, Town1LeftEaves, Town1MiddleEaves,
               Town1Corners, Town1Trees, Town1Plants, TownRuins, Sky, MidTrees, Polygons, Transitions, Rocks,
               Road, DesertBushes, DesertGrasses, DesertSagebrush, DesertDirt, DesertTrees, DesertPlants,
               RuinWalls, RuinRoof, RuinWindows, RuinTrim]
for i, atpSet in enumerate(Town1Region):
    Town1Region[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('TOWN1')

Town1Interior = [Town1IntWalls, Town1IntWindows, Town1IntShelf, Town1IntMisc, Town1IntShops, GodStuff,
                 TempleColumns, TempleArches, TempleWalls, TempleWindows, Polygons]
for i, atpSet in enumerate(Town1Interior):
    Town1Interior[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('TOWN1INT')

House1Region = [Town1Walls, Town1Windows, Town1Roofs, Town1LeftEaves, Town1RightEaves, Town1MiddleEaves,
                Town1Beams, Town1Trees, Town1Plants, House1Misc, MidTrees, BackTrees, Transitions, Road]
for i, atpSet in enumerate(House1Region):
    House1Region[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('HOUSE1')

House1Interior = [Town1IntWalls, Town1IntWindows, House1IntMisc]
for i, atpSet in enumerate(House1Interior):
    House1Interior[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('HOUSE1INT')

SwampRegion = [SwampPlants, SwampRocks, SwampStumps, SwampMidTrees, SwampForeTrees, SwampMiscTrees, SwampBack]
for i, atpSet in enumerate(SwampRegion):
    SwampRegion[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('SWAMP')

GuildRegion = [GuildExt, GuildInt, Town1IntShelf, Town1Shops]
for i, atpSet in enumerate(GuildRegion):
    GuildRegion[i] = atpSet = copy.deepcopy(atpSet)
    for obj in atpSet:
        obj.set_room_type('GUILD')

ATPList = {SwampRegion[0][0].roomType: SwampRegion, DesertRegion[0][0].roomType: DesertRegion,
           ForestRegion[0][0].roomType: ForestRegion, Town1Region[0][0].roomType: Town1Region,
           Town1Interior[0][0].roomType: Town1Interior, House1Region[0][0].roomType: House1Region,
           House1Interior[0][0].roomType: House1Region, DungeonRegion[0][0].roomType: DungeonRegion,
           GuildRegion[0][0].roomType: GuildRegion, BeachRegion[0][0].roomType: BeachRegion}

ATP_BY_PIC = {}
for roomType, region in ATPList.items():
    ATP_BY_PIC[roomType] = {'view': {}, 'atp': {}}
    for atp_set in region:
        for atp in atp_set:
            ATP_BY_PIC[roomType]['view'][atp.view] = atp
            ATP_BY_PIC[roomType]['atp'][atp.number] = atp

import json

json_dir = "/home/caleb/Git/Realm_World_Creator/Resources/atpinfo"

ATP_CATEGORIES = {}
keys = list(ATPList.keys())
for k in keys:
    info = {"roomType": k}
    v = ATPList[k]
    atps = {}
    info['atps'] = atps
    for region in v:
        for atp in region:
            ATPList[atp.number] = atp
            ATPList[str(atp.view)] = atp
            if atp.pCategory not in ATP_CATEGORIES.keys():
                ATP_CATEGORIES[atp.pCategory] = {}
            ATP_CATEGORIES[atp.pCategory][atp.number] = atp
            atps[atp.number] = {}
            for atr in atp.attributes:
                atps[atp.number][atr] = getattr(atp, atr)
    # with open(json_dir + f"/{k}.json_output", "w") as f:
    #     json_output.dump(info, f, indent=2)