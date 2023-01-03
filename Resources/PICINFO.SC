

(module# PICINFO)

(include "rlmrmmgr.sh")

(class PicInfo of Object
	(properties
		int	number:		0
		int	roomType:	0	  
		int	picture:		0
		int	horizon:		130
		id		polyList:	0	  
		int	pScaled:		TRUE 
		int	pBackY:		140
		int	pBackSize:	40
		int	pFrontY:		310
		int	pFrontSize: 128
	)
)

(class PicInfoList of Set
	(method (init)
		(super init: &rest)

		(self add:
			((PicInfo new:) 
				roomType:	FOREST, 		
				picture:  	3000,

			)
			((PicInfo new:) 
				roomType:	FOREST, 		
                                picture:        3001,

			)

			((PicInfo new:) 
				roomType: 	FOREST, 		
				picture: 	3009, 
				horizon: 	130,
				pBackY:	  	1,
				pBackSize: 	80,
				polyList: ((Polygon new:) 
								type: PBarredAccess,
								init: 0 0 0 247 137 150 261 131 358 128 446 153 
										575 227 639 265 639 0,
								yourself:
							 ),
			)

			((PicInfo new:) 
				roomType: 	DESERT, 		
				picture: 	3404, 
			)

			((PicInfo new:) 
				roomType: 	DESERT, 		
				picture: 	3405, 
			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   3406,
			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   3407,
			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   3408,
			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   3409,
			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   8406,
			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   8407,
			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   8408,
			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   8409,
			)

			((PicInfo new:) 
				roomType: 	BEACH,  		
				picture: 	3030,
				polyList: ((Polygon new:) 
								type: PBarredAccess,
								init: 0 104 0 316 160 317 372 104 0 104,
								yourself:
							 ),
			)

			((PicInfo new:) 
				roomType: BEACH,  		
				picture: 3031,
				polyList: ((Polygon new:) 
								type: PBarredAccess,
								init: 0 213 0 317 640 316 640 220 0 213,
								yourself:
							 ),
			)

			((PicInfo new:) 
				roomType: BEACH,  		
				picture: 3032,
			)

			((PicInfo new:) 
				roomType: TOWN1, 		
				picture:   3500,

				horizon:		100,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: TOWN1INT,
				picture:   4000,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)
			((PicInfo new:) 
				roomType: TOWN1INT,
				picture:   4001,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)
			((PicInfo new:) 
				roomType: HOUSE1, 		
				picture:   3201,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)
			((PicInfo new:) 
				roomType: HOUSE1INT,
				picture:   3300,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)
			
			((PicInfo new:) 
				roomType: DUNGEON,
				picture:   3071,
				pBackY:		160,
				pBackSize:	112,
				pFrontY:		320,
				pFrontSize: 112,
			)

			((PicInfo new:) 
				roomType: 	SWAMP, 		
				picture: 	6500, 
				horizon: 	130,
				pBackY:	  	1,
				pBackSize: 	80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   6000,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5000,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5001,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5002,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5003,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5004,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5005,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5006,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5510,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5511,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5512,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5513,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)

			((PicInfo new:) 
				roomType: CUSTOM,
				picture:   5514,
				horizon:		90,
				pBackY:		160,
				pBackSize:	 80,
				pFrontY:		320,
				pFrontSize: 80,

			)
		)
	)
)

