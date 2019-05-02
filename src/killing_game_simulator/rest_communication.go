package main

import (
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
	// generateImageStruct := GenerateImage{PlayersRemaining: state.PlayersRemaining, AllRounds: state.AllRounds}
	// generateImageJSON := processJSON(generateImageStruct)
	// fmt.Println(string(generateImageJSON))

	// resp, err := http.Post("http://127.0.0.1:5000/generate-image", "application/json", bytes.NewBuffer(generateImageJSON))
	resp, err := http.Get("http://127.0.0.1:5000/")
	if err != nil {
		fmt.Println(err.Error())
	}
	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(body))
	return resp, err

}

func sendDeleteImageRequest() {
	// req, err := http.NewRequest("DELETE", "127.0.0.1:5000/remove_image", nil)
	// if err != nil {
	// 	fmt.Println(err.Error())
	// }
	// return req, err
}
