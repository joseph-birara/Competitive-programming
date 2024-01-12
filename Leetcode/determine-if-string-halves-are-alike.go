package main

import (
	"fmt"
	"strings"
)

func halvesAreAlike(s string) bool {
	n := len(s) / 2
	return countVowels(s[:n]) == countVowels(s[n:])
}

func countVowels(st string) int {
	vowels := "aeiouAEIOU"
	result := 0
	for _, char := range st {
		if strings.ContainsRune(vowels, char) {
			result++
		}
	}
	return result
}


