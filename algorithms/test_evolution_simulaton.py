import mutate
from scipy import io


def main():
    data = io.loadmat("/Users/williamsumfest/Downloads/flhivdata.mat")
    
    doc = data['ptd'][0]
    alpha = 0.000016
    time = 1000
    dt = 10
    tree = mutate.simulate_evolution(doc, alpha, time, dt, 3)

    print tree.get_nodes()



if __name__ == "__main__":
    main()