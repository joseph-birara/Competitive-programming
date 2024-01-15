package main

import (
	"fmt"
	"sort"
)

func findWinners(matches [][]int) [][]int {
	losers := make([]int, 0)
	winners := make(map[int]struct{})
	dic := make(map[int]int)

	for _, match := range matches {
		los := match[1]
		dic[los]++
	}

	for key := range dic {
		if dic[key] == 1 {
			losers = append(losers, key)
		}
	}

	for _, match := range matches {
		win := match[0]
		if dic[win] == 0 {
			winners[win] = struct{}{}
		}
	}

	winnersList := make([]int, 0, len(winners))
	for key := range winners {
		winnersList = append(winnersList, key)
	}

	sort.Ints(winnersList)
	sort.Ints(losers)

	return [][]int{winnersList, losers}
}


