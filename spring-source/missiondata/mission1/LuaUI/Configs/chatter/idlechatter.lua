-- separate file so missions don't need to make a copy of the entire pilotdefs
local idleChatterDefs = {
	luckystar = {
		{image = portraits.milfeulle_concerned, text = "Tact, what do the aliens have against us?"},
		{image = portraits.milfeulle_sad, text = "I hope we're not going to end up in another war..."},
		{image = portraits.milfeulle_oh, text = "Hmmm... I wonder what those aliens look like in person..."},
		
	},
	kungfufighter = {
		{image = portraits.ranpha_serious, text = "A hostile alien fleet in the capital system...\nWhat's going on here?"},
		{image = portraits.ranpha_worried, text = "They might be attacking elsewhere in the Empire too... I hope my little brothers are alright."},
		{image = portraits.ranpha_normal, text = "Don't worry, Tact. I won't let them hurt you."},
	},
	trickmaster = {},
	happytrigger = {
		{image = portraits.forte_serious, text = "There's definitely more to these aliens than meets the eye."},
		{image = portraits.forte_what, text = "Tact, when we get back, it's time to have a serious talk with Naval Intelligence."},
		{image = portraits.forte_serious, text = "In any case, we need to resolve the situation before us. Quickly and decisively."},
	},
	harvester = {},
	sharpshooter = {
		{image = portraits.chitose_surprised, text = "Why are aliens attacking us? Have we unknowingly offended them?"},
		{image = portraits.chitose_sad, text = "Can we stop this, somehow? Can we find a way to communicate with them?"},
		{image = portraits.chitose_normal, text = "It seems for now, we have no choice but to fight. Tact, I've got your back."},
	},
}

return idleChatterDefs