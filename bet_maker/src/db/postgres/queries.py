def get_insert_bet_query() -> str:
    return "INSERT INTO bets (event_id, amount) VALUES ($1, $2) RETURNING id"


def get_all_bets_query() -> str:
    return "SELECT * FROM bets"


def get_update_bet_state_query() -> str:
    return "UPDATE bets SET state = $1 WHERE event_id = $2;"


def create_bets_table_query() -> str:
    return """
        CREATE TABLE IF NOT EXISTS bets (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            event_id UUID NOT NULL,
            amount numeric(8, 2) CHECK (amount > 0),
            state integer DEFAULT 1 CHECK (state IN (1, 2, 3))
        );
    """
