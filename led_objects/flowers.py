from led_objects.led_object import LedObject
from led_objects.objects_selector import elements_flatten


class Flower(LedObject):

    def __init__(self, num_pixels, start_index = 0):
        super(Flower, self).__init__(total_pixels=num_pixels)
        self.mapping = {"a": list(range(start_index, self.total_pixels))}
        self.create_random_for_all()


flower6 = Flower(50)
flower1 = Flower(50)

flowers = elements_flatten([flower1, flower6])

bottle5 = Flower(50)
bottle4 = Flower(50)

bottles = elements_flatten([bottle4, bottle5])

paper5 = Flower(50, 12)
paper2 = Flower(50, 9)

papers = [paper2, paper5]

strings = elements_flatten([flowers, bottles, papers])

gloves8 = Flower(50)
gloves = elements_flatten([gloves8])

