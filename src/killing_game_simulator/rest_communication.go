package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func processJSON(data GenerateImage) []byte {
	if data.AllRounds != nil || data.PlayersRemaining != nil {
		parsed, err := json.Marshal(data)
		if err != nil {
			fmt.Printf("Error: %s", err)
		}
		return parsed
	}
	return []byte{}
}

func sendGenerateImageRequest(state GameState) (*http.Response, error) {
	newPlayersRemaining := insertMastermind(state.PlayersRemaining, state.Mastermind)
	generateImageStruct := GenerateImage{PlayersRemaining: newPlayersRemaining, AllRounds: state.AllRounds}
	generateImageJSON := processJSON(generateImageStruct)

	resp, err := http.Post("http://127.0.0.1:5000/generate_image", "application/json", bytes.NewBuffer(generateImageJSON))
	if err != nil {
		fmt.Println(err.Error())
	}
	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(body))
	return resp, err

}

func sendDeleteImageRequest() {

}
