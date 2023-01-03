from stock_objects import StockObjList,StockObject
global StockObjList





class SOBJLeatherBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherBoots"
        self.pName = "Leather Boots"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 13

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTrollBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollBoots"
        self.pName = "Troll Leather Boots"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJLeatherLowBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherLowBoots"
        self.pName = "Leather Low Boots"
        self.loop = 0
        self.pBaseView = 10700
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 6

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTrollLowBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollLowBoots"
        self.pName = "Troll Low Boots"
        self.loop = 0
        self.pBaseView = 10700
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 13

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSollerets(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Sollerets"
        self.pName = "Sollerets"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 35

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIronSollerets(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronSollerets"
        self.pName = "Iron Sollerets"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 70

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSteelSollerets(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelSollerets"
        self.pName = "Steel Sollerets"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTemperedSteelSollerets(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelSollerets"
        self.pName = "Tempered Steel Sollerets"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMythrilSollerets(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilSollerets"
        self.pName = "Mythril Sollerets"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 35

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJObsidianiteSollerets(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteSollerets"
        self.pName = "Obsidianite Sollerets"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAdmantiumSollerets(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumSollerets"
        self.pName = "Admantium Sollerets"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJbDexterity(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "bDexterity"
        self.pName = "High Boots"
        self.pIDName = "Boots of Nimbleness"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJbClumsiness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "bClumsiness"
        self.pName = "High Boots"
        self.pIDName = "Boots of Tripping"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieBoots"
        self.pName = "Starting Boots"
        self.loop = 0
        self.pBaseView = 10700
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 6

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieLeatherBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieLeatherBoots"
        self.pName = "Newbie Leather Boots"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 13

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieSollerets(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieSollerets"
        self.pName = "Newbie Sollerets"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Cowl"
        self.pName = "Cowl"
        self.loop = 0
        self.pBaseView = 10000
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 93
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJExoticCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticCowl"
        self.pName = "Cowl"
        self.loop = 0
        self.pBaseView = 10000
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 93
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJLeatherCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherCowl"
        self.pName = "Leather Cowl"
        self.loop = 0
        self.pBaseView = 10000
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJTrollCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollCowl"
        self.pName = "Troll Leather Cowl"
        self.loop = 0
        self.pBaseView = 10000
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 16

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJChainCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ChainCowl"
        self.pName = "Chain Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJmaThurisazCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maThurisazCowl"
        self.pName = "Chain Cowl"
        self.pIDName = "Thurisaz Cowl"
        self.loop = 0
        self.pBaseView = 10050
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJIronCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronCowl"
        self.pName = "Iron Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJSteelCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelCowl"
        self.pName = "Steel Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJTemperedSteelCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelCowl"
        self.pName = "Tempered Steel Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJMythrilCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilCowl"
        self.pName = "Mythril Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJObsidianiteCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteCowl"
        self.pName = "Obsidianite Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 65

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJAdmantiumCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumCowl"
        self.pName = "Admantium Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJNewbieLeatherCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieLeatherCowl"
        self.pName = "Newbie Cowl"
        self.loop = 0
        self.pBaseView = 10000
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJNewbieChainCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieChainCowl"
        self.pName = "Newbie Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Pants"
        self.pName = "Hose"
        self.loop = 0
        self.pBaseView = 10500
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJExoticPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticPants"
        self.pName = "Hose"
        self.loop = 0
        self.pBaseView = 10500
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJLongSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LongSkirt"
        self.pName = "Long Skirt"
        self.loop = 0
        self.pBaseView = 21000
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 30
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJExoticLongSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticLongSkirt"
        self.pName = "Long Skirt"
        self.loop = 0
        self.pBaseView = 21000
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 30
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJShortSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ShortSkirt"
        self.pName = "Short Skirt"
        self.loop = 0
        self.pBaseView = 21500
        self.pAction = 29
        self.pClutStart = 37
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 3
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJExoticShortSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticShortSkirt"
        self.pName = "Short Skirt"
        self.loop = 0
        self.pBaseView = 21500
        self.pAction = 29
        self.pClutStart = 37
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 3
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJLeatherPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherPants"
        self.pName = "Leather Pants"
        self.loop = 0
        self.pBaseView = 10500
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTrollPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollPants"
        self.pName = "Troll Leather Pants"
        self.loop = 0
        self.pBaseView = 10500
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJLeatherLongSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherLongSkirt"
        self.pName = "Long Leather Skirt"
        self.loop = 0
        self.pBaseView = 21000
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 30
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJTrollLongSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollLongSkirt"
        self.pName = "Troll Leather Skirt"
        self.loop = 0
        self.pBaseView = 21000
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 30
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJLeatherShortSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherShortSkirt"
        self.pName = "Leather Skirt"
        self.loop = 0
        self.pBaseView = 21500
        self.pAction = 29
        self.pClutStart = 37
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 3
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJTrollShortSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollShortSkirt"
        self.pName = "Troll Short Skirt"
        self.loop = 0
        self.pBaseView = 21500
        self.pAction = 29
        self.pClutStart = 37
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 35

        self.bases.append("BWearable")
        self.pLayer = 3
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ChainPants"
        self.pName = "Chain Leggings"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 170

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIronChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronChainPants"
        self.pName = "Iron Leggings"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 240

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSteelChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelChainPants"
        self.pName = "Steel Leggings"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 170

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTemperedSteelChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelChainPants"
        self.pName = "Tempered Steel Leggings"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 210

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMythrilChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilChainPants"
        self.pName = "Mythril Leggings"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 140

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJObsidianiteChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteChainPants"
        self.pName = "Obsidianite Leggings"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 260

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAdmantiumChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumChainPants"
        self.pName = "Admantium Leggings"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 300

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJPlatePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PlatePants"
        self.pName = "Platemail Greaves"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIronPlatePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronPlatePants"
        self.pName = "Iron Greaves"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 300

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSteelPlatePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelPlatePants"
        self.pName = "Steel Greaves"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTemperedSteelPlatePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelPlatePants"
        self.pName = "Tempered Steel Greaves"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 280

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMythrilPlatePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilPlatePants"
        self.pName = "Mythril Greaves"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJObsidianitePlatePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianitePlatePants"
        self.pName = "Obsidianite Greaves"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 350

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAdmantiumPlatePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumPlatePants"
        self.pName = "Admantium Greaves"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 420

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbiePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbiePants"
        self.pName = "New Character Hose"
        self.loop = 0
        self.pBaseView = 10500
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieSkirt"
        self.pName = "Newbie Skirt"
        self.loop = 0
        self.pBaseView = 21000
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 30
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJNewbieLeatherSkirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieLeatherSkirt"
        self.pName = "Newbie Leather Skirt"
        self.loop = 0
        self.pBaseView = 21000
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 30
        self.pAreaWorn = 9
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJNewbieLeatherPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieLeatherPants"
        self.pName = "Newbie Leather Pants"
        self.loop = 0
        self.pBaseView = 10500
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieChainPants"
        self.pName = "Newbie Chain Pants"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 240

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJShirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Shirt"
        self.pName = "Doublet"
        self.loop = 0
        self.pBaseView = 10100
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJExoticShirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticShirt"
        self.pName = "Doublet"
        self.loop = 0
        self.pBaseView = 10100
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Tunic"
        self.pName = "Tunic"
        self.loop = 0
        self.pBaseView = 10400
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16387

        self.bases.append("BDescribed")

class SOBJExoticTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticTunic"
        self.pName = "Tunic"
        self.loop = 0
        self.pBaseView = 10400
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16387

        self.bases.append("BDescribed")

class SOBJRobe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Robe"
        self.pName = "Robe"
        self.loop = 0
        self.pBaseView = 11500
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 53
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 11

        self.bases.append("BWearable")
        self.pLayer = 50
        self.pAreaWorn = 2
        self.pMask = -16387

        self.bases.append("BDescribed")

class SOBJExoticRobe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticRobe"
        self.pName = "Robe"
        self.loop = 0
        self.pBaseView = 11500
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 53
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 11

        self.bases.append("BWearable")
        self.pLayer = 50
        self.pAreaWorn = 2
        self.pMask = -16387

        self.bases.append("BDescribed")

class SOBJLeatherShirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherShirt"
        self.pName = "Leather Armor"
        self.loop = 0
        self.pBaseView = 10100
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJTrollShirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollShirt"
        self.pName = "Troll Leather Shirt"
        self.loop = 0
        self.pBaseView = 10100
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJLeatherTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherTunic"
        self.pName = "Leather Tunic"
        self.loop = 0
        self.pBaseView = 10400
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 74
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16387

        self.bases.append("BDescribed")

class SOBJTrollTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollTunic"
        self.pName = "Troll Leather Tunic"
        self.loop = 0
        self.pBaseView = 10400
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 70

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16387

        self.bases.append("BDescribed")

class SOBJChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ChainTunic"
        self.pName = "Chain Vest"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJIronChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronChainTunic"
        self.pName = "Iron Chain Vest"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 260

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJSteelChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelChainTunic"
        self.pName = "Steel Chain Vest"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJTemperedSteelChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelChainTunic"
        self.pName = "Tempered Steel Chain Vest"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 220

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJMythrilChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilChainTunic"
        self.pName = "Mythril Chain Vest"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 150

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJObsidianiteChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteChainTunic"
        self.pName = "Obsidianite Chain Vest"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 280

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJAdmantiumChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumChainTunic"
        self.pName = "Admantium Chain Vest"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 330

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJPlateTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PlateTunic"
        self.pName = "Plate Armor"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 300

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJIronPlateTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronPlateTunic"
        self.pName = "Iron Plate Armor"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 325

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJSteelPlateTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelPlateTunic"
        self.pName = "Steel Plate Armor"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 300

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJTemperedSteelPlateTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelPlateTunic"
        self.pName = "Tempered Steel Plate Armor"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 320

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJMythrilPlateTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilPlateTunic"
        self.pName = "Mythril Plate Armor"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 200

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJObsidianitePlateTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianitePlateTunic"
        self.pName = "Obsidianite Plate Armor"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 380

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJAdmantiumPlateTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumPlateTunic"
        self.pName = "Admantium Plate Armor"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 460

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJNewbieShirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieShirt"
        self.pName = "Newbie Shirt"
        self.loop = 0
        self.pBaseView = 10100
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJNewbieRobe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieRobe"
        self.pName = "Newbie Robe"
        self.loop = 0
        self.pBaseView = 11500
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 11

        self.bases.append("BWearable")
        self.pLayer = 50
        self.pAreaWorn = 2
        self.pMask = -16387

        self.bases.append("BDescribed")

class SOBJNewbieLeatherShirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieLeatherShirt"
        self.pName = "Newbie Leather Shirt"
        self.loop = 0
        self.pBaseView = 10100
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJNewbieChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieChainTunic"
        self.pName = "Newbie Chain Tunic"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 260

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJGuardTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GuardTunic"
        self.pName = "Knight Tunic"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 175

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJEvilMinionTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "EvilMinionTunic"
        self.pName = "Knight Tunic"
        self.pIDName = "Evil Minion Tunic"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 175

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJProtectorTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ProtectorTunic"
        self.pName = "Knight Tunic"
        self.pIDName = "Protector Tunic"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 175

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJChampionTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ChampionTunic"
        self.pName = "Knight Tunic"
        self.pIDName = "Champion Tunic"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 175

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJWristband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Wristband"
        self.pName = "Wristband"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSilverband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Silverband"
        self.pName = "Silverbands"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJGoldband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Goldband"
        self.pName = "Goldbands"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIronband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Ironband"
        self.pName = "Iron Wristbands"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSteelband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Steelband"
        self.pName = "Steel Wristbands"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 15

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTemperedSteelband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelband"
        self.pName = "Tempered Steel Wristbands"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMythrilband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Mythrilband"
        self.pName = "Mythril Wristbands"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJObsidianiteband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Obsidianiteband"
        self.pName = "Obsidianite Wristbands"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAdmantiumband(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Admantiumband"
        self.pName = "Admantium Wristbands"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieBracers(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieBracers"
        self.pName = "Newbie Bracers"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 15

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJDye(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Dye"
        self.pName = "Bottle of Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdOlive(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dOlive"
        self.pName = "Bottle of Olive Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 48
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdLime(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dLime"
        self.pName = "Bottle of Lime Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 49
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdBlue(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dBlue"
        self.pName = "Bottle of Blue Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 53
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdAzure(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dAzure"
        self.pName = "Bottle of Azure Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdRed(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dRed"
        self.pName = "Bottle of Red Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdPink(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dPink"
        self.pName = "Bottle of Pink Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 59
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdGold(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dGold"
        self.pName = "Bottle of Gold Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdYellow(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dYellow"
        self.pName = "Bottle of Yellow Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 64
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdViolet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dViolet"
        self.pName = "Bottle of Violet Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 68
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdMagenta(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dMagenta"
        self.pName = "Bottle of Magenta Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 69
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdBrown(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dBrown"
        self.pName = "Bottle of Brown Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 73
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdTan(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dTan"
        self.pName = "Bottle of Tan Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 74
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdAqua(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dAqua"
        self.pName = "Bottle of Aqua Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 78
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdTeal(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dTeal"
        self.pName = "Bottle of Teal Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 79
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdGreen(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dGreen"
        self.pName = "Bottle of Green Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdJade(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dJade"
        self.pName = "Bottle of Jade Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdOrange(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dOrange"
        self.pName = "Bottle of Orange Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 88
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdAmber(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dAmber"
        self.pName = "Bottle of Amber Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 89
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdRoyal(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dRoyal"
        self.pName = "Bottle of Royal Purple Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 93
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdPurple(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dPurple"
        self.pName = "Bottle of Purple Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 94
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdBlack(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dBlack"
        self.pName = "Bottle of Black Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdGray(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dGray"
        self.pName = "Bottle of Gray Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 99
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdWhite(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dWhite"
        self.pName = "Bottle of White Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdOrangeMedium(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dOrangeMedium"
        self.pName = "Bottle of Medium Orange Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 89
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdLightOrange(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dLightOrange"
        self.pName = "Bottle of Light Orange Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 90
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdFlesh(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dFlesh"
        self.pName = "Bottle of Flesh Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 106
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJdLightFlesh(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "dLightFlesh"
        self.pName = "Bottle of Light Flesh Dye"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 107
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 192


        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

class SOBJScroll(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Scroll"
        self.pName = "Scroll"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJsPaper(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sPaper"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Paper"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJsDamnation(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sDamnation"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Damnation"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 151
        self.pTheurgism = 0

class SOBJsDisguise(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sDisguise"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Disguise"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJsEscape(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sEscape"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Escape"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 1
        self.pTheurgism = 0

class SOBJsGreaterIdentify(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sGreaterIdentify"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Greater Identify"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 129
        self.pTheurgism = 0

class SOBJsGreaterShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sGreaterShield"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Greater Shield"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 88
        self.pTheurgism = 0

class SOBJsIdentify(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sIdentify"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Identify"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 57
        self.pTheurgism = 0

class SOBJsImmolation(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sImmolation"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Immolation"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 32
        self.pTheurgism = 0

class SOBJsLostThought(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sLostThought"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Lost Thought"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 72
        self.pTheurgism = 0

class SOBJsMissileResistance(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sMissileResistance"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Missile Resistance"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 78
        self.pTheurgism = 0

class SOBJsMonsterSummoningI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sMonsterSummoningI"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Summon Ratling"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 133
        self.pTheurgism = 0

class SOBJsMonsterSummoningII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sMonsterSummoningII"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Summon Imp"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 136
        self.pTheurgism = 0

class SOBJsMonsterSummoningIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sMonsterSummoningIII"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Summon Ogre"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 137
        self.pTheurgism = 0

class SOBJsResistCold(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sResistCold"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Resist Cold"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 91
        self.pTheurgism = 0

class SOBJsResistFire(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sResistFire"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Resist Fire"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 90
        self.pTheurgism = 0

class SOBJsResistLightning(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sResistLightning"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Resist Lightning"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 92
        self.pTheurgism = 0

class SOBJsRusting(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sRusting"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Rusting"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 19
        self.pTheurgism = 0

class SOBJsShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sShield"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Shielding"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 87
        self.pTheurgism = 0

class SOBJsWraithform(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "sWraithform"
        self.pName = "Scroll"
        self.pIDName = "Scroll of Defenslessness"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 107
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 20
        self.pTheurgism = 0

class SOBJWeapon(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Weapon"
        self.pName = "Weapon"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BDescribed")

class SOBJThrowingDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThrowingDagger"
        self.pName = "Throwing Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJClaw(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Claw"
        self.pName = "Claw"
        self.loop = 0
        self.pBaseView = 16300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Dagger"
        self.pName = "Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ShortSword"
        self.pName = "Short Sword"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJLongSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LongSword"
        self.pName = "Long Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJBroadSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BroadSword"
        self.pName = "BroadSword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 110

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Club"
        self.pName = "Club"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 73
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 130

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Mace"
        self.pName = "Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJTwoHandSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TwoHandSword"
        self.pName = "Two Handed Sword"
        self.loop = 0
        self.pBaseView = 15000
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 200

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Axe"
        self.pName = "Battle Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 230

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJWarHammer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WarHammer"
        self.pName = "Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJMorningStar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MorningStar"
        self.pName = "Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Maul"
        self.pName = "Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJPowerRing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PowerRing"
        self.pName = "Power Ring"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJDeathHammer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DeathHammer"
        self.pName = "Death Hammer"
        self.loop = 0
        self.pBaseView = 14010
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJIronThrowingDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronThrowingDagger"
        self.pName = "Iron Throwing Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 15

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJIronClaw(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronClaw"
        self.pName = "Iron Claw"
        self.loop = 0
        self.pBaseView = 16300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 15

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJIronDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronDagger"
        self.pName = "Iron Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJIronShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronShortSword"
        self.pName = "Iron Short Sword"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJIronLongSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronLongSword"
        self.pName = "Iron Long Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 130

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJIronBroadSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronBroadSword"
        self.pName = "Iron Broad Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 160

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJWoodenClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WoodenClub"
        self.pName = "Oaken Cudgel"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 73
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJIronMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronMace"
        self.pName = "Iron Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 230

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJIronTwoHandSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronTwoHandSword"
        self.pName = "Iron Two-Handed Sword"
        self.loop = 0
        self.pBaseView = 15000
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJIronAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronAxe"
        self.pName = "Iron Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 330

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJWoodenMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WoodenMaul"
        self.pName = "Oaken Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 73
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 360

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJSteelThrowingDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelThrowingDagger"
        self.pName = "Steel Throwing Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJSteelClaw(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelClaw"
        self.pName = "Steel Claw"
        self.loop = 0
        self.pBaseView = 16300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJSteelDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelDagger"
        self.pName = "Steel Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJSteelShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelShortSword"
        self.pName = "Steel Short Sword"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJSteelLongSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelLongSword"
        self.pName = "Steel Long Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJSteelBroadSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelBroadSword"
        self.pName = "Steel Broad Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 110

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJSteelClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelClub"
        self.pName = "Steel Club"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 130

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJSteelMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelMace"
        self.pName = "Steel Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJSteelTwoHandSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelTwoHandSword"
        self.pName = "Steel Two-Handed Sword"
        self.loop = 0
        self.pBaseView = 15000
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 200

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJSteelAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelAxe"
        self.pName = "Steel Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 230

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJSteelMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelMaul"
        self.pName = "Steel Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJTemperedSteelThrowingDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelThrowingDagger"
        self.pName = "Tempered Steel Throwing Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJTemperedSteelClaw(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelClaw"
        self.pName = "Tempered Steel Claw"
        self.loop = 0
        self.pBaseView = 16300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 11

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJTemperedSteelDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelDagger"
        self.pName = "Tempered Steel Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 15

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJTemperedSteelShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelShortSword"
        self.pName = "Tempered Steel Short Sword"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJTemperedSteelLongSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelLongSword"
        self.pName = "Tempered Steel Long Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJTemperedSteelBroadSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelBroadSword"
        self.pName = "Tempered Steel Broad Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 130

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJTemperedSteelClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelClub"
        self.pName = "Tempered Steel Club"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 150

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJTemperedSteelMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelMace"
        self.pName = "Tempered Steel Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 200

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJTemperedSteelTwoHandSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelTwoHandSword"
        self.pName = "Tempered Steel Two-Handed Sword"
        self.loop = 0
        self.pBaseView = 15000
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 240

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJTemperedSteelAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelAxe"
        self.pName = "Tempered Steel Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 280

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJTemperedSteelMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelMaul"
        self.pName = "Tempered Steel Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 340

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJMythrilThrowingDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilThrowingDagger"
        self.pName = "Mythril Throwing Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJMythrilClaw(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilClaw"
        self.pName = "Mythril Claw"
        self.loop = 0
        self.pBaseView = 16300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJMythrilDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilDagger"
        self.pName = "Mythril Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJMythrilShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilShortSword"
        self.pName = "Mythril Short Sword"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJMythrilLongSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilLongSword"
        self.pName = "Mythril Long Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJMythrilBroadSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilBroadSword"
        self.pName = "Mythril Broad Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJMythrilClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilClub"
        self.pName = "Mythril Club"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJMythrilMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilMace"
        self.pName = "Mythril Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJMythrilTwoHandSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilTwoHandSword"
        self.pName = "Mythril Two-Handed Sword"
        self.loop = 0
        self.pBaseView = 15000
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 140

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJMythrilAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilAxe"
        self.pName = "Mythril Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 170

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJMythrilMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilMaul"
        self.pName = "Mythril Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 200

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJObsidianiteThrowingDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteThrowingDagger"
        self.pName = "Obsidianite Throwing Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 15

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJObsidianiteClaw(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteClaw"
        self.pName = "Obsidianite Claw"
        self.loop = 0
        self.pBaseView = 16300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 18

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJObsidianiteDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteDagger"
        self.pName = "Obsidianite Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJObsidianiteShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteShortSword"
        self.pName = "Obsidianite Short Sword"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 70

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJObsidianiteLongSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteLongSword"
        self.pName = "Obsidianite Long Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 130

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJObsidianiteBroadSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteBroadSword"
        self.pName = "Obsidianite Broad Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 160

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJObsidianiteClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteClub"
        self.pName = "Obsidianite Club"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJObsidianiteMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteMace"
        self.pName = "Obsidianite Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 230

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJObsidianiteTwoHandSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteTwoHandSword"
        self.pName = "Obsidianite Two-Handed Sword"
        self.loop = 0
        self.pBaseView = 15000
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJObsidianiteAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteAxe"
        self.pName = "Obsidianite Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 330

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJObsidianiteMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteMaul"
        self.pName = "Obsidianite Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 360

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJAdmantiumThrowingDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumThrowingDagger"
        self.pName = "Admantium Throwing Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 22

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJAdmantiumClaw(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumClaw"
        self.pName = "Admantium Claw"
        self.loop = 0
        self.pBaseView = 16300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 27

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJAdmantiumDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumDagger"
        self.pName = "Admantium Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJAdmantiumShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumShortSword"
        self.pName = "Admantium Short Sword"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJAdmantiumLongSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumLongSword"
        self.pName = "Admantium Long Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 150

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJAdmantiumBroadSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumBroadSword"
        self.pName = "Admantium Broad Sword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 190

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJAdmantiumClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumClub"
        self.pName = "Admantium Club"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 220

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJAdmantiumMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumMace"
        self.pName = "Admantium Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 250

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJAdmantiumTwoHandSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumTwoHandSword"
        self.pName = "Admantium Two-Handed Sword"
        self.loop = 0
        self.pBaseView = 15000
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 300

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJAdmantiumAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumAxe"
        self.pName = "Admantium Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 350

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJAdmantiumMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumMaul"
        self.pName = "Admantium Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 54
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 400

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJNewbieDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieDagger"
        self.pName = "Training Knife"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJNewbieSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieSword"
        self.pName = "Training Blade"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 130

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJNewbieShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieShortSword"
        self.pName = "Training Blade"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJNewbieMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieMace"
        self.pName = "Training Mace"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 230

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJNewbieMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieMaul"
        self.pName = "Training Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 99
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 360

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJTwoHandSaber(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TwoHandSaber"
        self.pName = "Two-Handed Saber"
        self.loop = 0
        self.pBaseView = 15010
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 104
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJmwStinger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwStinger"
        self.pName = "Throwing Dagger"
        self.pIDName = "The Stinger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJmwFangblade(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwFangblade"
        self.pName = "Dagger"
        self.pIDName = "Fangblade"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 83
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJmwExecutionersAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwExecutionersAxe"
        self.pName = "Battle Axe"
        self.pIDName = "The Executioner"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 93
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1000

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwLifeLeech(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwLifeLeech"
        self.pName = "Short Sword"
        self.pIDName = "Life Leech"
        self.loop = 0
        self.pBaseView = 15200
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwVulcanEdge(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwVulcanEdge"
        self.pName = "Long Sword"
        self.pIDName = "Vulcan Edge"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 58
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwNullsword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwNullsword"
        self.pName = "BroadSword"
        self.pIDName = "Nullsword"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 98
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwWrath(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwWrath"
        self.pName = "Two Handed Sword"
        self.pIDName = "The Wrath"
        self.loop = 0
        self.pBaseView = 15000
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 93
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 300

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJmwDefender(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwDefender"
        self.pName = "Long Sword"
        self.pIDName = "The Defender"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 53
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwUnholyClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwUnholyClub"
        self.pName = "Admantium Club"
        self.pIDName = "Unholy Club"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 97
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 220

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJmwMaceOfVirtue(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwMaceOfVirtue"
        self.pName = "Admantium Mace"
        self.pIDName = "Mace of Virtue"
        self.loop = 0
        self.pBaseView = 15700
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 79
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 250

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJmwVengenceSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwVengenceSword"
        self.pName = "Admantium Broad Sword"
        self.pIDName = "Sword of Vengeance"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 190

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

StockObjList.append(SOBJLeatherBoots())
StockObjList.append(SOBJTrollBoots())
StockObjList.append(SOBJLeatherLowBoots())
StockObjList.append(SOBJTrollLowBoots())
StockObjList.append(SOBJSollerets())
StockObjList.append(SOBJIronSollerets())
StockObjList.append(SOBJSteelSollerets())
StockObjList.append(SOBJTemperedSteelSollerets())
StockObjList.append(SOBJMythrilSollerets())
StockObjList.append(SOBJObsidianiteSollerets())
StockObjList.append(SOBJAdmantiumSollerets())
StockObjList.append(SOBJbDexterity())
StockObjList.append(SOBJbClumsiness())
StockObjList.append(SOBJNewbieBoots())
StockObjList.append(SOBJNewbieLeatherBoots())
StockObjList.append(SOBJNewbieSollerets())
StockObjList.append(SOBJCowl())
StockObjList.append(SOBJExoticCowl())
StockObjList.append(SOBJLeatherCowl())
StockObjList.append(SOBJTrollCowl())
StockObjList.append(SOBJChainCowl())
StockObjList.append(SOBJmaThurisazCowl())
StockObjList.append(SOBJIronCowl())
StockObjList.append(SOBJSteelCowl())
StockObjList.append(SOBJTemperedSteelCowl())
StockObjList.append(SOBJMythrilCowl())
StockObjList.append(SOBJObsidianiteCowl())
StockObjList.append(SOBJAdmantiumCowl())
StockObjList.append(SOBJNewbieLeatherCowl())
StockObjList.append(SOBJNewbieChainCowl())
StockObjList.append(SOBJPants())
StockObjList.append(SOBJExoticPants())
StockObjList.append(SOBJLongSkirt())
StockObjList.append(SOBJExoticLongSkirt())
StockObjList.append(SOBJShortSkirt())
StockObjList.append(SOBJExoticShortSkirt())
StockObjList.append(SOBJLeatherPants())
StockObjList.append(SOBJTrollPants())
StockObjList.append(SOBJLeatherLongSkirt())
StockObjList.append(SOBJTrollLongSkirt())
StockObjList.append(SOBJLeatherShortSkirt())
StockObjList.append(SOBJTrollShortSkirt())
StockObjList.append(SOBJChainPants())
StockObjList.append(SOBJIronChainPants())
StockObjList.append(SOBJSteelChainPants())
StockObjList.append(SOBJTemperedSteelChainPants())
StockObjList.append(SOBJMythrilChainPants())
StockObjList.append(SOBJObsidianiteChainPants())
StockObjList.append(SOBJAdmantiumChainPants())
StockObjList.append(SOBJPlatePants())
StockObjList.append(SOBJIronPlatePants())
StockObjList.append(SOBJSteelPlatePants())
StockObjList.append(SOBJTemperedSteelPlatePants())
StockObjList.append(SOBJMythrilPlatePants())
StockObjList.append(SOBJObsidianitePlatePants())
StockObjList.append(SOBJAdmantiumPlatePants())
StockObjList.append(SOBJNewbiePants())
StockObjList.append(SOBJNewbieSkirt())
StockObjList.append(SOBJNewbieLeatherSkirt())
StockObjList.append(SOBJNewbieLeatherPants())
StockObjList.append(SOBJNewbieChainPants())
StockObjList.append(SOBJShirt())
StockObjList.append(SOBJExoticShirt())
StockObjList.append(SOBJTunic())
StockObjList.append(SOBJExoticTunic())
StockObjList.append(SOBJRobe())
StockObjList.append(SOBJExoticRobe())
StockObjList.append(SOBJLeatherShirt())
StockObjList.append(SOBJTrollShirt())
StockObjList.append(SOBJLeatherTunic())
StockObjList.append(SOBJTrollTunic())
StockObjList.append(SOBJChainTunic())
StockObjList.append(SOBJIronChainTunic())
StockObjList.append(SOBJSteelChainTunic())
StockObjList.append(SOBJTemperedSteelChainTunic())
StockObjList.append(SOBJMythrilChainTunic())
StockObjList.append(SOBJObsidianiteChainTunic())
StockObjList.append(SOBJAdmantiumChainTunic())
StockObjList.append(SOBJPlateTunic())
StockObjList.append(SOBJIronPlateTunic())
StockObjList.append(SOBJSteelPlateTunic())
StockObjList.append(SOBJTemperedSteelPlateTunic())
StockObjList.append(SOBJMythrilPlateTunic())
StockObjList.append(SOBJObsidianitePlateTunic())
StockObjList.append(SOBJAdmantiumPlateTunic())
StockObjList.append(SOBJNewbieShirt())
StockObjList.append(SOBJNewbieRobe())
StockObjList.append(SOBJNewbieLeatherShirt())
StockObjList.append(SOBJNewbieChainTunic())
StockObjList.append(SOBJGuardTunic())
StockObjList.append(SOBJEvilMinionTunic())
StockObjList.append(SOBJProtectorTunic())
StockObjList.append(SOBJChampionTunic())
StockObjList.append(SOBJWristband())
StockObjList.append(SOBJSilverband())
StockObjList.append(SOBJGoldband())
StockObjList.append(SOBJIronband())
StockObjList.append(SOBJSteelband())
StockObjList.append(SOBJTemperedSteelband())
StockObjList.append(SOBJMythrilband())
StockObjList.append(SOBJObsidianiteband())
StockObjList.append(SOBJAdmantiumband())
StockObjList.append(SOBJNewbieBracers())
StockObjList.append(SOBJDye())
StockObjList.append(SOBJdOlive())
StockObjList.append(SOBJdLime())
StockObjList.append(SOBJdBlue())
StockObjList.append(SOBJdAzure())
StockObjList.append(SOBJdRed())
StockObjList.append(SOBJdPink())
StockObjList.append(SOBJdGold())
StockObjList.append(SOBJdYellow())
StockObjList.append(SOBJdViolet())
StockObjList.append(SOBJdMagenta())
StockObjList.append(SOBJdBrown())
StockObjList.append(SOBJdTan())
StockObjList.append(SOBJdAqua())
StockObjList.append(SOBJdTeal())
StockObjList.append(SOBJdGreen())
StockObjList.append(SOBJdJade())
StockObjList.append(SOBJdOrange())
StockObjList.append(SOBJdAmber())
StockObjList.append(SOBJdRoyal())
StockObjList.append(SOBJdPurple())
StockObjList.append(SOBJdBlack())
StockObjList.append(SOBJdGray())
StockObjList.append(SOBJdWhite())
StockObjList.append(SOBJdOrangeMedium())
StockObjList.append(SOBJdLightOrange())
StockObjList.append(SOBJdFlesh())
StockObjList.append(SOBJdLightFlesh())
StockObjList.append(SOBJScroll())
StockObjList.append(SOBJsPaper())
StockObjList.append(SOBJsDamnation())
StockObjList.append(SOBJsDisguise())
StockObjList.append(SOBJsEscape())
StockObjList.append(SOBJsGreaterIdentify())
StockObjList.append(SOBJsGreaterShield())
StockObjList.append(SOBJsIdentify())
StockObjList.append(SOBJsImmolation())
StockObjList.append(SOBJsLostThought())
StockObjList.append(SOBJsMissileResistance())
StockObjList.append(SOBJsMonsterSummoningI())
StockObjList.append(SOBJsMonsterSummoningII())
StockObjList.append(SOBJsMonsterSummoningIII())
StockObjList.append(SOBJsResistCold())
StockObjList.append(SOBJsResistFire())
StockObjList.append(SOBJsResistLightning())
StockObjList.append(SOBJsRusting())
StockObjList.append(SOBJsShield())
StockObjList.append(SOBJsWraithform())
StockObjList.append(SOBJWeapon())
StockObjList.append(SOBJThrowingDagger())
StockObjList.append(SOBJClaw())
StockObjList.append(SOBJDagger())
StockObjList.append(SOBJShortSword())
StockObjList.append(SOBJLongSword())
StockObjList.append(SOBJBroadSword())
StockObjList.append(SOBJClub())
StockObjList.append(SOBJMace())
StockObjList.append(SOBJTwoHandSword())
StockObjList.append(SOBJAxe())
StockObjList.append(SOBJWarHammer())
StockObjList.append(SOBJMorningStar())
StockObjList.append(SOBJMaul())
StockObjList.append(SOBJPowerRing())
StockObjList.append(SOBJDeathHammer())
StockObjList.append(SOBJIronThrowingDagger())
StockObjList.append(SOBJIronClaw())
StockObjList.append(SOBJIronDagger())
StockObjList.append(SOBJIronShortSword())
StockObjList.append(SOBJIronLongSword())
StockObjList.append(SOBJIronBroadSword())
StockObjList.append(SOBJWoodenClub())
StockObjList.append(SOBJIronMace())
StockObjList.append(SOBJIronTwoHandSword())
StockObjList.append(SOBJIronAxe())
StockObjList.append(SOBJWoodenMaul())
StockObjList.append(SOBJSteelThrowingDagger())
StockObjList.append(SOBJSteelClaw())
StockObjList.append(SOBJSteelDagger())
StockObjList.append(SOBJSteelShortSword())
StockObjList.append(SOBJSteelLongSword())
StockObjList.append(SOBJSteelBroadSword())
StockObjList.append(SOBJSteelClub())
StockObjList.append(SOBJSteelMace())
StockObjList.append(SOBJSteelTwoHandSword())
StockObjList.append(SOBJSteelAxe())
StockObjList.append(SOBJSteelMaul())
StockObjList.append(SOBJTemperedSteelThrowingDagger())
StockObjList.append(SOBJTemperedSteelClaw())
StockObjList.append(SOBJTemperedSteelDagger())
StockObjList.append(SOBJTemperedSteelShortSword())
StockObjList.append(SOBJTemperedSteelLongSword())
StockObjList.append(SOBJTemperedSteelBroadSword())
StockObjList.append(SOBJTemperedSteelClub())
StockObjList.append(SOBJTemperedSteelMace())
StockObjList.append(SOBJTemperedSteelTwoHandSword())
StockObjList.append(SOBJTemperedSteelAxe())
StockObjList.append(SOBJTemperedSteelMaul())
StockObjList.append(SOBJMythrilThrowingDagger())
StockObjList.append(SOBJMythrilClaw())
StockObjList.append(SOBJMythrilDagger())
StockObjList.append(SOBJMythrilShortSword())
StockObjList.append(SOBJMythrilLongSword())
StockObjList.append(SOBJMythrilBroadSword())
StockObjList.append(SOBJMythrilClub())
StockObjList.append(SOBJMythrilMace())
StockObjList.append(SOBJMythrilTwoHandSword())
StockObjList.append(SOBJMythrilAxe())
StockObjList.append(SOBJMythrilMaul())
StockObjList.append(SOBJObsidianiteThrowingDagger())
StockObjList.append(SOBJObsidianiteClaw())
StockObjList.append(SOBJObsidianiteDagger())
StockObjList.append(SOBJObsidianiteShortSword())
StockObjList.append(SOBJObsidianiteLongSword())
StockObjList.append(SOBJObsidianiteBroadSword())
StockObjList.append(SOBJObsidianiteClub())
StockObjList.append(SOBJObsidianiteMace())
StockObjList.append(SOBJObsidianiteTwoHandSword())
StockObjList.append(SOBJObsidianiteAxe())
StockObjList.append(SOBJObsidianiteMaul())
StockObjList.append(SOBJAdmantiumThrowingDagger())
StockObjList.append(SOBJAdmantiumClaw())
StockObjList.append(SOBJAdmantiumDagger())
StockObjList.append(SOBJAdmantiumShortSword())
StockObjList.append(SOBJAdmantiumLongSword())
StockObjList.append(SOBJAdmantiumBroadSword())
StockObjList.append(SOBJAdmantiumClub())
StockObjList.append(SOBJAdmantiumMace())
StockObjList.append(SOBJAdmantiumTwoHandSword())
StockObjList.append(SOBJAdmantiumAxe())
StockObjList.append(SOBJAdmantiumMaul())
StockObjList.append(SOBJNewbieDagger())
StockObjList.append(SOBJNewbieSword())
StockObjList.append(SOBJNewbieShortSword())
StockObjList.append(SOBJNewbieMace())
StockObjList.append(SOBJNewbieMaul())
StockObjList.append(SOBJTwoHandSaber())
StockObjList.append(SOBJmwStinger())
StockObjList.append(SOBJmwFangblade())
StockObjList.append(SOBJmwExecutionersAxe())
StockObjList.append(SOBJmwLifeLeech())
StockObjList.append(SOBJmwVulcanEdge())
StockObjList.append(SOBJmwNullsword())
StockObjList.append(SOBJmwWrath())
StockObjList.append(SOBJmwDefender())
StockObjList.append(SOBJmwUnholyClub())
StockObjList.append(SOBJmwMaceOfVirtue())
StockObjList.append(SOBJmwVengenceSword())
