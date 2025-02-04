import unittest
import oxy_logic
import oxy_data

class TestOxyGame(unittest.TestCase):
    
    def test_new_game(self):
        game = oxy_logic.newGame()
        self.assertEqual(len(game), 9)
    
    def test_save_and_restore_game(self):
        game = ["X", "O", "X", "O", "X", "O", "X", "O", " "]
        oxy_data.saveGame(game)
        restored_game = oxy_data.restoreGame()
        self.assertEqual(game, restored_game)

    def test_generate_move(self):
        game = ["X", "O", " ", " ", "X", " ", "O", " ", "X"]
        move = oxy_logic._generateMove(game)
        self.assertIn(move, [i for i, v in enumerate(game) if v == " "])

    def test_winning_move(self):
        game = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
        self.assertTrue(oxy_logic._isWinningMove(game))

    def test_user_move(self):
        game = oxy_logic.newGame()
        oxy_logic.userMove(game, 0)    
        self.assertEqual(game[0], "X")  
    
    def test_computer_move(self):
        game = ["X", "O", "X", "O", "X", "O", "X", "O", " "]
        result = oxy_logic.computerMove(game)
        self.assertEqual(result, "O")  

if __name__ == "__main__":
    unittest.main()
