#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

// class representing a state of the game
class Board
{
private:
    int player;
    std::vector<int> cells;

public:
    Board(int p)
    {
        player = p; // Denotes player id (AI -> 0, USER -> 1)
        cells.resize(9);
        std::fill(cells.begin(), cells.end(), -1); // Board is initialized with -1 to denote empty cells
    }

    // Returns the current player id
    int current_player()
    {
        return player;
    }

    // Returns legal moves
    std::vector<int> moves()
    {
        std::vector<int> m;
        int c = 1;
        for (auto cell : cells)
        {
            if (cell == -1)
                m.push_back(c);
            c++;
        }
        return m;
    }

    // Returns state of game after the result of the given action
    Board result(int action)
    {
        Board result_board(0);
        result_board.player = player;
        result_board.cells = cells;
        result_board.cells[action-1] = result_board.player;
        result_board.player ^= 1;
        return result_board;
    }

    // Terminal test, which returns true when the game is over(all cells cells
    bool game_over()
    {
        if (count(cells.begin(), cells.end(), -1))
        {
            if (utility(player))
                return true;
            return false;
        }
        return true;
    }

    // Defines the score (WIN -> 1, LOSS -> -1, DRAW -> 0)
    int utility(int p)
    {
        if (won(p))
            return 1;
        else if (won(p ^ 1))
            return -1;
        else
            return 0;
    }

    // Determines whether the player has any winning combination in the game board
    bool won(int p)
    {
        bool win_1 = (cells[0] == p && cells[1] == p && cells[2] == p);
        bool win_2 = (cells[3] == p && cells[4] == p && cells[5] == p);
        bool win_3 = (cells[6] == p && cells[7] == p && cells[8] == p);
        bool win_4 = (cells[0] == p && cells[3] == p && cells[6] == p);
        bool win_5 = (cells[1] == p && cells[4] == p && cells[7] == p);
        bool win_6 = (cells[2] == p && cells[5] == p && cells[8] == p);
        bool win_7 = (cells[0] == p && cells[4] == p && cells[8] == p);
        bool win_8 = (cells[2] == p && cells[4] == p && cells[6] == p);
        return (win_1 || win_2 || win_3 || win_4 || win_5 || win_6 || win_7 || win_8);
    }

    // Makes appropriate changes in the game board for the given action
    void fill(int action)
    {
        cells[action-1] = player;
        player ^= 1;
    }

    // Displays the game board onto the console
    void display()
    {
        std::cout << '\n';
        int filled_index = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = filled_index; j < filled_index + 3; j++)
            {
                if (cells[j] == -1)
                    std::cout << "   ";
                else if (cells[j] == 1)
                    std::cout << " X ";
                else
                    std::cout << " O ";
                if ((j + 1) % 3 != 0)
                    std::cout << '|';
                else
                    std::cout << '\n';
            }
            if (i != 2)
                std::cout << "---+---+---" << '\n';
            filled_index += 3;
        }
        std::cout << '\n';
    }
};

int min_value(Board board, int alpha, int beta);
int max_value(Board board, int alpha, int beta);

// Makes a decision of best move among all posible moves using alpha beta pruning
int alpha_beta(Board board)
{
    int decision;
    int maximum_score = std::numeric_limits<int>::min();
    int alpha = std::numeric_limits<int>::min();
    int beta = std::numeric_limits<int>::max();
    std::vector<int> moves = board.moves();
    for (auto i : moves)
    {
        int m_val = min_value(board.result(i), alpha, beta);
        alpha = std::max(alpha, m_val);
        if (m_val > maximum_score)
        {
            maximum_score = m_val;
            decision = i;
        }
    }
    return decision;
}

// Minimizing function
int min_value(Board board, int alpha, int beta)
{
    if (board.game_over())
        return board.utility(0);
    int v = std::numeric_limits<int>::max();
    auto moves = board.moves();
    for (auto i : moves)
    {
        v = std::min(v, max_value(board.result(i), alpha, beta));
        if (v <= alpha)
            return v;
        beta = std::min(beta, v);
    }
    return v;
}

// Maximizing function
int max_value(Board board, int alpha, int beta)
{
    if (board.game_over())
        return board.utility(0);
    int v = std::numeric_limits<int>::min();
    auto moves = board.moves();
    for (auto i : moves)
    {
        v = std::max(v, min_value(board.result(i), alpha, beta));
        if (v >= beta)
            return v;
        alpha = std::max(alpha, v);
    }
    return v;
}