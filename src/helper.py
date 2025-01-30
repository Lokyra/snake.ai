import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

plt.ion()


def plot(scores, mean_scores):
    plt.figure(1)
    plt.clf()
    plt.title("Training...")
    plt.xlabel("Number of Games")
    plt.ylabel("Score")
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    plt.show()
    plt.pause(0.1)
