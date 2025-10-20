from GameStatus_5120 import GameStatus


def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool,
            alpha: float = float('-inf'), beta: float = float('inf')):
    # Terminal test or depth limit
    terminal = game_state.is_terminal()
    if depth == 0 or terminal:
        return game_state.get_scores(terminal), None

    # Generate possible actions
    possible_moves = game_state.get_moves()
    if not possible_moves:
        # No move: treat as terminal
        return game_state.get_scores(True), None

    best_move = None

    if maximizingPlayer:
        value = float('-inf')
        for move in possible_moves:
            child = game_state.get_new_state(move)
            child_value, _ = minimax(child, depth - 1, False, alpha, beta)

            if child_value > value:
                value, best_move = child_value, move

            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, best_move

    else:
        value = float('inf')
        for move in possible_moves:
            child = game_state.get_new_state(move)
            child_value, _ = minimax(child, depth - 1, True, alpha, beta)

            if child_value < value:
                value, best_move = child_value, move

            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move



def negamax(game_status: GameStatus, depth: int, turn_multiplier: int,
            alpha: float = float('-inf'), beta: float = float('inf')):
    """
    Negamax with alpha–beta pruning.
    turn_multiplier: +1 for the side we're evaluating for, -1 for adversary
    """
    terminal = game_status.is_terminal()
    if depth == 0 or terminal:
        base = (game_status.get_negamax_scores(terminal)
                if hasattr(game_status, "get_negamax_scores")
                else game_status.get_scores(terminal))
        return turn_multiplier * base, None

    possible_moves = game_status.get_possible_moves()
    if not possible_moves:
        base = (game_status.get_negamax_scores(True)
                if hasattr(game_status, "get_negamax_scores")
                else game_status.get_scores(True))
        return turn_multiplier * base, None

    best_val = float('-inf')
    best_move = None

    for move in possible_moves:
        child = game_status.get_new_state(move)
        # Flip turn and bounds for the adversary, then negate on return
        child_val, _ = negamax(child, depth - 1, -turn_multiplier, -beta, -alpha)
        val = -child_val

        if val > best_val:
            best_val, best_move = val, move

        alpha = max(alpha, best_val)
        if alpha >= beta:
            break

    return best_val, best_move

    
            
    
             

	
    
