#!/bin/bash
data=videvo
method=IAC
subfolder=(AircraftTakingOff1 CoupleRidingMotorbike Cycling Ducks FarmingLandscape FatherAndChild2 Festival Freeway2 Koala Madagascar MenRidingMotorbike PalmTrees PoliceCar SilverCat SkateboarderTableJump Surfing TimeSquareTraffic Vineyard Waterfall2 YogaHut2)

for element in ${subfolder[@]}
do
echo $element
python dvp_video_consistency.py \
--max_epoch 25 \
--input demo/consistency/colorization/input-$element \
--processed demo/consistency/colorization/$element \
--task colorization \
--output ${method}+DVP/${data}/$element
done
