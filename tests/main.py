from build_plot.build_plot import PlotBuilder
from matplotlib import pyplot as plt
from chords.chords import chords_method, f



plotBuilder = PlotBuilder(plt)
plotBuilder.build_plot(0, 4, (-1, 1.5), 0.01, 0.1, chords_method, f)