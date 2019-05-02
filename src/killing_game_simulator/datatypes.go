package main

type Character struct {
	Name          string
	Talent        string
	Status        string
	CharacterType string
	CauseOfDeath  string
}

type Round struct {
	RoundName    string
	Murderer     Character
	VictimOne    Character
	VictimTwo    Character
	MurdererWins bool
}

type GameState struct {
	CurrentRound     Round
	Mastermind       Character
	PlayersRemaining []Character
	PreviousRounds   []Round
}
