package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
)

func initializeGame() GameState {
	characters := CharacterList
	startingRound := Round{RoundName: RoundNames[0]}
	mastermind, index := chooseCharacter(&characters)
	characters = append(characters[:index], characters[index+1:]...)
	return GameState{
		CurrentRound:     startingRound,
		Mastermind:       mastermind,
		PlayersRemaining: characters,
		PreviousRounds:   nil,
	}
}

func getRoundDescription(state GameState) string {
	round := state.CurrentRound
	if round.RoundName == "Prologue" {
		return "Let the killing games begin!"
	} else if strings.Contains(round.RoundName, "School Life") { // update to account for chapter 3 double murder
		if strings.Contains(round.RoundName, "Chapter 6") {
			return "On to the final trial! Who will win, the survivors or the mastermind?"
		} else if strings.Contains(round.RoundName, "Chapter 3") {
			return fmt.Sprintf("Two bodies have been discovered! %s, the %s was killed by %s, and %s, the %s was killed by %s! The class trial will begin shortly",
				round.VictimOne.Name, round.VictimOne.Talent, round.VictimOne.CauseOfDeath,
				round.VictimTwo.Name, round.VictimTwo.Talent, round.VictimTwo.CauseOfDeath)
		} else {
			return fmt.Sprintf("A body has been discovered! %s, the %s was killed by %s! The class trial will begin shortly", round.VictimOne.Name, round.VictimOne.Talent, round.VictimOne.CauseOfDeath)
		}
	} else if strings.Contains(round.RoundName, "Class Trial") {
		if round.MurdererWins {
			return fmt.Sprintf("%s got away with the crime and escaped Hope's Peak! Everyone else has been punished", round.Murderer)
		}
		return fmt.Sprintf("%s, the %s was found guilty of the crime! %d players remaining", round.Murderer.Name, round.Murderer.Talent, len(state.PlayersRemaining)+1) // +1 to account for mastermind not in players remaining
	} else { // Finale
		if round.MurdererWins {
			return fmt.Sprintf("%s is revelead to be the mastermind! %s successfully brought despair into the hearts of the survivors, and the survivors have been executed.", state.Mastermind.Name, state.Mastermind.Name)
		} else {
			return fmt.Sprintf("%s is revelead to be the mastermind! The survivors fought back despair with their hopes and defeated the mastermind!", state.Mastermind.Name)
		}
	}
}

func chooseCharacter(characters *[]Character) (Character, int) {
	index := rand.Intn(len(*characters))
	// fmt.Println("index in choose char is", index)
	character := CharacterList[index]
	return character, index
}

func chooseCauseOfDeath() string {
	return "bludgeoning"
}

func doesMurdererWin() bool {
	return false
}

func isSamePlayer(one, two Character) bool {
	return one.Name == two.Name && one.Talent == two.Talent
}

func getMurdererIndex(playersRemaining *[]Character, murderer Character) int {
	for i, player := range *playersRemaining {
		if isSamePlayer(player, murderer) {
			return i
		}
	}
	return -1
}

func chooseNextRoundName(currentRoundName string) string {
	length := len(RoundNames)
	for index, roundName := range RoundNames {
		if roundName == currentRoundName && index != length-1 {
			// fmt.Println("next round is", RoundNames[index+1])
			return RoundNames[index+1]
		}
	}
	return currentRoundName
}

func incrementRound(state GameState) GameState {
	if state.CurrentRound.MurdererWins || state.CurrentRound.RoundName == "Finale" {
		state = initializeGame()
	}
	if strings.Contains(state.CurrentRound.RoundName, "Class Trial") {
		state.CurrentRound.Murderer, state.CurrentRound.VictimOne, state.CurrentRound.VictimTwo, state.CurrentRound.MurdererWins = Character{}, Character{}, Character{}, false
	}
	state.CurrentRound.RoundName = chooseNextRoundName(state.CurrentRound.RoundName)
	// fmt.Println("roundName is", state.CurrentRound.RoundName)
	return state
}

