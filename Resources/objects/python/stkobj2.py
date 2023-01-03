from stock_objects import StockObjList,StockObject
global StockObjList





class SOBJmwTiwazSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwTiwazSword"
        self.pName = "BroadSword"
        self.pIDName = "Sword of Tiwaz"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 115
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 110

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwUruzDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwUruzDagger"
        self.pName = "Throwing Dagger"
        self.pIDName = "Uruz Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 115
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 22

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJmwSpecialNullsword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwSpecialNullsword"
        self.pName = "Nullsword"
        self.pIDName = "Sword of the Mists"
        self.loop = 0
        self.pBaseView = 15100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 48
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5900

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwBerserkersAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwBerserkersAxe"
        self.pName = "Battle Axe"
        self.pIDName = "Berserker's Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1750

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwOrcThugClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwOrcThugClub"
        self.pName = "Admantium Club"
        self.pIDName = "Thug Club"
        self.loop = 0
        self.pBaseView = 16100
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 220

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJmwOrcBanditSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwOrcBanditSword"
        self.pName = "Admantium Short Sword"
        self.pIDName = "Bandit Sword"
        self.loop = 0
        self.pBaseView = 15200
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

class SOBJmwOrcWarlordAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwOrcWarlordAxe"
        self.pName = "Admantium Axe"
        self.pIDName = "Warlord Axe"
        self.loop = 0
        self.pBaseView = 15900
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 350

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 1

class SOBJmwOrcMagusDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwOrcMagusDagger"
        self.pName = "Admantium Dagger"
        self.pIDName = "Magus Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJmwOrcScoutDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "mwOrcScoutDagger"
        self.pName = "Admantium Throwing Dagger"
        self.pIDName = "Scout Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 22

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 0

