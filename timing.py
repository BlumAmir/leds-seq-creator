
""" global object - accessed from other modules """
import copy

tf_global = None

def get_timing():
    global tf_global
    return copy.deepcopy(tf_global)

class TimeFrame:

    def __init__(self, bpm, start_beat_index, number_of_beats):
        self.bpm = bpm
        self.start_beat_index = start_beat_index
        self.end_beat_index = start_beat_index + number_of_beats

    def get_start_time_ms(self):
        return self.get_beat_time_ms(self.start_beat_index)

    def get_end_time_ms(self):
        return self.get_beat_time_ms(self.end_beat_index)

    def number_of_beats(self):
        return self.end_beat_index - self.start_beat_index

    def get_beat_time_ms(self, beat_index):
        return int(beat_index * self.__get_beats_per_second() * 1000.0)

    def __get_beats_per_second(self):
        return 60.0 / self.bpm

class TimeFrameFactory:

    def __init__(self, bpm, beats_per_episode):
        self.beats_per_episode = beats_per_episode
        self.bpm = bpm

    def from_beat(self, beat_start_index, beat_end_index):
        global tf_global
        tf_global = TimeFrame(self.bpm, beat_start_index, beat_end_index)

    def episodes_length(self, episode_start_index, num_of_episodes):
        global tf_global
        start_beat = episode_start_index * self.beats_per_episode
        num_of_beats = num_of_episodes * self.beats_per_episode
        tf_global = TimeFrame(self.bpm, start_beat, num_of_beats)

    def episodes_index(self, episode_start_index, episode_end_index):
        global tf_global
        start_beat = episode_start_index * self.beats_per_episode
        num_of_beats = (episode_end_index - episode_start_index) * self.beats_per_episode
        tf_global = TimeFrame(self.bpm, start_beat, num_of_beats)

    def single_episode(self, episode_index):
        global tf_global
        tf_global = self.episodes_length(episode_index, 1)