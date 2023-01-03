from stock_objects import StockObjList,StockObject
global StockObjList





class SOBJPlayer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Player"
        self.pName = ""
        self.loop = 0
        self.pBaseView = 0
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 0


class SOBJCombatCloud(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "CombatCloud"
        self.pName = "Combat Cloud"
        self.loop = 0
        self.pBaseView = 8037
        self.pAction = 0
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64
        self.pPolygon = -1


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJMoneyBag(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MoneyBag"
        self.pName = "Coin Purse"
        self.loop = 0
        self.pBaseView = 50500
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 0

class SOBJManaBag(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ManaBag"
        self.pName = "Mana Crystals"
        self.loop = 0
        self.pBaseView = 50600
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 0

class SOBJHead(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Head"
        self.pName = ""
        self.loop = 0
        self.pBaseView = 4000
        self.pAction = 0
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 5
        self.pBaseBitsHi = 0


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 0

        self.bases.append("BHead")

class SOBJCharacter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Character"
        self.pName = ""
        self.loop = 0
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJMaleCharacter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MaleCharacter"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJMaleAdventurer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MaleAdventurer"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJMaleWarrior(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MaleWarrior"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJMaleWizard(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MaleWizard"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJMaleThief(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MaleThief"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJFemaleCharacter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FemaleCharacter"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 17


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJFemaleAdventurer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FemaleAdventurer"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 17


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJFemaleWarrior(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FemaleWarrior"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 17


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJFemaleWizard(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FemaleWizard"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 17


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJFemaleThief(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FemaleThief"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 17


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJMaleCleric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MaleCleric"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJFemaleCleric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FemaleCleric"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 17


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJMaleMonk(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MaleMonk"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJFemaleMonk(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FemaleMonk"
        self.pName = "<bad engrave>"
        self.loop = 0
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 106
        self.pBaseBitsLo = 66
        self.pBaseBitsHi = 0
        self.pSoundGroup = 17


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

class SOBJChest(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Chest"
        self.pName = "Chest"
        self.loop = 0
        self.pBaseView = 50000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 18
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 12500
        self.pBulkCap = 5000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

class SOBJLockedChest(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LockedChest"
        self.pName = "Chest"
        self.loop = 0
        self.pBaseView = 50000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 146
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 12500
        self.pBulkCap = 5000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

        self.bases.append("BLockable")
        self.pAutoLock = 0
        self.pLockValue = 0
        self.pUnlockValue = 0
        self.pSkeletonLock = 1
        self.pSkeletonUnlock = 1
        self.pLocked = 0

class SOBJKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Key"
        self.pName = "Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 0
        self.pUnlockValue = 0
        self.pSkeletonLock = 0
        self.pSkeletonUnlock = 0

        self.bases.append("BDescribed")

class SOBJSign(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Sign"
        self.pName = "Sign"
        self.loop = 0
        self.pBaseView = 54350
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

class SOBJHut(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Hut"
        self.pName = "Tent"
        self.loop = 0
        self.pBaseView = 54850
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1024
        self.pBaseBitsHi = 64


        self.bases.append("BEntry")

        self.bases.append("BDescribed")

class SOBJStand(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Stand"
        self.pName = "Stand"
        self.loop = 0
        self.pBaseView = 54900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

class SOBJFountain(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Fountain"
        self.pName = "Fountain"
        self.loop = 0
        self.pBaseView = 54750
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

        self.bases.append("BDescribed")

class SOBJFountainA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FountainA"
        self.pName = "Fountain"
        self.loop = 0
        self.pBaseView = 54750
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 0


        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJGargoyleFountain(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GargoyleFountain"
        self.pName = "Gargoyle Fountain"
        self.loop = 0
        self.pBaseView = 62350
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJLadder(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Ladder"
        self.pName = "Ladder"
        self.loop = 0
        self.pBaseView = 39000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1024
        self.pBaseBitsHi = 64


        self.bases.append("BEntry")

        self.bases.append("BDescribed")

class SOBJSkullChest(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SkullChest"
        self.pName = "Skull Chest"
        self.loop = 0
        self.pBaseView = 55535
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 18
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 25000
        self.pBulkCap = 10000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

class SOBJSittingStump(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SittingStump"
        self.pName = "Sitting Stump"
        self.loop = 0
        self.pBaseView = 56250
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 65


        self.bases.append("BSit")

        self.bases.append("BDescribed")

class SOBJSittingRock(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SittingRock"
        self.pName = "Sitting Rock"
        self.loop = 0
        self.pBaseView = 56200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 65


        self.bases.append("BSit")

        self.bases.append("BDescribed")

class SOBJLockedChestIron(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LockedChestIron"
        self.pName = "Chest"
        self.loop = 0
        self.pBaseView = 50000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 146
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 12500
        self.pBulkCap = 5000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

        self.bases.append("BLockable")
        self.pAutoLock = 0
        self.pLockValue = 4
        self.pUnlockValue = 4
        self.pSkeletonLock = 1
        self.pSkeletonUnlock = 1
        self.pLocked = 1

class SOBJLockedChestSteel(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LockedChestSteel"
        self.pName = "Chest"
        self.loop = 0
        self.pBaseView = 50000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 146
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 12500
        self.pBulkCap = 5000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

        self.bases.append("BLockable")
        self.pAutoLock = 0
        self.pLockValue = 6
        self.pUnlockValue = 6
        self.pSkeletonLock = 1
        self.pSkeletonUnlock = 1
        self.pLocked = 1

class SOBJLockedChestBrass(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LockedChestBrass"
        self.pName = "Chest"
        self.loop = 0
        self.pBaseView = 50000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 146
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 12500
        self.pBulkCap = 5000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

        self.bases.append("BLockable")
        self.pAutoLock = 0
        self.pLockValue = 8
        self.pUnlockValue = 8
        self.pSkeletonLock = 1
        self.pSkeletonUnlock = 1
        self.pLocked = 1

class SOBJLockedChestBronze(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LockedChestBronze"
        self.pName = "Chest"
        self.loop = 0
        self.pBaseView = 50000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 146
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 12500
        self.pBulkCap = 5000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

        self.bases.append("BLockable")
        self.pAutoLock = 0
        self.pLockValue = 10
        self.pUnlockValue = 10
        self.pSkeletonLock = 1
        self.pSkeletonUnlock = 1
        self.pLocked = 1

class SOBJLockedChestJeweled(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LockedChestJeweled"
        self.pName = "Chest"
        self.loop = 0
        self.pBaseView = 50000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 146
        self.pBaseBitsHi = 64


        self.bases.append("BContainer")
        self.pWeightCap = 12500
        self.pBulkCap = 5000

        self.bases.append("BOpenable")

        self.bases.append("BDescribed")

        self.bases.append("BLockable")
        self.pAutoLock = 0
        self.pLockValue = 50
        self.pUnlockValue = 50
        self.pSkeletonLock = 1
        self.pSkeletonUnlock = 1
        self.pLocked = 1

class SOBJIronKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronKey"
        self.pName = "Iron Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 2
        self.pUnlockValue = 2
        self.pSkeletonLock = 0
        self.pSkeletonUnlock = 0

        self.bases.append("BDescribed")

class SOBJSteelKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelKey"
        self.pName = "Steel Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 12
        self.pUnlockValue = 12
        self.pSkeletonLock = 0
        self.pSkeletonUnlock = 0

        self.bases.append("BDescribed")

class SOBJBronzeKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BronzeKey"
        self.pName = "Bronze Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 22
        self.pUnlockValue = 22
        self.pSkeletonLock = 0
        self.pSkeletonUnlock = 0

        self.bases.append("BDescribed")

class SOBJBrassKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BrassKey"
        self.pName = "Brass Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 32
        self.pUnlockValue = 32
        self.pSkeletonLock = 0
        self.pSkeletonUnlock = 0

        self.bases.append("BDescribed")

class SOBJJeweledKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JeweledKey"
        self.pName = "Jeweled Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 50
        self.pUnlockValue = 50
        self.pSkeletonLock = 0
        self.pSkeletonUnlock = 0

        self.bases.append("BDescribed")

class SOBJRustySkeletonKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RustySkeletonKey"
        self.pName = "Rusty Skeleton Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 0
        self.pUnlockValue = 0
        self.pSkeletonLock = 32
        self.pSkeletonUnlock = 32

        self.bases.append("BDescribed")

class SOBJSilverSkeletonKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SilverSkeletonKey"
        self.pName = "Silver Skeleton Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 0
        self.pUnlockValue = 0
        self.pSkeletonLock = 49
        self.pSkeletonUnlock = 49

        self.bases.append("BDescribed")

class SOBJGoldSkeletonKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GoldSkeletonKey"
        self.pName = "Gold Skeleton Key"
        self.loop = 0
        self.pBaseView = 54450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 0
        self.pUnlockValue = 0
        self.pSkeletonLock = 255
        self.pSkeletonUnlock = 255

        self.bases.append("BDescribed")

class SOBJLockpick(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Lockpick"
        self.pName = "Lockpicks"
        self.loop = 0
        self.pBaseView = 52550
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 0
        self.pUnlockValue = 0
        self.pSkeletonLock = 0
        self.pSkeletonUnlock = 0

        self.bases.append("BDescribed")

class SOBJFood(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Food"
        self.pName = ""
        self.loop = 0
        self.pBaseView = 0
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8192
        self.pBaseBitsHi = 0


        self.bases.append("BConsume")

class SOBJDrink(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Drink"
        self.pName = ""
        self.loop = 0
        self.pBaseView = 0
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8192
        self.pBaseBitsHi = 0


        self.bases.append("BConsume")

class SOBJBread(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Bread"
        self.pName = "Loaf of Bread"
        self.loop = 0
        self.pBaseView = 52050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJVeggies(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Veggies"
        self.pName = "Vegetables"
        self.loop = 0
        self.pBaseView = 52100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJMeat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Meat"
        self.pName = "Meat"
        self.loop = 0
        self.pBaseView = 52000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJRatlingMeat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RatlingMeat"
        self.pName = "Ratling Meat"
        self.loop = 0
        self.pBaseView = 52000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJCheese(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Cheese"
        self.pName = "Cheese"
        self.loop = 0
        self.pBaseView = 52150
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJRatlingCheese(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RatlingCheese"
        self.pName = "Ratling Cheese"
        self.loop = 0
        self.pBaseView = 52150
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJWaterBottle(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WaterBottle"
        self.pName = "Bottle of Water"
        self.loop = 0
        self.pBaseView = 52200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJWineFlask(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WineFlask"
        self.pName = "Flask of Wine"
        self.loop = 0
        self.pBaseView = 50300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJAleJug(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AleJug"
        self.pName = "Jug Of Ale"
        self.loop = 0
        self.pBaseView = 52250
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 4
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJAmbrosia(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Ambrosia"
        self.pName = "Ambrosia"
        self.loop = 0
        self.pBaseView = 52300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 2
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJRawMeat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RawMeat"
        self.pName = "Ratling Raw Meat"
        self.loop = 0
        self.pBaseView = 52000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 8
        self.pWeight = 16

        self.bases.append("BDescribed")

class SOBJArcticRatMeat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ArcticRatMeat"
        self.pName = "Arctic Ratling Meat"
        self.loop = 0
        self.pBaseView = 52000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 8
        self.pWeight = 16

        self.bases.append("BDescribed")

class SOBJWharfRatMeat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WharfRatMeat"
        self.pName = "Wharf Ratling Meat"
        self.loop = 0
        self.pBaseView = 52000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 8
        self.pWeight = 16

        self.bases.append("BDescribed")

class SOBJFlameRatMeat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlameRatMeat"
        self.pName = "Flame Ratling Meat"
        self.loop = 0
        self.pBaseView = 52000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 8
        self.pWeight = 16

        self.bases.append("BDescribed")

class SOBJDemonRatMeat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DemonRatMeat"
        self.pName = "Demon Ratling Meat"
        self.loop = 0
        self.pBaseView = 52000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 8193
        self.pBaseBitsHi = 64


        self.bases.append("BConsume")

        self.bases.append("BCarryable")
        self.pBulk = 8
        self.pWeight = 16

        self.bases.append("BDescribed")

class SOBJBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Bar"
        self.pName = ""
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 0


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

class SOBJBolt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Bolt"
        self.pName = ""
        self.loop = 0
        self.pBaseView = 58200
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 0


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

class SOBJWoodBlock(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WoodBlock"
        self.pName = "Wooden Block"
        self.loop = 0
        self.pBaseView = 58150
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 105
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

class SOBJIronBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronBar"
        self.pName = "Iron Bar"
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 104
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

class SOBJSteelBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelBar"
        self.pName = "Steel Bar"
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 99
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

class SOBJTemperedSteelBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelBar"
        self.pName = "Carbon-Steel Bar"
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

class SOBJMythrilBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilBar"
        self.pName = "Mythril Bar"
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

class SOBJObsidianiteBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteBar"
        self.pName = "Obsidianite Block"
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

class SOBJAdmantiumBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumBar"
        self.pName = "Admantium Block"
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BDescribed")

class SOBJClothBolt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ClothBolt"
        self.pName = "Bolt of Fabric"
        self.loop = 0
        self.pBaseView = 58200
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BDescribed")

class SOBJLeatherBolt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherBolt"
        self.pName = "Bolt of Leather"
        self.loop = 0
        self.pBaseView = 58200
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 74
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BDescribed")

class SOBJTrollHideBolt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollHideBolt"
        self.pName = "Bolt of Troll Hide"
        self.loop = 0
        self.pBaseView = 58200
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 73
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BDescribed")

class SOBJSweatBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SweatBar"
        self.pName = "Block of Sweat Time"
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 200

        self.bases.append("BDescribed")

class SOBJMagicBar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicBar"
        self.pName = "Bar of Magical Energy"
        self.loop = 0
        self.pBaseView = 58250
        self.pAction = 29
        self.pClutStart = 98
        self.pColor = 30
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BDescribed")

class SOBJTent(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Tent"
        self.pName = "Tent"
        self.loop = 0
        self.pBaseView = 54850
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1024
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BEntry")

class SOBJBackPack(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BackPack"
        self.pName = "Backpack"
        self.loop = 0
        self.pBaseView = 50200
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 74
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

class SOBJRoyalPack(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RoyalPack"
        self.pName = "Backpack"
        self.loop = 0
        self.pBaseView = 50200
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 93
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

class SOBJBlackPack(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BlackPack"
        self.pName = "Backpack"
        self.loop = 0
        self.pBaseView = 50200
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 98
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

class SOBJTealPack(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TealPack"
        self.pName = "Backpack"
        self.loop = 0
        self.pBaseView = 50200
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 79
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

class SOBJLeatherPouch(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LeatherPouch"
        self.pName = "Leather Pouch"
        self.loop = 0
        self.pBaseView = 50450
        self.pAction = 29
        self.pClutStart = 75
        self.pColor = 75
        self.pBaseBitsLo = 3
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 50
        self.pWeight = 10

        self.bases.append("BContainer")
        self.pWeightCap = 200
        self.pBulkCap = 100

        self.bases.append("BDescribed")

class SOBJMirror(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Mirror"
        self.pName = "Mirror"
        self.loop = 0
        self.pBaseView = 52600
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJBowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Bowl"
        self.pName = "Bowl"
        self.loop = 0
        self.pBaseView = 52800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJBlackRose(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BlackRose"
        self.pName = "Black Rose"
        self.loop = 0
        self.pBaseView = 54500
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJRedRose(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RedRose"
        self.pName = "Red Rose"
        self.loop = 0
        self.pBaseView = 54550
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJWhiteRose(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WhiteRose"
        self.pName = "White Rose"
        self.loop = 0
        self.pBaseView = 53050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJBlueRose(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BlueRose"
        self.pName = "Blue Rose"
        self.loop = 0
        self.pBaseView = 53000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJYellowRose(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "YellowRose"
        self.pName = "Yellow Rose"
        self.loop = 0
        self.pBaseView = 54100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJPinkRose(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PinkRose"
        self.pName = "Pink Rose"
        self.loop = 0
        self.pBaseView = 54150
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJGreenRose(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GreenRose"
        self.pName = "Green Rose"
        self.loop = 0
        self.pBaseView = 53000
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 85
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJChrysanthenum(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Chrysanthenum"
        self.pName = "Chrysanthemum"
        self.loop = 0
        self.pBaseView = 53150
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJDaisy(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Daisy"
        self.pName = "Daisy"
        self.loop = 0
        self.pBaseView = 53100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJDrum(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Drum"
        self.pName = "Drum"
        self.loop = 0
        self.pBaseView = 53950
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 11

        self.bases.append("BDescribed")

class SOBJFlute(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Flute"
        self.pName = "Flute"
        self.loop = 0
        self.pBaseView = 53900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 11

        self.bases.append("BDescribed")

class SOBJStrynx(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Strynx"
        self.pName = "Strynx"
        self.loop = 1
        self.pBaseView = 54000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 16

        self.bases.append("BDescribed")

class SOBJLyre(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Lyre"
        self.pName = "Lyre"
        self.loop = 0
        self.pBaseView = 54050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 64

        self.bases.append("BDescribed")

class SOBJLute(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Lute"
        self.pName = "Lute"
        self.loop = 0
        self.pBaseView = 54600
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 16

        self.bases.append("BDescribed")

class SOBJAnimalHide(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AnimalHide"
        self.pName = "Animal Hide"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 73
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJWolfPelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WolfPelt"
        self.pName = "Wolf Pelt"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJWhiteWolfPelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WhiteWolfPelt"
        self.pName = "Wolf Pelt"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJFenrisPelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FenrisPelt"
        self.pName = "Fenris Pelt"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJBloodFenrisPelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BloodFenrisPelt"
        self.pName = "Blood Fenris Pelt"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJHellHoundPelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HellHoundPelt"
        self.pName = "Hell Hound Pelt"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 59
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJHowlingTerrorPelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HowlingTerrorPelt"
        self.pName = "Howling Terror Pelt"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJTrollHide(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollHide"
        self.pName = "Troll Hide"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 88
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJRockTrollHide(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RockTrollHide"
        self.pName = "Rock Troll Hide"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 74
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJDemonTrollHide(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DemonTrollHide"
        self.pName = "Demon Troll Hide"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJDireWolfPelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DireWolfPelt"
        self.pName = "Dire Wolf Pelt"
        self.loop = 0
        self.pBaseView = 50900
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 115
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJPlate(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Plate"
        self.pName = "Plate"
        self.loop = 0
        self.pBaseView = 52750
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJCandle(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Candle"
        self.pName = "Candle"
        self.loop = 0
        self.pBaseView = 52650
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJHammer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Hammer"
        self.pName = "Hammer"
        self.loop = 0
        self.pBaseView = 52700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 13

        self.bases.append("BDescribed")

class SOBJCarving(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Carving"
        self.pName = "Carving"
        self.loop = 0
        self.pBaseView = 50250
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 13

        self.bases.append("BDescribed")

class SOBJMug(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Mug"
        self.pName = "Mug"
        self.loop = 0
        self.pBaseView = 50350
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJChalice(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Chalice"
        self.pName = "Chalice"
        self.loop = 0
        self.pBaseView = 50250
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 11

        self.bases.append("BDescribed")

class SOBJSpring(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Spring"
        self.pName = "Spring"
        self.loop = 0
        self.pBaseView = 62600
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 0
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

class SOBJHollowTree(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HollowTree"
        self.pName = "Hollow Tree"
        self.loop = 0
        self.pBaseView = 61450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1040
        self.pBaseBitsHi = 64


        self.bases.append("BOpenable")

        self.bases.append("BEntry")

        self.bases.append("BDescribed")

class SOBJFireA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FireA"
        self.pName = "Fire"
        self.loop = 0
        self.pBaseView = 60600
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJFire1(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Fire1"
        self.pName = "Fire"
        self.loop = 0
        self.pBaseView = 60600
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJFireB(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FireB"
        self.pName = "Fire"
        self.loop = 0
        self.pBaseView = 60650
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJFire2(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Fire2"
        self.pName = "Fire"
        self.loop = 0
        self.pBaseView = 60650
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJEmbers(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Embers"
        self.pName = "Embers"
        self.loop = 0
        self.pBaseView = 60750
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJSmokeA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SmokeA"
        self.pName = "Smoke"
        self.loop = 0
        self.pBaseView = 60800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64
        self.pPolygon = -1


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJSmoke1(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Smoke1"
        self.pName = "Smoke"
        self.loop = 0
        self.pBaseView = 60800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJSmokeB(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SmokeB"
        self.pName = "Smoke"
        self.loop = 0
        self.pBaseView = 60850
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64
        self.pPolygon = -1


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJSmoke2(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Smoke2"
        self.pName = "Smoke"
        self.loop = 0
        self.pBaseView = 60850
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJSmokeC(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SmokeC"
        self.pName = "Smoke"
        self.loop = 0
        self.pBaseView = 60900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64
        self.pPolygon = -1


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJSmoke3(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Smoke3"
        self.pName = "Smoke"
        self.loop = 0
        self.pBaseView = 60900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJFireC(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FireC"
        self.pName = "Fire"
        self.loop = 0
        self.pBaseView = 60700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJFire3(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Fire3"
        self.pName = "Fire"
        self.loop = 0
        self.pBaseView = 60700
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 32
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJSpellComponent(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SpellComponent"
        self.pName = "Spell Component"
        self.loop = 0
        self.pBaseView = 57800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJTooth(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Tooth"
        self.pName = "Tooth"
        self.loop = 0
        self.pBaseView = 57800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJDaemonTooth(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DaemonTooth"
        self.pName = "Daemon Tooth"
        self.loop = 0
        self.pBaseView = 57800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 8

        self.bases.append("BDescribed")

class SOBJFinger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Finger"
        self.pName = "Finger"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJZombieFinger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ZombieFinger"
        self.pName = "Zombie Finger"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJNugget(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Nugget"
        self.pName = "Nugget"
        self.loop = 0
        self.pBaseView = 50950
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJGoldNugget(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GoldNugget"
        self.pName = "Gold Nugget"
        self.loop = 0
        self.pBaseView = 50950
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJGuano(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Guano"
        self.pName = "Ball of Guano"
        self.loop = 0
        self.pBaseView = 57750
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 73
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJImpGuano(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ImpGuano"
        self.pName = "Imp Guano"
        self.loop = 0
        self.pBaseView = 57750
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJRatGuano(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RatGuano"
        self.pName = "Rat Guano"
        self.loop = 0
        self.pBaseView = 57750
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJDaemonGuano(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DaemonGuano"
        self.pName = "Daemon Guano"
        self.loop = 0
        self.pBaseView = 57750
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 107
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJDaveGuano(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DaveGuano"
        self.pName = "Dave's Guano"
        self.loop = 0
        self.pBaseView = 57760
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJJawBone(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JawBone"
        self.pName = "Jaw Bone"
        self.loop = 0
        self.pBaseView = 57900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJEyeball(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Eyeball"
        self.pName = "Eye"
        self.loop = 0
        self.pBaseView = 57950
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJKilrogEyeball(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "KilrogEyeball"
        self.pName = "Eye of Kilrog"
        self.loop = 0
        self.pBaseView = 57950
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJOgreEyeball(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OgreEyeball"
        self.pName = "Ogre Eye"
        self.loop = 0
        self.pBaseView = 57950
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJRock(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Rock"
        self.pName = "Pebble"
        self.loop = 0
        self.pBaseView = 58000
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 48
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJLeaf(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Leaf"
        self.pName = "Oak Leaf"
        self.loop = 0
        self.pBaseView = 58050
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJClump(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Clump"
        self.pName = "Clump of Grass"
        self.loop = 0
        self.pBaseView = 58100
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJAmberRod(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AmberRod"
        self.pName = "Amber Rod"
        self.loop = 0
        self.pBaseView = 51400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BDescribed")

class SOBJObsidianDust(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianDust"
        self.pName = "Bag of Obsidian Dust"
        self.loop = 0
        self.pBaseView = 50450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJSilvergrass(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Silvergrass"
        self.pName = "Silvergrass"
        self.loop = 0
        self.pBaseView = 58100
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJGoldenberries(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Goldenberries"
        self.pName = "Goldenberries"
        self.loop = 0
        self.pBaseView = 58100
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJPigweed(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Pigweed"
        self.pName = "Pigweed"
        self.loop = 0
        self.pBaseView = 58100
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 106
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJDevilweed(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Devilweed"
        self.pName = "Devilweed"
        self.loop = 0
        self.pBaseView = 58100
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJCorbalite(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Corbalite"
        self.pName = "Corbalite Rock"
        self.loop = 0
        self.pBaseView = 58000
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 53
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJBasalt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Basalt"
        self.pName = "Basalt Rock"
        self.loop = 0
        self.pBaseView = 58000
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJSulfur(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Sulfur"
        self.pName = "Sulfur Rock"
        self.loop = 0
        self.pBaseView = 58000
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJMarble(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Marble"
        self.pName = "Chip of Marble"
        self.loop = 0
        self.pBaseView = 58000
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJElderOak(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ElderOak"
        self.pName = "Elder Oak Leaf"
        self.loop = 0
        self.pBaseView = 58050
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJSilverthorn(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Silverthorn"
        self.pName = "Silverthorn Leaf"
        self.loop = 0
        self.pBaseView = 58050
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJTobac(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Tobac"
        self.pName = "Tobac Leaf"
        self.loop = 0
        self.pBaseView = 58050
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 104
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJPerfectRose(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PerfectRose"
        self.pName = "Perfect Rose"
        self.loop = 0
        self.pBaseView = 54550
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 99
        self.pTheurgism = 0

class SOBJDespothesScepter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DespothesScepter"
        self.pName = "Despothes' Scepter"
        self.loop = 0
        self.pBaseView = 57000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 51
        self.pTheurgism = 0

class SOBJDuachsCrystal(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DuachsCrystal"
        self.pName = "Duach's Crystal"
        self.loop = 0
        self.pBaseView = 57100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 125
        self.pTheurgism = 0

class SOBJDuachsCrystalGreen(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DuachsCrystalGreen"
        self.pName = "Duach's Green Crystal"
        self.loop = 0
        self.pBaseView = 57200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 33
        self.pBaseBitsHi = 72


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 125
        self.pTheurgism = 0

        self.bases.append("BCycle")
        self.pCycleSpeed = 6
        self.pCycleType = 0

class SOBJMabonsStaff(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MabonsStaff"
        self.pName = "Mabon's Staff"
        self.loop = 0
        self.pBaseView = 57400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = 71
        self.pTheurgism = 0

class SOBJClothing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Clothing"
        self.pName = "Clothing"
        self.loop = 0
        self.pBaseView = 0
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Helmet"
        self.pName = "Clothing"
        self.pIDName = "Helmet"
        self.loop = 0
        self.pBaseView = 30100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIronHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronHelmet"
        self.pName = "Helmet"
        self.pIDName = "Iron Helmet"
        self.loop = 0
        self.pBaseView = 30100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSteelHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelHelmet"
        self.pName = "Helmet"
        self.pIDName = "Steel Helmet"
        self.loop = 0
        self.pBaseView = 30100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJTemperedSteelHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelHelmet"
        self.pName = "Helmet"
        self.pIDName = "Tempered Steel Helmet"
        self.loop = 0
        self.pBaseView = 30100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 55

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMythrilHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilHelmet"
        self.pName = "Helmet"
        self.pIDName = "Mythril Helmet"
        self.loop = 0
        self.pBaseView = 30100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJObsidianiteHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteHelmet"
        self.pName = "Helmet"
        self.pIDName = "Obsidianite Helmet"
        self.loop = 0
        self.pBaseView = 30100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 75

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAdmantiumHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumHelmet"
        self.pName = "Helmet"
        self.pIDName = "Admantium Helmet"
        self.loop = 0
        self.pBaseView = 30100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJWizardCap(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WizardCap"
        self.pName = "Clothing"
        self.pIDName = "Wizard Hat"
        self.loop = 0
        self.pBaseView = 35100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIronLegionHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronLegionHelmet"
        self.pName = "Iron Helmet"
        self.pIDName = "Iron Legion Helmet"
        self.loop = 0
        self.pBaseView = 30800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJIronMinervaHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IronMinervaHelmet"
        self.pName = "Iron Helmet"
        self.pIDName = "Iron Minerva Helmet"
        self.loop = 0
        self.pBaseView = 31200
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 104
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJSteelLegionHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelLegionHelmet"
        self.pName = "Steel Helmet"
        self.pIDName = "Steel Legion Helmet"
        self.loop = 0
        self.pBaseView = 30800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJSteelMinervaHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SteelMinervaHelmet"
        self.pName = "Steel Helmet"
        self.pIDName = "Steel Minerva Helmet"
        self.loop = 0
        self.pBaseView = 31200
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJTemperedSteelLegionHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelLegionHelmet"
        self.pName = "Tempered Steel Helmet"
        self.pIDName = "Tempered Steel Legion Helmet"
        self.loop = 0
        self.pBaseView = 30800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 55

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJTemperedSteelMinervaHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TemperedSteelMinervaHelmet"
        self.pName = "Tempered Steel Helmet"
        self.pIDName = "Tempered Steel Minerva Helmet"
        self.loop = 0
        self.pBaseView = 31200
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 55

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJMythrilLegionHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilLegionHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Mythril Legion Helmet"
        self.loop = 0
        self.pBaseView = 30800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJMythrilMinervaHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MythrilMinervaHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Mythril Minerva Helmet"
        self.loop = 0
        self.pBaseView = 31200
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 83
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJObsidianiteLegionHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteLegionHelmet"
        self.pName = "Obsidianite Helmet"
        self.pIDName = "Obsidianite Legion Helmet"
        self.loop = 0
        self.pBaseView = 30800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 75

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJObsidianiteMinervaHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ObsidianiteMinervaHelmet"
        self.pName = "Obsidianite Helmet"
        self.pIDName = "Obsidianite Minerva Helmet"
        self.loop = 0
        self.pBaseView = 31200
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 75

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJAdmantiumLegionHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumLegionHelmet"
        self.pName = "Admantium Helmet"
        self.pIDName = "Admantium Legion Helmet"
        self.loop = 0
        self.pBaseView = 30800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJAdmantiumMinervaHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdmantiumMinervaHelmet"
        self.pName = "Admantium Helmet"
        self.pIDName = "Admantium Minerva Helmet"
        self.loop = 0
        self.pBaseView = 31200
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 54
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJNourishHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NourishHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Helm of Nourishment"
        self.loop = 0
        self.pBaseView = 30150
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNightSoulHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NightSoulHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Night Soul"
        self.loop = 0
        self.pBaseView = 30200
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJNightmareHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NightmareHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Nightmare Helm"
        self.loop = 0
        self.pBaseView = 30250
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJCenturionHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "CenturionHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Centurion Helm"
        self.loop = 0
        self.pBaseView = 30300
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJIntellHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IntellHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Helmet of Intelligence"
        self.loop = 0
        self.pBaseView = 30350
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3585

        self.bases.append("BDescribed")

class SOBJBandanna(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Bandanna"
        self.pName = "Clothing"
        self.pIDName = "Masked Bandanna"
        self.loop = 0
        self.pBaseView = 30900
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJThiefMask(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThiefMask"
        self.pName = "Clothing"
        self.pIDName = "Thieves' Mask"
        self.loop = 0
        self.pBaseView = 30950
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1793

        self.bases.append("BDescribed")

class SOBJHood(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Hood"
        self.pName = "Clothing"
        self.pIDName = "Cloth Hood"
        self.loop = 0
        self.pBaseView = 30500
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJShiftHood(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ShiftHood"
        self.pName = "Clothing"
        self.pIDName = "Hood of Shifting"
        self.loop = 0
        self.pBaseView = 30550
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJVikingHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "VikingHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Viking Helmet"
        self.loop = 0
        self.pBaseView = 30600
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJBerserkHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BerserkHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Berserker's Helmet"
        self.loop = 0
        self.pBaseView = 30650
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSaurianHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SaurianHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Saurian Helm"
        self.loop = 0
        self.pBaseView = 30700
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJDefenseHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DefenseHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Helmet of Defense"
        self.loop = 0
        self.pBaseView = 30750
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJLegionWarriorHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LegionWarriorHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Warrior's Helm"
        self.loop = 0
        self.pBaseView = 30850
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3331

        self.bases.append("BDescribed")

class SOBJTribuneHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TribuneHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Tribune Helm"
        self.loop = 0
        self.pBaseView = 30400
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJConquererHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ConquererHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Helmet of the Conquerer"
        self.loop = 0
        self.pBaseView = 30450
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJRaptorHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RaptorHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Raptor Helm"
        self.loop = 0
        self.pBaseView = 31000
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJPredatorHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PredatorHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Helm of the Predator"
        self.loop = 0
        self.pBaseView = 31050
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJDruidHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DruidHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Druidic Helm"
        self.loop = 0
        self.pBaseView = 31100
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJFiannaHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FiannaHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Helm of the Fianna"
        self.loop = 0
        self.pBaseView = 31150
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJMinervaWarriorHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MinervaWarriorHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Warrior's Helm"
        self.loop = 0
        self.pBaseView = 31250
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -27906

        self.bases.append("BDescribed")

class SOBJHuntressHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HuntressHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Huntress Helm"
        self.loop = 0
        self.pBaseView = 31300
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJRangerHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RangerHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Ranger's Helm"
        self.loop = 0
        self.pBaseView = 31350
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 25

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJMageHat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MageHat"
        self.pName = "Clothing"
        self.pIDName = "Mage's Hat"
        self.loop = 0
        self.pBaseView = 35150
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -19201

        self.bases.append("BDescribed")

class SOBJUplanderHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "UplanderHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Uplander's Helm"
        self.loop = 0
        self.pBaseView = 31800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJKhanHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "KhanHelmet"
        self.pName = "Uplander's Helm"
        self.pIDName = "Helm of the Khan"
        self.loop = 0
        self.pBaseView = 31850
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJCourtierHat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "CourtierHat"
        self.pName = "Clothing"
        self.pIDName = "Courtier's Hat"
        self.loop = 0
        self.pBaseView = 31900
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJLadyRealmHat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LadyRealmHat"
        self.pName = "Clothing"
        self.pIDName = "Lady of The Realm Hat"
        self.loop = 0
        self.pBaseView = 31950
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -2

        self.bases.append("BDescribed")

class SOBJIdiotHat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IdiotHat"
        self.pName = "Clothing"
        self.pIDName = "Village Idiot's Hat"
        self.loop = 0
        self.pBaseView = 32000
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJJesterHat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JesterHat"
        self.pName = "Clothing"
        self.pIDName = "Jester's Hat"
        self.loop = 0
        self.pBaseView = 32050
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 58
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -3

        self.bases.append("BDescribed")

class SOBJSorcererHelm(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SorcererHelm"
        self.pName = "Clothing"
        self.pIDName = "Sorcerer's Hood"
        self.loop = 0
        self.pBaseView = 30550
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 229
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 50

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -19201

        self.bases.append("BDescribed")

class SOBJGladiatorHelm(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "GladiatorHelm"
        self.pName = "Mythril Helmet"
        self.pIDName = "Gladiator's Helmet"
        self.loop = 0
        self.pBaseView = 30650
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 20
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 150

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAdvHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AdvHelmet"
        self.pName = "Mythril Helmet"
        self.pIDName = "Adventurer's Mantle"
        self.loop = 0
        self.pBaseView = 30450
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 229
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJBanditMask(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BanditMask"
        self.pName = "Clothing"
        self.pIDName = "Bandit Mask"
        self.loop = 0
        self.pBaseView = 30950
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 105
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 85

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJCastleHelm(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "CastleHelm"
        self.pName = "Helmet"
        self.pIDName = "Castle Helmet"
        self.loop = 0
        self.pBaseView = 35750
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJPharoahHelm(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "PharoahHelm"
        self.pName = "Helmet"
        self.pIDName = "Pharoah Helmet"
        self.loop = 0
        self.pBaseView = 35850
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJAquaHelm(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "AquaHelm"
        self.pName = "Helmet"
        self.pIDName = "Aqua Helmet"
        self.loop = 0
        self.pBaseView = 17001
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 80

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJSkullHood(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SkullHood"
        self.pName = "Clothing"
        self.pIDName = "Skull Hood"
        self.loop = 0
        self.pBaseView = 17051
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 30

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJValorHelmet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ValorHelmet"
        self.pName = "Helmet"
        self.pIDName = "Valor Helmet"
        self.loop = 0
        self.pBaseView = 35550
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJOgreHead(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OgreHead"
        self.pName = "Helmet"
        self.pIDName = "Ogre Head"
        self.loop = 0
        self.pBaseView = 35600
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMinotaurHead(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MinotaurHead"
        self.pName = "Helmet"
        self.pIDName = "Minotaur Head"
        self.loop = 0
        self.pBaseView = 35650
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJWolfHead(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WolfHead"
        self.pName = "Helmet"
        self.pIDName = "Wolf Head"
        self.loop = 0
        self.pBaseView = 35800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJDevilHead(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "DevilHead"
        self.pName = "Helmet"
        self.pIDName = "Devil Head"
        self.loop = 0
        self.pBaseView = 35900
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMedusaHead(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MedusaHead"
        self.pName = "Helmet"
        self.pIDName = "Medusa Head"
        self.loop = 0
        self.pBaseView = 35952
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 60

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJJackOHelmet01(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JackOHelmet01"
        self.pName = "Iron Helmet"
        self.pIDName = "Happy Harvest Helmet"
        self.loop = 0
        self.pBaseView = 35200
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJJackOHelmet02(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JackOHelmet02"
        self.pName = "Iron Helmet"
        self.pIDName = "Grumpy Harvest Helmet"
        self.loop = 0
        self.pBaseView = 35250
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJJackOHelmet03(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JackOHelmet03"
        self.pName = "Iron Helmet"
        self.pIDName = "Cyclops Harvest Helmet"
        self.loop = 0
        self.pBaseView = 35300
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJJackOHelmet04(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JackOHelmet04"
        self.pName = "Iron Helmet"
        self.pIDName = "Masked Harvest Helmet"
        self.loop = 0
        self.pBaseView = 35350
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJJackOHelmet05(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JackOHelmet05"
        self.pName = "Iron Helmet"
        self.pIDName = "Wolf Harvest Helmet"
        self.loop = 0
        self.pBaseView = 35400
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJJackOHelmet06(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "JackOHelmet06"
        self.pName = "Iron Helmet"
        self.pIDName = "Gremlin Harvest Helmet"
        self.loop = 0
        self.pBaseView = 35450
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 88
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 192


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 100

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 0
        self.pMask = -1

        self.bases.append("BDescribed")

        self.bases.append("BDye")
        self.pHairDye = 0

class SOBJBelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Belt"
        self.pName = "Belt"
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

class SOBJbStrength(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "bStrength"
        self.pName = "Belt"
        self.pIDName = "Belt of Strength"
        self.loop = 0
        self.pBaseView = 10200
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
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

class SOBJbWeakness(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "bWeakness"
        self.pName = "Belt"
        self.pIDName = "Belt of Weakness"
        self.loop = 0
        self.pBaseView = 10200
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
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

class SOBJbLoad(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "bLoad"
        self.pName = "Belt"
        self.pIDName = "Belt of Load"
        self.loop = 0
        self.pBaseView = 10200
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
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

class SOBJbCarrying(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "bCarrying"
        self.pName = "Belt"
        self.pIDName = "Belt of Carrying"
        self.loop = 0
        self.pBaseView = 10200
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
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

class SOBJShoes(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Shoes"
        self.pName = "Shoes"
        self.loop = 0
        self.pBaseView = 10700
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 100
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJHighBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HighBoots"
        self.pName = "High Boots"
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

class SOBJExoticBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticBoots"
        self.pName = "High Boots"
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

class SOBJLowBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LowBoots"
        self.pName = "Low Boots"
        self.loop = 0
        self.pBaseView = 10700
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 100
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

class SOBJExoticLowBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ExoticLowBoots"
        self.pName = "Low Boots"
        self.loop = 0
        self.pBaseView = 10700
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 100
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

StockObjList = []
StockObjList.append(SOBJPlayer())
StockObjList.append(SOBJCombatCloud())
StockObjList.append(SOBJMoneyBag())
StockObjList.append(SOBJManaBag())
StockObjList.append(SOBJHead())
StockObjList.append(SOBJCharacter())
StockObjList.append(SOBJMaleCharacter())
StockObjList.append(SOBJMaleAdventurer())
StockObjList.append(SOBJMaleWarrior())
StockObjList.append(SOBJMaleWizard())
StockObjList.append(SOBJMaleThief())
StockObjList.append(SOBJFemaleCharacter())
StockObjList.append(SOBJFemaleAdventurer())
StockObjList.append(SOBJFemaleWarrior())
StockObjList.append(SOBJFemaleWizard())
StockObjList.append(SOBJFemaleThief())
StockObjList.append(SOBJMaleCleric())
StockObjList.append(SOBJFemaleCleric())
StockObjList.append(SOBJMaleMonk())
StockObjList.append(SOBJFemaleMonk())
StockObjList.append(SOBJChest())
StockObjList.append(SOBJLockedChest())
StockObjList.append(SOBJKey())
StockObjList.append(SOBJSign())
StockObjList.append(SOBJHut())
StockObjList.append(SOBJStand())
StockObjList.append(SOBJFountain())
StockObjList.append(SOBJFountainA())
StockObjList.append(SOBJGargoyleFountain())
StockObjList.append(SOBJLadder())
StockObjList.append(SOBJSkullChest())
StockObjList.append(SOBJSittingStump())
StockObjList.append(SOBJSittingRock())
StockObjList.append(SOBJLockedChestIron())
StockObjList.append(SOBJLockedChestSteel())
StockObjList.append(SOBJLockedChestBrass())
StockObjList.append(SOBJLockedChestBronze())
StockObjList.append(SOBJLockedChestJeweled())
StockObjList.append(SOBJIronKey())
StockObjList.append(SOBJSteelKey())
StockObjList.append(SOBJBronzeKey())
StockObjList.append(SOBJBrassKey())
StockObjList.append(SOBJJeweledKey())
StockObjList.append(SOBJRustySkeletonKey())
StockObjList.append(SOBJSilverSkeletonKey())
StockObjList.append(SOBJGoldSkeletonKey())
StockObjList.append(SOBJLockpick())
StockObjList.append(SOBJFood())
StockObjList.append(SOBJDrink())
StockObjList.append(SOBJBread())
StockObjList.append(SOBJVeggies())
StockObjList.append(SOBJMeat())
StockObjList.append(SOBJRatlingMeat())
StockObjList.append(SOBJCheese())
StockObjList.append(SOBJRatlingCheese())
StockObjList.append(SOBJWaterBottle())
StockObjList.append(SOBJWineFlask())
StockObjList.append(SOBJAleJug())
StockObjList.append(SOBJAmbrosia())
StockObjList.append(SOBJRawMeat())
StockObjList.append(SOBJArcticRatMeat())
StockObjList.append(SOBJWharfRatMeat())
StockObjList.append(SOBJFlameRatMeat())
StockObjList.append(SOBJDemonRatMeat())
StockObjList.append(SOBJBar())
StockObjList.append(SOBJBolt())
StockObjList.append(SOBJWoodBlock())
StockObjList.append(SOBJIronBar())
StockObjList.append(SOBJSteelBar())
StockObjList.append(SOBJTemperedSteelBar())
StockObjList.append(SOBJMythrilBar())
StockObjList.append(SOBJObsidianiteBar())
StockObjList.append(SOBJAdmantiumBar())
StockObjList.append(SOBJClothBolt())
StockObjList.append(SOBJLeatherBolt())
StockObjList.append(SOBJTrollHideBolt())
StockObjList.append(SOBJSweatBar())
StockObjList.append(SOBJMagicBar())
StockObjList.append(SOBJTent())
StockObjList.append(SOBJBackPack())
StockObjList.append(SOBJRoyalPack())
StockObjList.append(SOBJBlackPack())
StockObjList.append(SOBJTealPack())
StockObjList.append(SOBJLeatherPouch())
StockObjList.append(SOBJMirror())
StockObjList.append(SOBJBowl())
StockObjList.append(SOBJBlackRose())
StockObjList.append(SOBJRedRose())
StockObjList.append(SOBJWhiteRose())
StockObjList.append(SOBJBlueRose())
StockObjList.append(SOBJYellowRose())
StockObjList.append(SOBJPinkRose())
StockObjList.append(SOBJGreenRose())
StockObjList.append(SOBJChrysanthenum())
StockObjList.append(SOBJDaisy())
StockObjList.append(SOBJDrum())
StockObjList.append(SOBJFlute())
StockObjList.append(SOBJStrynx())
StockObjList.append(SOBJLyre())
StockObjList.append(SOBJLute())
StockObjList.append(SOBJAnimalHide())
StockObjList.append(SOBJWolfPelt())
StockObjList.append(SOBJWhiteWolfPelt())
StockObjList.append(SOBJFenrisPelt())
StockObjList.append(SOBJBloodFenrisPelt())
StockObjList.append(SOBJHellHoundPelt())
StockObjList.append(SOBJHowlingTerrorPelt())
StockObjList.append(SOBJTrollHide())
StockObjList.append(SOBJRockTrollHide())
StockObjList.append(SOBJDemonTrollHide())
StockObjList.append(SOBJDireWolfPelt())
StockObjList.append(SOBJPlate())
StockObjList.append(SOBJCandle())
StockObjList.append(SOBJHammer())
StockObjList.append(SOBJCarving())
StockObjList.append(SOBJMug())
StockObjList.append(SOBJChalice())
StockObjList.append(SOBJSpring())
StockObjList.append(SOBJHollowTree())
StockObjList.append(SOBJFireA())
StockObjList.append(SOBJFire1())
StockObjList.append(SOBJFireB())
StockObjList.append(SOBJFire2())
StockObjList.append(SOBJEmbers())
StockObjList.append(SOBJSmokeA())
StockObjList.append(SOBJSmoke1())
StockObjList.append(SOBJSmokeB())
StockObjList.append(SOBJSmoke2())
StockObjList.append(SOBJSmokeC())
StockObjList.append(SOBJSmoke3())
StockObjList.append(SOBJFireC())
StockObjList.append(SOBJFire3())
StockObjList.append(SOBJSpellComponent())
StockObjList.append(SOBJTooth())
StockObjList.append(SOBJDaemonTooth())
StockObjList.append(SOBJFinger())
StockObjList.append(SOBJZombieFinger())
StockObjList.append(SOBJNugget())
StockObjList.append(SOBJGoldNugget())
StockObjList.append(SOBJGuano())
StockObjList.append(SOBJImpGuano())
StockObjList.append(SOBJRatGuano())
StockObjList.append(SOBJDaemonGuano())
StockObjList.append(SOBJDaveGuano())
StockObjList.append(SOBJJawBone())
StockObjList.append(SOBJEyeball())
StockObjList.append(SOBJKilrogEyeball())
StockObjList.append(SOBJOgreEyeball())
StockObjList.append(SOBJRock())
StockObjList.append(SOBJLeaf())
StockObjList.append(SOBJClump())
StockObjList.append(SOBJAmberRod())
StockObjList.append(SOBJObsidianDust())
StockObjList.append(SOBJSilvergrass())
StockObjList.append(SOBJGoldenberries())
StockObjList.append(SOBJPigweed())
StockObjList.append(SOBJDevilweed())
StockObjList.append(SOBJCorbalite())
StockObjList.append(SOBJBasalt())
StockObjList.append(SOBJSulfur())
StockObjList.append(SOBJMarble())
StockObjList.append(SOBJElderOak())
StockObjList.append(SOBJSilverthorn())
StockObjList.append(SOBJTobac())
StockObjList.append(SOBJPerfectRose())
StockObjList.append(SOBJDespothesScepter())
StockObjList.append(SOBJDuachsCrystal())
StockObjList.append(SOBJDuachsCrystalGreen())
StockObjList.append(SOBJMabonsStaff())
StockObjList.append(SOBJClothing())
StockObjList.append(SOBJHelmet())
StockObjList.append(SOBJIronHelmet())
StockObjList.append(SOBJSteelHelmet())
StockObjList.append(SOBJTemperedSteelHelmet())
StockObjList.append(SOBJMythrilHelmet())
StockObjList.append(SOBJObsidianiteHelmet())
StockObjList.append(SOBJAdmantiumHelmet())
StockObjList.append(SOBJWizardCap())
StockObjList.append(SOBJIronLegionHelmet())
StockObjList.append(SOBJIronMinervaHelmet())
StockObjList.append(SOBJSteelLegionHelmet())
StockObjList.append(SOBJSteelMinervaHelmet())
StockObjList.append(SOBJTemperedSteelLegionHelmet())
StockObjList.append(SOBJTemperedSteelMinervaHelmet())
StockObjList.append(SOBJMythrilLegionHelmet())
StockObjList.append(SOBJMythrilMinervaHelmet())
StockObjList.append(SOBJObsidianiteLegionHelmet())
StockObjList.append(SOBJObsidianiteMinervaHelmet())
StockObjList.append(SOBJAdmantiumLegionHelmet())
StockObjList.append(SOBJAdmantiumMinervaHelmet())
StockObjList.append(SOBJNourishHelmet())
StockObjList.append(SOBJNightSoulHelmet())
StockObjList.append(SOBJNightmareHelmet())
StockObjList.append(SOBJCenturionHelmet())
StockObjList.append(SOBJIntellHelmet())
StockObjList.append(SOBJBandanna())
StockObjList.append(SOBJThiefMask())
StockObjList.append(SOBJHood())
StockObjList.append(SOBJShiftHood())
StockObjList.append(SOBJVikingHelmet())
StockObjList.append(SOBJBerserkHelmet())
StockObjList.append(SOBJSaurianHelmet())
StockObjList.append(SOBJDefenseHelmet())
StockObjList.append(SOBJLegionWarriorHelmet())
StockObjList.append(SOBJTribuneHelmet())
StockObjList.append(SOBJConquererHelmet())
StockObjList.append(SOBJRaptorHelmet())
StockObjList.append(SOBJPredatorHelmet())
StockObjList.append(SOBJDruidHelmet())
StockObjList.append(SOBJFiannaHelmet())
StockObjList.append(SOBJMinervaWarriorHelmet())
StockObjList.append(SOBJHuntressHelmet())
StockObjList.append(SOBJRangerHelmet())
StockObjList.append(SOBJMageHat())
StockObjList.append(SOBJUplanderHelmet())
StockObjList.append(SOBJKhanHelmet())
StockObjList.append(SOBJCourtierHat())
StockObjList.append(SOBJLadyRealmHat())
StockObjList.append(SOBJIdiotHat())
StockObjList.append(SOBJJesterHat())
StockObjList.append(SOBJSorcererHelm())
StockObjList.append(SOBJGladiatorHelm())
StockObjList.append(SOBJAdvHelmet())
StockObjList.append(SOBJBanditMask())
StockObjList.append(SOBJCastleHelm())
StockObjList.append(SOBJPharoahHelm())
StockObjList.append(SOBJAquaHelm())
StockObjList.append(SOBJSkullHood())
StockObjList.append(SOBJValorHelmet())
StockObjList.append(SOBJOgreHead())
StockObjList.append(SOBJMinotaurHead())
StockObjList.append(SOBJWolfHead())
StockObjList.append(SOBJDevilHead())
StockObjList.append(SOBJMedusaHead())
StockObjList.append(SOBJJackOHelmet01())
StockObjList.append(SOBJJackOHelmet02())
StockObjList.append(SOBJJackOHelmet03())
StockObjList.append(SOBJJackOHelmet04())
StockObjList.append(SOBJJackOHelmet05())
StockObjList.append(SOBJJackOHelmet06())
StockObjList.append(SOBJBelt())
StockObjList.append(SOBJbStrength())
StockObjList.append(SOBJbWeakness())
StockObjList.append(SOBJbLoad())
StockObjList.append(SOBJbCarrying())
StockObjList.append(SOBJShoes())
StockObjList.append(SOBJHighBoots())
StockObjList.append(SOBJExoticBoots())
StockObjList.append(SOBJLowBoots())
StockObjList.append(SOBJExoticLowBoots())