class SOBJmaDragonPlate(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maDragonPlate"
        self.pName = "Plate Armor"
        self.pIDName = "Dragonscale Plate"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 58
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

class SOBJmaInsulPlate(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maInsulPlate"
        self.pName = "Plate Armor"
        self.pIDName = "Plate of Insulation"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 100
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

class SOBJmaDensePlate(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maDensePlate"
        self.pName = "Plate Armor"
        self.pIDName = "Plate of Density"
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

class SOBJmaDenseGreaves(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maDenseGreaves"
        self.pName = "Platemail Greaves"
        self.pIDName = "Greaves of Density"
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

class SOBJmaDenseCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maDenseCowl"
        self.pName = "Chain Cowl"
        self.pIDName = "Cowl of Density"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJmaDenseBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maDenseBoots"
        self.pName = "Sollerets"
        self.pIDName = "Boots of Density"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 120

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJmaDenseBands(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maDenseBands"
        self.pName = "Wristband"
        self.pIDName = "Bands of Density"
        self.loop = 0
        self.pBaseView = 10300
        self.pAction = 29
        self.pClutStart = 44
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 40
        self.pAreaWorn = 4
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJmaBracersOfDefense(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maBracersOfDefense"
        self.pName = "Mythril Wristbands"
        self.pIDName = "Bracers of Defense"
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

class SOBJmaInvulPlate(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "maInvulPlate"
        self.pName = "Plate Armor"
        self.pIDName = "Plate of Invulnerability"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 93
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

class SOBJShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Shield"
        self.pName = "Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJWoodShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WoodShield"
        self.pName = "Wooden Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 70

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJRoundShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RoundShield"
        self.pName = "Bronze Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LargeShield"
        self.pName = "Large Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 150

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJKnightsShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "KnightsShield"
        self.pName = "Knight's Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 220

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJWoodRoundShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WoodRoundShield"
        self.pName = "Wooden Round Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 105
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 70

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIronRoundShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronRoundShield"
        self.pName = "Iron Round Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 110

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSteelRoundShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelRoundShield"
        self.pName = "Steel Round Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTemperedSteelRoundShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelRoundShield"
        self.pName = "Tempered Steel Round Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMythrilRoundShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilRoundShield"
        self.pName = "Mythril Round Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 75

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJObsidianiteRoundShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteRoundShield"
        self.pName = "Obsidianite Round Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 150

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAdmantiumRoundShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumRoundShield"
        self.pName = "Admantium Round Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 200

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJWoodLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WoodLargeShield"
        self.pName = "Wooden Tower Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 105
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIronLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronLargeShield"
        self.pName = "Iron Tower Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 165

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSteelLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelLargeShield"
        self.pName = "Steel Tower Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 130

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTemperedSteelLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelLargeShield"
        self.pName = "Tempered Steel Tower Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 140

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMythrilLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilLargeShield"
        self.pName = "Mythril Tower Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 110

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJObsidianiteLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteLargeShield"
        self.pName = "Obsidianite Tower Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 190

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAdmantiumLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumLargeShield"
        self.pName = "Admantium Tower Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieSmallShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieSmallShield"
        self.pName = "Small Training Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 74
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieShield"
        self.pName = "Small Training Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 74
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNewbieLargeShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NewbieLargeShield"
        self.pName = "Large Training Shield"
        self.loop = 0
        self.pBaseView = 16500
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 74
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 130

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJLeftHandPowerRing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeftHandPowerRing"
        self.pName = "Power Ring = Shield"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -12033

        self.bases.append("BDescribed")

class SOBJStatue(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Statue"
        self.pName = "Statue"
        self.loop = 0
        self.pBaseView = 54700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 0

        self.bases.append("BDescribed")

class SOBJElphamesScales(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ElphamesScales"
        self.pName = "Elphame's Scales"
        self.loop = 0
        self.pBaseView = 57250
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJGem(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Gem"
        self.pName = "Gem"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJCrystal(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Crystal"
        self.pName = "Crystal"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 41
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJRubyChip(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RubyChip"
        self.pName = "Ruby Chip"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJAquamarine(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Aquamarine"
        self.pName = "Aquamarine"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 78
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJTurquoise(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Turquoise"
        self.pName = "Turquoise"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJTopaz(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Topaz"
        self.pName = "Topaz"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 64
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJEmmerald(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Emmerald"
        self.pName = "Emmerald"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJEmerald(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Emerald"
        self.pName = "Emerald"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJRuby(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Ruby"
        self.pName = "Ruby"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJJet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Jet"
        self.pName = "Jet"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJDiamond(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Diamond"
        self.pName = "Diamond"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 41
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJTempleTrophy(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TempleTrophy"
        self.pName = "Temple Trophy"
        self.loop = 0
        self.pBaseView = 56800
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10000

        self.bases.append("BDescribed")

class SOBJMistGem(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGem"
        self.pName = "Mist Talisman"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 40
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemI"
        self.pName = "Talisman of Hope"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 73
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemII"
        self.pName = "Talisman of Courage"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 78
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemIII"
        self.pName = "Talisman of Life"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemIV"
        self.pName = "Talisman of Luck"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemV"
        self.pName = "Talisman of Happiness"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 79
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemVI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemVI"
        self.pName = "Talisman of Faith"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemVII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemVII"
        self.pName = "Talisman of Honor"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 55
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemVIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemVIII"
        self.pName = "Talisman of Love"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 59
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJMistGemIX(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MistGemIX"
        self.pName = "Talisman of Immortality"
        self.loop = 0
        self.pBaseView = 50850
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 56
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJLargeAmethyst(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LargeAmethyst"
        self.pName = "Amethyst"
        self.loop = 0
        self.pBaseView = 50851
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJFlawlessAmethyst(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlawlessAmethyst"
        self.pName = "Flawless Amethyst"
        self.loop = 0
        self.pBaseView = 50851
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJLargeDiamond(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LargeDiamond"
        self.pName = "Diamond"
        self.loop = 0
        self.pBaseView = 50852
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJFlawlessDiamond(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlawlessDiamond"
        self.pName = "Flawless Diamond"
        self.loop = 0
        self.pBaseView = 50852
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJLargeEmerald(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LargeEmerald"
        self.pName = "Emerald"
        self.loop = 0
        self.pBaseView = 50853
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJFlawlessEmerald(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlawlessEmerald"
        self.pName = "Flawless Emerald"
        self.loop = 0
        self.pBaseView = 50853
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJLargeJet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LargeJet"
        self.pName = "Jet"
        self.loop = 0
        self.pBaseView = 50858
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJFlawlessJet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlawlessJet"
        self.pName = "Flawless Jet"
        self.loop = 0
        self.pBaseView = 50858
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJLargeRuby(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LargeRuby"
        self.pName = "Ruby"
        self.loop = 0
        self.pBaseView = 50859
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJFlawlessRuby(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlawlessRuby"
        self.pName = "Flawless Ruby"
        self.loop = 0
        self.pBaseView = 50859
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJLargeSapphire(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LargeSapphire"
        self.pName = "Sapphire"
        self.loop = 0
        self.pBaseView = 50860
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJFlawlessSapphire(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlawlessSapphire"
        self.pName = "Flawless Sapphire"
        self.loop = 0
        self.pBaseView = 50860
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJLargeTopaz(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LargeTopaz"
        self.pName = "Topaz"
        self.loop = 0
        self.pBaseView = 50861
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJFlawlessTopaz(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlawlessTopaz"
        self.pName = "Flawless Topaz"
        self.loop = 0
        self.pBaseView = 50861
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJNPC(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NPC"
        self.pName = "<bad engrave>"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJStrongBox(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "StrongBox"
        self.pName = "Strong Box"
        self.loop = 0
        self.pBaseView = 50000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 16402
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 12500
        self.pBulkCap = 5000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

        self.bases.append("BPassword")

class SOBJDoor(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Door"
        self.pName = "Door"
        self.loop = 0
        self.pBaseView = 60000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1040
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

        self.bases.append("BOpenable")

class SOBJPWDoor(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PWDoor"
        self.pName = "Door"
        self.loop = 0
        self.pBaseView = 60000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 17424
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

        self.bases.append("BOpenable")

        self.bases.append("BPassword")

class SOBJPlankDoor(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PlankDoor"
        self.pName = "Plank Door"
        self.loop = 0
        self.pBaseView = 60000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1040
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

        self.bases.append("BOpenable")

class SOBJSimpleDoor(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SimpleDoor"
        self.pName = "Door"
        self.loop = 0
        self.pBaseView = 60100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1040
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

        self.bases.append("BOpenable")

class SOBJDoorway(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Doorway"
        self.pName = "Door"
        self.loop = 0
        self.pBaseView = 60200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1024
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

class SOBJRuinDoorA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RuinDoorA"
        self.pName = "Door"
        self.loop = 0
        self.pBaseView = 60050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1040
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

        self.bases.append("BOpenable")

class SOBJRuinDoorB(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RuinDoorB"
        self.pName = "Door"
        self.loop = 0
        self.pBaseView = 60150
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1040
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

        self.bases.append("BOpenable")

class SOBJGlowingPortal(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GlowingPortal"
        self.pName = "Glowing Portal"
        self.loop = 0
        self.pBaseView = 30105
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1056
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJChair(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Chair"
        self.pName = "Chair"
        self.loop = 0
        self.pBaseView = 60500
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 65


        self.bases.append("BSit")

        self.bases.append("BDescribed")

class SOBJStool(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Stool"
        self.pName = "Stool"
        self.loop = 0
        self.pBaseView = 62550
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 65


        self.bases.append("BSit")

        self.bases.append("BDescribed")

class SOBJBed(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Bed"
        self.pName = "Bed"
        self.loop = 0
        self.pBaseView = 61700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

class SOBJFirePlace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FirePlace"
        self.pName = "Fireplace"
        self.loop = 0
        self.pBaseView = 60300
        self.pAction = 30
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Baldric"
        self.pName = "Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 58
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJOliveBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OliveBaldric"
        self.pName = "Olive Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 48
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJBlueBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BlueBaldric"
        self.pName = "Neophyte's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 53
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJAzureBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AzureBaldric"
        self.pName = "Azure Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJRedBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RedBaldric"
        self.pName = "Familiar Player's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 58
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJPinkBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PinkBaldric"
        self.pName = "Pink Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 59
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJGoldBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GoldBaldric"
        self.pName = "Seasoned Player's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJYellowBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "YellowBaldric"
        self.pName = "Veteran's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 64
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJVioletBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "VioletBaldric"
        self.pName = "Violet Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 68
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJMagentaBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagentaBaldric"
        self.pName = "Expert Player's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 69
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJBrownBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BrownBaldric"
        self.pName = "Skilled Player's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 73
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJTanBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TanBaldric"
        self.pName = "Tan Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 74
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJAquaBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AquaBaldric"
        self.pName = "Aqua Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 78
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJTealBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TealBaldric"
        self.pName = "Teal Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 79
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJJadeBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JadeBaldric"
        self.pName = "Jade Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 84
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJAmberBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AmberBaldric"
        self.pName = "Grand-Master's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 89
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJRoyalBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RoyalBaldric"
        self.pName = "Legend's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 93
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJPurpleBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PurpleBaldric"
        self.pName = "Pink Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 59
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJRealPurpleBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RealPurpleBaldric"
        self.pName = "Purple Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 94
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJWhiteBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WhiteBaldric"
        self.pName = "White Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJBlackBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BlackBaldric"
        self.pName = "White Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJRealBlackBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RealBlackBaldric"
        self.pName = "Black Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJGrayBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GrayBaldric"
        self.pName = "Advanced Player's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJGreenBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GreenBaldric"
        self.pName = "Master Player's Baldric"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJSatoriBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SatoriBaldric"
        self.pName = "Baldric of Satori"
        self.loop = 0
        self.pBaseView = 10900
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 30
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJThistlebark(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Thistlebark"
        self.pName = "Thistlebark"
        self.loop = 0
        self.pBaseView = 10950
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 11
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJThistlebarkA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThistlebarkA"
        self.pName = "Thistlebark"
        self.pIDName = "Sacred Temple Sash"
        self.loop = 0
        self.pBaseView = 10950
        self.pAction = 29
        self.pClutStart = -1
        self.pColor = 125
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJThistlebarkB(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThistlebarkB"
        self.pName = "Thistlebark"
        self.loop = 0
        self.pBaseView = 10950
        self.pAction = 29
        self.pClutStart = -1
        self.pColor = 126
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJPumpkinBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PumpkinBaldric"
        self.pName = "Pumpkin Baldric"
        self.loop = 0
        self.pBaseView = 10750
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 11
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJCrestedBaldric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "CrestedBaldric"
        self.pName = "Crested Baldric"
        self.loop = 0
        self.pBaseView = 10800
        self.pAction = 29
        self.pClutStart = 11
        self.pColor = 11
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 80
        self.pAreaWorn = 99
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAmulet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Amulet"
        self.pName = "Amulet"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaConcentration(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aConcentration"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Concentration"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaChoking(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aChoking"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Choking"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaClumsiness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aClumsiness"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Clumsiness"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaColdProtection(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aColdProtection"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Cold Protection"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaCombat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aCombat"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Combat"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaDexterity(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aDexterity"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Dexterity"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaDodging(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aDodging"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Dodging"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaEndurance(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aEndurance"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Endurance"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaFireProtection(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aFireProtection"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Fire Protection"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaMemory(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aMemory"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Memory"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaGrounding(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aGrounding"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Grounding"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaIntelligence(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aIntelligence"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Intelligence"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaRetention(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aRetention"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Retention"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaShielding(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aShielding"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Shielding"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaStrength(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aStrength"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Strength"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaStupidity(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aStupidity"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Stupidity"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaVulnerability(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aVulnerability"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Vulnerability"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaWeakness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aWeakness"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Weakness"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaWeatherproofing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aWeatherproofing"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Weatherproofing"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaFreeWill(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aFreeWill"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Free Will"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJaDeathProtection(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "aDeathProtection"
        self.pName = "Amulet"
        self.pIDName = "Amulet of Death Magic Protection"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJWand(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Wand"
        self.pName = "Wand"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 1

class SOBJwStick(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wStick"
        self.pName = "Wand"
        self.pIDName = "Polished Stick"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 1

class SOBJwBerserk(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wBerserk"
        self.pName = "Wand"
        self.pIDName = "Wand of Berserk"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 58
        self.pTheurgism = 1

class SOBJwFireballs(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wFireballs"
        self.pName = "Wand"
        self.pIDName = "Wand of Fireballs"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 44
        self.pTheurgism = 1

class SOBJwFreezingWind(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wFreezingWind"
        self.pName = "Wand"
        self.pIDName = "Wand of Freezing Wind"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 40
        self.pTheurgism = 1

class SOBJwLightning(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wLightning"
        self.pName = "Wand"
        self.pIDName = "Wand of Lightning"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 45
        self.pTheurgism = 1

class SOBJwNakedness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wNakedness"
        self.pName = "Wand"
        self.pIDName = "Wand of Nakedness"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 1

class SOBJwPoisonBolts(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wPoisonBolts"
        self.pName = "Wand"
        self.pIDName = "Wand of Poison Bolts"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 105
        self.pTheurgism = 1

class SOBJwRust(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wRust"
        self.pName = "Wand"
        self.pIDName = "Wand of Rust"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 19
        self.pTheurgism = 1

class SOBJwStoning(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wStoning"
        self.pName = "Wand"
        self.pIDName = "Wand of Stoning"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 43
        self.pTheurgism = 1

class SOBJwUgly(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "wUgly"
        self.pName = "Wand"
        self.pIDName = "Wand of Ugly"
        self.loop = 0
        self.pBaseView = 51700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 1

class SOBJPotion(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Potion"
        self.pName = ""
        self.pIDName = "Potion"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpWater(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pWater"
        self.pName = "Potion"
        self.pIDName = "Potion of Purified Water"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 98
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpSwampWater(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pSwampWater"
        self.pName = "Potion"
        self.pIDName = "Bottle of Swamp Water"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 79
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpClumsiness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pClumsiness"
        self.pName = "Potion"
        self.pIDName = "Potion of Clumsiness"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpCurePoison(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pCurePoison"
        self.pName = "Potion"
        self.pIDName = "Potion of Cure Poison"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpDexterity(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pDexterity"
        self.pName = "Potion"
        self.pIDName = "Potion of Dexterity"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpGreaterHealth(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pGreaterHealth"
        self.pName = "Potion"
        self.pIDName = "Potion of Greater Health"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpHealth(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pHealth"
        self.pName = "Potion"
        self.pIDName = "Potion of Health"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpInvisibility(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pInvisibility"
        self.pName = "Potion"
        self.pIDName = "Potion of Invisibility"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpPain(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pPain"
        self.pName = "Potion"
        self.pIDName = "Potion of Pain"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpPoison(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pPoison"
        self.pName = "Potion"
        self.pIDName = "Potion of Poison"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpRegeneration(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pRegeneration"
        self.pName = "Potion"
        self.pIDName = "Potion of Regeneration"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpSeeInvisibility(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pSeeInvisibility"
        self.pName = "Potion"
        self.pIDName = "Potion of See Invisible"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpStrength(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pStrength"
        self.pName = "Potion"
        self.pIDName = "Potion of Strength"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpWeakness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pWeakness"
        self.pName = "Potion"
        self.pIDName = "Potion of Weakness"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpAcidShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pAcidShield"
        self.pName = "Potion"
        self.pIDName = "Potion of Acid Shield"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpColdShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pColdShield"
        self.pName = "Potion"
        self.pIDName = "Potion of Cold Shield"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpPoisonShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pPoisonShield"
        self.pName = "Potion"
        self.pIDName = "Potion of Poison Shield"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpLightningShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pLightningShield"
        self.pName = "Potion"
        self.pIDName = "Potion of Lightning Shield"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpFireShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pFireShield"
        self.pName = "Potion"
        self.pIDName = "Potion of Fire Shield"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpAcidCurse(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pAcidCurse"
        self.pName = "Potion"
        self.pIDName = "Potion of Acid Curse"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpColdCurse(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pColdCurse"
        self.pName = "Potion"
        self.pIDName = "Potion of Cold Curse"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpPoisonCurse(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pPoisonCurse"
        self.pName = "Potion"
        self.pIDName = "Potion of Poison Curse"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpLightningCurse(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pLightningCurse"
        self.pName = "Potion"
        self.pIDName = "Potion of Lightning Curse"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpFireCurse(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pFireCurse"
        self.pName = "Potion"
        self.pIDName = "Potion of Fire Curse"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpInvulnerability(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pInvulnerability"
        self.pName = "Potion"
        self.pIDName = "Potion of Invulnerability"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpShift(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pShift"
        self.pName = "Potion"
        self.pIDName = "Potion of Shifting"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpGreaterInvisibility(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pGreaterInvisibility"
        self.pName = "Potion"
        self.pIDName = "Potion of Greater Invisibility"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJpDeath(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "pDeath"
        self.pName = "Potion"
        self.pIDName = "Potion of Death"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

class SOBJRing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Ring"
        self.pName = "Ring"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrCopper(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rCopper"
        self.pName = "Ring"
        self.pIDName = "Ring of Copper"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrEngagement(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rEngagement"
        self.pName = "Ring"
        self.pIDName = "Engagement Ring"
        self.loop = 0
        self.pBaseView = 51900
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrWedding(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rWedding"
        self.pName = "Ring"
        self.pIDName = "Wedding Ring"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrWedding2(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rWedding2"
        self.pName = "Ring"
        self.pIDName = "Expensive Wedding Ring"
        self.loop = 0
        self.pBaseView = 51900
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrWedding3(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rWedding3"
        self.pName = "Ring"
        self.pIDName = "Royal Wedding Ring"
        self.loop = 0
        self.pBaseView = 51950
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrClumsiness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rClumsiness"
        self.pName = "Ring"
        self.pIDName = "Ring of Clumsiness"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrDexterity(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rDexterity"
        self.pName = "Ring"
        self.pIDName = "Ring of Dexterity"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrEndurance(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rEndurance"
        self.pName = "Ring"
        self.pIDName = "Ring of Endurance"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrEternalNourishment(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rEternalNourishment"
        self.pName = "Ring"
        self.pIDName = "Ring of Eternal Nourishment"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrGender(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rGender"
        self.pName = "Ring"
        self.pIDName = "Ring of Gender"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrIntelligence(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rIntelligence"
        self.pName = "Ring"
        self.pIDName = "Ring of Intelligence"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrNakedness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rNakedness"
        self.pName = "Ring"
        self.pIDName = "Ring of Nakedness"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrRegeneration(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rRegeneration"
        self.pName = "Ring"
        self.pIDName = "Ring of Regeneration"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrStrength(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rStrength"
        self.pName = "Ring"
        self.pIDName = "Ring of Strength"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrStupidity(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rStupidity"
        self.pName = "Ring"
        self.pIDName = "Ring of Stupidity"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrUgly(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rUgly"
        self.pName = "Ring"
        self.pIDName = "Ring of Ugliness"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJrWeakness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "rWeakness"
        self.pName = "Ring"
        self.pIDName = "Ring of Weakness"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 700
        self.pMask = -1

class SOBJOrb(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Orb"
        self.pName = "Orb"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJoGlass(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oGlass"
        self.pName = "Orb"
        self.pIDName = "Glass Orb"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJoGroupTeleport(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oGroupTeleport"
        self.pName = "Orb"
        self.pIDName = "Orb of Teleportation"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 17
        self.pTheurgism = 0

class SOBJoImmolation(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oImmolation"
        self.pName = "Orb"
        self.pIDName = "Orb of Immolation"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 32
        self.pTheurgism = 0

class SOBJoWind(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oWind"
        self.pName = "Orb"
        self.pIDName = "Orb of Wind"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 31
        self.pTheurgism = 0

class SOBJoFlame(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oFlame"
        self.pName = "Orb"
        self.pIDName = "Flame Orb"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 26
        self.pTheurgism = 0

class SOBJoFumbling(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oFumbling"
        self.pName = "Orb"
        self.pIDName = "Orb of Fumbling"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJoForgetfulness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oForgetfulness"
        self.pName = "Orb"
        self.pIDName = "Orb of Forgetfulness"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 72
        self.pTheurgism = 0

class SOBJoHolding(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oHolding"
        self.pName = "Orb"
        self.pIDName = "Orb of Holding"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 52
        self.pTheurgism = 0

class SOBJoHealing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oHealing"
        self.pName = "Orb"
        self.pIDName = "Orb of Healing"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJoGreaterHealing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oGreaterHealing"
        self.pName = "Orb"
        self.pIDName = "Orb of Greater Healing"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJoExtension(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "oExtension"
        self.pName = "Orb"
        self.pIDName = "Orb of Extension"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 12
        self.pTheurgism = 0

class SOBJBook(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Book"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

class SOBJTome(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Tome"
        self.pName = "Book"
        self.pIDName = "Tome"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJtBook(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "tBook"
        self.pName = "Tome"
        self.pIDName = "Book of Tales"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJtDivineInspiration(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "tDivineInspiration"
        self.pName = "Tome"
        self.pIDName = "Tome of Divine Inspiration"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJtEvilDeeds(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "tEvilDeeds"
        self.pName = "Tome"
        self.pIDName = "Tome of Evil Deeds"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJtForgetfulness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "tForgetfulness"
        self.pName = "Tome"
        self.pIDName = "Tome of Forgetfulness"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJtGreaterWorks(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "tGreaterWorks"
        self.pName = "Tome"
        self.pIDName = "Tome of Greater Works"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJtUnderstanding(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "tUnderstanding"
        self.pName = "Tome"
        self.pIDName = "Tome of Understanding"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJSpellBook(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SpellBook"
        self.pName = "Tome"
        self.pIDName = "Tome"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 74


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

        self.bases.append("BScroll")

class SOBJElixir(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Elixir"
        self.pName = ""
        self.pIDName = "Elixir"
        self.loop = 0
        self.pBaseView = 51600
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

class SOBJeLife(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "eLife"
        self.pName = "Elixir"
        self.pIDName = "Life Elixir"
        self.loop = 0
        self.pBaseView = 51600
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

class SOBJePurify(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ePurify"
        self.pName = "Elixir"
        self.pIDName = "Purifying Elixir"
        self.loop = 0
        self.pBaseView = 51600
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

class SOBJeSpoiled(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "eSpoiled"
        self.pName = "Elixir"
        self.pIDName = "Spoiled Elixir"
        self.loop = 0
        self.pBaseView = 51600
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = -1
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

class SOBJBauble(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Bauble"
        self.pName = "Bauble"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 63
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

class SOBJbaFire(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "baFire"
        self.pName = "Bauble"
        self.pIDName = "Fire Bauble"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 26
        self.pTheurgism = 0

class SOBJbaCold(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "baCold"
        self.pName = "Bauble"
        self.pIDName = "Ice Bauble"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 28
        self.pTheurgism = 0

class SOBJbaAcid(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "baAcid"
        self.pName = "Bauble"
        self.pIDName = "Acid Bauble"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 102
        self.pTheurgism = 0

class SOBJbaLightning(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "baLightning"
        self.pName = "Bauble"
        self.pIDName = "Lightning Bauble"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 45
        self.pTheurgism = 0

class SOBJbaShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "baShield"
        self.pName = "Bauble"
        self.pIDName = "Shield Bauble"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 100
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

class SOBJbaHealth(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "baHealth"
        self.pName = "Bauble"
        self.pIDName = "Bauble of Health"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 79
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 79
        self.pTheurgism = 0

class SOBJbaExperience(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "baExperience"
        self.pName = "Bauble"
        self.pIDName = "Bauble of Experience"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 93
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

class SOBJMagicalArtifact(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicalArtifact"
        self.pName = "Magical Artifact"
        self.loop = 0
        self.pBaseView = 0
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

class SOBJMagicWand(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicWand"
        self.pName = "Magical Wand"
        self.loop = 0
        self.pBaseView = 0
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

class SOBJAmuletOfProtection(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AmuletOfProtection"
        self.pName = "Amulet of Protection"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 5
        self.pWeight = 10

        self.bases.append("BDescribed")

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJHoldingPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HoldingPants"
        self.pName = "Pants of Holding"
        self.loop = 0
        self.pBaseView = 10500
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 63
        self.pBaseBitsLo = 11
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 300

class SOBJInvisPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "InvisPants"
        self.pName = "Pants of Invisibility"
        self.loop = 0
        self.pBaseView = 10500
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 53
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

class SOBJMagicBelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicBelt"
        self.pName = "Belt of See Invisible"
        self.loop = 0
        self.pBaseView = 10200
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = 78
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 60
        self.pAreaWorn = 8
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMagicBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicBoots"
        self.pName = "Boots of Invisibility"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 100
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

class SOBJBackPackOfHolding(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BackPackOfHolding"
        self.pName = "Backpack of Holding"
        self.loop = 0
        self.pBaseView = 50200
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 63
        self.pBaseBitsLo = 11
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 100
        self.pWeight = 30

        self.bases.append("BContainer")
        self.pWeightCap = 5000
        self.pBulkCap = 600

        self.bases.append("BDescribed")

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 18
        self.pMask = -1

class SOBJHealElixir(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HealElixir"
        self.pName = "Healing Elixir"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 68
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJBigHealElixir(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BigHealElixir"
        self.pName = "Greater Healing Elixir"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 53
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJRegenElixir(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RegenElixir"
        self.pName = "Elixir of Regeneration"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 83
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJPoisonCure(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PoisonCure"
        self.pName = "Poison Cure"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 58
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJBanana12Pack(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Banana12Pack"
        self.pName = "Leather Pouch"
        self.loop = 0
        self.pBaseView = 50450
        self.pAction = 29
        self.pClutStart = 75
        self.pColor = 78
        self.pBaseBitsLo = 3
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 50
        self.pWeight = 10

        self.bases.append("BContainer")
        self.pWeightCap = 200
        self.pBulkCap = 100

        self.bases.append("BDescribed")

class SOBJBanana25Pack(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Banana25Pack"
        self.pName = "Backpack"
        self.loop = 0
        self.pBaseView = 50200
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 78
        self.pBaseBitsLo = 11
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 100
        self.pWeight = 30

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 400

        self.bases.append("BDescribed")

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 18
        self.pMask = -1

StockObjList.append(SOBJmwTiwazSword())
StockObjList.append(SOBJmwUruzDagger())
StockObjList.append(SOBJmwSpecialNullsword())
StockObjList.append(SOBJmwBerserkersAxe())
StockObjList.append(SOBJmwOrcThugClub())
StockObjList.append(SOBJmwOrcBanditSword())
StockObjList.append(SOBJmwOrcWarlordAxe())
StockObjList.append(SOBJmwOrcMagusDagger())
StockObjList.append(SOBJmwOrcScoutDagger())
StockObjList.append(SOBJmaDragonPlate())
StockObjList.append(SOBJmaInsulPlate())
StockObjList.append(SOBJmaDensePlate())
StockObjList.append(SOBJmaDenseGreaves())
StockObjList.append(SOBJmaDenseCowl())
StockObjList.append(SOBJmaDenseBoots())
StockObjList.append(SOBJmaDenseBands())
StockObjList.append(SOBJmaBracersOfDefense())
StockObjList.append(SOBJmaInvulPlate())
StockObjList.append(SOBJShield())
StockObjList.append(SOBJWoodShield())
StockObjList.append(SOBJRoundShield())
StockObjList.append(SOBJLargeShield())
StockObjList.append(SOBJKnightsShield())
StockObjList.append(SOBJWoodRoundShield())
StockObjList.append(SOBJIronRoundShield())
StockObjList.append(SOBJSteelRoundShield())
StockObjList.append(SOBJTemperedSteelRoundShield())
StockObjList.append(SOBJMythrilRoundShield())
StockObjList.append(SOBJObsidianiteRoundShield())
StockObjList.append(SOBJAdmantiumRoundShield())
StockObjList.append(SOBJWoodLargeShield())
StockObjList.append(SOBJIronLargeShield())
StockObjList.append(SOBJSteelLargeShield())
StockObjList.append(SOBJTemperedSteelLargeShield())
StockObjList.append(SOBJMythrilLargeShield())
StockObjList.append(SOBJObsidianiteLargeShield())
StockObjList.append(SOBJAdmantiumLargeShield())
StockObjList.append(SOBJNewbieSmallShield())
StockObjList.append(SOBJNewbieShield())
StockObjList.append(SOBJNewbieLargeShield())
StockObjList.append(SOBJLeftHandPowerRing())
StockObjList.append(SOBJStatue())
StockObjList.append(SOBJElphamesScales())
StockObjList.append(SOBJGem())
StockObjList.append(SOBJCrystal())
StockObjList.append(SOBJRubyChip())
StockObjList.append(SOBJAquamarine())
StockObjList.append(SOBJTurquoise())
StockObjList.append(SOBJTopaz())
StockObjList.append(SOBJEmmerald())
StockObjList.append(SOBJEmerald())
StockObjList.append(SOBJRuby())
StockObjList.append(SOBJJet())
StockObjList.append(SOBJDiamond())
StockObjList.append(SOBJTempleTrophy())
StockObjList.append(SOBJMistGem())
StockObjList.append(SOBJMistGemI())
StockObjList.append(SOBJMistGemII())
StockObjList.append(SOBJMistGemIII())
StockObjList.append(SOBJMistGemIV())
StockObjList.append(SOBJMistGemV())
StockObjList.append(SOBJMistGemVI())
StockObjList.append(SOBJMistGemVII())
StockObjList.append(SOBJMistGemVIII())
StockObjList.append(SOBJMistGemIX())
StockObjList.append(SOBJLargeAmethyst())
StockObjList.append(SOBJFlawlessAmethyst())
StockObjList.append(SOBJLargeDiamond())
StockObjList.append(SOBJFlawlessDiamond())
StockObjList.append(SOBJLargeEmerald())
StockObjList.append(SOBJFlawlessEmerald())
StockObjList.append(SOBJLargeJet())
StockObjList.append(SOBJFlawlessJet())
StockObjList.append(SOBJLargeRuby())
StockObjList.append(SOBJFlawlessRuby())
StockObjList.append(SOBJLargeSapphire())
StockObjList.append(SOBJFlawlessSapphire())
StockObjList.append(SOBJLargeTopaz())
StockObjList.append(SOBJFlawlessTopaz())
StockObjList.append(SOBJNPC())
StockObjList.append(SOBJStrongBox())
StockObjList.append(SOBJDoor())
StockObjList.append(SOBJPWDoor())
StockObjList.append(SOBJPlankDoor())
StockObjList.append(SOBJSimpleDoor())
StockObjList.append(SOBJDoorway())
StockObjList.append(SOBJRuinDoorA())
StockObjList.append(SOBJRuinDoorB())
StockObjList.append(SOBJGlowingPortal())
StockObjList.append(SOBJChair())
StockObjList.append(SOBJStool())
StockObjList.append(SOBJBed())
StockObjList.append(SOBJFirePlace())
StockObjList.append(SOBJBaldric())
StockObjList.append(SOBJOliveBaldric())
StockObjList.append(SOBJBlueBaldric())
StockObjList.append(SOBJAzureBaldric())
StockObjList.append(SOBJRedBaldric())
StockObjList.append(SOBJPinkBaldric())
StockObjList.append(SOBJGoldBaldric())
StockObjList.append(SOBJYellowBaldric())
StockObjList.append(SOBJVioletBaldric())
StockObjList.append(SOBJMagentaBaldric())
StockObjList.append(SOBJBrownBaldric())
StockObjList.append(SOBJTanBaldric())
StockObjList.append(SOBJAquaBaldric())
StockObjList.append(SOBJTealBaldric())
StockObjList.append(SOBJJadeBaldric())
StockObjList.append(SOBJAmberBaldric())
StockObjList.append(SOBJRoyalBaldric())
StockObjList.append(SOBJPurpleBaldric())
StockObjList.append(SOBJRealPurpleBaldric())
StockObjList.append(SOBJWhiteBaldric())
StockObjList.append(SOBJBlackBaldric())
StockObjList.append(SOBJRealBlackBaldric())
StockObjList.append(SOBJGrayBaldric())
StockObjList.append(SOBJGreenBaldric())
StockObjList.append(SOBJSatoriBaldric())
StockObjList.append(SOBJThistlebark())
StockObjList.append(SOBJThistlebarkA())
StockObjList.append(SOBJThistlebarkB())
StockObjList.append(SOBJPumpkinBaldric())
StockObjList.append(SOBJCrestedBaldric())
StockObjList.append(SOBJAmulet())
StockObjList.append(SOBJaConcentration())
StockObjList.append(SOBJaChoking())
StockObjList.append(SOBJaClumsiness())
StockObjList.append(SOBJaColdProtection())
StockObjList.append(SOBJaCombat())
StockObjList.append(SOBJaDexterity())
StockObjList.append(SOBJaDodging())
StockObjList.append(SOBJaEndurance())
StockObjList.append(SOBJaFireProtection())
StockObjList.append(SOBJaMemory())
StockObjList.append(SOBJaGrounding())
StockObjList.append(SOBJaIntelligence())
StockObjList.append(SOBJaRetention())
StockObjList.append(SOBJaShielding())
StockObjList.append(SOBJaStrength())
StockObjList.append(SOBJaStupidity())
StockObjList.append(SOBJaVulnerability())
StockObjList.append(SOBJaWeakness())
StockObjList.append(SOBJaWeatherproofing())
StockObjList.append(SOBJaFreeWill())
StockObjList.append(SOBJaDeathProtection())
StockObjList.append(SOBJWand())
StockObjList.append(SOBJwStick())
StockObjList.append(SOBJwBerserk())
StockObjList.append(SOBJwFireballs())
StockObjList.append(SOBJwFreezingWind())
StockObjList.append(SOBJwLightning())
StockObjList.append(SOBJwNakedness())
StockObjList.append(SOBJwPoisonBolts())
StockObjList.append(SOBJwRust())
StockObjList.append(SOBJwStoning())
StockObjList.append(SOBJwUgly())
StockObjList.append(SOBJPotion())
StockObjList.append(SOBJpWater())
StockObjList.append(SOBJpSwampWater())
StockObjList.append(SOBJpClumsiness())
StockObjList.append(SOBJpCurePoison())
StockObjList.append(SOBJpDexterity())
StockObjList.append(SOBJpGreaterHealth())
StockObjList.append(SOBJpHealth())
StockObjList.append(SOBJpInvisibility())
StockObjList.append(SOBJpPain())
StockObjList.append(SOBJpPoison())
StockObjList.append(SOBJpRegeneration())
StockObjList.append(SOBJpSeeInvisibility())
StockObjList.append(SOBJpStrength())
StockObjList.append(SOBJpWeakness())
StockObjList.append(SOBJpAcidShield())
StockObjList.append(SOBJpColdShield())
StockObjList.append(SOBJpPoisonShield())
StockObjList.append(SOBJpLightningShield())
StockObjList.append(SOBJpFireShield())
StockObjList.append(SOBJpAcidCurse())
StockObjList.append(SOBJpColdCurse())
StockObjList.append(SOBJpPoisonCurse())
StockObjList.append(SOBJpLightningCurse())
StockObjList.append(SOBJpFireCurse())
StockObjList.append(SOBJpInvulnerability())
StockObjList.append(SOBJpShift())
StockObjList.append(SOBJpGreaterInvisibility())
StockObjList.append(SOBJpDeath())
StockObjList.append(SOBJRing())
StockObjList.append(SOBJrCopper())
StockObjList.append(SOBJrEngagement())
StockObjList.append(SOBJrWedding())
StockObjList.append(SOBJrWedding2())
StockObjList.append(SOBJrWedding3())
StockObjList.append(SOBJrClumsiness())
StockObjList.append(SOBJrDexterity())
StockObjList.append(SOBJrEndurance())
StockObjList.append(SOBJrEternalNourishment())
StockObjList.append(SOBJrGender())
StockObjList.append(SOBJrIntelligence())
StockObjList.append(SOBJrNakedness())
StockObjList.append(SOBJrRegeneration())
StockObjList.append(SOBJrStrength())
StockObjList.append(SOBJrStupidity())
StockObjList.append(SOBJrUgly())
StockObjList.append(SOBJrWeakness())
StockObjList.append(SOBJOrb())
StockObjList.append(SOBJoGlass())
StockObjList.append(SOBJoGroupTeleport())
StockObjList.append(SOBJoImmolation())
StockObjList.append(SOBJoWind())
StockObjList.append(SOBJoFlame())
StockObjList.append(SOBJoFumbling())
StockObjList.append(SOBJoForgetfulness())
StockObjList.append(SOBJoHolding())
StockObjList.append(SOBJoHealing())
StockObjList.append(SOBJoGreaterHealing())
StockObjList.append(SOBJoExtension())
StockObjList.append(SOBJBook())
StockObjList.append(SOBJTome())
StockObjList.append(SOBJtBook())
StockObjList.append(SOBJtDivineInspiration())
StockObjList.append(SOBJtEvilDeeds())
StockObjList.append(SOBJtForgetfulness())
StockObjList.append(SOBJtGreaterWorks())
StockObjList.append(SOBJtUnderstanding())
StockObjList.append(SOBJSpellBook())
StockObjList.append(SOBJElixir())
StockObjList.append(SOBJeLife())
StockObjList.append(SOBJePurify())
StockObjList.append(SOBJeSpoiled())
StockObjList.append(SOBJBauble())
StockObjList.append(SOBJbaFire())
StockObjList.append(SOBJbaCold())
StockObjList.append(SOBJbaAcid())
StockObjList.append(SOBJbaLightning())
StockObjList.append(SOBJbaShield())
StockObjList.append(SOBJbaHealth())
StockObjList.append(SOBJbaExperience())
StockObjList.append(SOBJMagicalArtifact())
StockObjList.append(SOBJMagicWand())
StockObjList.append(SOBJAmuletOfProtection())
StockObjList.append(SOBJHoldingPants())
StockObjList.append(SOBJInvisPants())
StockObjList.append(SOBJMagicBelt())
StockObjList.append(SOBJMagicBoots())
StockObjList.append(SOBJBackPackOfHolding())
StockObjList.append(SOBJHealElixir())
StockObjList.append(SOBJBigHealElixir())
StockObjList.append(SOBJRegenElixir())
StockObjList.append(SOBJPoisonCure())
StockObjList.append(SOBJBanana12Pack())
StockObjList.append(SOBJBanana25Pack())
