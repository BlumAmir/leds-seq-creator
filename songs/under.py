from animations import brightness
from animations.hue_shift import hue_shift_jump_on_cycle
from infra.animations_factory import color, effect
from infra.length import short, medium, long, soft, hard, total
from infra.stored_animations import save, beat, load
from led_objects.cabbages import cabbage1, cabbage6, brain7, cup_cake4, cabbage5, cabbages, donut1, donut3, \
    brains, twists, donuts
from led_objects.flood import cup_cakes, rugs
from led_objects.led_object import all
from led_objects.flowers import flower6, flowers, paper5, papers, bottles, paper2, flower1
from led_objects.objects_selector import elements
from led_objects.stands import sticks8, single_sticks, sticks7, sticks3, lifas5, lifas1, lifas4, sticks, lifas, stands, \
    single_lifas, single_stands
from network.send_to_mqtt import send_to_mqtt, start_song
from infra.timing import song_settings, episodes, episode, cycle, cycle_beats, beats
from infra.colors import *

song_settings(bpm=128, beats_per_episode=32, start_offset=3)

elements(all)

beats(0, 2)
color.uniform((0.0, 0.9, 1.0))


def pattern(first_beat, main_color=coral, second_color=indigo, standing_elem=sticks8):
    beats(first_beat,first_beat+8)
    cycle(8)
    offset = 0
    def pattern_inner(offset, standing_elem, main_color=pink_string):
        cycle_beats(offset, offset + 0.25)
        elements(standing_elem.stand(1))
        color.uniform(main_color)

        cycle_beats(offset + 0.25, offset + 0.5)
        elements(standing_elem.stand(2))
        color.uniform(main_color)

        cycle_beats(offset + 0.5, offset + 0.75)
        elements(standing_elem.stand(3))
        color.uniform(main_color)

        cycle_beats(offset + 0.75, offset + 1.25)
        elements(standing_elem.stand(4))
        color.uniform(main_color)

        cycle_beats(offset + 1.25, offset + 1.75)
        elements(standing_elem.stand(5))
        color.uniform(main_color)

        cycle_beats(offset + 1.75, offset + 2)
        elements(standing_elem.stand(1))
        color.uniform(main_color)

        cycle_beats(offset + 2, offset + 2.5)
        elements(standing_elem.stand(2))
        color.uniform(main_color)

        cycle_beats(offset + 2.5, offset + 3)
        elements(standing_elem.stand(3))
        color.uniform(main_color)


    pattern_inner(0, standing_elem)

    cycle_beats(3, 3.5)
    elements(standing_elem.stand(4))
    color.uniform(second_color)

    cycle_beats(3.5, 4)
    elements(standing_elem.stand(5))
    color.uniform(main_color)

    pattern_inner(4, standing_elem)

    cycle_beats(7, 8)
    elements(standing_elem.stand(4))
    color.uniform(main_color)

pattern(2, standing_elem=sticks8, main_color=light_indigo)
pattern(10, standing_elem=sticks7, main_color=light_indigo)


beats(2, 18)
color.gradient(0.0, 2.0)

cycle(8)
elements(single_stands)
cycle_beats(0, 4)
effect.snake(1.0, True)
cycle_beats(4, 8)
effect.snake(1.0, False)


elements(all)

#BEAT

beats(18, 52)
color.uniform((0.7, 0.9, 1.0))

def grad_everry_beat():
    color.gradient(0.0, 4.0)
    cycle(1)
    effect.saw_tooth()

beats(52, 80)
elements([cabbages, rugs])
grad_everry_beat()

beats(56, 80)
elements(donuts)
grad_everry_beat()

beats(60, 80)
elements(cup_cakes)
grad_everry_beat()

beats(64, 80)
elements(bottles)
grad_everry_beat()

beats(68, 80)
elements(flowers)
grad_everry_beat()

beats(72, 80)
elements(papers)
grad_everry_beat()


# STICKS RING

beats(80, 112)
elements(single_stands)
color.gradient(0.0, 2.0)

beats(80, 112)
for e in all:
    e.random
elements(stands)
cycle(2.0)
effect.segment_breath(0.5)
for e in all:
    e.straight

elements(single_stands)
cycle(8)
cycle_beats(0, 4)
effect.snake(4.0)
cycle_beats(4, 8)
effect.snake(4.0, True)

beats(112, 116)
color.uniform((0.6, 0.9, 1.0))

beats(116, 182)
color.uniform((0.1, 0.9, 1.0))

beats(182, 216)
color.uniform((0.8, 0.9, 1.0))

beats(216, 244)
color.uniform((0.2, 0.9, 1.0))

beats(244, 280)
color.uniform((0.7, 0.9, 1.0))

beats(280, 348)
color.uniform((0.0, 0.9, 1.0))




send_to_mqtt("under")
start_song("under", 40)


