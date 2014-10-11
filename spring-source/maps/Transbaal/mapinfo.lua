local mapinfo = {
	name        = "Transbaal",
	shortname   = "Transbaal",
	description = "The Imperial home system.",
	author      = "Brocolli, compiled by KingRaptor",
	version     = "",
	modtype     = 3, --// 1=primary, 0=hidden, 3=map
	depend      = {},
	replace     = {},
	
	mapHardness = 10000,
	voidwater = true,
	--voidground = true,

	light = {
		sunDir = ".5 1 .2",				--direction of sun (spring will normalize it later)(y component is upward)
		unitAmbientColor = "0.5 0.5 0.5",		--ambient (non sun lit) color of units (and wreckage etc)
		unitSunColor = "1.3 1.3 1.3",			--color of units where fully sun lit (added to ambient)
		unitShadowDensity = 0.7,			--how far from the non shadowed to the ambient color stuff in shadow will go
	},
	
	teams = {
		[0] = {startPos = {x = 256, z = 256}},
		[1] = {startPos = {x = 10240 - 256, z = 10240 - 256}},
	},
	
	smf = {
		minHeight = -500,
		maxHeight = -499,
	},
	
	atmosphere  =  {
		skyBox  =  "transbaal.dds",
		sunColor = "1 1 1",
		skyColor = "0 0 0",
		cloudColor = "0 0 0",
		cloudDensity = 0,
		fogColor = "0 0 0",
		fogStart = 0,
	},
	
	terrainTypes = {
		[0] = {
			name = "Default",
			hardness = 1.0,
			receiveTracks = true,
			moveSpeeds = {
				tank  = 1.0,
				kbot  = 1.0,
				hover = 1.0,
				ship  = 1.0,
			},
		},
	},
}

return mapinfo