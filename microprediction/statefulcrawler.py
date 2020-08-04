
from collections import OrderedDict
from microprediction.crawler import MicroCrawler


class StreamCrawler(MicroCrawler):

    # Crawler maintaining state for each stream

    ########################################################
    #  Override the following methods                      #
    ########################################################

    def initial_state(self, name, lagged_values, lagged_times, **ignore):
        return None

    def update_state(self, state, lagged_values=None, lagged_times=None, **ignore):
        return state

    def sample_using_state(self, state, lagged_values, lagged_times, name, delay, **ignore):
        raise NotImplemented('Need to implement sample_using_state when deriving from StreamCrawler')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stream_state = OrderedDict()

    ########################################################
    #  Maybe leave this alone                              #
    ########################################################

    def sample(self, lagged_values, lagged_times=None, name=None, delay=None, **ignored):
        """ Calls sample_using_state """

        if name not in self.stream_state:
            self.stream_state.update(
                {name: self.initial_state(name=name, lagged_values=lagged_values, lagged_times=lagged_times)})
        state = self.stream_state[name]
        state = self.update_state(state=state, lagged_values=lagged_values, lagged_times=lagged_times)
        samples = self.sample_using_state(state=state, lagged_values=lagged_values, lagged_times=lagged_times,
                                          name=name, delay=delay)
        self.stream_state[name] = state
        return samples


#TODO: HorizonCrawler