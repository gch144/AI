#include "tic.hh"
using namespace std;

void ask(int &var, string prompt, vector<int> vals)
{
    while (1)
    {
        cout << prompt;
        cin >> var;
        if (count(vals.begin(), vals.end(), var))
            return;
    }
}

int main()
{
    cout << "-------------------------------------------------------\n";
    cout << "Tic Tac Toe AI with Alpha Beta Pruning\n";
    cout << "-------------------------------------------------------\n\n";
    int player;
    ask(player, "AI or User first? [0/1]: ", {0, 1});
    Board board(player);
    while (1)
    {
        board.display();
        if (board.game_over())
        {
            int result = board.utility(0);
            string message = (result == 1) ? "AI wins, you lose." : (result == 0) ? "Draw match."
                                                                                  : "Not possible.";
            cout << "-------------------------------------------------------\n";
            cout << message << '\n';
            cout << "-------------------------------------------------------\n";
            break;
        }
        int move;
        if (!board.current_player())
        {
            cout << "\nAI TURN\n";
            move = alpha_beta(board);
        }
        else
        {
            cout << "\nUSER TURN\n";
            cout << "Available Moves: ";
            auto moves = board.moves();
            cout << "| ";
            for (auto m : moves)
                cout << m << " | ";
            cout << '\n';
            ask(move, "Enter your move: ", moves);
        }
        board.fill(move);
    }
    return 0;
}