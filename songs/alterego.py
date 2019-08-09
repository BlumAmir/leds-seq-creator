from animations import brightness
from animations.hue_shift import hue_shift_jump_on_cycle
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands
from network.send_to_mqtt import send_to_mqtt
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=123, beats_per_episode=32)

# episodes(0, 30)
# elements(cabbage1)
# cycle(beats=4)
#
# cycle_beats(1.5, 2)
# color.uniform((0.35, 0.9, 1.0))
# effect.saw_tooth(1.0)
#
# cycle_beats(2.5, 3)
# color.uniform((0.4, 0.7, 1.0))
# effect.saw_tooth(1.0)
#
# episodes(1, 30)
# effect.brightness(0.5)
#
# x = [flower1, cabbage1,]
#
# episodes(1, 30)
# elements(x)
# cycle(2)
# color.alternate(red, coral, number_of_pixels=10)
# color.gradient(0.3, 0.5)
# effect.saw_tooth(medium)
# effect.snake(4.0)
#
# episodes(2, 30)
# effect.brightness(0.5)


# episodes(0, 30)
# elements(all)
# cycle(4)
# color.alternate((0.0, 1.0, 1.0), (0.05, 0.8, 1.0))
#
# elements(flower1)
# color.uniform((0.0, 1.0, 1.0))
#
# elements(cabbage1)
# color.uniform((0.1, 1.0, 1.0))
#
# elements(cabbage2)
# color.uniform((0.2, 1.0, 1.0))
#
# elements(cup_cake1)
# color.uniform((0.3, 1.0, 1.0))
# elements(cup_cake2)
# color.uniform((0.4, 1.0, 1.0))
#
# elements(paper1)
# color.uniform((0.4, 1.0, 1.0))
#
# elements(lifa3)
# color.uniform((0.0, 1.0, 0.3))
# elements(lifa3.stick(5))
# color.uniform((0.9, 1.0, 1.0))

episodes(0, 30)
elements(single_stands)
cycle(8)
color.uniform(green)
effect.snake()
#effect.breath(soft)



send_to_mqtt("alterego")



