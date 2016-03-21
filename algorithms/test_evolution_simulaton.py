import mutate
from scipy import io


def main():
    data = io.loadmat("/Users/williamsumfest/Downloads/flhivdata.mat")
    
    doc = data['ptd'][0]
    alpha = 0.0000009
    time = 10000000
    dt = 10000
    tree = mutate.simulate_evolution(doc, alpha, time, dt, 4)

    return tree



if __name__ == "__main__":
    main()


