#!/bin/bash

# DAVIS
#subfolder=(bike-packing blackswan bmx-trees breakdance camel car-roundabout car-shadow cows dance-twirl dog dogs-jump drift-chicane drift-straight goat gold-fish horsejump-high india judo kite-surf lab-coat libby loading mbike-trick motocross-jump paragliding-launch parkour pigs scooter-black shooting soapbox)

# videvo
subfolder=(AircraftTakingOff1 CoupleRidingMotorbike Cycling Ducks FarmingLandscape FatherAndChild2 Festival Freeway2 Koala Madagascar MenRidingMotorbike PalmTrees PoliceCar SilverCat SkateboarderTableJump Surfing TimeSquareTraffic Vineyard Waterfall2 YogaHut2)

for element in ${subfolder[@]}
do
echo demo/consistency/colorization/$element
done