func doRound(state GameState) GameState {
	if strings.Contains(state.CurrentRound.RoundName, "School Life") {
		if !strings.Contains(state.CurrentRound.RoundName, "Chapter 6") {
			victim, victimIndex := chooseCharacter(&state.PlayersRemaining)
			victim.Status = "dead"
			victim.CharacterType = "victim"
			victim.CauseOfDeath = chooseCauseOfDeath()
			// fmt.Println("Before first append")
			state.PlayersRemaining = append(state.PlayersRemaining[:victimIndex], state.PlayersRemaining[victimIndex+1:]...)
			state.CurrentRound.VictimOne = victim
		} else {
			victim := Character{}
			state.CurrentRound.VictimOne = victim
		}
		if strings.Contains(state.CurrentRound.RoundName, "Chapter 3") {
			victimTwo, victimTwoIndex := chooseCharacter(&state.PlayersRemaining)
			victimTwo.Status = "dead"
			victimTwo.CharacterType = "victim"
			victimTwo.CauseOfDeath = chooseCauseOfDeath()
			state.PlayersRemaining = append(state.PlayersRemaining[:victimTwoIndex], state.PlayersRemaining[victimTwoIndex+1:]...)
			state.CurrentRound.VictimTwo = victimTwo
		}
		state.PreviousRounds = append(state.PreviousRounds, state.CurrentRound)
	}
	if strings.Contains(state.CurrentRound.RoundName, "Class Trial") {
		murderer, _ := chooseCharacter(&state.PlayersRemaining)
		// fmt.Println("chosen murderer is", murderer.Name)
		murderer.CharacterType = "blackened"
		// state.PlayersRemaining = append(state.PlayersRemaining[:murdererIndex], state.PlayersRemaining[murdererIndex+1:]...)
		state.CurrentRound.Murderer = murderer
		state.CurrentRound.MurdererWins = doesMurdererWin()
		if !state.CurrentRound.MurdererWins {
			state.CurrentRound.Murderer.Status = "dead"
			index := getMurdererIndex(&state.PlayersRemaining, state.CurrentRound.Murderer)
			// fmt.Println("len of players remaining:", len(state.PlayersRemaining))
			// fmt.Println("index:", index)
			// fmt.Println("murderer:", state.CurrentRound.Murderer.Name) //shows up empty
			state.PlayersRemaining = append(state.PlayersRemaining[:index], state.PlayersRemaining[index+1:]...)
		}
		length := len(state.PreviousRounds)
		state.PreviousRounds[length-1] = state.CurrentRound // overwriting last round, as we're sending previous rounds to API
	}
	if strings.Contains(state.CurrentRound.RoundName, "Finale") {
		murderer := state.Mastermind
		murderer.CharacterType = "blackened"
		state.CurrentRound.Murderer = murderer
		state.CurrentRound.MurdererWins = doesMurdererWin() // mastermind winning or not
		if !state.CurrentRound.MurdererWins {
			state.CurrentRound.Murderer.Status, state.Mastermind.Status = "dead", "dead"
			// index := getMurdererIndex(&state.PlayersRemaining, state.CurrentRound.Murderer)
			// fmt.Println("murderer:", state.CurrentRound.Murderer.Name) //shows up empty
			// state.PlayersRemaining = append(state.PlayersRemaining[:index], state.PlayersRemaining[index+1:]...)
		}
		length := len(state.PreviousRounds)
		state.PreviousRounds[length-1] = state.CurrentRound // overwriting last round, as we're sending previous rounds to API
	}

	return state
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	state := initializeGame()
	for scanner.Scan() {
		//initialize game

		//do round
		state = doRound(state)

		//print info about round
		fmt.Println(getRoundDescription(state))

		//post round data to fb

		//go to next round
		state = incrementRound(state)
	}
}
