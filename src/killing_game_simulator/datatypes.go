package main

type Character struct {
	Name          string `json:"name"`
	Talent        string `json:"talent"`
	Status        string `json:"status"`
	CharacterType string `json:"character_type"`
	CauseOfDeath  string `json:"cause_of_death"`
}

type Round struct {
	RoundName    string    `json:"round_name"`
	Murderer     Character `json:"murderer"`
	VictimOne    Character `json:"victim_one"`
	VictimTwo    Character `json:"victim_two"`
	MurdererWins bool      `json:"murderer_wins"`
}

type GameState struct {
	CurrentRound     Round       `json:"current_round"`
	Mastermind       Character   `json:"mastermind"`
	PlayersRemaining []Character `json:"players_remaining"`
	AllRounds        []Round     `json:"all_rounds"`
}

type GenerateImage struct {
	PlayersRemaining []Character `json:"players_remaining"`
	AllRounds        []Round     `json:"all_rounds"`
}
