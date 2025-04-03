def ai_play(self):
    depth = 3
    if depth == 0 or self.is_terminal_node():
        return

    if self.player == "AI" and self.player_id == 1:
        """best_move = self.minmax(depth, 0, 0, self.player_id)
        # print(best_move)
        r, c = best_move[0], best_move[1]

        self.drawPieces(c, r)"""

        best_move = self.get_best_move()
        if best_move is None:
            best_move = random.choice(self.empty_cells())
            print(f'+++++++++{best_move}+++++++++++++')

        print(f'*************{best_move}***************')
        r, c = best_move[0], best_move[1]
        self.drawPieces(c, r)
        self.grid[r][c] = 1
        if self.check_game(self.grid, 1):
            self.gameFinished = True
            self.winner = str(self.player)
            print(f"{self.player} win")
        else:
            self.player = "Human"
            self.player_id = -1

    self.moves_count += 1


    def minmax(self, depth, isMax):
        """if player_number == 1:
            best = [1, 1, -np.inf]
        else:
            best = [1, 1, +np.inf]"""

        self.evaluate()

        if isMax:
            best_score = -np.inf

            for [r, c] in self.empty_cells():
                self.grid[r][c] = 1
                score = self.minmax(depth + 1, False)
                self.grid[r][c] = 0
                # Update the best score
                best_score = max(score, best_score)
            return best_score

        else:
            # if it is the minimizing player's turn (human), we want to minimize the score
            best_score = np.inf
            for [r, c] in self.empty_cells():
                # Make a calculating move
                self.grid[r][c] = -1
                # Recursively call minimax with the next depth and the maximizing player
                score = self.minmax(depth + 1, True)
                # Reset the move
                self.grid[r][c] = 0
                # Update the best score
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        """Find the best move for AI using minimax"""
        best_score = -np.inf
        best_move = None  # [1, 1]

        for [r, c] in self.empty_cells():
            # Make a calculating move
            self.grid[r][c] = 1
            # Recursively call minimax with the next depth and the minimizing player
            score = self.minmax(100, True)
            # Reset the move
            self.grid[r][c] = 0

            # Update the best score
            if score > best_score:
                best_score = score
                best_move = [r, c]

        return best_move
