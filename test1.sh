#!/bin/bash
data=DAVIS
method=RUIC
subfolder=(bike-packing blackswan bmx-trees breakdance camel car-roundabout car-shadow cows dance-twirl dog dogs-jump drift-chicane drift-straight goat gold-fish horsejump-high india judo kite-surf lab-coat libby loading mbike-trick motocross-jump paragliding-launch parkour pigs scooter-black shooting soapbox)

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
