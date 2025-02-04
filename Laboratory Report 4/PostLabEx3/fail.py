import unittest
import oxy_logic
import oxy_data

class TestOxyGame(unittest.TestCase):
    
    def test_new_game(self):
        game = oxy_logic.newGame()
        self.assertEqual(len(game), 10)  
    
    def test_save_and_restore_game(self):
        game = ["X", "O", "X", "O", "X", "O", "X", "O", " "]
        oxy_data.saveGame(game)
        restored_game = oxy_data.restoreGame()
        self.assertNotEqual(game, restored_game)  

    def test_generate_move(self):
        game = ["X", "O", "X", "O", "X", "O", "X", "O", "X"] 
        move = oxy_logic._generateMove(game)
        self.assertNotEqual(move, -1)  

    def test_winning_move(self):
        game = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
        self.assertFalse(oxy_logic._isWinningMove(game))  

    def test_user_move(self):
        game = oxy_logic.newGame()
        result = oxy_logic.userMove(game, 0)
        self.assertEqual(result, "O") 
    
    def test_computer_move(self):
        game = ["X", "O", "X", "O", "X", "O", "X", "O", " "]
        result = oxy_logic.computerMove(game)
        self.assertEqual(result, "X")

if __name__ == "__main__":
    unittest.main()
