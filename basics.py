import numpy as np
import numpy.linalg as la

# Board spec: UIUCMonopolyDraft1.png

def get_transition_matrix(size=16):
    board_matrix = np.zeros((size, size))

    # First compute assuming no re-roll of dice
    # and no jumps (jail/chance cards)

    # Second, account for 6 being a re-roll
    for from_index in range(size):
        for i in range(5):
            # For dice rolls of 1-5
            to_index = (from_index + i + 1) % size
            board_matrix[to_index, from_index] = 1/6
        for i in range(6):
            # For dice rolls of 6, followed by 1-6
            to_index = (from_index + i + 7) % size
            board_matrix[to_index, from_index] = 1/36

    # This accounts for all dice rolls
    # We will now implement chance cards. For a chance card, we have a
    # 1/5 probability of getting a "pass go",
    # or a 0.2 probability of starting that turn at 0
    # This means that the existing probabilities are multiplied by 0.8
    # Added to column 0 multiplied by 0.2

    chance_indices = [3, 7, 14]
    chance_probability = 0.2
    for from_index in chance_indices:
        board_matrix[:, from_index] *= 0.8
        board_matrix[:, from_index] += board_matrix[:, 0] * 0.2

    # Now account for the "go to jail square"
    # Go to jail square sends you to jail with probability 1, costing 1 turn

    go_to_jail_index = 12
    jail_index = 4
    board_matrix[:, go_to_jail_index] = 0.0
    board_matrix[jail_index, go_to_jail_index] = 1.0
    return board_matrix

def print_list_form(mat):
    for i in range(mat.shape[0]):
        print (list(mat[i, :]))

def main():
    M = get_transition_matrix()

    # Set initial state as being on the 0 index square, i.e "go"
    x_initial = np.zeros(16)
    x_initial[0] = 1.0
    print (x_initial)

    # Run a loop for 50 iterations, stopping if the power iteration converges
    num_turns = 50
    turn = 0
    x = x_initial
    tol = 10**-6
    err = 1
    while turn < num_turns and err > tol:
        x_new = M @ x
        print ("Turn #" + str(turn+1))
        print (x_new)
        err = la.norm(x-x_new)
        turn += 1
        x = x_new


if __name__ == '__main__':
    main()
